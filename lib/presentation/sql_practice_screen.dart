import 'package:flutter/material.dart';

import '../runtime/sql_practice.dart';
import 'curriculum_screen.dart';
import 'localized_text.dart';

class SqlPracticeScreen extends StatefulWidget {
  const SqlPracticeScreen({super.key, this.execute = runSqlPractice});
  final Future<SqlPracticeResult> Function(String) execute;
  @override
  State<SqlPracticeScreen> createState() => _SqlPracticeScreenState();
}

class _SqlPracticeScreenState extends State<SqlPracticeScreen> {
  final editor = TextEditingController(text: sqlStarter);
  SqlPracticeResult? result;
  bool busy = false;
  bool get changed => editor.text != sqlStarter;
  @override
  void dispose() {
    editor.dispose();
    super.dispose();
  }

  Future<void> run() async {
    setState(() {
      busy = true;
      result = null;
    });
    try {
      final next = await widget.execute(editor.text);
      if (mounted) setState(() => result = next);
    } catch (_) {
      if (mounted) {
        setState(
          () => result = const SqlPracticeResult(
            error: 'SQL practice could not start. Your query is still here; try again.',
          ),
        );
      }
    } finally {
      if (mounted) setState(() => busy = false);
    }
  }

  Future<void> leave() async {
    if (busy) return;
    final discard = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const LText('Leave SQL practice?'),
        content: const LText(
          'This query is temporary. Copy it before leaving if you want to keep it.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const LText('Keep editing'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: const LText('Discard and leave'),
          ),
        ],
      ),
    );
    if (discard == true && mounted) {
      setState(() => allowExit = true);
      WidgetsBinding.instance.addPostFrameCallback((_) {
        if (mounted) Navigator.pop(context);
      });
    }
  }

  bool allowExit = false;
  @override
  Widget build(BuildContext context) => PopScope(
    canPop: !busy && (!changed || allowExit),
    onPopInvokedWithResult: (didPop, _) {
      if (!didPop) leave();
    },
    child: Scaffold(
      appBar: AppBar(title: const LText('Offline SQL practice')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 900),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                infoCard(
                  'Before you begin',
                  'Read fictional tables with SELECT, filters, joins, grouping, and ordering. Each run uses fresh data and shows at most 100 rows. Queries here are temporary; copy any work you want to keep. Updates, subqueries, and server-specific commands are not supported in this practice.',
                ),
                const LText('Practice tables'),
                codeSample(sqlSchema),
                const LText(
                  'Try finding books priced at 100. Then count loans for each book, including books with no loans.',
                ),
                const SizedBox(height: 16),
                TextField(
                  controller: editor,
                  onChanged: (_) => setState(() {}),
                  enabled: !busy,
                  minLines: 4,
                  maxLines: 12,
                  maxLength: 2000,
                  textDirection: TextDirection.ltr,
                  style: const TextStyle(fontFamily: 'LearnMono'),
                  decoration: InputDecoration(
                    border: const OutlineInputBorder(),
                    labelText: tx(context, 'Your SQL query'),
                  ),
                ),
                const SizedBox(height: 12),
                FilledButton.icon(
                  onPressed: busy ? null : run,
                  icon: busy
                      ? const SizedBox(
                          width: 20,
                          height: 20,
                          child: CircularProgressIndicator(strokeWidth: 2),
                        )
                      : const Icon(Icons.play_arrow),
                  label: LText(busy ? 'Running...' : 'Run query'),
                ),
                if (result?.error != null)
                  infoCard('Review and try again', result!.error!),
                if (result != null && result!.error == null) ...[
                  const SizedBox(height: 20),
                  const LText('Query result'),
                  if (result!.rows.isEmpty)
                    const LText(
                      'No rows matched. Check your filter; an empty result is not an execution error.',
                    ),
                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Directionality(
                      textDirection: TextDirection.ltr,
                      child: DataTable(
                        columns: [
                          for (final name in result!.columns)
                            DataColumn(label: Text(name)),
                        ],
                        rows: [
                          for (final row in result!.rows)
                            DataRow(
                              cells: [
                                for (final value in row)
                                  DataCell(SelectableText(value)),
                              ],
                            ),
                        ],
                      ),
                    ),
                  ),
                ],
              ],
            ),
          ),
        ),
      ),
    ),
  );
}
