import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/sqlite_progress_repository.dart';
import 'package:learn_by_marifat_team/domain/curriculum.dart';
import 'package:learn_by_marifat_team/domain/learner_state.dart';
import 'package:learn_by_marifat_team/domain/portfolio.dart';
import 'package:learn_by_marifat_team/presentation/curriculum_screen.dart';

import 'support.dart';

void main() {
  const curriculum = BundledCurriculum();
  LearningController model() => LearningController(
    courses: BundledCourse(),
    curriculum: curriculum,
    progress: MemoryProgress(),
    runner: TestRunner(),
  );
  test('all requested courses have aligned plans, projects, and acyclic prerequisites', () {
    final catalog = curriculum.catalog;
    expect(catalog.length, 15);
    final ids = catalog.map((c) => c.id).toSet();
    expect(ids.length, 15);
    expect(portfolioIds(curriculum).length, 225);
    void visit(String id, Set<String> path) {
      expect(path.contains(id), isFalse, reason: 'Prerequisite cycle at $id');
      final course = catalog.firstWhere((c) => c.id == id);
      for (final prerequisite in course.prerequisites) {
        expect(ids, contains(prerequisite));
        visit(prerequisite, {...path, id});
      }
    }

    for (final course in catalog) {
      visit(course.id, {});
      expect(course.modules.length, 6);
      expect(course.projects.length, 3);
      final plans = course.modules.expand((m) => m.plans).toList();
      expect(plans.map((p) => p.level).toSet(), BloomLevel.values.toSet());
      expect(plans.fold<int>(0, (n, p) => n + p.minutes), 900);
      for (final module in course.modules) {
        expect(module.explanation.length, greaterThan(100));
        expect(module.example, isNotEmpty);
        for (final plan in module.plans) {
          expect(plan.activity, isNotEmpty);
          expect(plan.evidence, isNotEmpty);
          expect(plan.objective, isNotEmpty);
        }
      }
      for (final project in course.projects) {
        expect(project.requirements.length, 3);
        expect(project.milestones.length, 5);
      }
    }
  });
  test('generated catalog matches distributed JSON exactly', () {
    final source = jsonDecode(
      File('assets/curriculum/catalog.json').readAsStringSync(),
    ) as List;
    expect(
      source.map((dynamic c) => c['title']).toList(),
      curriculum.catalog.map((c) => c.title).toList(),
    );
    for (var i = 0; i < source.length; i++) {
      final original = StudyCourse(source[i] as Map<String, dynamic>);
      final bundled = curriculum.catalog[i];
      expect(
        original.modules.map((m) => m.example),
        bundled.modules.map((m) => m.example),
      );
      expect(
        original.modules.expand((m) => m.plans).map((p) => p.activity),
        bundled.modules.expand((m) => m.plans).map((p) => p.activity),
      );
    }
  });
  test(
    'v1 migration preserves foundations and initializes empty portfolio',
    () {
      final controller = model();
      addTearDown(controller.dispose);
      final old = jsonDecode(
        LearnerState(solved: {'hello-q'}).encode(),
      ) as Map<String, dynamic>;
      old['version'] = 1;
      old.remove('portfolio');
      final migrated = controller.validateBackup(jsonEncode(old));
      expect(migrated.solved, {'hello-q'});
      expect(migrated.portfolio, isEmpty);
      expect(jsonDecode(migrated.encode())['version'], 3);
    },
  );
  test('portfolio round trip preserves evidence, milestones, and rubric independently of quiz grades', () async {
    final controller = model();
    addTearDown(controller.dispose);
    await controller.savePortfolio(
      'python-p1',
      PortfolioEntry(
        evidence: 'Tested empty input and 20 + 30 = 50 AFN.',
        milestones: {0, 1, 2},
        scores: [2, 2, 3, 2, 2],
      ),
    );
    final restored = controller.validateBackup(await controller.exportBackup());
    expect(restored.portfolio['python-p1']!.milestones, {0, 1, 2});
    expect(restored.portfolio['python-p1']!.scores, [2, 2, 3, 2, 2]);
    expect(restored.solved, isEmpty);
    await expectLater(
      controller.savePortfolio('unknown', PortfolioEntry()),
      throwsFormatException,
    );
    expect(controller.state.portfolio.length, 1);
  });
  test('invalid rubric, milestone, and oversized evidence are rejected', () {
    for (final changes in [
      <String, dynamic>{
        'scores': [4, 0, 0, 0, 0],
      },
      {
        'milestones': [5],
      },
      {'evidence': 'x' * 4001},
    ]) {
      expect(
        () =>
            PortfolioEntry.fromJson({...PortfolioEntry().toJson(), ...changes}),
        throwsFormatException,
      );
    }
  });
  test('portfolio persists through real SQLite close and reopen', () async {
    sqfliteFfiInit();
    final directory = await Directory.systemTemp.createTemp(
      'marifat-portfolio-',
    );
    addTearDown(() => directory.delete(recursive: true));
    final path = '${directory.path}/learner.db';
    final repository = await SqliteProgressRepository.open(
      databaseFactoryFfi,
      path,
      BundledCourse(),
    );
    await repository.save(
      LearnerState(
        portfolio: {
          'flutter-dart-p3': PortfolioEntry(
            evidence: 'Relaunch test passed',
            milestones: {0, 3},
          ),
        },
      ),
    );
    await repository.close();
    final reopened = await SqliteProgressRepository.open(
      databaseFactoryFfi,
      path,
      BundledCourse(),
    );
    try {
      expect(
        (await reopened.load()).portfolio['flutter-dart-p3']!.evidence,
        'Relaunch test passed',
      );
    } finally {
      await reopened.close();
    }
  });
  testWidgets('search reaches course projects and saves evidence on a phone', (
    tester,
  ) async {
    final controller = model();
    addTearDown(controller.dispose);
    tester.view.physicalSize = const Size(390, 844);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(body: CurriculumScreen(controller: controller)),
      ),
    );
    await tester.enterText(find.byType(TextField), 'Flutter');
    await tester.pump();
    await tester.ensureVisible(find.text('Flutter and Dart'));
    await tester.tap(find.text('Flutter and Dart'));
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.text('Mini learning platform'));
    await tester.tap(find.text('Mini learning platform'));
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.byType(TextField));
    await tester.enterText(
      find.byType(TextField),
      'Built a local course list; empty-state test passed.',
    );
    await tester.ensureVisible(find.byKey(const Key('save-portfolio')));
    await tester.tap(find.byKey(const Key('save-portfolio')));
    await tester.pumpAndSettle();
    expect(
      controller.state.portfolio['flutter-dart-p3']!.evidence,
      contains('empty-state'),
    );
    expect(tester.takeException(), isNull);
  });
  testWidgets('project rubric fits narrow screens with enlarged text', (
    tester,
  ) async {
    final controller = model();
    addTearDown(controller.dispose);
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(
      MaterialApp(
        builder: (context, child) => MediaQuery(
          data: MediaQuery.of(context)
              .copyWith(textScaler: const TextScaler.linear(1.5)),
          child: child!,
        ),
        home: ProjectDetail(
          controller: controller,
          project: curriculum.catalog.first.projects.first,
        ),
      ),
    );
    await tester.ensureVisible(find.byKey(const Key('save-portfolio')));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });
}
