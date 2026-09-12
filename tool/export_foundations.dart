import 'dart:convert';
import 'dart:io';

import 'package:learn_by_marifat_team/data/bundled_course.dart';

void main() {
  final data = [
    for (final l in BundledCourse().lessons)
      {
        'id': l.id,
        'title': l.title,
        'summary': l.summary,
        'concept': l.concept,
        'takeaway': l.takeaway,
        'exercises': [
          for (final e in l.exercises)
            {
              'id': e.id,
              'prompt': e.prompt,
              'explanation': e.explanation,
              'options': e.options,
              'hint': e.hint,
            },
        ],
      },
  ];
  File('assets/curriculum/python_foundations.json')
      .writeAsStringSync(const JsonEncoder.withIndent('  ').convert(data));
}
