import 'topic_lock.dart';
import 'course_adventure.dart';
export 'course_adventure.dart' show CourseDetail;
import '../data/project_guides.dart';
import 'project_workspace.dart';
import 'localized_text.dart';

import 'package:flutter/material.dart';

import '../application/learning_controller.dart';
import '../domain/curriculum.dart';
import '../domain/portfolio.dart';
import 'app.dart';
import 'theme.dart';

const rubricDimensions = [
  'Correctness',
  'Design',
  'Verification',
  'Usability / accessibility',
  'Reproducibility',
];

class BeginnerScreen extends StatefulWidget {
  const BeginnerScreen({
    super.key,
    required this.controller,
    required this.course,
  });
  final LearningController controller;
  final StudyCourse course;
  @override
  State<BeginnerScreen> createState() => _BeginnerScreenState();
}

class _BeginnerScreenState extends State<BeginnerScreen> {
  int? selected;
  bool checked = false;
  @override
  Widget build(BuildContext context) {
    final guide = widget.course.beginner;
    return Scaffold(
      appBar: AppBar(title: LText(widget.course.title)),
      body: PageBody(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const PageHeading(
              'First steps',
              'Start the first lesson',
              'Take one step at a time. Read, predict, try, and explain.',
            ),
            infoCard('Before you begin', guide.before),
            infoCard('Words you will use', guide.terms.join('\n\n')),
            const SizedBox(height: 16),
            const LText(
              'Worked example',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
            ),
            codeSample(guide.code),
            for (var i = 0; i < guide.trace.length; i++)
              infoCard('Step ${i + 1}', guide.trace[i]),
            const SizedBox(height: 16),
            LText(
              guide.question,
              style: const TextStyle(fontWeight: FontWeight.bold),
            ),
            RadioGroup<int>(
              groupValue: selected,
              onChanged: (value) => setState(() {
                selected = value;
                checked = false;
              }),
              child: Column(
                children: [
                  for (var i = 0; i < guide.options.length; i++)
                    RadioListTile<int>(
                      title: LText(guide.options[i]),
                      value: i,
                    ),
                ],
              ),
            ),
            FilledButton(
              onPressed: selected == null
                  ? null
                  : () => setState(() => checked = true),
              child: const LText('Check readiness'),
            ),
            if (checked)
              infoCard(
                selected == guide.answer
                    ? 'Ready for guided practice'
                    : 'Review and try again',
                selected == guide.answer
                    ? 'You identified the result. Now explain why it happens, then try the task below.'
                    : 'Return to the numbered explanation. Trace each line in order and distinguish code from displayed output. You can retry without losing progress.',
              ),
            infoCard('Guided practice', guide.task),
            ExpansionTile(
              title: const LText('Need a hint?'),
              children: [infoCard('Hint', guide.hint)],
            ),
            ExpansionTile(
              title: const LText('Reference solution — open after trying'),
              children: [
                codeSample(guide.solution),
                infoCard('Expected result', guide.result),
              ],
            ),
            infoCard(
              'Before moving on',
              'Run or trace your solution, compare the result, and explain each line in your own words. Change one value and predict the new result. If you cannot yet explain it, repeat this lesson before the next module.',
            ),
            infoCard(
              'If something goes wrong',
              'Check the file name, capital letters, quotes, brackets, and indentation against the example. Make one change at a time. Save before running. A missing compiler or package is a setup issue: use the listed provisioned tools or ask your teacher; repeated code edits will not install it.',
            ),
            const SizedBox(height: 20),
            FilledButton.icon(
              onPressed: checked && selected == guide.answer
                  ? () async {
                      await safely(
                        context,
                        () => widget.controller.completeIntroduction(
                          widget.course.id,
                        ),
                        success: 'Topic 1 unlocked',
                      );
                      if (context.mounted &&
                          widget.controller.introComplete(widget.course)) {
                        Navigator.pop(context);
                      }
                    }
                  : null,
              icon: const Icon(Icons.check_circle_outline),
              label: const LText('Complete introduction and unlock topic 1'),
            ),
          ],
        ),
      ),
    );
  }
}

