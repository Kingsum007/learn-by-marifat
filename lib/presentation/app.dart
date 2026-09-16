import 'course_adventure.dart';
import 'sql_practice_screen.dart';
import 'localized_text.dart';

import 'package:flutter/material.dart';

import 'learning_localizations.dart';

import '../application/learning_controller.dart';
import '../data/backup_files.dart';
import '../domain/course.dart';
import 'code_workbench.dart';
import 'lesson_screen.dart';
import 'theme.dart';
import 'curriculum_screen.dart';
import 'about_support_screen.dart';

class LearnApp extends StatelessWidget {
  const LearnApp({super.key, required this.controller});
  final LearningController controller;
  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: controller,
    builder: (context, _) => MaterialApp(
      title: 'Learn By Marifat Team',
      locale: Locale(controller.state.language),
      supportedLocales: const [Locale('en'), Locale('fa'), Locale('ps')],
      localizationsDelegates: learningLocalizations,
      debugShowCheckedModeBanner: false,
      theme: learnTheme(false),
      darkTheme: learnTheme(true),
      themeMode: controller.state.dark ? ThemeMode.dark : ThemeMode.light,
      home: HomeShell(controller: controller),
    ),
  );
}

class HomeShell extends StatefulWidget {
  const HomeShell({super.key, required this.controller});
  final LearningController controller;
  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  int selected = 0;
  void showPage(Widget page) => Navigator.of(context).push(
    MaterialPageRoute<void>(
      builder: (_) => Scaffold(appBar: AppBar(), body: page),
    ),
  );
  @override
  Widget build(BuildContext context) {
    final wide = MediaQuery.sizeOf(context).width >= 900;
    final labels = ['Home', 'Courses', 'Practice'];
    final icons = [
      Icons.home_rounded,
      Icons.auto_stories_rounded,
      Icons.science_outlined,
    ];
    final pages = [
      Dashboard(
        controller: widget.controller,
        onBrowse: () => setState(() => selected = 1),
      ),
      CurriculumScreen(controller: widget.controller),
      PageBody(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const PageHeading(
              'Your space',
              'Practice at your pace.',
              'Start with a lesson. Use these tools when you want to explore.',
            ),
            Card(
              child: ListTile(
                leading: const Icon(Icons.terminal),
                title: const LText('Code lab'),
                subtitle: const LText(
                  'Choose a language, write code, and keep a separate draft for each.',
                ),
                trailing: const Icon(Icons.chevron_right),
                onTap: () => showPage(
                  PageBody(child: CodeWorkbench(controller: widget.controller)),
                ),
              ),
            ),
            Card(
              child: ListTile(
                leading: const Icon(Icons.table_chart_outlined),
                title: const LText('Offline SQL practice'),
                subtitle: const LText(
                  'Explore fictional tables and see real query results.',
                ),
                trailing: const Icon(Icons.chevron_right),
                onTap: () => Navigator.push(
                  context,
                  MaterialPageRoute<void>(
                    builder: (_) => const SqlPracticeScreen(),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 16),
            Card(
              child: ListTile(
                leading: const Icon(Icons.insights),
                title: const LText('Progress'),
                subtitle: const LText('See what you have practiced.'),
                trailing: const Icon(Icons.chevron_right),
                onTap: () =>
                    showPage(ProgressScreen(controller: widget.controller)),
              ),
            ),
          ],
        ),
      ),
    ];
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 76,
        title: const Brand(),
        actions: [
          IconButton(
            tooltip: tx(context, 'Settings'),
            onPressed: () =>
                showPage(SettingsScreen(controller: widget.controller)),
            icon: const Icon(Icons.settings_outlined),
          ),
          const SizedBox(width: 12),
        ],
      ),
      body: SafeArea(
        child: Row(
          children: [
            if (wide)
              NavigationRail(
                selectedIndex: selected,
                onDestinationSelected: (i) => setState(() => selected = i),
                labelType: NavigationRailLabelType.all,
                destinations: [
                  for (var i = 0; i < labels.length; i++)
                    NavigationRailDestination(
                      icon: Icon(icons[i]),
                      label: LText(labels[i]),
                    ),
                ],
              ),
            Expanded(
              child: IndexedStack(index: selected, children: pages),
            ),
          ],
        ),
      ),
      bottomNavigationBar: wide
          ? null
          : NavigationBar(
              selectedIndex: selected,
              onDestinationSelected: (i) => setState(() => selected = i),
              destinations: [
                for (var i = 0; i < labels.length; i++)
                  NavigationDestination(
                    icon: Icon(icons[i]),
                    label: tx(context, labels[i]),
                  ),
              ],
            ),
    );
  }
}

