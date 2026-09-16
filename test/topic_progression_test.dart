import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/domain/portfolio.dart';
import 'package:learn_by_marifat_team/presentation/curriculum_screen.dart';

import 'support.dart';

void main() {
  LearningController model(MemoryProgress store) => LearningController(
    courses: BundledCourse(),
    curriculum: const BundledCurriculum(),
    progress: store,
    runner: TestRunner(),
  );
  test('foundation locks require every earlier exercise, including gaps in old progress', () async {
    final c = model(MemoryProgress());
    addTearDown(c.dispose);
    expect(c.lessonUnlocked(c.lessons.first), isTrue);
    expect(c.lessonUnlocked(c.lessons[1]), isFalse);
    await c.importBackup(
      c.state
          .copyWith(solved: c.lessons[1].exercises.map((e) => e.id).toSet())
          .encode(),
    );
    expect(c.lessonUnlocked(c.lessons[2]), isFalse);
    for (final e in c.lessons.first.exercises) {
      await c.importBackup(
        c.state.copyWith(solved: {...c.state.solved, e.id}).encode(),
      );
    }
    expect(c.lessonUnlocked(c.lessons[2]), isTrue);
  });
  test('workshop activities unlock sequentially only after persisted confirmation and evidence', () async {
    final store = MemoryProgress();
    final c = model(store);
    addTearDown(c.dispose);
    await seedCourseProgress(c, 'database-foundations');
    await c.completeIntroduction('sql');
    final course = c.curriculum.catalog.firstWhere((c) => c.id == 'sql');
    final first = course.modules.first;
    final a = first.plans.first.id;
    expect(c.moduleUnlocked(course, first), isTrue);
    expect(c.portfolioUnlocked(first.plans[1].id), isFalse);
    await c.savePortfolio(a, PortfolioEntry(evidence: 'I checked the output.'));
    expect(c.portfolioUnlocked(first.plans[1].id), isFalse);
    store.fail = true;
    await expectLater(
      c.savePortfolio(a, PortfolioEntry(evidence: 'Checked.', milestones: {0})),
      throwsStateError,
    );
    expect(c.portfolioUnlocked(first.plans[1].id), isFalse);
    store.fail = false;
    await c.savePortfolio(
      a,
      PortfolioEntry(evidence: 'Checked.', milestones: {0}),
    );
    expect(c.portfolioUnlocked(first.plans[1].id), isTrue);
    expect(c.moduleUnlocked(course, course.modules[1]), isFalse);
    await c.savePortfolio(
      first.plans[1].id,
      PortfolioEntry(evidence: 'Independent task checked.', milestones: {0}),
    );
    expect(c.moduleUnlocked(course, course.modules[1]), isTrue);
    final restored = model(store);
    addTearDown(restored.dispose);
    await restored.initialize();
    final sql = restored.curriculum.catalog.firstWhere((c) => c.id == 'sql');
    expect(restored.moduleUnlocked(sql, sql.modules[1]), isTrue);
    expect(restored.portfolioUnlocked(sql.projects.first.id), isFalse);
    await seedCourseProgress(restored, 'database-foundations');
    await seedCourseProgress(restored, 'sql');
    expect(restored.portfolioUnlocked(sql.projects.first.id), isTrue);
    expect(restored.portfolioUnlocked(sql.projects[1].id), isFalse);
  });
  testWidgets('direct project route cannot bypass an unfinished course', (
    tester,
  ) async {
    final c = model(MemoryProgress());
    addTearDown(c.dispose);
    await tester.pumpWidget(
      MaterialApp(
        home: ProjectDetail(
          controller: c,
          project: c.curriculum.catalog.first.projects.first,
        ),
      ),
    );
    expect(find.text('Topic locked'), findsOneWidget);
    expect(find.text('Open workspace'), findsNothing);
  });

  test(
    'course prerequisites unlock only after required courses complete',
    () async {
      final controller = model(MemoryProgress());
      addTearDown(controller.dispose);
      final catalog = controller.curriculum.catalog;
      final foundations = catalog.firstWhere(
        (course) => course.id == 'database-foundations',
      );
      final sql = catalog.firstWhere((course) => course.id == 'sql');
      final sqlite = catalog.firstWhere((course) => course.id == 'sqlite');
      expect(controller.courseUnlocked(foundations), isTrue);
      expect(controller.courseUnlocked(sql), isFalse);
      expect(controller.courseUnlocked(sqlite), isFalse);

      await seedCourseProgress(controller, foundations.id);
      expect(controller.courseUnlocked(sql), isTrue);
      expect(controller.courseUnlocked(sqlite), isFalse);

      await seedCourseProgress(controller, sql.id);
      expect(controller.courseUnlocked(sqlite), isTrue);
    },
  );

  test(
    'zero-knowledge introduction unlocks the first module and persists',
    () async {
      final store = MemoryProgress();
      final controller = model(store);
      addTearDown(controller.dispose);
      final java = controller.curriculum.catalog.firstWhere(
        (course) => course.id == 'java',
      );
      expect(controller.introComplete(java), isFalse);
      expect(controller.moduleUnlocked(java, java.modules.first), isFalse);
      await controller.completeIntroduction(java.id);
      expect(controller.introComplete(java), isTrue);
      expect(controller.moduleUnlocked(java, java.modules.first), isTrue);

      final restored = model(store);
      addTearDown(restored.dispose);
      await restored.initialize();
      final restoredJava = restored.curriculum.catalog.firstWhere(
        (course) => course.id == 'java',
      );
      expect(restored.introComplete(restoredJava), isTrue);
      expect(
        restored.moduleUnlocked(restoredJava, restoredJava.modules.first),
        isTrue,
      );
    },
  );

  testWidgets('catalogue labels a locked course with its prerequisite', (
    tester,
  ) async {
    final controller = model(MemoryProgress());
    addTearDown(controller.dispose);
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(body: CurriculumScreen(controller: controller)),
      ),
    );
    await tester.enterText(find.byType(TextField), 'SQLite');
    await tester.pumpAndSettle();
    expect(find.textContaining('Finish first:'), findsOneWidget);
    expect(find.byIcon(Icons.lock_outline), findsOneWidget);
    await tester.tap(find.text('SQLite'));
    await tester.pumpAndSettle();
    expect(find.byType(CourseDetail), findsNothing);
  });

  testWidgets('direct course route cannot bypass prerequisites', (
    tester,
  ) async {
    final controller = model(MemoryProgress());
    addTearDown(controller.dispose);
    final sqlite = controller.curriculum.catalog.firstWhere(
      (course) => course.id == 'sqlite',
    );
    await tester.pumpWidget(
      MaterialApp(
        home: CourseDetail(controller: controller, course: sqlite),
      ),
    );
    expect(find.text('Topic locked'), findsOneWidget);
    expect(find.text('Your coding adventure'), findsNothing);
  });

  testWidgets('beginner introduction remains usable with large text', (
    tester,
  ) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    final controller = model(MemoryProgress());
    addTearDown(controller.dispose);
    final java = controller.curriculum.catalog.firstWhere(
      (course) => course.id == 'java',
    );
    await tester.pumpWidget(
      MaterialApp(
        builder: (context, child) => MediaQuery(
          data: MediaQuery.of(context)
              .copyWith(textScaler: const TextScaler.linear(1.5)),
          child: child!,
        ),
        home: BeginnerScreen(controller: controller, course: java),
      ),
    );
    await tester.ensureVisible(
      find.text(java.beginner.options[java.beginner.answer]),
    );
    await tester.tap(find.text(java.beginner.options[java.beginner.answer]));
    await tester.pump();
    await tester.ensureVisible(find.text('Check readiness'));
    await tester.tap(find.text('Check readiness'));
    await tester.pump();
    await tester.ensureVisible(
      find.text('Complete introduction and unlock topic 1'),
    );
    await tester.tap(find.text('Complete introduction and unlock topic 1'));
    await tester.pumpAndSettle();
    expect(controller.introComplete(java), isTrue);
    expect(tester.takeException(), isNull);
  });
}
