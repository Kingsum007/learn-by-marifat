// Generated dictionaries are imported separately to keep the resolver testable.
import 'translation_catalog.dart';

String translate(String source, String language) {
  if (language == 'en' || source.isEmpty) return source;
  final values = translations[language];
  if (values == null) return source;
  final exact = values[source] ?? values[source.toLowerCase()];
  if (exact != null) return exact;
  for (final entry in values.entries.where((e) => e.key.contains('{0}'))) {
    final tokens = RegExp(r'\{\d+\}').allMatches(entry.key).toList();
    var pattern = '^';
    var end = 0;
    for (final token in tokens) {
      pattern += '${RegExp.escape(entry.key.substring(end, token.start))}(.*?)';
      end = token.end;
    }
    pattern += '${RegExp.escape(entry.key.substring(end))}\$';
    final match = RegExp(pattern, dotAll: true).firstMatch(source);
    if (match == null) continue;
    var output = entry.value;
    for (var i = 0; i < tokens.length; i++) {
      output = output.replaceAll(
        tokens[i].group(0)!,
        translate(match.group(i + 1)!, language),
      );
    }
    return output;
  }
  for (final separator in ['\n\n', '\n', ' · ', ' → ', ', ']) {
    if (source.contains(separator)) {
      return source
          .split(separator)
          .map((s) => translate(s, language))
          .join(separator);
    }
  }
  if (source.startsWith('• ')) {
    return '• ${translate(source.substring(2), language)}';
  }
  return source;
}