class Brand extends StatelessWidget {
  const Brand({super.key});
  @override
  Widget build(BuildContext context) => Row(
    mainAxisSize: MainAxisSize.min,
    children: [
      ClipRRect(
        borderRadius: BorderRadius.circular(12),
        child: Image.asset(
          'assets/brand/marifat.png',
          width: 64,
          height: 64,
          semanticLabel: 'Marifat Software Team',
        ),
      ),
      const SizedBox(width: 10),
      Flexible(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            LText(
              'Marifat',
              style: Theme.of(context).textTheme.titleLarge
                  ?.copyWith(fontWeight: FontWeight.w800),
            ),
            const LText('Learn by doing', style: TextStyle(fontSize: 12)),
          ],
        ),
      ),
    ],
  );
}

class OfflineBadge extends StatelessWidget {
  const OfflineBadge({super.key});
  @override
  Widget build(BuildContext context) => Container(
    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 7),
    decoration: BoxDecoration(
      color: mint,
      borderRadius: BorderRadius.circular(30),
    ),
    child: const Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(Icons.offline_bolt, color: green, size: 15),
        SizedBox(width: 5),
        LText(
          '100% offline',
          style: TextStyle(
            color: green,
            fontSize: 11,
            fontWeight: FontWeight.w700,
          ),
        ),
      ],
    ),
  );
}

class PageBody extends StatelessWidget {
  const PageBody({super.key, required this.child});
  final Widget child;
  @override
  Widget build(BuildContext context) => SingleChildScrollView(
    child: Center(
      child: Container(
        constraints: const BoxConstraints(maxWidth: 1120),
        padding: EdgeInsets.all(
          MediaQuery.sizeOf(context).width < 600 ? 20 : 40,
        ),
        child: child,
      ),
    ),
  );
}

void openLesson(
  BuildContext context,
  LearningController controller,
  Lesson lesson,
) => Navigator.of(context).push(
  MaterialPageRoute<void>(
    builder: (_) => LessonScreen(controller: controller, lesson: lesson),
  ),
);

class Dashboard extends StatelessWidget {
  const Dashboard({
    super.key,
    required this.controller,
    required this.onBrowse,
  });
  final LearningController controller;
  final VoidCallback onBrowse;
  @override
  Widget build(BuildContext context) => PageBody(
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Wrap(
          spacing: 8,
          runSpacing: 8,
          children: [
            for (final entry in const {
              'fa': 'دری',
              'ps': 'پښتو',
              'en': 'English',
            }.entries)
              ChoiceChip(
                label: Text(entry.value),
                selected: controller.state.language == entry.key,
                onSelected: (_) => safely(
                  context,
                  () => controller.preferences(language: entry.key),
                ),
              ),
          ],
        ),
        const SizedBox(height: 24),
        PageHeading(
          'Welcome to Marifat',
          controller.state.solved.isEmpty
              ? 'Your first step starts here.'
              : 'Welcome back. Let’s continue.',
          'No programming experience needed. We will take it one step at a time.',
        ),
        Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              colors: [Color(0xFF102F61), Color(0xFF087C89)],
            ),
            borderRadius: BorderRadius.circular(24),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const LText(
                'Start with Python',
                style: TextStyle(
                  color: Colors.white70,
                  fontWeight: FontWeight.w600,
                ),
              ),
              const SizedBox(height: 12),
              LText(
                controller.nextLesson.title,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 27,
                  fontWeight: FontWeight.w800,
                ),
              ),
              const SizedBox(height: 10),
              const LText(
                'Read a short example, try one small task, and see what happens.',
                style: TextStyle(color: Colors.white, height: 1.7),
              ),
              const SizedBox(height: 20),
              FilledButton.icon(
                style: FilledButton.styleFrom(
                  backgroundColor: Colors.white,
                  foregroundColor: ink,
                ),
                onPressed: () =>
                    openLesson(context, controller, controller.nextLesson),
                icon: const Icon(Icons.play_arrow_rounded),
                label: LText(
                  controller.state.solved.isEmpty
                      ? 'Start learning'
                      : controller.completion == 1
                      ? 'Review the course'
                      : 'Continue learning',
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: 20),
        RewardsPanel(controller: controller),
        const SizedBox(height: 20),
        Card(
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const LText(
                  'How learning works',
                  style: TextStyle(fontWeight: FontWeight.w800, fontSize: 18),
                ),
                const SizedBox(height: 16),
                for (final item in const [
                  (
                    Icons.visibility_outlined,
                    '1. See an example',
                    'We explain the code before asking you to write it.',
                  ),
                  (
                    Icons.touch_app_outlined,
                    '2. Try it yourself',
                    'Choose an answer, arrange lines, or change a small program.',
                  ),
                  (
                    Icons.favorite_outline,
                    '3. Learn from the result',
                    'Mistakes are welcome. Use a hint and try again.',
                  ),
                ])
                  Padding(
                    padding: const EdgeInsets.only(bottom: 16),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Icon(item.$1, color: green),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              LText(
                                item.$2,
                                style: const TextStyle(
                                  fontWeight: FontWeight.w700,
                                ),
                              ),
                              const SizedBox(height: 4),
                              LText(
                                item.$3,
                                style: const TextStyle(height: 1.6),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
              ],
            ),
          ),
        ),
        const SizedBox(height: 20),
        Card(
          child: ExpansionTile(
            title: const LText('Your learning path'),
            subtitle: LText(
              '${controller.state.solved.length}/${controller.totalExercises} exercises completed',
            ),
            children: [
              for (final lesson in controller.lessons)
                ListTile(
                  leading: Icon(
                    controller.solvedIn(lesson) == lesson.exercises.length
                        ? Icons.check_circle
                        : Icons.circle_outlined,
                    color: green,
                  ),
                  title: LText(lesson.title),
                  onTap: controller.lessonUnlocked(lesson)
                      ? () => openLesson(context, controller, lesson)
                      : null,
                ),
            ],
          ),
        ),
        const SizedBox(height: 16),
        TextButton(
          onPressed: onBrowse,
          child: const LText('Explore other courses'),
        ),
        const Center(child: OfflineBadge()),
      ],
    ),
  );
}

