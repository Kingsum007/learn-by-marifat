import 'topic_lock.dart';
import 'reward_feedback.dart';
import 'localized_text.dart';

import 'package:flutter/material.dart';

import '../application/learning_controller.dart';
import '../domain/assessment.dart';
import '../domain/course.dart';
import '../data/detailed_foundations.dart';
import 'code_workbench.dart';
import 'theme.dart';

class LessonScreen extends StatefulWidget {
  const LessonScreen({
    super.key,
    required this.controller,
    required this.lesson,
  });
  final LearningController controller;
  final Lesson lesson;
  @override
  State<LessonScreen> createState() => _LessonScreenState();
}

class _LessonScreenState extends State<LessonScreen> {
  late int step;
  @override
  void initState() {
    super.initState();
    step = widget.controller.solvedIn(widget.lesson) > 0 ? 2 : 0;
  }

  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: widget.controller,
    builder: (context, _) {
      if (!widget.controller.lessonUnlocked(widget.lesson)) {
        return TopicGate(
          controller: widget.controller,
          allowed: () => false,
          child: const SizedBox(),
        );
      }
      final lesson = widget.lesson;
      final controller = widget.controller;
      final guide =
          (detailedFoundations[lesson.id]
                  as Map<String, dynamic>?)?[controller.state.language]
              as List<dynamic>?;
      final complete = controller.solvedIn(lesson) == lesson.exercises.length;
      final labels = [
        'Understand the idea',
        'See it in action',
        'Try it yourself',
      ];
      void advance() {
        if (step < 2) {
          setState(() => step++);
          return;
        }
        if (complete) {
          final index = controller.lessons.indexOf(lesson);
          if (index + 1 < controller.lessons.length) {
            Navigator.of(context).pushReplacement(
              MaterialPageRoute<void>(
                builder: (_) => LessonScreen(
                  controller: controller,
                  lesson: controller.lessons[index + 1],
                ),
              ),
            );
          } else {
            Navigator.of(context).pop();
          }
          return;
        }
        final exercise = lesson.exercises.firstWhere(
          (e) => !controller.state.solved.contains(e.id),
        );
        Navigator.of(context).push(
          MaterialPageRoute<void>(
            builder: (_) =>
                ExerciseScreen(controller: controller, exercise: exercise),
          ),
        );
      }

      return Scaffold(
        appBar: AppBar(
          title: const LText('Python fundamentals'),
          actions: [
            IconButton(
              tooltip: tx(context, 'Bookmark lesson'),
              onPressed: () =>
                  safely(context, () => controller.toggleBookmark(lesson.id)),
              icon: Icon(
                controller.state.bookmarks.contains(lesson.id)
                    ? Icons.bookmark
                    : Icons.bookmark_outline,
              ),
            ),
          ],
        ),
        body: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 760),
            child: ListView(
              padding: const EdgeInsets.all(24),
              children: [
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (var i = 0; i < 3; i++)
                      ChoiceChip(
                        label: LText(labels[i]),
                        selected: step == i,
                        onSelected: (_) => setState(() => step = i),
                      ),
                  ],
                ),
                const SizedBox(height: 24),
                LText(
                  lesson.title,
                  style: Theme.of(context).textTheme.headlineMedium
                      ?.copyWith(fontWeight: FontWeight.w800),
                ),
                const SizedBox(height: 12),
                LText(
                  lesson.summary,
                  style: Theme.of(context).textTheme.bodyLarge,
                ),
                const SizedBox(height: 24),
                if (step == 0)
                  Card(
                    child: Padding(
                      padding: const EdgeInsets.all(24),
                      child: LText(
                        guide?[0] as String? ?? lesson.concept,
                        protectInlineCode: true,
                        style: const TextStyle(height: 1.9, fontSize: 17),
                      ),
                    ),
                  ),
                if (step == 1) ...[
                  const LText('Read the code'),
                  const SizedBox(height: 12),
                  Container(
                    padding: const EdgeInsets.all(24),
                    decoration: BoxDecoration(
                      color: ink,
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: SelectableText(
                      lesson.example,
                      textDirection: TextDirection.ltr,
                      style: const TextStyle(
                        color: Colors.white,
                        fontFamily: 'LearnMono',
                        height: 1.8,
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),
                  if (guide != null) ...[
                    LText(
                      guide[1] as String,
                      protectInlineCode: true,
                      style: const TextStyle(height: 1.9, fontSize: 17),
                    ),
                    const SizedBox(height: 16),
                    const LText('Output'),
                    Container(
                      width: double.infinity,
                      padding: const EdgeInsets.all(16),
                      margin: const EdgeInsets.symmetric(vertical: 12),
                      decoration: BoxDecoration(
                        border: Border.all(
                          color: Theme.of(context).colorScheme.outline,
                        ),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: SelectableText(
                        foundationOutputs[lesson.id] as String,
                        textDirection: TextDirection.ltr,
                        style: const TextStyle(
                          fontFamily: 'LearnMono',
                          height: 1.7,
                        ),
                      ),
                    ),
                  ],
                  LText(
                    lesson.takeaway,
                    protectInlineCode: true,
                    style: const TextStyle(height: 1.8),
                  ),
                ],
                if (step == 2) ...[
                  if (guide != null) ...[
                    LText(
                      guide[2] as String,
                      protectInlineCode: true,
                      style: const TextStyle(height: 1.9, fontSize: 17),
                    ),
                    const SizedBox(height: 20),
                  ],
                  LText(
                    complete ? 'You finished this lesson. Well done.' : 'Try one activity at a time. You can always use a hint.',
                    style: const TextStyle(height: 1.8),
                  ),
                  const SizedBox(height: 16),
                  for (final exercise in lesson.exercises)
                    Card(
                      child: ListTile(
                        leading: Icon(
                          controller.state.solved.contains(exercise.id)
                              ? Icons.check_circle
                              : Icons.circle_outlined,
                          color: green,
                        ),
                        title: LText(switch (exercise.kind) {
                          ExerciseKind.choice => 'Check your understanding',
                          ExerciseKind.order => 'Arrange the code',
                          ExerciseKind.code => 'Write a program',
                        }),
                        trailing: const Icon(Icons.chevron_right),
                        onTap: () => Navigator.of(context).push(
                          MaterialPageRoute<void>(
                            builder: (_) => ExerciseScreen(
                              controller: controller,
                              exercise: exercise,
                            ),
                          ),
                        ),
                      ),
                    ),
                ],
              ],
            ),
          ),
        ),
        bottomNavigationBar: SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(20, 12, 20, 16),
            child: FilledButton.icon(
              onPressed: advance,
              icon: const Icon(Icons.arrow_forward_rounded),
              label: LText(
                step == 0
                    ? 'See an example'
                    : step == 1
                    ? 'Try it yourself'
                    : complete
                    ? (controller.lessons.last == lesson
                          ? 'Back to home'
                          : 'Next lesson')
                    : 'Try the next activity',
              ),
            ),
          ),
        ),
      );
    },
  );
}

