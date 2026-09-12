import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/domain/assessment.dart';
import 'package:learn_by_marifat_team/runtime/python_vm.dart';

void main() {
  final solutions = {
    'hello': 'print("Salam")\nprint("Kabul")',
    'variables': 'books = 12\nbooks = books + 3\nprint(books)',
    'numbers': 'print(23 % 4)',
    'decisions': 'score = 65\nif score >= 50:\n    print("Pass")',
    'loops': 'for n in range(1, 4):\n    print(n)',
    'lists': 'marks = [10, 20, 30]\ntotal = 0\nfor mark in marks:\n    total = total + mark\nprint(total)',
    'functions': 'def add(a, b):\n    return a + b\nprint(add(4, 6))',
  };
  for (final lesson in BundledCourse().lessons) {
    test('reference solution passes ${lesson.id} coding task', () {
      final result = PythonVm().run(solutions[lesson.id]!);
      expect(result.error, isNull);
      expect(
        GradeExercise()
            .output(lesson.exercises.last, result.output, error: result.error)
            .correct,
        isTrue,
      );
    });
  }
}
