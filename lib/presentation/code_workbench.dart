import 'localized_text.dart';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../application/learning_controller.dart';
import '../domain/assessment.dart';
import '../domain/course.dart';
import '../runtime/python_vm.dart';
import 'theme.dart';

class CodeWorkbench extends StatefulWidget {
  const CodeWorkbench({
    super.key,
    required this.controller,
    this.exercise,
    this.initialCode = 'name = "Afghanistan"\nprint("Hello, " + name)\n\nfor n in range(1, 4):\n    print(n)',
  });
  final LearningController controller;
  final Exercise? exercise;
  final String initialCode;
  @override
  State<CodeWorkbench> createState() => _CodeWorkbenchState();
}

class _CodeWorkbenchState extends State<CodeWorkbench> {
  late final TextEditingController editor;
  bool busy = false, dirty = false;
  RunResult? result;
  Assessment? assessment;
  String get id => widget.exercise?.id ?? 'playground';
  @override
  void initState() {
    super.initState();
    editor = TextEditingController(
      text:
          widget.controller.state.drafts[id] ??
          widget.exercise?.starter ??
          widget.initialCode,
    );
  }

  @override
  void dispose() {
    editor.dispose();
    super.dispose();
  }

  Future<void> save() async {
    setState(() => busy = true);
    try {
      await safely(context, () async {
        await widget.controller.saveDraft(id, editor.text);
        if (mounted) {
          setState(() => dirty = false);
        }
      }, success: 'Draft saved on this device.');
    } finally {
      if (mounted) {
        setState(() => busy = false);
      }
    }
  }

  Future<void> run() async {
    setState(() {
      busy = true;
      assessment = null;
      result = null;
    });
    try {
      await safely(context, () async {
        if (widget.exercise != null) {
          final evaluated = await widget.controller.submitCode(
            widget.exercise!,
            editor.text,
          );
          if (mounted) {
            setState(() {
              result = evaluated.$1;
              assessment = evaluated.$2;
              dirty = false;
            });
          }
        } else {
          await widget.controller.saveDraft(id, editor.text);
          final output = await widget.controller.runner.run(editor.text);
          if (mounted) {
            setState(() {
              result = output;
              dirty = false;
            });
          }
        }
      });
    } finally {
      if (mounted) {
        setState(() => busy = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) => PopScope(
    canPop: !dirty && !busy,
    onPopInvokedWithResult: (didPop, value) async {
      if (didPop || busy) return;
      final choice = await showDialog<String>(
        context: context,
        builder: (context) => AlertDialog(
          title: const LText('Save your changes?'),
          content: const LText('Your code has changes that are not saved yet.'),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context, 'cancel'),
              child: const LText('Keep editing'),
            ),
            TextButton(
              onPressed: () => Navigator.pop(context, 'discard'),
              child: const LText('Discard changes'),
            ),
            FilledButton(
              onPressed: () => Navigator.pop(context, 'save'),
              child: const LText('Save and leave'),
            ),
          ],
        ),
      );
      if (!mounted || choice == null || choice == 'cancel') return;
      if (choice == 'save') await save();
      if (choice == 'discard' && mounted) setState(() => dirty = false);
      if (mounted && !dirty) {
        setState(() {});
        WidgetsBinding.instance.addPostFrameCallback((_) {
          if (mounted) Navigator.of(context).pop();
        });
      }
    },
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Row(
          children: [
            const Icon(Icons.code, size: 20),
            const SizedBox(width: 8),
            const Expanded(
              child: LText(
                'main.py',
                style: TextStyle(fontWeight: FontWeight.w700),
              ),
            ),
            LText(
              dirty ? 'Unsaved changes' : 'Local draft',
              style: const TextStyle(fontSize: 12),
            ),
          ],
        ),
        const SizedBox(height: 12),
        Directionality(
          textDirection: TextDirection.ltr,
          child: TextField(
            key: const Key('code-editor'),
            controller: editor,
            enabled: !busy,
            minLines: 9,
            maxLines: 20,
            autocorrect: false,
            enableSuggestions: false,
            keyboardType: TextInputType.multiline,
            textInputAction: TextInputAction.newline,
            inputFormatters: [LengthLimitingTextInputFormatter(12000)],
            style: const TextStyle(
              fontFamily: 'monospace',
              fontSize: 14,
              height: 1.8,
            ),
            decoration: const InputDecoration(
              label: LText('Python practice code'),
              alignLabelWithHint: true,
              helper: LText(
                'Use four spaces for indentation. Save or run to keep your draft.',
              ),
            ),
            onChanged: (_) => setState(() {
              dirty = true;
              assessment = null;
              result = null;
            }),
          ),
        ),
        const SizedBox(height: 12),
        Wrap(
          spacing: 10,
          runSpacing: 10,
          children: [
            FilledButton.icon(
              key: const Key('run-code'),
              onPressed: busy ? null : run,
              icon: busy
                  ? const SizedBox(
                      width: 16,
                      height: 16,
                      child: CircularProgressIndicator(strokeWidth: 2),
                    )
                  : const Icon(Icons.play_arrow),
              label: LText(
                busy
                    ? 'Running…'
                    : widget.exercise == null
                    ? 'Run code'
                    : 'Run & check',
              ),
            ),
            OutlinedButton.icon(
              onPressed: busy ? null : save,
              icon: const Icon(Icons.save_outlined),
              label: const LText('Save draft'),
            ),
            TextButton(
              onPressed: busy
                  ? null
                  : () {
                      final selection = editor.selection;
                      final start = selection.isValid
                          ? selection.start
                          : editor.text.length;
                      final end = selection.isValid ? selection.end : start;
                      if (editor.text.length + 4 > 12000) {
                        return;
                      }
                      editor.value = TextEditingValue(
                        text: editor.text.replaceRange(start, end, '    '),
                        selection: TextSelection.collapsed(offset: start + 4),
                      );
                      setState(() => dirty = true);
                    },
              child: const LText('+ 4 spaces'),
            ),
          ],
        ),
        const SizedBox(height: 20),
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: ink,
            borderRadius: BorderRadius.circular(16),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const LText(
                'OUTPUT',
                style: TextStyle(
                  color: Color(0xFFA9C5BC),
                  fontSize: 11,
                  letterSpacing: 2,
                ),
              ),
              const SizedBox(height: 12),
              SelectableText(
                result == null
                    ? tx(context, 'Your output will appear here.')
                    : result!.output.isEmpty
                    ? tx(context, '(no output)')
                    : result!.output.trimRight(),
                textDirection: TextDirection.ltr,
                style: const TextStyle(
                  color: Colors.white,
                  fontFamily: 'monospace',
                  height: 1.7,
                ),
              ),
              if (result?.error != null) ...[
                const SizedBox(height: 12),
                LText(
                  result!.error!,
                  style: const TextStyle(color: Color(0xFFFFBCAC)),
                ),
              ],
            ],
          ),
        ),
        if (assessment != null) ...[
          const SizedBox(height: 16),
          FeedbackPanel(assessment!),
        ],
        if (widget.exercise != null) ...[
          const SizedBox(height: 10),
          ExpansionTile(
            title: const LText('Need a hint?'),
            children: [
              Padding(
                padding: const EdgeInsets.all(16),
                child: LText(widget.exercise!.hint),
              ),
            ],
          ),
          ExpansionTile(
            title: const LText('Expected output'),
            children: [
              Padding(
                padding: const EdgeInsets.all(16),
                child: SelectableText(
                  widget.exercise!.expected.trimRight(),
                  style: const TextStyle(fontFamily: 'monospace'),
                ),
              ),
            ],
          ),
        ],
        const SizedBox(height: 16),
        const LanguageGuide(),
      ],
    ),
  );
}

