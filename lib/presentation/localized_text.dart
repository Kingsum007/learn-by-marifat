import 'package:flutter/material.dart';

import '../data/translations.dart';

/// Translates authored prose only. Code, identifiers, output and learner input
/// remain unchanged and are explicitly rendered with ordinary Text widgets.
String tx(BuildContext context, String source) =>
    translate(source, Localizations.localeOf(context).languageCode);

// Isolate inline technical fragments so RTL prose cannot reverse list elements
// or comparisons. Full code editors/blocks already have explicit LTR direction.
String isolateInlineCode(String text) => text.replaceAllMapped(
  RegExp(
    r'\[[0-9 ,]+\]|[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_0-9]+)*(?:\([^()\n]*\))?(?:\s*(?:>=|<=|>|<|==|!=)\s*[A-Za-z_][A-Za-z_0-9]*)?',
  ),
  (match) => '\u2066${match[0]}\u2069',
);

class LText extends StatelessWidget {
  const LText(
    this.data, {
    super.key,
    this.style,
    this.protectInlineCode = false,
    this.textAlign,
    this.textDirection,
    this.maxLines,
    this.overflow,
    this.softWrap,
    this.semanticsLabel,
  });
  final String data;
  final bool protectInlineCode;
  final TextStyle? style;
  final TextAlign? textAlign;
  final TextDirection? textDirection;
  final int? maxLines;
  final TextOverflow? overflow;
  final bool? softWrap;
  final String? semanticsLabel;
  @override
  Widget build(BuildContext context) => Text(
    protectInlineCode && Directionality.of(context) == TextDirection.rtl
        ? isolateInlineCode(tx(context, data))
        : tx(context, data),
    style: style,
    textAlign: textAlign,
    textDirection: textDirection,
    maxLines: maxLines,
    overflow: overflow,
    softWrap: softWrap,
    semanticsLabel: semanticsLabel == null
        ? null
        : tx(context, semanticsLabel!),
  );
}