class StatCard extends StatelessWidget {
  const StatCard(this.value, this.label, this.icon, {super.key});
  final String value, label;
  final IconData icon;
  @override
  Widget build(BuildContext context) => Card(
    child: Padding(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(icon, size: 20, color: Theme.of(context).colorScheme.primary),
          const SizedBox(height: 14),
          LText(
            value,
            style: Theme.of(context).textTheme.headlineMedium
                ?.copyWith(fontWeight: FontWeight.w800),
          ),
          const SizedBox(height: 5),
          LText(label, style: const TextStyle(fontSize: 12)),
        ],
      ),
    ),
  );
}

class LessonCard extends StatelessWidget {
  const LessonCard({super.key, required this.controller, required this.lesson});
  final LearningController controller;
  final Lesson lesson;
  @override
  Widget build(BuildContext context) => Card(
    child: InkWell(
      borderRadius: BorderRadius.circular(20),
      onTap: controller.lessonUnlocked(lesson)
          ? () => openLesson(context, controller, lesson)
          : null,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Row(
          children: [
            Container(
              width: 46,
              height: 46,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: mint,
                borderRadius: BorderRadius.circular(14),
              ),
              child: !controller.lessonUnlocked(lesson)
                  ? const Icon(Icons.lock_outline)
                  : controller.solvedIn(lesson) == lesson.exercises.length
                  ? const Icon(Icons.check, color: green)
                  : LText(
                      '${controller.lessons.indexOf(lesson) + 1}'.padLeft(
                        2,
                        '0',
                      ),
                      style: const TextStyle(
                        color: green,
                        fontSize: 17,
                        fontWeight: FontWeight.w800,
                      ),
                    ),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  LText(
                    lesson.title,
                    style: const TextStyle(
                      fontWeight: FontWeight.w800,
                      fontSize: 16,
                    ),
                  ),
                  const SizedBox(height: 5),
                  LText(lesson.summary, style: const TextStyle(fontSize: 13)),
                  const SizedBox(height: 8),
                  LText(
                    '${lesson.minutes} min  ·  ${controller.solvedIn(lesson)}/${lesson.exercises.length} completed',
                    style: TextStyle(
                      fontSize: 11,
                      color: Theme.of(context).colorScheme.primary,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 8),
            const Icon(Icons.arrow_forward, size: 19),
          ],
        ),
      ),
    ),
  );
}

class LibraryScreen extends StatefulWidget {
  const LibraryScreen({super.key, required this.controller});
  final LearningController controller;
  @override
  State<LibraryScreen> createState() => _LibraryScreenState();
}

