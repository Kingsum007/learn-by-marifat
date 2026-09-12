import 'course.dart';

class Assessment {
  const Assessment(this.correct, this.message);
  final bool correct;
  final String message;
}

/// Pure policies: the UI cannot award progress without going through grading.
class GradeExercise {
  Assessment choice(Exercise exercise, int selected) {
    if (exercise.kind != ExerciseKind.choice ||
        selected < 0 ||
        selected >= exercise.options.length) {
      throw ArgumentError('Invalid choice submission.');
    }
    return Assessment(selected == exercise.answer, exercise.explanation);
  }

  Assessment order(Exercise exercise, List<String> blocks) {
    if (exercise.kind != ExerciseKind.order) {
      throw ArgumentError('Not an ordering exercise.');
    }
    final correct =
        blocks.length == exercise.blocks.length &&
        List.generate(
          blocks.length,
          (i) => blocks[i] == exercise.blocks[i],
        ).every((v) => v);
    return Assessment(correct, exercise.explanation);
  }

  Assessment output(Exercise exercise, String actual, {String? error}) {
    if (exercise.kind != ExerciseKind.code) {
      throw ArgumentError('Not a coding exercise.');
    }
    String normalize(String value) =>
        value.replaceAll('\r\n', '\n').trimRight();
    return Assessment(
      error == null && normalize(actual) == normalize(exercise.expected),
      error ?? exercise.explanation,
    );
  }
}
