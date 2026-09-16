import 'topic_lock.dart';

import 'package:flutter/material.dart';

import '../application/learning_controller.dart';
import '../domain/curriculum.dart';
import '../data/module_guides.dart';
import 'sql_practice_screen.dart';
import 'app.dart';
import 'curriculum_screen.dart';
import 'lesson_screen.dart';
import 'localized_text.dart';
import 'theme.dart';

class RewardsPanel extends StatelessWidget {
  const RewardsPanel({super.key, required this.controller});
  final LearningController controller;
  @override
  Widget build(BuildContext context) {
    final rewards = controller.rewards;
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              children: [
                const Icon(
                  Icons.bolt_rounded,
                  color: Color(0xFFFFAB24),
                  size: 32,
                ),
                LText(
                  '${rewards.xp} XP',
                  style: Theme.of(context).textTheme.titleLarge
                      ?.copyWith(fontWeight: FontWeight.w900),
                ),
                const Spacer(),
                LText(
                  'Level ${rewards.level}',
                  style: const TextStyle(fontWeight: FontWeight.w800),
                ),
              ],
            ),
            const SizedBox(height: 12),
            if (!rewards.isComplete)
              TweenAnimationBuilder<double>(
                tween: Tween(end: rewards.levelProgress / 100),
                duration: const Duration(milliseconds: 450),
                builder: (_, value, _) => LinearProgressIndicator(
                  value: value,
                  minHeight: 10,
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            const SizedBox(height: 10),
            LText(
              rewards.isComplete
                  ? 'All foundation missions completed!'
                  : '${100 - rewards.levelProgress} XP to the next level',
            ),
            const SizedBox(height: 16),
            ExpansionTile(
              title: const LText('Your badges'),
              children: [
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (final badge in const [
                      'First spark',
                      'Problem solver',
                      'Lesson champion',
                      'Python explorer',
                    ])
                      Chip(
                        avatar: Icon(
                          rewards.badges.contains(badge)
                              ? Icons.emoji_events_rounded
                              : Icons.lock_outline,
                          size: 18,
                          color: rewards.badges.contains(badge)
                              ? const Color(0xFFB76700)
                              : null,
                        ),
                        label: LText(badge),
                      ),
                  ],
                ),
                const SizedBox(height: 8),
                const LText(
                  'Badges: solve 1 challenge, solve 5 challenges, finish 1 lesson, then finish all 7 foundation lessons.',
                ),
                const SizedBox(height: 8),
                const LText(
                  'Earn 10 XP for each new correct answer and 20 XP for a completed Python lesson. Replays are always free.',
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class CourseDetail extends StatelessWidget {
  const CourseDetail({
    super.key,
    required this.controller,
    required this.course,
  });
  final LearningController controller;
  final StudyCourse course;
  @override
  Widget build(BuildContext context) => TopicGate(
    controller: controller,
    allowed: () => controller.courseUnlocked(course),
    child: ListenableBuilder(
      listenable: controller,
      builder: (context, _) {
        final python = course.id == 'python';
        return Scaffold(
          appBar: AppBar(title: LText(course.title)),
          body: PageBody(
            child: Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 780),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    Container(
                      padding: const EdgeInsets.all(24),
                      decoration: BoxDecoration(
                        gradient: const LinearGradient(
                          colors: [Color(0xFF153D83), Color(0xFF087C89)],
                        ),
                        borderRadius: BorderRadius.circular(28),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Icon(
                            Icons.rocket_launch_rounded,
                            color: Color(0xFFFFCF64),
                            size: 44,
                          ),
                          const SizedBox(height: 16),
                          const LText(
                            'Your coding adventure',
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 28,
                              fontWeight: FontWeight.w900,
                            ),
                          ),
                          const SizedBox(height: 10),
                          LText(
                            python
                                ? 'Follow the path. Solve a challenge. Collect your next badge.'
                                : 'Explore each stop with a short explanation, an example, and a task.',
                            style: const TextStyle(
                              color: Colors.white,
                              height: 1.7,
                            ),
                          ),
                          const SizedBox(height: 20),
                          FilledButton.icon(
                            style: FilledButton.styleFrom(
                              backgroundColor: Colors.white,
                              foregroundColor: ink,
                            ),
                            onPressed: () => Navigator.push(
                              context,
                              MaterialPageRoute<void>(
                                builder: (_) => python
                                    ? LessonScreen(
                                        controller: controller,
                                        lesson: controller.nextLesson,
                                      )
                                    : controller.introComplete(course)
                                    ? WorkshopScreen(
                                        controller: controller,
                                        module: course.modules.firstWhere(
                                          (module) => !controller
                                              .moduleComplete(module),
                                          orElse: () => course.modules.last,
                                        ),
                                      )
                                    : BeginnerScreen(
                                        controller: controller,
                                        course: course,
                                      ),
                              ),
                            ),
                            icon: const Icon(Icons.play_arrow_rounded),
                            label: LText(
                              !python && controller.introComplete(course)
                                  ? 'Continue learning'
                                  : python && controller.completion == 1
                                  ? 'Review the course'
                                  : python && controller.state.solved.isNotEmpty
                                  ? 'Continue learning'
                                  : 'Start learning',
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 20),
                    if (python) RewardsPanel(controller: controller),
                    const SizedBox(height: 28),
                    const LText(
                      'Your mission map',
                      style: TextStyle(
                        fontSize: 23,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                    const SizedBox(height: 8),
                    const LText(
                      'Complete each topic to unlock the next. Finished topics remain available for review.',
                    ),
                    const SizedBox(height: 24),
                    if (python)
                      for (var i = 0; i < controller.lessons.length; i++)
                        MissionStop(
                          locked: !controller.lessonUnlocked(
                            controller.lessons[i],
                          ),
                          index: i,
                          title: controller.lessons[i].title,
                          subtitle:
                              '${controller.solvedIn(controller.lessons[i])}/${controller.lessons[i].exercises.length} challenges',
                          complete:
                              controller.solvedIn(controller.lessons[i]) ==
                              controller.lessons[i].exercises.length,
                          current:
                              controller.lessons[i].id ==
                              controller.nextLesson.id,
                          onTap: () => Navigator.push(
                            context,
                            MaterialPageRoute<void>(
                              builder: (_) => LessonScreen(
                                controller: controller,
                                lesson: controller.lessons[i],
                              ),
                            ),
                          ),
                        ),
                    const SizedBox(height: 16),
                    infoCard(
                      'From foundations to advanced practice',
                      'Finish the earlier topics first. For Python foundations, solve every challenge. For workshops, save evidence and confirm completion in both practice activities. Projects unlock after the workshops.',
                    ),
                    infoCard('Before you begin', course.beginner.before),
                    for (var i = 0; i < course.modules.length; i++)
                      MissionStop(
                        locked: !controller.moduleUnlocked(
                          course,
                          course.modules[i],
                        ),
                        index: i,
                        title: course.modules[i].title,
                        subtitle: i < 3
                            ? 'Build your foundation'
                            : i < 6
                            ? 'Connect your skills'
                            : 'Advanced practice',
                        complete: controller.moduleComplete(course.modules[i]),
                        current: false,
                        onTap: () => Navigator.push(
                          context,
                          MaterialPageRoute<void>(
                            builder: (_) => WorkshopScreen(
                              controller: controller,
                              module: course.modules[i],
                            ),
                          ),
                        ),
                      ),
                    const SizedBox(height: 20),
                    const LText(
                      'Build your first real project',
                      style: TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.w800,
                      ),
                    ),
                    const SizedBox(height: 14),
                    for (final project in course.projects)
                      Padding(
                        padding: const EdgeInsets.only(bottom: 12),
                        child: Card(
                          child: ListTile(
                            contentPadding: const EdgeInsets.all(18),
                            leading: const Icon(
                              Icons.construction_rounded,
                              color: green,
                              size: 32,
                            ),
                            title: LText(project.title),
                            subtitle: LText(
                              controller.portfolioUnlocked(project.id)
                                  ? 'Project challenge'
                                  : 'Topic locked',
                            ),
                            trailing: Icon(
                              controller.portfolioUnlocked(project.id)
                                  ? Icons.chevron_right
                                  : Icons.lock_outline,
                            ),
                            onTap: controller.portfolioUnlocked(project.id)
                                ? () => Navigator.push(
                                    context,
                                    MaterialPageRoute<void>(
                                      builder: (_) => ProjectDetail(
                                        controller: controller,
                                        project: project,
                                      ),
                                    ),
                                  )
                                : null,
                          ),
                        ),
                      ),
                    OutlinedButton.icon(
                      onPressed: () => Navigator.push(
                        context,
                        MaterialPageRoute<void>(
                          builder: (_) => CourseReferenceScreen(
                            controller: controller,
                            course: course,
                          ),
                        ),
                      ),
                      icon: const Icon(Icons.menu_book),
                      label: const LText(
                        'Reference library and advanced tools',
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        );
      },
    ),
  );
}

class MissionStop extends StatelessWidget {
  const MissionStop({
    super.key,
    required this.index,
    required this.title,
    required this.subtitle,
    required this.complete,
    required this.current,
    required this.onTap,
    this.locked = false,
  });
  final int index;
  final String title, subtitle;
  final bool complete, current;
  final bool locked;
  final VoidCallback onTap;
  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.only(bottom: 12),
    child: Card(
      color: complete ? Theme.of(context).colorScheme.primaryContainer : null,
      child: ListTile(
        enabled: !locked,
        onTap: locked ? null : onTap,
        contentPadding: const EdgeInsets.symmetric(
          horizontal: 16,
          vertical: 10,
        ),
        leading: Container(
          width: 48,
          height: 48,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: complete
                ? green
                : current
                ? const Color(0xFF6651D7)
                : Theme.of(context).colorScheme.surfaceContainerHighest,
            borderRadius: BorderRadius.circular(14),
          ),
          child: locked
              ? const Icon(Icons.lock_outline)
              : complete
              ? const Icon(Icons.check_rounded, color: Colors.white)
              : LText(
                  '${index + 1}',
                  style: TextStyle(
                    color: current ? Colors.white : null,
                    fontWeight: FontWeight.w900,
                  ),
                ),
        ),
        title: LText(
          title,
          style: const TextStyle(fontWeight: FontWeight.w800),
        ),
        subtitle: Padding(
          padding: const EdgeInsets.only(top: 6),
          child: LText(
            locked
                ? 'Finish the previous topic to unlock this lesson.'
                : subtitle,
          ),
        ),
        trailing: Icon(locked ? Icons.lock_outline : Icons.chevron_right),
      ),
    ),
  );
}

class WorkshopScreen extends StatefulWidget {
  const WorkshopScreen({
    super.key,
    required this.controller,
    required this.module,
  });
  final LearningController controller;
  final StudyModule module;
  @override
  State<WorkshopScreen> createState() => _WorkshopScreenState();
}

class _WorkshopScreenState extends State<WorkshopScreen> {
  int step = 0;
  Map<String, dynamic>? get guide =>
      moduleGuides[widget.module.plans.first.id] as Map<String, dynamic>? ??
      {
        'trace': widget.module.explanation,
        'practice': widget.module.practice,
        'review': widget.module.plans.first.evidence,
      };
  StudyCourse get course => widget.controller.curriculum.catalog.firstWhere(
    (c) => c.modules.contains(widget.module),
  );
  @override
  Widget build(BuildContext context) => TopicGate(
    controller: widget.controller,
    allowed: () => widget.controller.moduleUnlocked(course, widget.module),
    child: Scaffold(
      appBar: AppBar(title: LText(widget.module.title)),
      body: PageBody(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Wrap(
              spacing: 8,
              children: [
                for (var i = 0; i < 3; i++)
                  ChoiceChip(
                    label: LText(
                      const [
                        'Understand the idea',
                        'See it in action',
                        'Your turn',
                      ][i],
                    ),
                    selected: step == i,
                    onSelected: (_) => setState(() => step = i),
                  ),
              ],
            ),
            const SizedBox(height: 16),
            LinearProgressIndicator(
              value: (step + 1) / 3,
              minHeight: 8,
              borderRadius: BorderRadius.circular(8),
            ),
            const SizedBox(height: 24),
            AnimatedSwitcher(
              duration: MediaQuery.disableAnimationsOf(context)
                  ? Duration.zero
                  : const Duration(milliseconds: 280),
              switchInCurve: Curves.easeOutCubic,
              switchOutCurve: Curves.easeInCubic,
              transitionBuilder: (child, animation) => FadeTransition(
                opacity: animation,
                child: SlideTransition(
                  position: Tween<Offset>(
                    begin: const Offset(.03, 0),
                    end: Offset.zero,
                  ).animate(animation),
                  child: child,
                ),
              ),
              child: Column(
                key: ValueKey(step),
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  LText(
                    const [
                      'Understand the idea',
                      'See it in action',
                      'Your turn',
                    ][step],
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                  const SizedBox(height: 20),
                  if (step == 0) ...[
                    infoCard(
                      'Your learning goal',
                      widget.module.plans.first.objective,
                    ),
                    if (course.modules.indexOf(widget.module) > 0) ...[
                      infoCard(
                        'Build on the previous lesson',
                        'Before starting, explain the previous example in your own words and repeat its practice without copying. If you are unsure, revisit it first.',
                      ),
                      OutlinedButton.icon(
                        icon: const Icon(Icons.history_rounded),
                        label: LText(
                          course
                              .modules[course.modules.indexOf(widget.module) -
                                  1]
                              .title,
                        ),
                        onPressed: () => Navigator.push(
                          context,
                          MaterialPageRoute<void>(
                            builder: (_) => WorkshopScreen(
                              controller: widget.controller,
                              module:
                                  course.modules[course.modules.indexOf(
                                        widget.module,
                                      ) -
                                      1],
                            ),
                          ),
                        ),
                      ),
                    ],
                    if (course.modules.first == widget.module) ...[
                      infoCard('Before you begin', course.beginner.before),
                      infoCard(
                        'Words you will use',
                        course.beginner.terms.join('\n\n'),
                      ),
                    ],
                    LText(
                      widget.module.explanation,
                      protectInlineCode: true,
                      style: const TextStyle(fontSize: 18, height: 1.8),
                    ),
                  ],
                  if (step == 1) ...[
                    infoCard(
                      'Pause and predict',
                      'Before reading the explanation, identify the input, follow each operation, and write the result you expect. Some examples are fragments: check the course tools before trying to run them.',
                    ),
                    codeSample(widget.module.example),
                    if (guide != null)
                      infoCard(
                        'Walk through the example',
                        guide!['trace'] as String,
                      ),
                  ],
                  if (step == 2) ...[
                    if (guide != null) ...[
                      infoCard('Guided practice', guide!['practice'] as String),
                      infoCard('Check your work', guide!['review'] as String),
                    ],
                    if (const {
                      'database-foundations',
                      'sql',
                      'sqlite',
                    }.contains(course.id))
                      FilledButton.icon(
                        onPressed: () => Navigator.push(
                          context,
                          MaterialPageRoute<void>(
                            builder: (_) => const SqlPracticeScreen(),
                          ),
                        ),
                        icon: const Icon(Icons.table_chart_outlined),
                        label: const LText('Open offline SQL practice'),
                      ),
                    infoCard(
                      'Quick checkpoint',
                      'Reproduce the example, change one value, and predict the result. If it fails, find the first step that differs from your prediction and change one thing at a time. Continue when you can complete the task and explain one correction you made.',
                    ),
                    infoCard('Course tools', course.tools),
                    const LText(
                      'These workshops use the course tools. They do not award automatic XP.',
                    ),
                    for (final plan in widget.module.plans)
                      Padding(
                        padding: const EdgeInsets.only(top: 16),
                        child: OutlinedButton(
                          onPressed: () => Navigator.push(
                            context,
                            MaterialPageRoute<void>(
                              builder: (_) => PlanDetail(
                                controller: widget.controller,
                                plan: plan,
                              ),
                            ),
                          ),
                          child: LText(plan.title),
                        ),
                      ),
                  ],
                ],
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: FilledButton(
            onPressed: () {
              if (step < 2) {
                setState(() => step++);
                return;
              }
              Navigator.pop(context);
            },
            child: LText(step < 2 ? 'Continue' : 'Back to course'),
          ),
        ),
      ),
    ),
  );
}
