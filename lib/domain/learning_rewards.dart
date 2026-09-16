/// Rewards are derived from persisted, uniquely solved exercises. Replays cannot
/// mint points, and backup restore cannot desynchronize a separate XP counter.
class LearningRewards {
  LearningRewards(Set<String> solved, List<Set<String>> lessons)
    : totalLessons = lessons.length,
      solvedCount = solved
          .intersection(lessons.expand((ids) => ids).toSet())
          .length,
      completedLessons = lessons
          .where((ids) => ids.isNotEmpty && solved.containsAll(ids))
          .length;
  final int solvedCount, completedLessons, totalLessons;
  bool get isComplete => totalLessons > 0 && completedLessons == totalLessons;
  int get xp => solvedCount * 10 + completedLessons * 20;
  int get level => 1 + xp ~/ 100;
  int get levelProgress => xp % 100;
  List<String> get badges => [
    if (solvedCount >= 1) 'First spark',
    if (solvedCount >= 5) 'Problem solver',
    if (completedLessons >= 1) 'Lesson champion',
    if (completedLessons >= 7) 'Python explorer',
  ];
}