class _LibraryScreenState extends State<LibraryScreen> {
  String query = '';
  bool bookmarksOnly = false;
  @override
  Widget build(BuildContext context) {
    final lessons = widget.controller.lessons
        .where(
          (l) =>
              (!bookmarksOnly ||
                  widget.controller.state.bookmarks.contains(l.id)) &&
              '${l.title} ${l.summary} ${l.concept}'.toLowerCase().contains(
                query.toLowerCase(),
              ),
        )
        .toList();
    return PageBody(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const PageHeading(
            'The complete course',
            'A foundation you can build on.',
            'Seven guided lessons. Learn in order, or revisit a concept whenever you need it.',
          ),
          TextField(
            onChanged: (value) => setState(() => query = value),
            decoration: const InputDecoration(
              prefixIcon: Icon(Icons.search),
              label: LText('Search lessons and concepts'),
            ),
          ),
          const SizedBox(height: 12),
          FilterChip(
            label: const LText('Bookmarked lessons'),
            selected: bookmarksOnly,
            onSelected: (value) => setState(() => bookmarksOnly = value),
          ),
          const SizedBox(height: 20),
          if (lessons.isEmpty)
            const Padding(
              padding: EdgeInsets.symmetric(vertical: 32),
              child: LText(
                'No lessons found. Try another search or turn off the bookmark filter.',
              ),
            ),
          ...lessons.map(
            (lesson) => Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: LessonCard(controller: widget.controller, lesson: lesson),
            ),
          ),
        ],
      ),
    );
  }
}

