import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/module_guides.dart';
import 'package:learn_by_marifat_team/data/translation_catalog.dart';

void main() {
  test('every non-Python module has a translated explanation and concrete practice', () {
    final courses = const BundledCurriculum().catalog.where(
      (c) => c.id != 'python',
    );
    expect(courses.length, 19);
    expect(moduleGuides.length, 304);
    for (final course in courses) {
      for (final module in course.modules) {
        final guide =
            moduleGuides[module.plans.first.id] as Map<String, dynamic>;
        expect((guide['trace'] as String).length, greaterThan(180));
        for (final key in ['trace', 'practice', 'review']) {
          for (final language in ['fa', 'ps']) {
            final text = translations[language]![guide[key]];
            expect(text, isNotNull, reason: '${module.title}/$key/$language');
            expect(text!.trim(), isNotEmpty);
            expect(text, isNot(guide[key]));
          }
        }
      }
    }
  });
}
