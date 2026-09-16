import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/translations.dart';
import 'package:learn_by_marifat_team/presentation/course_adventure.dart';
import 'package:learn_by_marifat_team/presentation/learning_localizations.dart';
import 'package:learn_by_marifat_team/presentation/sql_practice_screen.dart';
import 'package:learn_by_marifat_team/presentation/theme.dart';
import 'package:learn_by_marifat_team/runtime/sql_practice.dart';
import 'package:learn_by_marifat_team/presentation/code_workbench.dart';
import 'package:learn_by_marifat_team/domain/lab_language.dart';

import 'support.dart';

void main() {
  setUpAll(() async {
    await (FontLoader(
      'LearnMono',
    )..addFont(rootBundle.load('assets/fonts/noto-sans-mono.ttf'))).load();
    for (final font in [
      ('LearnArabic', 'assets/fonts/noto-naskh-arabic.ttf'),
      ('LearnSans', 'assets/fonts/roboto-regular.ttf'),
    ]) {
      final loader = FontLoader(font.$1)..addFont(rootBundle.load(font.$2));
      await loader.load();
    }
    final icons = FontLoader('MaterialIcons')
      ..addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'));
    await icons.load();
  });
  Widget host(Widget screen, String language) => MaterialApp(
    debugShowCheckedModeBanner: false,
    theme: learnTheme(false),
    locale: Locale(language),
    supportedLocales: const [Locale('en'), Locale('fa'), Locale('ps')],
    localizationsDelegates: learningLocalizations,
    home: screen,
  );
  for (final language in ['fa', 'ps']) {
    testWidgets('$language language-selectable code lab', (tester) async {
      tester.view.physicalSize = const Size(420, 900);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      final controller = LearningController(
        courses: BundledCourse(),
        curriculum: const BundledCurriculum(),
        progress: MemoryProgress(),
        runner: TestRunner(),
      );
      addTearDown(controller.dispose);
      await controller.selectLabLanguage('java');
      await tester.pumpWidget(
        RepaintBoundary(
          key: const Key('lab-capture'),
          child: host(
            Scaffold(
              body: SingleChildScrollView(
                padding: const EdgeInsets.all(20),
                child: CodeWorkbench(controller: controller),
              ),
            ),
            language,
          ),
        ),
      );
      await tester.pumpAndSettle();
      expect(find.text('Main.java'), findsOneWidget);
      expect(find.byKey(const Key('run-code')), findsNothing);
      expect(
        tester
            .widget<DropdownButton<LabLanguage>>(
              find.byKey(const Key('lab-language')),
            )
            .items!
            .length,
        19,
      );
      expect(
        Directionality.of(tester.element(find.byKey(const Key('code-editor')))),
        TextDirection.ltr,
      );
      expect(tester.takeException(), isNull);
      await expectLater(
        find.byKey(const Key('lab-capture')),
        matchesGoldenFile('../preview/code-lab-$language.png'),
      );
      await tester.tap(find.byKey(const Key('lab-language')));
      await tester.pumpAndSettle();
      await tester.tap(find.text('CSS').last);
      await tester.pumpAndSettle();
      expect(controller.state.labLanguage, 'css');
      expect(find.text('style.css'), findsOneWidget);
    });
    testWidgets(
      '$language database workshop explains code and exposes practice',
      (tester) async {
        tester.view.physicalSize = const Size(420, 900);
        tester.view.devicePixelRatio = 1;
        addTearDown(tester.view.resetPhysicalSize);
        addTearDown(tester.view.resetDevicePixelRatio);
        final controller = LearningController(
          courses: BundledCourse(),
          curriculum: const BundledCurriculum(),
          progress: MemoryProgress(),
          runner: TestRunner(),
        );
        addTearDown(controller.dispose);
        await seedCourseProgress(controller, 'database-foundations');
        await seedCourseProgress(controller, 'sql');
        final course = controller.curriculum.catalog.firstWhere(
          (c) => c.id == 'sql',
        );
        await tester.pumpWidget(
          RepaintBoundary(
            key: const Key('expanded-lesson'),
            child: host(
              WorkshopScreen(controller: controller, module: course.modules[1]),
              language,
            ),
          ),
        );
        await tester.tap(
          find.widgetWithText(
            ChoiceChip,
            translate('See it in action', language),
          ),
        );
        await tester.pumpAndSettle();
        await tester.ensureVisible(
          find.text(translate('Walk through the example', language)),
        );
        await tester.pumpAndSettle();
        expect(tester.takeException(), isNull);
        await expectLater(
          find.byKey(const Key('expanded-lesson')),
          matchesGoldenFile('../preview/database-$language.png'),
        );
        await tester.ensureVisible(
          find.widgetWithText(ChoiceChip, translate('Your turn', language)),
        );
        await tester.tap(
          find.widgetWithText(ChoiceChip, translate('Your turn', language)),
        );
        await tester.pumpAndSettle();
        await tester.ensureVisible(
          find.text(translate('Open offline SQL practice', language)),
        );
        await tester.tap(
          find.text(translate('Open offline SQL practice', language)),
        );
        await tester.pumpAndSettle();
        expect(find.byType(SqlPracticeScreen), findsOneWidget);
        expect(
          tester.widget<TextField>(find.byType(TextField)).textDirection,
          TextDirection.ltr,
        );
        expect(tester.takeException(), isNull);
      },
    );
  }
  testWidgets('SQL results and error feedback preserve editable query', (
    tester,
  ) async {
    await tester.pumpWidget(
      host(
        SqlPracticeScreen(execute: (query) async => runSqlPracticeSync(query)),
        'en',
      ),
    );
    await tester.ensureVisible(find.text('Run query'));
    await tester.tap(find.text('Run query'));
    await tester.pumpAndSettle();
    expect(find.byType(DataTable), findsOneWidget);
    expect(find.text('150'), findsOneWidget);
    await tester.enterText(find.byType(TextField), 'DELETE FROM books');
    await tester.ensureVisible(find.text('Run query'));
    await tester.tap(find.text('Run query'));
    await tester.pumpAndSettle();
    expect(find.byType(DataTable), findsNothing);
    expect(
      tester.widget<TextField>(find.byType(TextField)).controller!.text,
      'DELETE FROM books',
    );
    await tester.state<NavigatorState>(find.byType(Navigator)).maybePop();
    await tester.pumpAndSettle();
    expect(find.text('Leave SQL practice?'), findsOneWidget);
    await tester.tap(find.text('Keep editing'));
    await tester.pumpAndSettle();
    expect(find.byType(SqlPracticeScreen), findsOneWidget);
  });
}