class FeedbackPanel extends StatelessWidget {
  const FeedbackPanel(this.assessment, {super.key});
  final Assessment assessment;
  @override
  Widget build(BuildContext context) => Semantics(
    liveRegion: true,
    child: Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surfaceContainerHigh,
        borderRadius: BorderRadius.circular(14),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          LText(
            assessment.correct
                ? '✓ Nicely done. Progress saved.'
                : 'Try again — you are learning.',
            style: const TextStyle(fontWeight: FontWeight.w800),
          ),
          const SizedBox(height: 8),
          LText(assessment.message, style: const TextStyle(height: 1.6)),
          if (!assessment.correct)
            const Padding(
              padding: EdgeInsets.only(top: 8),
              child: LText(
                'Review the example, adjust your answer, and retry.',
              ),
            ),
        ],
      ),
    ),
  );
}

class LanguageGuide extends StatelessWidget {
  const LanguageGuide({super.key});
  @override
  Widget build(BuildContext context) => const ExpansionTile(
    title: LText('Offline Python subset · language guide'),
    subtitle: LText('A learning interpreter, not full CPython'),
    children: [
      Padding(
        padding: EdgeInsets.all(16),
        child: LText(
          'Supported: numbers, strings, booleans, lists, variables, arithmetic, comparisons, and/or/not, '
          'if/else, for, while, simple top-level functions and return. Built-ins: print, range, len, str, int. '
          'List and string indexing are supported. Use four-space indentation.\n\n'
          'Not supported: imports, packages, input(), files, networking, classes, exceptions, f-strings, '
          'list methods, keyword/default arguments, closures, chained comparisons, break/continue, or full Python semantics. '
          'Names use Latin letters. String indexing uses UTF-16 units in this version.\n\n'
          'Limits: 12,000 code characters, 20,000 execution steps, 1,000 list/range items, '
          '16,000 output characters, 32 function calls deep, and a 3-second worker timeout. '
          'Each run starts with fresh variables.\n\n'
          'Coding exercises compare displayed output. They do not prove that a particular algorithm was used. '
          'Use these for practice, not secure examinations.',
          style: TextStyle(height: 1.6),
        ),
      ),
    ],
  );
}
