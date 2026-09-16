import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/detailed_foundations.dart';
import 'package:learn_by_marifat_team/runtime/python_vm.dart';

void main() {
  test('every taught example produces its documented output offline', () {
    for (final lesson in BundledCourse().lessons) {
      final result = PythonVm().run(lesson.example);
      expect(result.error, isNull, reason: lesson.id);
      expect(
        result.output.trim(),
        foundationOutputs[lesson.id],
        reason: lesson.id,
      );
    }
  });

  test(
    'all foundation lessons contain complete parallel teaching sections',
    () {
      expect(
        detailedFoundations.keys.toSet(),
        BundledCourse().lessons.map((l) => l.id).toSet(),
      );
      for (final entry in detailedFoundations.entries) {
        final guide = entry.value as Map<String, dynamic>;
        expect(guide.keys.toSet(), {'en', 'fa', 'ps'});
        for (final language in ['en', 'fa', 'ps']) {
          final sections = guide[language] as List<dynamic>;
          expect(sections.length, 3);
          for (final section in sections.cast<String>()) {
            expect(
              section.length,
              greaterThan(300),
              reason: '${entry.key}/$language',
            );
            expect(section, contains('\n\n'));
            if (language != 'en') {
              expect(section, matches(RegExp(r'[\u0600-\u06ff]')));
              expect(guide['en'], isNot(contains(section)));
            }
          }
        }
      }
    },
  );
}
