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
  const BeginnerScreen({super.key, required this.course});
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
      fontFamily: 'monospace',
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
    final matches = catalog.where(
      (c) =>
          '${c.title} ${tx(context, c.title)} ${c.modules.map((m) => '${m.title} ${tx(context, m.title)}').join(' ')} ${c.projects.map((p) => '${p.title} ${tx(context, p.title)}').join(' ')}'
              .toLowerCase()
              .contains(query.toLowerCase()),
    );
    return PageBody(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const PageHeading(
            'Learn By Marifat Team',
            'Choose your course.',
            'Choose something you would like to build.',
          ),
          const LText(
            'New to programming? Start with Python. Some advanced courses need additional tools; each course explains what is needed.',
          ),
          const SizedBox(height: 16),
          FilledButton.icon(
            onPressed: () => Navigator.of(context).push(
              MaterialPageRoute<void>(
                builder: (_) => Scaffold(
                  appBar: AppBar(
                    title: const LText('Interactive Python foundations'),
                  ),
                  body: LibraryScreen(controller: widget.controller),
                ),
              ),
            ),
            icon: const Icon(Icons.play_arrow),
            label: const LText('Practice Python foundations'),
          ),
          const SizedBox(height: 20),
          TextField(
            decoration: InputDecoration(
              label: LText('Search courses, topics, or projects'),
              prefixIcon: Icon(Icons.search),
            ),
            onChanged: (value) => setState(() => query = value),
          ),
          const SizedBox(height: 16),
          if (matches.isEmpty)
            const Padding(
              padding: EdgeInsets.all(24),
              child: LText('No matching courses. Try another topic.'),
            ),
          for (final course in matches)
            Card(
              child: ListTile(
                contentPadding: const EdgeInsets.all(20),
                title: LText(
                  course.title,
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
                subtitle: Padding(
                  padding: const EdgeInsets.only(top: 8),
                  child: LText(
                    course.prerequisites.isEmpty
                        ? 'Start here — no experience needed'
                        : 'Build on what you already know',
                  ),
                ),
                trailing: const Icon(Icons.arrow_forward),
                onTap: () => Navigator.of(context).push(
                  MaterialPageRoute<void>(
                    builder: (_) => CourseDetail(
                      controller: widget.controller,
                      course: course,
                    ),
                  ),
                ),
              ),
            ),
        ],
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
  Widget build(BuildContext context) => Scaffold(
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
                    builder: (_) => BeginnerScreen(course: course),
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
                label: const LText('Open seven interactive foundation lessons'),
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
                          fontFamily: 'monospace',
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
                            builder: (_) =>
                                PlanDetail(controller: controller, plan: plan),
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
        LText(body, style: const TextStyle(height: 1.6)),
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
  Widget build(BuildContext context) => Scaffold(
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
          PortfolioEditor(controller: controller, id: plan.id),
        ],
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
  Widget build(BuildContext context) => Scaffold(
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
