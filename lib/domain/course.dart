enum ExerciseKind { choice, order, code }

class Exercise {
  const Exercise({
    required this.id,
    required this.kind,
    required this.prompt,
    required this.explanation,
    this.options = const [],
    this.answer = 0,
    this.blocks = const [],
    this.starter = '',
    this.expected = '',
    this.hint = '',
  });
  final String id, prompt, explanation, starter, expected, hint;
  final ExerciseKind kind;
  final List<String> options, blocks;
  final int answer;
}

class Lesson {
  const Lesson({
    required this.id,
    required this.title,
    required this.summary,
    required this.minutes,
    required this.concept,
    required this.example,
    required this.exercises,
    required this.takeaway,
  });
  final String id, title, summary, concept, example, takeaway;
  final int minutes;
  final List<Exercise> exercises;
}

abstract interface class CourseRepository {
  List<Lesson> get lessons;
}
