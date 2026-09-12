/// Evidence is learner-authored; checklist and rubric entries are self-assessed.
class PortfolioEntry {
  PortfolioEntry({
    this.evidence = '',
    Set<int> milestones = const {},
    List<int> scores = const [0, 0, 0, 0, 0],
    Map<String, String> files = const {},
  }) : milestones = Set.unmodifiable(milestones),
       scores = List.unmodifiable(scores),
       files = Map.unmodifiable(files);
  final Map<String, String> files;
  final String evidence;
  final Set<int> milestones;
  final List<int> scores;
  Map<String, dynamic> toJson() => {
    'evidence': evidence,
    'milestones': milestones.toList(),
    'scores': scores,
    'files': files,
  };
  factory PortfolioEntry.fromJson(dynamic data) {
    if (data is! Map<String, dynamic> ||
        data['evidence'] is! String ||
        (data['evidence'] as String).length > 4000 ||
        data['milestones'] is! List ||
        (data['milestones'] as List).length > 5 ||
        (data['milestones'] as List).any(
          (dynamic n) => n is! int || n < 0 || n > 4,
        ) ||
        data['scores'] is! List ||
        (data['scores'] as List).length != 5 ||
        (data['scores'] as List).any(
          (dynamic n) => n is! int || n < 0 || n > 3,
        )) {
      throw const FormatException('Invalid portfolio evidence or rubric.');
    }
    final dynamic files = data['files'] ?? <String, dynamic>{};
    if (files is! Map<String, dynamic> ||
        files.length > 4 ||
        files.entries.any(
          (e) =>
              !RegExp(r'^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,79}$').hasMatch(e.key) ||
              e.value is! String ||
              (e.value as String).length > 12000,
        )) {
      throw const FormatException(
        'Invalid workspace files. Use at most four files of 12,000 characters each.',
      );
    }
    return PortfolioEntry(
      files: files.cast<String, String>(),
      evidence: data['evidence'] as String,
      milestones: (data['milestones'] as List).cast<int>().toSet(),
      scores: (data['scores'] as List).cast<int>(),
    );
  }
}
