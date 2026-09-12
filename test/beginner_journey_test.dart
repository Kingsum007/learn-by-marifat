import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/translations.dart';
import 'package:learn_by_marifat_team/presentation/app.dart';
import 'package:learn_by_marifat_team/presentation/lesson_screen.dart';

import 'support.dart';

void main() {
  LearningController model() => LearningController(
    courses: BundledCourse(),
    curriculum: const BundledCurriculum(),
    progress: MemoryProgress(),
    runner: TestRunner(),
  );
  testWidgets('beginner moves from concept to example to first activity', (
    tester,
  ) async {
    final controller = model();
    addTearDown(controller.dispose);
    await tester.pumpWidget(LearnApp(controller: controller));
    expect(
      tester
          .widget<NavigationBar>(find.byType(NavigationBar))
          .destinations
          .length,
      3,
    );
    await tester.ensureVisible(find.text('Start learning'));
    await tester.tap(find.text('Start learning'));
    await tester.pumpAndSettle();
    expect(find.text(controller.lessons.first.concept), findsOneWidget);
    expect(find.byType(SelectableText), findsNothing);
    await tester.tap(find.text('See an example'));
    await tester.pumpAndSettle();
    expect(find.text(controller.lessons.first.example), findsOneWidget);
    await tester.tap(find.widgetWithText(FilledButton, 'Try it yourself'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Try the next activity'));
    await tester.pumpAndSettle();
    expect(find.byType(ExerciseScreen), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
  testWidgets(
    'language is selectable before starting and settings remain reachable',
    (tester) async {
      final controller = model();
      addTearDown(controller.dispose);
      await tester.pumpWidget(LearnApp(controller: controller));
      await tester.tap(find.text('دری'));
      await tester.pumpAndSettle();
      expect(controller.state.language, 'fa');
      expect(find.text(translate('Start learning', 'fa')), findsOneWidget);
      await tester.tap(find.byTooltip(translate('Settings', 'fa')));
      await tester.pumpAndSettle();
      expect(find.byType(SettingsScreen), findsOneWidget);
      expect(tester.takeException(), isNull);
    },
  );
  testWidgets(
    'leaving the code lab can save changes without losing the draft',
    (tester) async {
      final controller = model();
      addTearDown(controller.dispose);
      await tester.pumpWidget(LearnApp(controller: controller));
      await tester.tap(find.text('Practice'));
      await tester.pumpAndSettle();
      await tester.tap(find.text('Code lab'));
      await tester.pumpAndSettle();
      await tester.enterText(
        find.byKey(const Key('code-editor')),
        'print(123)',
      );
      await tester.pump();
      await tester.pageBack();
      await tester.pumpAndSettle();
      expect(find.text('Save your changes?'), findsOneWidget);
      await tester.tap(find.text('Keep editing'));
      await tester.pumpAndSettle();
      expect(
        tester
            .widget<TextField>(find.byKey(const Key('code-editor')))
            .controller!
            .text,
        'print(123)',
      );
      await tester.pump();
      await tester.pageBack();
      await tester.pumpAndSettle();
      await tester.tap(find.text('Save and leave'));
      await tester.pumpAndSettle();
      expect(controller.state.drafts['playground'], 'print(123)');
      expect(find.byKey(const Key('code-editor')), findsNothing);
      expect(tester.takeException(), isNull);
    },
  );
}
