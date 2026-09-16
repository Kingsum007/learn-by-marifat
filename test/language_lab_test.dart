import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/domain/lab_language.dart';
import 'package:learn_by_marifat_team/domain/learner_state.dart';
import 'package:learn_by_marifat_team/presentation/code_workbench.dart';
import 'package:learn_by_marifat_team/runtime/sql_practice.dart';

import 'support.dart';

void main() {
  LearnerState decode(String source) =>
      LearnerState.decode(source, exerciseIds: const {}, lessonIds: const {});
  test(
    'language drafts and choice round trip while old Python backups still load',
    () {
      final original = LearnerState(
        labLanguage: 'java',
        drafts: {
          for (final language in labLanguages)
            language.draftId: language.starter,
        },
      );
      final restored = decode(original.encode());
      expect(restored.labLanguage, 'java');
      expect(restored.drafts, original.drafts);
      final old = jsonDecode(
        LearnerState(drafts: const {'playground': 'print(7)'}).encode(),
      ) as Map<String, dynamic>;
      old.remove('labLanguage');
      expect(decode(jsonEncode(old)).labLanguage, 'python');
      old['labLanguage'] = 'unknown';
      expect(() => decode(jsonEncode(old)), throwsFormatException);
      old['labLanguage'] = 'python';
      old['drafts'] = {'lab-unknown': 'code'};
      expect(() => decode(jsonEncode(old)), throwsFormatException);
    },
  );

  LearningController model(MemoryProgress store) => LearningController(
    courses: BundledCourse(),
    curriculum: const BundledCurriculum(),
    progress: store,
    runner: TestRunner(),
  );
  Widget host(LearningController controller, {bool exercise = false}) =>
      MaterialApp(
        home: Scaffold(
          body: SingleChildScrollView(
            child: CodeWorkbench(
              controller: controller,
              exercise: exercise
                  ? controller.lessons.first.exercises.last
                  : null,
              sqlRunner: (source) async => runSqlPracticeSync(source),
            ),
          ),
        ),
      );
  Future<void> select(WidgetTester tester, String id) async {
    tester
        .widget<DropdownButton<LabLanguage>>(
          find.byKey(const Key('lab-language')),
        )
        .onChanged!(labLanguages.firstWhere((l) => l.id == id));
    await tester.pumpAndSettle();
  }

  String current(WidgetTester tester) => tester
      .widget<DropdownButton<LabLanguage>>(
        find.byKey(const Key('lab-language')),
      )
      .value!
      .id;
  String code(WidgetTester tester) => tester
      .widget<TextField>(find.byKey(const Key('code-editor')))
      .controller!
      .text;

  testWidgets(
    'switching saves separate drafts and cancellation keeps current language',
    (tester) async {
      final store = MemoryProgress();
      final controller = model(store);
      addTearDown(controller.dispose);
      await tester.pumpWidget(host(controller));
      await tester.enterText(find.byKey(const Key('code-editor')), 'print(99)');
      await tester.pump();
      await select(tester, 'java');
      await tester.tap(find.text('Keep editing'));
      await tester.pumpAndSettle();
      expect(current(tester), 'python');
      expect(code(tester), 'print(99)');
      await select(tester, 'java');
      await tester.tap(find.text('Save and switch'));
      await tester.pumpAndSettle();
      expect(current(tester), 'java');
      expect(controller.state.drafts['playground'], 'print(99)');
      expect(find.byKey(const Key('run-code')), findsNothing);
      await tester.enterText(
        find.byKey(const Key('code-editor')),
        'class Notes {}',
      );
      await tester.pump();
      await tester.ensureVisible(find.text('Save draft'));
      await tester.tap(find.text('Save draft'));
      await tester.pumpAndSettle();
      await select(tester, 'python');
      expect(code(tester), 'print(99)');
      await select(tester, 'java');
      expect(code(tester), 'class Notes {}');
      expect(store.state.labLanguage, 'java');
      await tester.pumpWidget(const SizedBox());
      await tester.pumpWidget(host(controller));
      expect(current(tester), 'java');
      expect(code(tester), 'class Notes {}');
    },
  );

  testWidgets(
    'failed save or preference write cannot discard code during switching',
    (tester) async {
      final store = MemoryProgress();
      final controller = model(store);
      addTearDown(controller.dispose);
      await tester.pumpWidget(host(controller));
      await tester.enterText(
        find.byKey(const Key('code-editor')),
        'print(123)',
      );
      await tester.pump();
      store.fail = true;
      await select(tester, 'java');
      await tester.tap(find.text('Save and switch'));
      await tester.pumpAndSettle();
      expect(current(tester), 'python');
      expect(code(tester), 'print(123)');
      await select(tester, 'java');
      await tester.tap(find.text('Discard changes'));
      await tester.pumpAndSettle();
      expect(current(tester), 'python');
      expect(code(tester), 'print(123)');
      store.fail = false;
      await select(tester, 'java');
      await tester.tap(find.text('Discard changes'));
      await tester.pumpAndSettle();
      expect(current(tester), 'java');
      expect(controller.state.drafts.containsKey('playground'), isFalse);
    },
  );

  testWidgets('SQL selection uses SQLite and exercises stay fixed to Python', (
    tester,
  ) async {
    final controller = model(MemoryProgress());
    addTearDown(controller.dispose);
    await tester.pumpWidget(host(controller));
    await select(tester, 'sql');
    await tester.enterText(
      find.byKey(const Key('code-editor')),
      'SELECT SUM(price) AS total FROM books',
    );
    await tester.ensureVisible(find.byKey(const Key('run-code')));
    await tester.tap(find.byKey(const Key('run-code')));
    await tester.pumpAndSettle();
    expect(find.text('total\n350'), findsOneWidget);
    expect(controller.state.drafts['lab-sql'], contains('SUM'));
    await tester.pumpWidget(const SizedBox());
    await tester.pumpWidget(host(controller, exercise: true));
    expect(find.byKey(const Key('lab-language')), findsNothing);
    expect(code(tester), controller.lessons.first.exercises.last.starter);
  });
}