Widget codeSample(String source) => Container(
  width: double.infinity,
  margin: const EdgeInsets.symmetric(vertical: 12),
  padding: const EdgeInsets.all(20),
  color: ink,
  child: SelectableText(
    source,
    textDirection: TextDirection.ltr,
    style: const TextStyle(
      color: Colors.white,
      fontFamily: 'LearnMono',
      fontFamilyFallback: ['LearnSans'],
      height: 1.8,
    ),
  ),
);

class CurriculumScreen extends StatefulWidget {
  const CurriculumScreen({super.key, required this.controller});
  final LearningController controller;
  @override
  State<CurriculumScreen> createState() => _CurriculumScreenState();
}

class _CurriculumScreenState extends State<CurriculumScreen> {
  String query = '';
  @override
  Widget build(BuildContext context) {
    final catalog = widget.controller.curriculum.catalog;
    final matches = catalog
        .where(
          (c) =>
              '${c.title} ${tx(context, c.title)} ${c.modules.map((m) => '${m.title} ${tx(context, m.title)}').join(' ')} ${c.projects.map((p) => '${p.title} ${tx(context, p.title)}').join(' ')}'
                  .toLowerCase()
                  .contains(query.toLowerCase()),
        )
        .toList();
    return ListenableBuilder(
      listenable: widget.controller,
      builder: (context, _) => PageBody(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _CourseHero(
              onStart: () => Navigator.of(context).push(
                MaterialPageRoute<void>(
                  builder: (_) => CourseDetail(
                    controller: widget.controller,
                    course: catalog.firstWhere(
                      (course) => course.id == 'python',
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 24),
            TextField(
              decoration: InputDecoration(
                hintText: tx(context, 'Search courses, topics, or projects'),
                prefixIcon: const Icon(Icons.search),
              ),
              onChanged: (value) => setState(() => query = value),
            ),
            const SizedBox(height: 24),
            Row(
              children: [
                const Expanded(
                  child: LText(
                    'Learning paths',
                    style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900),
                  ),
                ),
                LText(
                  '${matches.length} courses',
                  style: TextStyle(
                    color: Theme.of(context).colorScheme.onSurfaceVariant,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 6),
            const LText(
              'Begin with the first available path. New paths unlock as you complete their foundations.',
            ),
            const SizedBox(height: 16),
            if (matches.isEmpty)
              const Padding(
                padding: EdgeInsets.all(24),
                child: LText('No matching courses. Try another topic.'),
              ),
            LayoutBuilder(
              builder: (context, constraints) => GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: matches.length,
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: constraints.maxWidth >= 760 ? 2 : 1,
                  mainAxisExtent: 176,
                  crossAxisSpacing: 14,
                  mainAxisSpacing: 14,
                ),
                itemBuilder: (context, index) {
                  final course = matches[index];
                  final unlocked = widget.controller.courseUnlocked(course);
                  final missing = course.prerequisites
                      .map((id) => catalog.firstWhere((c) => c.id == id))
                      .where((c) => !widget.controller.courseComplete(c))
                      .map((c) => c.title)
                      .join(', ');
                  return _CourseChoiceCard(
                    index: index,
                    course: course,
                    unlocked: unlocked,
                    completed: widget.controller.courseComplete(course),
                    missingPrerequisites: missing,
                    onTap: unlocked
                        ? () => Navigator.of(context).push(
                            MaterialPageRoute<void>(
                              builder: (_) => CourseDetail(
                                controller: widget.controller,
                                course: course,
                              ),
                            ),
                          )
                        : null,
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _CourseHero extends StatelessWidget {
  const _CourseHero({required this.onStart});

  final VoidCallback onStart;

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    return DecoratedBox(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: AlignmentDirectional.topStart,
          end: AlignmentDirectional.bottomEnd,
          colors: [colors.primaryContainer, colors.tertiaryContainer],
        ),
        borderRadius: BorderRadius.circular(28),
      ),
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: LayoutBuilder(
          builder: (context, constraints) {
            final compact = constraints.maxWidth < 620;
            final introduction = Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 7,
                  ),
                  decoration: BoxDecoration(
                    color: colors.surface.withValues(alpha: .75),
                    borderRadius: BorderRadius.circular(99),
                  ),
                  child: const LText(
                    'START HERE',
                    style: TextStyle(fontSize: 11, fontWeight: FontWeight.w900),
                  ),
                ),
                const SizedBox(height: 14),
                LText(
                  'Learn programming step by step',
                  style: Theme.of(context).textTheme.headlineMedium
                      ?.copyWith(fontWeight: FontWeight.w900, height: 1.2),
                ),
                const SizedBox(height: 10),
                const LText(
                  'Never coded before? Begin with Python. We explain every new idea, then help you practise it in a small project.',
                  style: TextStyle(height: 1.6),
                ),
              ],
            );
            final action = FilledButton.icon(
              onPressed: onStart,
              icon: const Icon(Icons.play_arrow_rounded),
              label: const LText('Start with Python'),
            );
            if (compact) {
              return Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [introduction, const SizedBox(height: 18), action],
              );
            }
            return Row(
              children: [
                Expanded(child: introduction),
                const SizedBox(width: 28),
                action,
              ],
            );
          },
        ),
      ),
    );
  }
}

class _CourseChoiceCard extends StatelessWidget {
  const _CourseChoiceCard({
    required this.index,
    required this.course,
    required this.unlocked,
    required this.completed,
    required this.missingPrerequisites,
    required this.onTap,
  });

  final int index;
  final StudyCourse course;
  final bool unlocked, completed;
  final String missingPrerequisites;
  final VoidCallback? onTap;

  IconData get icon => switch (course.id) {
    'python' => Icons.terminal_rounded,
    'web-design' => Icons.palette_outlined,
    'web-development' => Icons.language_rounded,
    'java' || 'kotlin' || 'cpp' => Icons.data_object_rounded,
    'android' => Icons.android_rounded,
    'ios' || 'swift' => Icons.phone_iphone_rounded,
    'javascript' ||
    'reactjs' ||
    'nodejs' ||
    'expressjs' => Icons.javascript_rounded,
    'reactnative' || 'flutter-dart' => Icons.devices_rounded,
    'database-foundations' ||
    'sql' ||
    'sqlite' ||
    'postgresql' ||
    'mongodb' => Icons.storage_rounded,
    _ => Icons.school_outlined,
  };

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    final status = completed
        ? 'Completed'
        : unlocked
        ? 'Ready to start'
        : 'Locked';
    final description = unlocked
        ? course.prerequisites.isEmpty
              ? 'Beginner friendly · no prior experience needed'
              : 'Your next learning path is ready'
        : 'Finish first: $missingPrerequisites';
    final card = Semantics(
      button: true,
      enabled: unlocked,
      label: '${tx(context, course.title)}. ${tx(context, status)}',
      child: Card(
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.all(18),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Container(
                      width: 44,
                      height: 44,
                      decoration: BoxDecoration(
                        color: unlocked
                            ? colors.primaryContainer
                            : colors.surfaceContainerHighest,
                        borderRadius: BorderRadius.circular(14),
                      ),
                      child: Icon(
                        unlocked ? icon : Icons.lock_outline,
                        color: unlocked
                            ? colors.onPrimaryContainer
                            : colors.onSurfaceVariant,
                      ),
                    ),
                    const Spacer(),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 5,
                      ),
                      decoration: BoxDecoration(
                        color: completed
                            ? colors.tertiaryContainer
                            : colors.surfaceContainerHighest,
                        borderRadius: BorderRadius.circular(99),
                      ),
                      child: LText(
                        status,
                        style: const TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.w800,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 12),
                LText(
                  course.title,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                const SizedBox(height: 5),
                Expanded(
                  child: LText(
                    description,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      color: colors.onSurfaceVariant,
                      height: 1.35,
                    ),
                  ),
                ),
                Row(
                  children: [
                    Expanded(
                      child: LText(
                        '${course.modules.length} modules',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(fontSize: 12),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: LText(
                        '${course.projects.length} projects',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(fontSize: 12),
                      ),
                    ),
                    if (unlocked) const Icon(Icons.arrow_forward_rounded),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
    final reduceMotion = MediaQuery.disableAnimationsOf(context);
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: 0, end: 1),
      duration: reduceMotion
          ? Duration.zero
          : Duration(milliseconds: 180 + (index.clamp(0, 8) * 35)),
      curve: Curves.easeOutCubic,
      child: card,
      builder: (context, value, child) => Opacity(
        opacity: value,
        child: Transform.translate(
          offset: Offset(0, 12 * (1 - value)),
          child: child,
        ),
      ),
    );
  }
}

class CourseReferenceScreen extends StatelessWidget {
  const CourseReferenceScreen({
    super.key,
    required this.controller,
    required this.course,
  });
  final LearningController controller;
  final StudyCourse course;
  @override
  Widget build(BuildContext context) => TopicGate(
    controller: controller,
    allowed: () => course.modules.every(controller.moduleComplete),
    child: Scaffold(
      appBar: AppBar(title: LText(course.title)),
      body: ListenableBuilder(
        listenable: controller,
        builder: (context, _) => PageBody(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Card(
                child: ListTile(
                  leading: const Icon(Icons.school_outlined),
                  title: const LText('Start the first lesson'),
                  subtitle: const LText(
                    'Meet the basics with a short example and a guided task.',
                  ),
                  trailing: const Icon(Icons.arrow_forward),
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute<void>(
                      builder: (_) => BeginnerScreen(
                        controller: controller,
                        course: course,
                      ),
                    ),
                  ),
                ),
              ),
              ExpansionTile(
                title: const LText('Before you start: time and tools'),
                children: [
                  LText(
                    '15 guided hours + 42 project hours',
                    style: Theme.of(context).textTheme.titleLarge,
                  ),
                  const SizedBox(height: 8),
                  const LText(
                    'Estimates exclude additional practice. Plans progress from foundations to an independent capstone. Completion requires evidence, not simply reading.',
                  ),
                  const SizedBox(height: 16),
                  LText(
                    'Prerequisites: ${course.prerequisites.isEmpty ? 'No prior programming; basic device and file use.' : course.prerequisites.map((id) => controller.curriculum.catalog.firstWhere((c) => c.id == id).title).join(', ')}',
                  ),
                  for (final id in course.prerequisites)
                    TextButton(
                      onPressed: () => Navigator.of(context).push(
                        MaterialPageRoute<void>(
                          builder: (_) => CourseDetail(
                            controller: controller,
                            course: controller.curriculum.catalog.firstWhere(
                              (c) => c.id == id,
                            ),
                          ),
                        ),
                      ),
                      child: LText(
                        'Open prerequisite: ${controller.curriculum.catalog.firstWhere((c) => c.id == id).title}',
                      ),
                    ),
                  const SizedBox(height: 16),
                  infoCard('Offline development tools', course.tools),
                ],
              ),
              if (course.id == 'python')
                TextButton.icon(
                  onPressed: () => Navigator.of(context).push(
                    MaterialPageRoute<void>(
                      builder: (_) => Scaffold(
                        appBar: AppBar(
                          title: const LText('Interactive Python foundations'),
                        ),
                        body: LibraryScreen(controller: controller),
                      ),
                    ),
                  ),
                  icon: const Icon(Icons.terminal),
                  label: const LText(
                    'Open seven interactive foundation lessons',
                  ),
                ),
              const SizedBox(height: 20),
              LText(
                'Lessons and activities',
                style: Theme.of(context).textTheme.headlineSmall,
              ),
              for (final module in course.modules)
                Card(
                  child: ExpansionTile(
                    title: LText(module.title),
                    subtitle: LText('Two guided activities'),
                    childrenPadding: const EdgeInsets.all(16),
                    expandedCrossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      LText(
                        module.explanation,
                        style: const TextStyle(height: 1.6),
                      ),
                      const SizedBox(height: 12),
                      const LText(
                        'Worked example / design fragment — use the course toolchain',
                      ),
                      const SizedBox(height: 8),
                      Container(
                        width: double.infinity,
                        padding: const EdgeInsets.all(16),
                        color: Theme.of(context)
                            .colorScheme
                            .surfaceContainerHighest,
                        child: SelectableText(
                          module.example,
                          textDirection: TextDirection.ltr,
                          style: const TextStyle(
                            fontFamily: 'LearnMono',
                            height: 1.5,
                          ),
                        ),
                      ),
                      for (final plan in module.plans)
                        ListTile(
                          contentPadding: EdgeInsets.zero,
                          leading: Icon(
                            controller.state.portfolio.containsKey(plan.id)
                                ? Icons.note_alt
                                : Icons.auto_stories_outlined,
                          ),
                          title: LText(plan.title),
                          subtitle: LText('${plan.minutes} minutes'),
                          trailing: const Icon(Icons.arrow_forward),
                          onTap: () => Navigator.of(context).push(
                            MaterialPageRoute<void>(
                              builder: (_) => PlanDetail(
                                controller: controller,
                                plan: plan,
                              ),
                            ),
                          ),
                        ),
                    ],
                  ),
                ),
              const SizedBox(height: 20),
              LText(
                'Real-world projects',
                style: Theme.of(context).textTheme.headlineSmall,
              ),
              const LText(
                'Each assignment includes acceptance conditions and an in-app workspace for four small source or note files. Full builds require the listed development tools.',
              ),
              for (final project in course.projects)
                Card(
                  child: ListTile(
                    contentPadding: const EdgeInsets.all(20),
                    title: LText(project.title),
                    subtitle: LText(
                      '${project.hours} hours · ${controller.state.portfolio[project.id]?.milestones.length ?? 0}/5 milestones self-reported\n${project.brief}',
                    ),
                    trailing: const Icon(Icons.arrow_forward),
                    onTap: () => Navigator.of(context).push(
                      MaterialPageRoute<void>(
                        builder: (_) => ProjectDetail(
                          controller: controller,
                          project: project,
                        ),
                      ),
                    ),
                  ),
                ),
            ],
          ),
        ),
      ),
    ),
  );
}

