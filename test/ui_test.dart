import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/presentation/app.dart';
import 'package:learn_by_marifat_team/presentation/code_workbench.dart';
import 'package:learn_by_marifat_team/presentation/lesson_screen.dart';
import 'package:learn_by_marifat_team/presentation/theme.dart';

import 'support.dart';

void main() {
  setUpAll(() async {
    final font = FontLoader('LearnSans')
      ..addFont(rootBundle.load('assets/fonts/roboto-regular.ttf'))
      ..addFont(rootBundle.load('assets/fonts/roboto-bold.ttf'))
      ..addFont(rootBundle.load('assets/fonts/roboto-black.ttf'));
    await font.load();
    await (FontLoader(
      'LearnArabic',
    )..addFont(rootBundle.load('assets/fonts/noto-naskh-arabic.ttf'))).load();
    await (FontLoader(
      'MaterialIcons',
    )..addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'))).load();
  });
  late LearningController controller;
  setUp(
    () => controller = LearningController(
      courses: BundledCourse(),
      curriculum: const BundledCurriculum(),
      progress: MemoryProgress(),
      runner: TestRunner(),
    ),
  );
  tearDown(() => controller.dispose());
  testWidgets('phone overview opens lesson and navigation works', (
    tester,
  ) async {
    tester.view.physicalSize = const Size(390, 844);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(LearnApp(controller: controller));
    expect(find.text('Start learning'), findsOneWidget);
    expect(tester.takeException(), isNull);
    await tester.ensureVisible(find.text('Start learning'));
    await tester.tap(find.text('Start learning'));
    await tester.pumpAndSettle();
    expect(find.byType(LessonScreen), findsOneWidget);
    expect(find.text('Your first program'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
  testWidgets('choice assessment saves progress through UI', (tester) async {
    await tester.pumpWidget(
      MaterialApp(
        theme: learnTheme(false),
        home: ExerciseScreen(
          controller: controller,
          exercise: controller.lessons.first.exercises.first,
        ),
      ),
    );
    await tester.tap(find.text('B.  Salam'));
    await tester.pump();
    await tester.tap(find.text('Check answer'));
    await tester.pumpAndSettle();
    expect(controller.state.solved, {'hello-q'});
    expect(find.text('✓ Nicely done. Progress saved.'), findsOneWidget);
  });
  testWidgets('code editor executes and persists a draft', (tester) async {
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: SingleChildScrollView(
            child: CodeWorkbench(controller: controller),
          ),
        ),
      ),
    );
    await tester.enterText(find.byKey(const Key('code-editor')), 'print(42)');
    await tester.ensureVisible(find.byKey(const Key('run-code')));
    await tester.tap(find.byKey(const Key('run-code')));
    await tester.pumpAndSettle();
    expect(find.text('42'), findsOneWidget);
    expect(controller.state.drafts['playground'], 'print(42)');
  });
  testWidgets('phone supports larger text without layout exceptions', (
    tester,
  ) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(
      MaterialApp(
        theme: learnTheme(false),
        home: MediaQuery(
          data: const MediaQueryData(
            size: Size(360, 800),
            textScaler: TextScaler.linear(1.5),
          ),
          child: HomeShell(controller: controller),
        ),
      ),
    );
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });
  testWidgets('desktop overview visual regression', (tester) async {
    tester.view.physicalSize = const Size(1440, 1040);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(
      RepaintBoundary(
        key: const Key('capture'),
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
      find.byKey(const Key('capture')),
      matchesGoldenFile('../preview/dashboard.png'),
    );
    await tester.tap(find.text('Courses'));
    await tester.pumpAndSettle();
    await tester.runAsync(
      () => precacheImage(
        const AssetImage('assets/brand/marifat.png'),
        tester.element(find.byType(MaterialApp).first),
      ),
    );
    await tester.pumpAndSettle();
    await expectLater(
      find.byKey(const Key('capture')),
      matchesGoldenFile('../preview/curriculum.png'),
    );
  });
}
