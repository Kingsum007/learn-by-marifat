import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/domain/learning_rewards.dart';

import 'support.dart';

void main() {
  test(
    'only known solved challenges count and lessons add a one-time bonus',
    () {
      final lessons = [
        {'a', 'b', 'c'},
        {'d', 'e', 'f'},
      ];
      expect(LearningRewards({'unknown'}, lessons).xp, 0);
      final first = LearningRewards({'a'}, lessons);
      expect(first.xp, 10);
      expect(first.level, 1);
      expect(first.badges, ['First spark']);
      final complete = LearningRewards({'a', 'b', 'c'}, lessons);
      expect(complete.xp, 50);
      expect(complete.completedLessons, 1);
      expect(complete.badges, contains('Lesson champion'));
      final both = LearningRewards({'a', 'b', 'c', 'd', 'e', 'f'}, lessons);
      expect(both.xp, 100);
      expect(both.level, 2);
      expect(both.levelProgress, 0);
      expect(both.isComplete, isTrue);
      expect(first.isComplete, isFalse);
    },
  );
  test('wrong answers and concurrent replays cannot mint XP; restore reproduces rewards', () async {
    final progress = MemoryProgress();
    LearningController model() => LearningController(
      courses: BundledCourse(),
      curriculum: const BundledCurriculum(),
      progress: progress,
      runner: TestRunner(),
    );
    final controller = model();
    addTearDown(controller.dispose);
    final exercise = controller.lessons.first.exercises.first;
    await controller.submitChoice(
      exercise,
      (exercise.answer + 1) % exercise.options.length,
    );
    expect(controller.rewards.xp, 0);
    await Future.wait([
      controller.submitChoice(exercise, exercise.answer),
      controller.submitChoice(exercise, exercise.answer),
    ]);
    expect(controller.rewards.xp, 10);
    final reopened = model();
    addTearDown(reopened.dispose);
    await reopened.initialize();
    expect(reopened.rewards.xp, 10);
    final state = controller.validateBackup(await controller.exportBackup());
    expect(state.solved, controller.state.solved);
  });
  test('failed persistence awards nothing', () async {
    final progress = MemoryProgress()..fail = true;
    final controller = LearningController(
      courses: BundledCourse(),
      curriculum: const BundledCurriculum(),
      progress: progress,
      runner: TestRunner(),
    );
    addTearDown(controller.dispose);
    final exercise = controller.lessons.first.exercises.first;
    await expectLater(
      controller.submitChoice(exercise, exercise.answer),
      throwsStateError,
    );
    expect(controller.rewards.xp, 0);
    expect(controller.rewards.badges, isEmpty);
  });
}
