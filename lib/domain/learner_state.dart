import 'dart:convert';

import 'portfolio.dart';
import 'lab_language.dart';

/// Immutable aggregate. Persistence and backup use the same validated schema.
class LearnerState {
  LearnerState({
    Set<String> solved = const {},
    Set<String> bookmarks = const {},
    Set<String> completedIntros = const {},
    Map<String, String> drafts = const {},
    Map<String, int> attempts = const {},
    Map<String, PortfolioEntry> portfolio = const {},
    this.language = 'en',
    this.dark = false,
    this.labLanguage = 'python',
  }) : solved = Set.unmodifiable(solved),
       bookmarks = Set.unmodifiable(bookmarks),
       completedIntros = Set.unmodifiable(completedIntros),
       drafts = Map.unmodifiable(drafts),
       attempts = Map.unmodifiable(attempts),
       portfolio = Map.unmodifiable(portfolio);
  final Map<String, PortfolioEntry> portfolio;
  final Set<String> solved, bookmarks, completedIntros;
  final Map<String, String> drafts;
  final Map<String, int> attempts;
  final String language;
  final bool dark;
  final String labLanguage;

  LearnerState copyWith({
    Set<String>? solved,
    Set<String>? bookmarks,
    Set<String>? completedIntros,
    Map<String, String>? drafts,
    Map<String, int>? attempts,
    Map<String, PortfolioEntry>? portfolio,
    String? language,
    bool? dark,
    String? labLanguage,
  }) => LearnerState(
    solved: solved ?? this.solved,
    bookmarks: bookmarks ?? this.bookmarks,
    completedIntros: completedIntros ?? this.completedIntros,
    drafts: drafts ?? this.drafts,
    attempts: attempts ?? this.attempts,
    portfolio: portfolio ?? this.portfolio,
    language: language ?? this.language,
    dark: dark ?? this.dark,
    labLanguage: labLanguage ?? this.labLanguage,
  );

  String encode() => jsonEncode({
    'format': 'kohi-backup',
    'version': 4,
    'portfolio': portfolio.map((key, value) => MapEntry(key, value.toJson())),
    'solved': solved.toList(),
    'bookmarks': bookmarks.toList(),
    'completedIntros': completedIntros.toList(),
    'drafts': drafts,
    'attempts': attempts,
    'language': language,
    'dark': dark,
    'labLanguage': labLanguage,
  });

  static LearnerState decode(
    String source, {
    required Set<String> exerciseIds,
    required Set<String> lessonIds,
    Set<String> portfolioIds = const {},
    Set<String> courseIds = const {},
  }) {
    if (source.length > 16000000 || utf8.encode(source).length > 16000000) {
      throw const FormatException('Backup exceeds 16 MB.');
    }
    final dynamic data;
    try {
      data = jsonDecode(source);
    } on FormatException {
      throw const FormatException('Backup is not valid JSON.');
    }
    if (data is! Map<String, dynamic> ||
        data['format'] != 'kohi-backup' ||
        ![1, 2, 3, 4].contains(data['version'])) {
      throw const FormatException(
        'This is not a supported Learn By Marifat Team backup (version 1, 2, 3, or 4).',
      );
    }
    Set<String> ids(String key, Set<String> allowed) {
      final dynamic value = data[key];
      if (value is! List ||
          value.length > allowed.length ||
          value.any((dynamic id) => id is! String || !allowed.contains(id))) {
        throw FormatException('Invalid $key in backup.');
      }
      return value.cast<String>().toSet();
    }

    final dynamic drafts = data['drafts'], attempts = data['attempts'];
    if (drafts is! Map<String, dynamic> ||
        drafts.length > exerciseIds.length + labDraftIds.length ||
        drafts.entries.any(
          (e) =>
              !(exerciseIds.contains(e.key) || labDraftIds.contains(e.key)) ||
              e.value is! String ||
              (e.value as String).length > 12000,
        )) {
      throw const FormatException('Invalid code drafts in backup.');
    }
    if (attempts is! Map<String, dynamic> ||
        attempts.length > exerciseIds.length ||
        attempts.entries.any(
          (e) =>
              !exerciseIds.contains(e.key) ||
              e.value is! int ||
              (e.value as int) < 0 ||
              (e.value as int) > 1000000,
        )) {
      throw const FormatException('Invalid attempts in backup.');
    }
    if (!['en', 'fa', 'ps'].contains(data['language']) ||
        data['dark'] is! bool ||
        !labLanguages.any((l) => l.id == (data['labLanguage'] ?? 'python'))) {
      throw const FormatException('Invalid preferences in backup.');
    }
    final dynamic portfolio = data['version'] == 1
        ? <String, dynamic>{}
        : data['portfolio'];
    if (portfolio is! Map<String, dynamic> ||
        portfolio.length > portfolioIds.length ||
        portfolio.keys.any((id) => !portfolioIds.contains(id))) {
      throw const FormatException('Invalid portfolio identifiers in backup.');
    }
    return LearnerState(
      portfolio: portfolio.map(
        (key, dynamic value) => MapEntry(key, PortfolioEntry.fromJson(value)),
      ),
      solved: ids('solved', exerciseIds),
      bookmarks: ids('bookmarks', lessonIds),
      completedIntros: data['version'] == 4
          ? ids('completedIntros', courseIds)
          : {
              for (final courseId in courseIds)
                if (portfolio.keys.any((id) => id.startsWith('$courseId-')))
                  courseId,
            },
      drafts: drafts.cast<String, String>(),
      attempts: attempts.cast<String, int>(),
      language: data['language'] as String,
      dark: data['dark'] as bool,
      labLanguage: (data['labLanguage'] ?? 'python') as String,
    );
  }
}

abstract interface class ProgressRepository {
  Future<LearnerState> load();
  Future<void> save(LearnerState state);
  Future<void> close();
}