Widget infoCard(String title, String body) => Card(
  child: Padding(
    padding: const EdgeInsets.all(20),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        LText(
          title,
          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 8),
        LText(
          body,
          protectInlineCode: true,
          style: const TextStyle(height: 1.8, fontSize: 16),
        ),
      ],
    ),
  ),
);

class PlanDetail extends StatelessWidget {
  const PlanDetail({super.key, required this.controller, required this.plan});
  final LearningController controller;
  final LessonPlan plan;
  StudyCourse get course => controller.curriculum.catalog.firstWhere(
    (c) => c.modules.any((m) => m.plans.any((p) => p.id == plan.id)),
  );
  StudyModule get module =>
      course.modules.firstWhere((m) => m.plans.any((p) => p.id == plan.id));
  @override
  Widget build(BuildContext context) => TopicGate(
    controller: controller,
    allowed: () => controller.portfolioUnlocked(plan.id),
    child: Scaffold(
      appBar: AppBar(title: LText(plan.title)),
      body: PageBody(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            infoCard('What you will learn', plan.objective),
            infoCard(
              'Session plan',
              plan.minutes == 60
                  ? 'Retrieval 5 min → worked explanation 15 → guided practice 20 → assessment 15 → reflection 5.'
                  : 'Retrieval 10 min → design 15 → implementation 35 → testing and review 20 → reflection 10.',
            ),
            infoCard(module.title, module.explanation),
            codeSample(module.example),
            FilledButton.icon(
              onPressed: () => Navigator.push(
                context,
                MaterialPageRoute<void>(
                  builder: (_) => ProjectWorkspace(
                    controller: controller,
                    course: course,
                    id: plan.id,
                    title: plan.title,
                    seed: module.example,
                    requirements: [plan.activity, plan.evidence],
                  ),
                ),
              ),
              icon: const Icon(Icons.code),
              label: const LText('Open workspace'),
            ),
            infoCard('Learning activity', plan.activity),
            infoCard('Assessment evidence', plan.evidence),
            infoCard(
              'If you need another attempt',
              'Reduce the example to one record. Trace each state change on paper, explain the failure, then try again with a different input. For an extension, add one justified requirement and regression tests.',
            ),
            PortfolioEditor(
              controller: controller,
              id: plan.id,
              milestones: const [
                'I completed this activity and checked my work.',
              ],
            ),
          ],
        ),
      ),
    ),
  );
}

