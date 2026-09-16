import 'topic_lock.dart';
import '../data/project_guides.dart';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../application/learning_controller.dart';
import '../domain/curriculum.dart';
import '../runtime/python_vm.dart';
import 'app.dart';
import 'localized_text.dart';
import 'theme.dart';

/// Local text workspace. It does not pretend to compile unsupported languages.
class ProjectWorkspace extends StatefulWidget {
  const ProjectWorkspace({
    super.key,
    required this.controller,
    required this.course,
    required this.id,
    required this.title,
    required this.seed,
    required this.requirements,
  });
  final LearningController controller;
  final StudyCourse course;
  final String id, title, seed;
  final List<String> requirements;
  @override
  State<ProjectWorkspace> createState() => _ProjectWorkspaceState();
}

class _ProjectWorkspaceState extends State<ProjectWorkspace> {
  late Map<String, String> files;
  late String selected;
  late final TextEditingController editor;
  bool busy = false, dirty = false;
  RunResult? result;
  String get mainFile => switch (widget.course.id) {
    'python' => 'main.py',
    'java' => 'Main.java',
    'kotlin' || 'android' => 'Main.kt',
    'swift' || 'ios' => 'main.swift',
    'cpp' => 'main.cpp',
    'web-design' => 'index.html',
    'reactjs' || 'reactnative' => 'App.jsx',
    'flutter-dart' => 'main.dart',
    _ => 'main.js',
  };
  @override
  void initState() {
    super.initState();
    final saved = widget.controller.state.portfolio[widget.id]?.files;
    files = saved != null && saved.isNotEmpty
        ? {...saved}
        : {
            mainFile: widget.seed,
            'README.md': '',
            'TESTS.md': '',
            'NOTES.md': '',
          };
    selected = files.keys.first;
    editor = TextEditingController(text: files[selected]);
  }

  @override
  void dispose() {
    editor.dispose();
    super.dispose();
  }

  Future<bool> save() async {
    files[selected] = editor.text;
    var success = false;
    await safely(context, () async {
      await widget.controller.saveWorkspace(widget.id, files);
      success = true;
      if (mounted) setState(() => dirty = false);
    }, success: 'Workspace files saved on this device.');
    return success;
  }