class ExerciseScreen extends StatefulWidget {
  const ExerciseScreen({
    super.key,
    required this.controller,
    required this.exercise,
  });
  final LearningController controller;
  final Exercise exercise;
  @override
  State<ExerciseScreen> createState() => _ExerciseScreenState();
}

class _ExerciseScreenState extends State<ExerciseScreen> {
  int? choice;
  late List<String> blocks;
  bool busy = false;
  Assessment? feedback;
  int earned = 0;
  @override
  void initState() {
    super.initState();
    blocks = widget.exercise.blocks.reversed.toList();
  }

  Future<void> check() async {
    final prior = widget.controller.rewards.xp;
    setState(() {
      busy = true;
      earned = 0;
    });
    await safely(context, () async {
      final result = widget.exercise.kind == ExerciseKind.choice
          ? await widget.controller.submitChoice(widget.exercise, choice!)
          : await widget.controller.submitOrder(widget.exercise, blocks);
      if (mounted) {
        setState(() {
          feedback = result;
          earned = widget.controller.rewards.xp - prior;
        });
      }
    });
    if (mounted) {
      setState(() => busy = false);
    }
  }

  @override
  Widget build(BuildContext context) => TopicGate(
    controller: widget.controller,
    allowed: () => widget.controller.exerciseUnlocked(widget.exercise),
    child: Scaffold(
      appBar: AppBar(title: const LText('Practice')),
      body: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 800),
          child: ListView(
            padding: const EdgeInsets.all(24),
            children: [
              PageHeading(
                'Learn by doing',
                widget.exercise.kind == ExerciseKind.code
                    ? 'Your turn to code.'
                    : 'A small challenge.',
                widget.exercise.prompt,
              ),
              if (widget.exercise.kind == ExerciseKind.code)
                CodeWorkbench(
                  controller: widget.controller,
                  exercise: widget.exercise,
                )
              else ...[
                if (widget.exercise.kind == ExerciseKind.choice)
                  ...widget.exercise.options.asMap().entries.map(
                    (entry) => Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: Semantics(
                        selected: choice == entry.key,
                        child: OutlinedButton(
                          onPressed: busy
                              ? null
                              : () => setState(() {
                                  choice = entry.key;
                                  feedback = null;
                                }),
                          style: OutlinedButton.styleFrom(
                            backgroundColor: choice == entry.key
                                ? Theme.of(context).colorScheme.primaryContainer
                                : null,
                          ),
                          child: Align(
                            alignment: Alignment.centerLeft,
                            child: LText(
                              '${String.fromCharCode(65 + entry.key)}.  ${entry.value}',
                            ),
                          ),
                        ),
                      ),
                    ),
                  )
                else ...[
                  const LText(
                    'Move each line up or down. Keep the indentation shown.',
                  ),
                  const SizedBox(height: 12),
                  ...blocks.asMap().entries.map(
                    (entry) => Padding(
                      padding: const EdgeInsets.only(bottom: 8),
                      child: Card(
                        child: Padding(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 12,
                            vertical: 8,
                          ),
                          child: Row(
                            children: [
                              Expanded(
                                child: Text(
                                  entry.value,
                                  textDirection: TextDirection.ltr,
                                  style: const TextStyle(
                                    fontFamily: 'LearnMono',
                                  ),
                                ),
                              ),
                              IconButton(
                                tooltip: tx(
                                  context,
                                  'Move line ${entry.key + 1} up',
                                ),
                                onPressed: busy || entry.key == 0
                                    ? null
                                    : () => setState(() {
                                        final value = blocks.removeAt(
                                          entry.key,
                                        );
                                        blocks.insert(entry.key - 1, value);
                                        feedback = null;
                                      }),
                                icon: const Icon(Icons.arrow_upward, size: 20),
                              ),
                              IconButton(
                                tooltip: tx(
                                  context,
                                  'Move line ${entry.key + 1} down',
                                ),
                                onPressed:
                                    busy || entry.key == blocks.length - 1
                                    ? null
                                    : () => setState(() {
                                        final value = blocks.removeAt(
                                          entry.key,
                                        );
                                        blocks.insert(entry.key + 1, value);
                                        feedback = null;
                                      }),
                                icon: const Icon(
                                  Icons.arrow_downward,
                                  size: 20,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
                const SizedBox(height: 16),
                FilledButton(
                  onPressed:
                      busy ||
                          (widget.exercise.kind == ExerciseKind.choice &&
                              choice == null)
                      ? null
                      : check,
                  child: LText(busy ? 'Saving…' : 'Check answer'),
                ),
                if (feedback != null) ...[
                  const SizedBox(height: 20),
                  FeedbackPanel(feedback!),
                  if (earned > 0) RewardFeedback(points: earned),
                ],
              ],
              const SizedBox(height: 24),
              TextButton.icon(
                onPressed: () => Navigator.of(context).pop(),
                icon: const Icon(Icons.arrow_back),
                label: const LText('Back to lesson'),
              ),
            ],
          ),
        ),
      ),
    ),
  );
}