class ProjectDetail extends StatelessWidget {
  const ProjectDetail({
    super.key,
    required this.controller,
    required this.project,
  });
  final LearningController controller;
  final StudyProject project;
  StudyCourse get course => controller.curriculum.catalog.firstWhere(
    (c) => c.projects.any((p) => p.id == project.id),
  );
  @override
  Widget build(BuildContext context) => TopicGate(
    controller: controller,
    allowed: () => controller.portfolioUnlocked(project.id),
    child: Scaffold(
      appBar: AppBar(title: LText(project.title)),
      body: PageBody(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            infoCard('Project brief · ${project.hours} hours', project.brief),
            if (projectGuides[project.id] case final guide?) ...[
              const SectionLabel('Guided project walkthrough'),
              for (var i = 0; i < guide.steps.length; i++)
                Card(
                  child: ExpansionTile(
                    initiallyExpanded: i == 0,
                    title: LText(
                      const [
                        'The problem',
                        'Follow an example',
                        'Your turn',
                        'Find and fix a mistake',
                        'Make a choice',
                        'Build something of your own',
                      ][i],
                    ),
                    childrenPadding: const EdgeInsets.all(20),
                    children: [
                      Text(
                        isolateInlineCode(
                          tx(
                            context,
                            guide.steps[i],
                          ).split(':').skip(1).join(':').trim(),
                        ),
                        style: const TextStyle(height: 1.7),
                      ),
                    ],
                  ),
                ),
              infoCard(
                'In-app practice scope',
                'The practice workspace runs the calculation and validation core. The full reference program below needs CPython on a computer; its file and database operations cannot run in the teaching interpreter.',
              ),
              ExpansionTile(
                title: const LText('Complete reference program'),
                children: [
                  LText(
                    'Save this source using the filename shown, then use the local commands below.',
                  ),
                  Text(guide.file, textDirection: TextDirection.ltr),
                  codeSample(guide.reference),
                  codeSample(guide.commands),
                  const LText(
                    'Save all three reference programs and test_projects.py in the same folder. Run the command below with CPython; no packages or network are required.',
                  ),
                  ExpansionTile(
                    title: const LText('Reference regression tests'),
                    children: [codeSample(projectReferenceTests)],
                  ),
                  codeSample(projectTestCommand),
                ],
              ),
            ],
            infoCard(
              'Acceptance conditions',
              project.requirements.map((r) => '• $r').join('\n\n'),
            ),

            infoCard(
              'Deliverables',
              'Save small source files and design, usage, and test notes in the workspace. Include fictional fixtures, a component diagram, and one architecture decision. Larger external build folders need a separate backup.',
            ),
            FilledButton.icon(
              onPressed: () => Navigator.push(
                context,
                MaterialPageRoute<void>(
                  builder: (_) => ProjectWorkspace(
                    controller: controller,
                    course: course,
                    id: project.id,
                    title: project.title,
                    seed:
                        projectGuides[project.id]?.starter ??
                        course.beginner.code,
                    requirements: project.requirements,
                  ),
                ),
              ),
              icon: const Icon(Icons.code),
              label: const LText('Open workspace'),
            ),
            PortfolioEditor(
              controller: controller,
              id: project.id,
              milestones: project.milestones,
            ),
          ],
        ),
      ),
    ),
  );
}

