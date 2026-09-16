import 'package:learn_by_marifat_team/presentation/curriculum_screen.dart';
import 'package:learn_by_marifat_team/presentation/theme.dart';
import 'package:flutter/services.dart';
import 'package:learn_by_marifat_team/presentation/app.dart';

import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:learn_by_marifat_team/presentation/learning_localizations.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/translation_catalog.dart';
import 'package:learn_by_marifat_team/data/translations.dart';
import 'package:learn_by_marifat_team/domain/portfolio.dart';
import 'package:learn_by_marifat_team/presentation/project_workspace.dart';

import 'support.dart';

void main() {
  setUpAll(() async {
    await (FontLoader(
      'LearnMono',
    )..addFont(rootBundle.load('assets/fonts/noto-sans-mono.ttf'))).load();
    await (FontLoader('LearnSans')
          ..addFont(rootBundle.load('assets/fonts/roboto-regular.ttf'))
          ..addFont(rootBundle.load('assets/fonts/roboto-bold.ttf'))
          ..addFont(rootBundle.load('assets/fonts/roboto-black.ttf')))
        .load();
    await (FontLoader(
      'LearnArabic',
    )..addFont(rootBundle.load('assets/fonts/noto-naskh-arabic.ttf'))).load();
    await (FontLoader(
      'MaterialIcons',
    )..addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'))).load();
  });
  LearningController model() => LearningController(
    courses: BundledCourse(),
    curriculum: const BundledCurriculum(),
    progress: MemoryProgress(),
    runner: TestRunner(),
  );
  test('every inventoried content key has both translations and matching placeholders', () {
    final keys = (jsonDecode(
      File('assets/curriculum/translation_inventory.json').readAsStringSync(),
    ) as List).cast<String>();
    final token = RegExp(r'\{\d+\}');
    for (final language in ['fa', 'ps']) {
      for (final key in keys) {
        final value = translations[language]![key];
        expect(value, isNotNull, reason: '$language: $key');
        expect(value, isNotEmpty, reason: '$language: $key');
        expect(
          token.allMatches(value!).map((m) => m.group(0)).toSet(),
          token.allMatches(key).map((m) => m.group(0)).toSet(),
          reason: key,
        );
      }
    }
  });
  test('translation handles dynamic labels and preserves source code', () {
    expect(translate('Lesson · 60 minutes', 'fa'), 'Lesson · 60 دقیقه');
    for (final language in ['en', 'fa', 'ps']) {
      expect(translate('print("Hello")', language), 'print("Hello")');
      expect(translate('Save files', language), isNotEmpty);
    }
  });
  test(
    'workspace and evidence saves preserve each other and round trip',
    () async {
      final controller = model();
      addTearDown(controller.dispose);
      await controller.saveWorkspace('python-p1', {
        'main.py': 'print(42)',
        'NOTES.md': 'یادداشت',
      });
      await controller.savePortfolio(
        'python-p1',
        PortfolioEntry(evidence: 'Checked 42', milestones: {1}),
      );
      await controller.saveWorkspace('python-p1', {'main.py': 'print(43)'});
      final restored = controller.validateBackup(
        await controller.exportBackup(),
      );
      expect(restored.portfolio['python-p1']!.files, {'main.py': 'print(43)'});
      expect(restored.portfolio['python-p1']!.evidence, 'Checked 42');
      expect(restored.portfolio['python-p1']!.milestones, {1});
      final old =
          jsonDecode(await controller.exportBackup()) as Map<String, dynamic>;
      old['version'] = 2;
      (old['portfolio']['python-p1'] as Map).remove('files');
      expect(
        controller
            .validateBackup(jsonEncode(old))
            .portfolio['python-p1']!
            .files,
        isEmpty,
      );
    },
  );
  test('invalid workspace writes never replace saved files', () async {
    final controller = model();
    addTearDown(controller.dispose);
    await controller.saveWorkspace('python-p1', {'main.py': 'print(42)'});
    for (final files in [
      {'../escape': 'bad'},
      {'main.py': 'x' * 12001},
      {for (var i = 0; i < 5; i++) 'file$i': 'x'},
    ]) {
      await expectLater(
        controller.saveWorkspace('python-p1', files),
        throwsFormatException,
      );
      expect(controller.state.portfolio['python-p1']!.files, {
        'main.py': 'print(42)',
      });
    }
  });
  for (final language in ['fa', 'ps']) {
    testWidgets(
      '$language dark mission map renders and opens a playable lesson',
      (tester) async {
        tester.view.physicalSize = const Size(1100, 1050);
        tester.view.devicePixelRatio = 1;
        addTearDown(tester.view.resetPhysicalSize);
        addTearDown(tester.view.resetDevicePixelRatio);
        final controller = model();
        addTearDown(controller.dispose);
        final exercise = controller.lessons.first.exercises.first;
        await controller.submitChoice(exercise, exercise.answer);
        await tester.pumpWidget(
          RepaintBoundary(
            key: const Key('mission-capture'),
            child: MaterialApp(
              debugShowCheckedModeBanner: false,
              theme: learnTheme(true),
              locale: Locale(language),
              supportedLocales: const [
                Locale('en'),
                Locale('fa'),
                Locale('ps'),
              ],
              localizationsDelegates: learningLocalizations,
              home: CourseDetail(
                controller: controller,
                course: controller.curriculum.catalog.first,
              ),
            ),
          ),
        );
        await tester.pumpAndSettle();
        expect(tester.takeException(), isNull);
        await expectLater(
          find.byKey(const Key('mission-capture')),
          matchesGoldenFile('../preview/mission-$language.png'),
        );
        final lesson = find.text(
          translate(controller.lessons.first.title, language),
        );
        await tester.ensureVisible(lesson);
        await tester.tap(lesson);
        await tester.pumpAndSettle();
        expect(
          find.text(translate('Try the next activity', language)),
          findsOneWidget,
        );
        expect(tester.takeException(), isNull);
      },
    );

    testWidgets('$language guided lesson phone layout', (tester) async {
      tester.view.physicalSize = const Size(390, 844);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      final controller = model();
      addTearDown(controller.dispose);
      await controller.preferences(language: language);
      await tester.pumpWidget(
        RepaintBoundary(
          key: const Key('lesson-capture'),
          child: LearnApp(controller: controller),
        ),
      );
      await tester.pumpAndSettle();
      await tester.ensureVisible(
        find.text(translate('Start learning', language)),
      );
      await tester.tap(find.text(translate('Start learning', language)));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
      await expectLater(
        find.byKey(const Key('lesson-capture')),
        matchesGoldenFile('../preview/lesson-$language.png'),
      );
    });

    testWidgets('$language project walkthrough phone layout', (tester) async {
      tester.view.physicalSize = const Size(390, 844);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      final controller = model();
      await seedCourseProgress(controller, 'python');
      addTearDown(controller.dispose);
      await tester.pumpWidget(
        RepaintBoundary(
          key: const Key('project-capture'),
          child: MaterialApp(
            debugShowCheckedModeBanner: false,
            theme: learnTheme(false),
            locale: Locale(language),
            supportedLocales: const [Locale('en'), Locale('fa'), Locale('ps')],
            localizationsDelegates: learningLocalizations,
            home: ProjectDetail(
              controller: controller,
              project: controller.curriculum.catalog.first.projects.first,
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
      await tester.runAsync(
        () => precacheImage(
          const AssetImage('assets/brand/marifat.png'),
          tester.element(find.byType(MaterialApp).first),
        ),
      );
      await tester.pumpAndSettle();
      await expectLater(
        find.byKey(const Key('project-capture')),
        matchesGoldenFile('../preview/project-$language.png'),
      );
      await tester.ensureVisible(
        find.text(translate('Open workspace', language)),
      );
      await tester.tap(find.text(translate('Open workspace', language)));
      await tester.pumpAndSettle();
      expect(
        tester
            .widget<TextField>(find.byKey(const Key('workspace-editor')))
            .controller!
            .text,
        contains('def total_expenses'),
      );
      expect(tester.takeException(), isNull);
    });
    testWidgets('$language phone overview renders with bundled Arabic font', (
      tester,
    ) async {
      tester.view.physicalSize = const Size(390, 844);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      final controller = model();
      addTearDown(controller.dispose);
      await controller.preferences(language: language);
      await tester.pumpWidget(
        RepaintBoundary(
          key: const Key('localized-capture'),
          child: LearnApp(controller: controller),
        ),
      );
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
      await tester.runAsync(
        () => precacheImage(
          const AssetImage('assets/brand/marifat.png'),
          tester.element(find.byType(MaterialApp).first),
        ),
      );
      await tester.pumpAndSettle();
      await expectLater(
        find.byKey(const Key('localized-capture')),
        matchesGoldenFile('../preview/overview-$language.png'),
      );
      await tester.tap(find.text(translate('Courses', language)));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
      await expectLater(
        find.byKey(const Key('localized-capture')),
        matchesGoldenFile('../preview/curriculum-$language.png'),
      );
    });
    testWidgets('$language workspace uses RTL chrome and LTR editable code', (
      tester,
    ) async {
      final controller = model();
      await seedCourseProgress(controller, 'python');
      addTearDown(controller.dispose);
      final course = controller.curriculum.catalog.first;
      await tester.pumpWidget(
        MaterialApp(
          locale: Locale(language),
          supportedLocales: const [Locale('en'), Locale('fa'), Locale('ps')],
          localizationsDelegates: learningLocalizations,
          home: ProjectWorkspace(
            controller: controller,
            course: course,
            id: 'python-p1',
            title: course.title,
            seed: 'print(42)',
            requirements: const [],
          ),
        ),
      );
      await tester.pumpAndSettle();
      expect(
        Directionality.of(tester.element(find.byType(Scaffold))),
        TextDirection.rtl,
      );
      expect(
        Directionality.of(
          tester.element(find.byKey(const Key('workspace-editor'))),
        ),
        TextDirection.ltr,
      );
      await tester.enterText(
        find.byKey(const Key('workspace-editor')),
        'print(43)',
      );
      await tester.ensureVisible(find.byKey(const Key('save-workspace')));
      await tester.tap(find.byKey(const Key('save-workspace')));
      await tester.pumpAndSettle();
      expect(
        controller.state.portfolio['python-p1']!.files['main.py'],
        'print(43)',
      );
      expect(tester.takeException(), isNull);
    });
  }
}
