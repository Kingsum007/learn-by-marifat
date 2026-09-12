import 'package:learn_by_marifat_team/presentation/localized_text.dart';

import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/project_guides.dart';
import 'package:learn_by_marifat_team/presentation/project_workspace.dart';
import 'package:learn_by_marifat_team/runtime/python_vm.dart';

import 'support.dart';

void main() {
  test('RTL prose protects complete numeric lists and code comparisons', () {
    expect(isolateInlineCode('print()'), '\u2066print()\u2069');
    expect(
      isolateInlineCode('نمونه [20, 30] او quantity >= stock'),
      'نمونه \u2066[20, 30]\u2069 او \u2066quantity >= stock\u2069',
    );
  });
  for (final entry in projectGuides.entries) {
    test(
      '${entry.key} reference core executes and starter needs completion',
      () {
        final guide = entry.value;
        final solved = PythonVm().run(guide.solution);
        expect(solved.error, isNull);
        expect(solved.output.trim(), guide.expected);
        final starter = PythonVm().run(guide.starter);
        expect(starter.error, isNull);
        expect(starter.output.trim(), isNot(guide.expected));
        expect(guide.steps.length, 6);
        expect(
          guide.reference,
          File('projects/python/${guide.file}')
              .readAsStringSync()
              .replaceFirst('\uFEFF', '')
              .replaceAll('\r\n', '\n'),
        );
      },
    );
  }
  test('guide JSON and executable bundle stay synchronized', () {
    final json = jsonDecode(
      File('assets/curriculum/project_guides.json').readAsStringSync(),
    ) as Map;
    expect(projectGuides.keys, json.keys);
    for (final entry in projectGuides.entries) {
      expect(entry.value.solution, json[entry.key]['solution']);
      expect(entry.value.steps, json[entry.key]['steps']);
    }
  });
  testWidgets(
    'loading a practice solution requires confirmation and explicit save',
    (tester) async {
      final controller = LearningController(
        courses: BundledCourse(),
        curriculum: const BundledCurriculum(),
        progress: MemoryProgress(),
        runner: TestRunner(),
      );
      addTearDown(controller.dispose);
      await controller.saveWorkspace('python-p1', {'main.py': 'print(99)'});
      final guide = projectGuides['python-p1']!;
      await tester.pumpWidget(
        MaterialApp(
          home: ProjectWorkspace(
            controller: controller,
            course: controller.curriculum.catalog.first,
            id: 'python-p1',
            title: 'Practice',
            seed: guide.starter,
            requirements: const [],
          ),
        ),
      );
      await tester.pumpAndSettle();
      final load = find.widgetWithText(TextButton, 'Load practice solution');
      await tester.ensureVisible(load);
      await tester.tap(load);
      await tester.pumpAndSettle();
      await tester.tap(find.text('Keep editing'));
      await tester.pumpAndSettle();
      expect(
        tester
            .widget<TextField>(find.byKey(const Key('workspace-editor')))
            .controller!
            .text,
        'print(99)',
      );
      await tester.tap(load);
      await tester.pumpAndSettle();
      await tester.tap(
        find.widgetWithText(FilledButton, 'Load practice solution'),
      );
      await tester.pumpAndSettle();
      expect(
        tester
            .widget<TextField>(find.byKey(const Key('workspace-editor')))
            .controller!
            .text,
        guide.solution,
      );
      expect(
        controller.state.portfolio['python-p1']!.files['main.py'],
        'print(99)',
      );
      await tester.ensureVisible(find.byKey(const Key('save-workspace')));
      await tester.tap(find.byKey(const Key('save-workspace')));
      await tester.pumpAndSettle();
      expect(
        controller.state.portfolio['python-p1']!.files['main.py'],
        guide.solution,
      );
      expect(tester.takeException(), isNull);
    },
  );
}