class PortfolioEditor extends StatefulWidget {
  const PortfolioEditor({
    super.key,
    required this.controller,
    required this.id,
    this.milestones = const [],
  });
  final LearningController controller;
  final String id;
  final List<String> milestones;
  @override
  State<PortfolioEditor> createState() => _PortfolioEditorState();
}

class _PortfolioEditorState extends State<PortfolioEditor> {
  late final TextEditingController evidence;
  late Set<int> checked;
  late List<int> scores;
  bool busy = false, dirty = false;
  @override
  void initState() {
    super.initState();
    final entry =
        widget.controller.state.portfolio[widget.id] ?? PortfolioEntry();
    evidence = TextEditingController(text: entry.evidence);
    checked = {...entry.milestones};
    scores = [...entry.scores];
  }

  @override
  void dispose() {
    evidence.dispose();
    super.dispose();
  }

  Future<void> save() async {
    setState(() => busy = true);
    await safely(context, () async {
      await widget.controller.savePortfolio(
        widget.id,
        PortfolioEntry(
          evidence: evidence.text,
          milestones: checked,
          scores: scores,
        ),
      );
      if (mounted) setState(() => dirty = false);
    }, success: 'Evidence and self-assessment saved on this device.');
    if (mounted) setState(() => busy = false);
  }

