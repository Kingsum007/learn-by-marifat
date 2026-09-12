import 'package:flutter/foundation.dart';

import '../domain/assessment.dart';
import '../domain/curriculum.dart';
import '../domain/portfolio.dart';
import '../domain/course.dart';
import '../domain/learner_state.dart';
import '../runtime/code_runner.dart';
import '../runtime/python_vm.dart';

/// Application coordinator with explicit dependencies and serialized commits.
/// State becomes visible only after persistence succeeds.
class LearningController extends ChangeNotifier {
  LearningController({
    required this.courses,
    required this.progress,
    required this.runner,
    required this.curriculum,
  });
  final CourseRepository courses;
  final ProgressRepository progress;
  final CodeRunner runner;
  final CurriculumRepository curriculum;
  Future<void> savePortfolio(String id, PortfolioEntry entry) => _commit(
    (s) => s.copyWith(
      portfolio: {
        ...s.portfolio,
        id: PortfolioEntry(
          evidence: entry.evidence,
          milestones: entry.milestones,
          scores: entry.scores,
          files: s.portfolio[id]?.files ?? entry.files,
        ),
      },
    ),
  );
  Future<void> saveWorkspace(String id, Map<String, String> files) =>
      _commit((s) {
        final entry = s.portfolio[id] ?? PortfolioEntry();
        return s.copyWith(
          portfolio: {
            ...s.portfolio,
            id: PortfolioEntry(
              evidence: entry.evidence,
              milestones: entry.milestones,
              scores: entry.scores,
              files: files,
            ),
          },
        );
      });
  final grader = GradeExercise();
  LearnerState _state = LearnerState();
  LearnerState get state => _state;
  Future<void>? _pending;
  int restoredGeneration = 0;
  List<Lesson> get lessons => courses.lessons;
  int get totalExercises =>
      lessons.fold(0, (n, lesson) => n + lesson.exercises.length);
  int solvedIn(Lesson lesson) =>
      lesson.exercises.where((e) => _state.solved.contains(e.id)).length;
  Lesson get nextLesson => lessons.firstWhere(
    (l) => solvedIn(l) < l.exercises.length,
    orElse: () => lessons.last,
  );
  double get completion => _state.solved.length / totalExercises;

  Future<void> initialize() async {
    _state = await progress.load();
    notifyListeners();
  }

  Future<void> _commit(LearnerState Function(LearnerState) update) {
    final task = (_pending ?? Future<void>.value()).then((_) async {
      final next = update(_state);
      validateBackup(next.encode());
      await progress.save(next);
      _state = next;
      notifyListeners();
    });
    _pending = task.then<void>((_) {}, onError: (Object _, StackTrace _) {});
    return task;
  }

  Future<void> _record(Exercise exercise, Assessment result) => _commit(
    (s) => s.copyWith(
      solved: result.correct ? {...s.solved, exercise.id} : s.solved,
      attempts: {
        ...s.attempts,
        exercise.id: (s.attempts[exercise.id] ?? 0) + 1,
      },
    ),
  );

  Future<Assessment> submitChoice(Exercise exercise, int selection) async {
    final result = grader.choice(exercise, selection);
    await _record(exercise, result);
    return result;
  }

  Future<Assessment> submitOrder(Exercise exercise, List<String> blocks) async {
    final result = grader.order(exercise, blocks);
    await _record(exercise, result);
    return result;
  }

  Future<(RunResult, Assessment)> submitCode(
    Exercise exercise,
    String source,
  ) async {
    await saveDraft(exercise.id, source);
    final run = await runner.run(source);
    final assessment = grader.output(exercise, run.output, error: run.error);
    await _record(exercise, assessment);
    return (run, assessment);
  }

  Future<void> saveDraft(String id, String source) {
    if (source.length > 12000) {
      throw const FormatException('Code exceeds 12,000 characters.');
    }
    return _commit((s) => s.copyWith(drafts: {...s.drafts, id: source}));
  }

  Future<void> toggleBookmark(String id) => _commit((s) {
    final bookmarks = {...s.bookmarks};
    if (!bookmarks.add(id)) {
      bookmarks.remove(id);
    }
    return s.copyWith(bookmarks: bookmarks);
  });
  Future<void> preferences({String? language, bool? dark}) =>
      _commit((s) => s.copyWith(language: language, dark: dark));
  Future<String> exportBackup() async {
    await _pending;
    return _state.encode();
  }

  LearnerState validateBackup(String source) => LearnerState.decode(
    source,
    portfolioIds: portfolioIds(curriculum),
    exerciseIds: lessons.expand((l) => l.exercises).map((e) => e.id).toSet(),
    lessonIds: lessons.map((l) => l.id).toSet(),
  );
  Future<void> importBackup(String source) async {
    final validated = validateBackup(source);
    await _commit((_) => validated);
    restoredGeneration++;
    notifyListeners();
  }
}