class ProgressScreen extends StatelessWidget {
  const ProgressScreen({super.key, required this.controller});
  final LearningController controller;
  @override
  Widget build(BuildContext context) => PageBody(
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const PageHeading(
          'See how far you have come',
          'Every attempt is a step forward.',
          'Python foundation exercise results and your wider learning portfolio are saved on this device.',
        ),
        Card(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                LText(
                  '${controller.state.solved.length} of ${controller.totalExercises} exercises complete',
                  style: Theme.of(context).textTheme.titleLarge
                      ?.copyWith(fontWeight: FontWeight.w800),
                ),
                const SizedBox(height: 16),
                LinearProgressIndicator(
                  value: controller.completion,
                  minHeight: 10,
                  borderRadius: BorderRadius.circular(10),
                  semanticsLabel: tx(context, 'Course completion'),
                  semanticsValue: tx(
                    context,
                    '${(controller.completion * 100).round()} percent',
                  ),
                ),
                const SizedBox(height: 16),
                LText(
                  '${controller.state.attempts.values.fold(0, (a, b) => a + b)} total submissions · No streaks to lose. Learn at your own pace.',
                ),
              ],
            ),
          ),
        ),
        const SizedBox(height: 24),
        infoCard(
          'Learning portfolio',
          '${controller.state.portfolio.length} saved evidence entries across 15 curricula. Project milestones and rubric scores are self-assessed; they do not change your automatically graded Python exercise results. Open Courses to continue a plan or project.',
        ),
        ...controller.lessons.map(
          (lesson) => Padding(
            padding: const EdgeInsets.only(bottom: 12),
            child: LessonCard(controller: controller, lesson: lesson),
          ),
        ),
        if (controller.completion == 1)
          const Card(
            child: Padding(
              padding: EdgeInsets.all(24),
              child: LText(
                'You completed Python fundamentals! Try rewriting the examples without looking, then test your understanding on a full Python environment.',
              ),
            ),
          ),
      ],
    ),
  );
}

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key, required this.controller});
  final LearningController controller;
  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool busy = false;
  final files = BackupFiles();
  Future<void> backup(bool restore) async {
    setState(() => busy = true);
    await safely(context, () async {
      if (restore) {
        final source = await files.import(
          title: tx(context, 'Open Learn By Marifat Team backup'),
        );
        if (source == null || !mounted) {
          return;
        }
        final preview = widget.controller.validateBackup(source);
        final confirmed = await showDialog<bool>(
          context: context,
          builder: (context) => AlertDialog(
            title: const LText('Restore this backup?'),
            content: LText(
              'This backup contains ${preview.solved.length} completed exercises, ${preview.drafts.length} drafts, and ${preview.portfolio.length} portfolio entries. '
              'It will replace the progress, saved drafts, and preferences on this device. Export your current data first if you want to keep it.',
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context, false),
                child: const LText('Cancel'),
              ),
              FilledButton(
                onPressed: () => Navigator.pop(context, true),
                child: const LText('Replace & restore'),
              ),
            ],
          ),
        );
        if (confirmed != true) {
          return;
        }
        await widget.controller.importBackup(source);
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(
              content: LText('Backup restored, including saved code drafts.'),
            ),
          );
        }
      } else {
        final saved = await files.export(
          await widget.controller.exportBackup(),
          title: mounted
              ? tx(context, 'Save Learn By Marifat Team backup')
              : 'Save Learn By Marifat Team backup',
        );
        if (mounted && saved) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(
              content: LText(
                'Backup exported. Keep a copy outside this device.',
              ),
            ),
          );
        }
      }
    });
    if (mounted) {
      setState(() => busy = false);
    }
  }

  @override
  Widget build(BuildContext context) => PageBody(
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const PageHeading(
          'Make it yours',
          'Your learning. Your device.',
          'No account, no subscription, and no connection required.',
        ),
        Card(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SectionLabel('Appearance'),
                SwitchListTile(
                  contentPadding: EdgeInsets.zero,
                  title: const LText('Dark appearance'),
                  subtitle: const LText('A softer workspace in low light'),
                  value: widget.controller.state.dark,
                  onChanged: (value) => safely(
                    context,
                    () => widget.controller.preferences(dark: value),
                  ),
                ),
                const Divider(),
                const SizedBox(height: 16),
                const LText(
                  'Learning language',
                  style: TextStyle(fontWeight: FontWeight.w700),
                ),
                const SizedBox(height: 12),
                Wrap(
                  spacing: 10,
                  runSpacing: 8,
                  children: [
                    for (final entry in {
                      'en': 'English',
                      'fa': 'دری',
                      'ps': 'پښتو',
                    }.entries)
                      ChoiceChip(
                        label: LText(entry.value),
                        selected: widget.controller.state.language == entry.key,
                        onSelected: (_) => safely(
                          context,
                          () => widget.controller.preferences(
                            language: entry.key,
                          ),
                        ),
                      ),
                  ],
                ),
                const SizedBox(height: 12),
                const LText(
                  'Choose English, Dari, or Pashto for the interface and learning content. Code and program output keep their original spelling. Translations still require native-speaker review.',
                  style: TextStyle(fontSize: 12, height: 1.6),
                ),
              ],
            ),
          ),
        ),
        const SizedBox(height: 20),
        Card(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SectionLabel('Keep your progress'),
                const SizedBox(height: 14),
                const LText(
                  'A backup you can carry.',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.w800),
                ),
                const SizedBox(height: 10),
                const LText(
                  'Export progress and saved code to a JSON file. Transfer it using local storage or USB. '
                  'Uninstalling the app can erase local data. Backups are readable files; store them where you trust.',
                  style: TextStyle(height: 1.7),
                ),
                const SizedBox(height: 20),
                Wrap(
                  spacing: 12,
                  runSpacing: 12,
                  children: [
                    FilledButton.icon(
                      onPressed: busy ? null : () => backup(false),
                      icon: const Icon(Icons.file_upload_outlined),
                      label: const LText('Export backup'),
                    ),
                    OutlinedButton.icon(
                      onPressed: busy ? null : () => backup(true),
                      icon: const Icon(Icons.file_download_outlined),
                      label: const LText('Restore backup'),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
        const SizedBox(height: 24),
        Card(
          child: ListTile(
            contentPadding: const EdgeInsets.all(20),
            leading: const Icon(Icons.favorite_outline, color: green),
            title: const LText('About, contact, and support'),
            subtitle: const LText(
              'Meet Marifat Team and find the HesabPay support number.',
            ),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => Navigator.push(
              context,
              MaterialPageRoute<void>(
                builder: (_) => const AboutSupportScreen(),
              ),
            ),
          ),
        ),
        const SizedBox(height: 24),
        const LanguageGuide(),
        const SizedBox(height: 24),
        const LText(
          'Learn By Marifat Team 3.1 · 20 offline courses\nOriginal course content. A local-first learning application for Afghan CS students. '
          'No analytics, remote services, or online activation. Practice scores are learning aids, not formal credentials.',
          style: TextStyle(fontSize: 12, height: 1.8),
        ),
        TextButton(
          onPressed: () => showLicensePage(
            context: context,
            applicationName: 'Learn By Marifat Team',
            applicationVersion: '3.1.0',
          ),
          child: const LText('Open-source licenses'),
        ),
      ],
    ),
  );
}
