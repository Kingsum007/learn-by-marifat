import 'localized_text.dart';

import 'package:flutter/material.dart';

const ink = Color(0xFF102F61);
const green = Color(0xFF087C89);
const mint = Color(0xFFE0F5F4);
const amber = Color(0xFF48DDD0);

ThemeData learnTheme(bool dark) {
  final scheme = ColorScheme.fromSeed(
    seedColor: green,
    brightness: dark ? Brightness.dark : Brightness.light,
    surface: dark ? const Color(0xFF142128) : const Color(0xFFF3F6FC),
  );
  return ThemeData(
    fontFamily: 'LearnSans',
    fontFamilyFallback: const ['LearnArabic'],
    useMaterial3: true,
    colorScheme: scheme,
    scaffoldBackgroundColor: scheme.surface,
    textTheme: ThemeData(brightness: scheme.brightness).textTheme.apply(
      fontFamily: 'LearnSans',
      fontFamilyFallback: const ['LearnArabic'],
      bodyColor: dark ? const Color(0xFFE7EEE9) : ink,
      displayColor: dark ? const Color(0xFFE7EEE9) : ink,
    ),
    appBarTheme: AppBarTheme(
      backgroundColor: scheme.surface,
      foregroundColor: scheme.onSurface,
      elevation: 0,
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: scheme.surfaceContainerLow,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(14),
        borderSide: BorderSide.none,
      ),
    ),
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(
        padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 18),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 18),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
    cardTheme: CardThemeData(
      elevation: 0,
      margin: EdgeInsets.zero,
      color: dark ? const Color(0xFF1C3037) : Colors.white,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(20),
        side: BorderSide(
          color: dark ? const Color(0xFF30464D) : const Color(0xFFE0E7F1),
        ),
      ),
    ),
  );
}

class SectionLabel extends StatelessWidget {
  const SectionLabel(this.text, {super.key});
  final String text;
  @override
  Widget build(BuildContext context) => LText(
    text,
    style: TextStyle(
      color: Theme.of(context).colorScheme.primary,
      fontSize: 11,
      fontWeight: FontWeight.w800,
      letterSpacing: .2,
    ),
  );
}

class PageHeading extends StatelessWidget {
  const PageHeading(this.eyebrow, this.title, this.subtitle, {super.key});
  final String eyebrow, title, subtitle;
  @override
  Widget build(BuildContext context) => Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      SectionLabel(eyebrow),
      const SizedBox(height: 12),
      LText(
        title,
        style: Theme.of(context).textTheme.headlineLarge
            ?.copyWith(fontWeight: FontWeight.w800, letterSpacing: -1),
      ),
      const SizedBox(height: 8),
      LText(
        subtitle,
        style: Theme.of(context).textTheme.bodyLarge?.copyWith(height: 1.6),
      ),
      const SizedBox(height: 28),
    ],
  );
}

Future<void> safely(
  BuildContext context,
  Future<void> Function() action, {
  String? success,
}) async {
  try {
    await action();
    if (context.mounted && success != null) {
      ScaffoldMessenger.of(context)
          .showSnackBar(SnackBar(content: LText(success)));
    }
  } catch (error) {
    if (context.mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: LText(
            error is FormatException
                ? error.message
                : 'Could not save or read your data. Please try again.',
          ),
        ),
      );
    }
  }
}