  @override
  Widget build(BuildContext context) => PopScope(
    canPop: !dirty && !busy,
    onPopInvokedWithResult: (didPop, result) async {
      if (didPop || busy) return;
      final discard = await showDialog<bool>(
        context: context,
        builder: (context) => AlertDialog(
          title: const LText('Leave without saving?'),
          content: const LText(
            'Your latest evidence and self-assessment changes have not been saved.',
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context, false),
              child: const LText('Keep editing'),
            ),
            TextButton(
              onPressed: () => Navigator.pop(context, true),
              child: const LText('Discard changes'),
            ),
          ],
        ),
      );
      if (discard == true && context.mounted) {
        setState(() => dirty = false);
        WidgetsBinding.instance.addPostFrameCallback((_) {
          if (context.mounted) Navigator.of(context).pop();
        });
      }
    },
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        if (widget.milestones.isNotEmpty) ...[
          const SizedBox(height: 16),
          LText(
            'Project milestones',
            style: Theme.of(context).textTheme.titleLarge,
          ),
          for (var i = 0; i < widget.milestones.length; i++)
            CheckboxListTile(
              contentPadding: EdgeInsets.zero,
              value: checked.contains(i),
              title: LText(widget.milestones[i]),
              onChanged: busy
                  ? null
                  : (value) => setState(() {
                      dirty = true;
                      value == true ? checked.add(i) : checked.remove(i);
                    }),
            ),
          infoCard(
            'Review your work',
            '0 = absent; 1 = partial with major gaps; 2 = meets requirements with evidence; 3 = meets requirements plus justified edge-case improvements. Aim for every dimension at least 2 and every acceptance condition demonstrated. A teacher or peer should review the evidence; this is not automatic certification.',
          ),
          for (var i = 0; i < rubricDimensions.length; i++)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 8),
              child: DropdownButtonFormField<int>(
                isExpanded: true,
                initialValue: scores[i],
                decoration: InputDecoration(label: LText(rubricDimensions[i])),
                items: [
                  for (var n = 0; n <= 3; n++)
                    DropdownMenuItem(
                      value: n,
                      child: LText(
                        '$n — ${['Absent', 'Partial', 'Meets requirements', 'Improvements'][n]}',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),
                ],
                onChanged: busy
                    ? null
                    : (value) => setState(() {
                        scores[i] = value!;
                        dirty = true;
                      }),
              ),
            ),
        ],
        const SizedBox(height: 20),
        TextField(
          controller: evidence,
          enabled: !busy,
          minLines: 5,
          maxLines: 12,
          maxLength: 4000,
          decoration: InputDecoration(
            label: LText('Evidence and reflection'),
            hintText: tx(
              context,
              'What did you build? Which tests passed or failed? Record file names, decisions, feedback, and your next improvement.',
            ),
          ),
          onChanged: (_) => setState(() => dirty = true),
        ),
        const LText(
          'Use fictional data. Save before leaving this page. External files are not attached to the app backup.',
        ),
        const SizedBox(height: 12),
        FilledButton.icon(
          key: const Key('save-portfolio'),
          onPressed: busy ? null : save,
          icon: const Icon(Icons.save_outlined),
          label: LText(
            busy
                ? 'Saving…'
                : dirty
                ? 'Save evidence • unsaved changes'
                : 'Save evidence',
          ),
        ),
        const SizedBox(height: 24),
      ],
    ),
  );
}