  Future<void> loadSolution() async {
    final guide = projectGuides[widget.id];
    if (guide == null) return;
    final replace = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const LText('Replace current source?'),
        content: const LText(
          'This replaces the current source with the practice solution. Your previous saved version stays unchanged until you press Save files.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const LText('Keep editing'),
          ),
          FilledButton(
            onPressed: () => Navigator.pop(context, true),
            child: const LText('Load practice solution'),
          ),
        ],
      ),
    );
    if (replace == true && mounted) {
      setState(() {
        editor.text = guide.solution;
        dirty = true;
        result = null;
      });
    }
  }

  Future<void> run() async {
    setState(() => busy = true);
    try {
      if (await save()) {
        final output = await widget.controller.runner.run(editor.text);
        if (mounted) setState(() => result = output);
      }
    } finally {
      if (mounted) setState(() => busy = false);
    }
  }

  @override
  Widget build(BuildContext context) => TopicGate(
    controller: widget.controller,
    allowed: () => widget.controller.portfolioUnlocked(widget.id),
    child: PopScope(
      canPop: !dirty && !busy,
      onPopInvokedWithResult: (didPop, value) async {
        if (didPop || busy) return;
        final discard = await showDialog<bool>(
          context: context,
          builder: (context) => AlertDialog(
            title: const LText('Leave without saving?'),
            content: const LText('Your source changes have not been saved.'),
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
        if (discard == true && mounted) {
          setState(() => dirty = false);
          WidgetsBinding.instance.addPostFrameCallback((_) {
            if (mounted) Navigator.pop(context);
          });
        }
      },
      child: Scaffold(
        appBar: AppBar(title: LText(widget.title)),
        body: PageBody(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const PageHeading(
                'In-app workspace',
                'Write, save, and revise.',
                'Your files are stored locally and included in your exported backup.',
              ),
              LText(
                projectGuides.containsKey(widget.id)
                    ? 'Complete the practice function, run the supplied examples, and compare with the expected output. These examples check the core rules, not the full project requirements.'
                    : 'The initial code is a small teaching example, not a completed project. Extend it to meet the requirements below.',
              ),
              const SizedBox(height: 12),
              for (final requirement in widget.requirements)
                Padding(
                  padding: const EdgeInsets.only(bottom: 8),
                  child: LText('• $requirement'),
                ),
              const SizedBox(height: 12),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final name in files.keys)
                    ChoiceChip(
                      label: Text(name, textDirection: TextDirection.ltr),
                      selected: selected == name,
                      onSelected: busy
                          ? null
                          : (_) => setState(() {
                              files[selected] = editor.text;
                              selected = name;
                              editor.text = files[name]!;
                              result = null;
                            }),
                    ),
                ],
              ),
              const SizedBox(height: 16),
              Directionality(
                textDirection: TextDirection.ltr,
                child: TextField(
                  key: const Key('workspace-editor'),
                  controller: editor,
                  enabled: !busy,
                  minLines: 12,
                  maxLines: 24,
                  autocorrect: false,
                  enableSuggestions: false,
                  keyboardType: TextInputType.multiline,
                  style: const TextStyle(fontFamily: 'LearnMono', height: 1.6),
                  inputFormatters: [LengthLimitingTextInputFormatter(12000)],
                  decoration: const InputDecoration(
                    label: LText('Source or project notes'),
                    helper: LText(
                      'Each file supports up to 12,000 characters. Save before leaving.',
                    ),
                  ),
                  onChanged: (_) => setState(() {
                    dirty = true;
                    result = null;
                  }),
                ),
              ),
              const SizedBox(height: 12),
              Wrap(
                spacing: 12,
                runSpacing: 8,
                children: [
                  FilledButton.icon(
                    key: const Key('save-workspace'),
                    onPressed: busy
                        ? null
                        : () async {
                            setState(() => busy = true);
                            await save();
                            if (mounted) setState(() => busy = false);
                          },
                    icon: const Icon(Icons.save),
                    label: LText(
                      dirty ? 'Save files • unsaved changes' : 'Save files',
                    ),
                  ),
                  if (widget.course.id == 'python' && selected.endsWith('.py'))
                    OutlinedButton.icon(
                      onPressed: busy ? null : run,
                      icon: const Icon(Icons.play_arrow),
                      label: const LText('Run with teaching Python'),
                    ),
                ],
              ),
              const SizedBox(height: 16),
              LText(
                widget.course.id == 'python'
                    ? 'Execution uses the documented Python subset. Imports, files, classes, and full CPython are not supported. Output is not an automatic project grade.'
                    : 'Source editing and storage work here. This language has no embedded compiler in this release; these files are not being executed or automatically graded.',
              ),
              if (result != null) ...[
                const SizedBox(height: 16),
                const LText('OUTPUT'),
                SelectableText(
                  result!.output,
                  textDirection: TextDirection.ltr,
                  style: const TextStyle(fontFamily: 'LearnMono'),
                ),
                if (result!.error != null) LText(result!.error!),
              ],
              if (projectGuides[widget.id] case final guide?) ...[
                const SizedBox(height: 16),
                const LText('Expected practice output'),
                SelectableText(
                  guide.expected,
                  textDirection: TextDirection.ltr,
                ),
                if (selected == mainFile)
                  TextButton(
                    onPressed: busy ? null : loadSolution,
                    child: const LText('Load practice solution'),
                  ),
                const LText(
                  'Explain each result before viewing the solution. Matching output is practice feedback, not certification of a complete project.',
                ),
              ],
              const SizedBox(height: 20),
              const LText(
                'Use README.md to explain your design and usage. Use TESTS.md for inputs, expected results, actual results, and failures. Keep questions and reflections in NOTES.md.',
              ),
            ],
          ),
        ),
      ),
    ),
  );
}
