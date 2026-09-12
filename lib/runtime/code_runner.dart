import 'dart:async';
import 'dart:isolate';

import 'python_vm.dart';

abstract interface class CodeRunner {
  Future<RunResult> run(String source);
}

/// Worker isolation keeps input responsive. The isolate is killed on completion
/// or timeout, in addition to the VM's operation and allocation budgets.
class IsolateCodeRunner implements CodeRunner {
  @override
  Future<RunResult> run(String source) async {
    final port = ReceivePort();
    Isolate? worker;
    try {
      worker = await Isolate.spawn(_run, (port.sendPort, source));
      return await port.first.timeout(const Duration(seconds: 3)) as RunResult;
    } on TimeoutException {
      return const RunResult(
        '',
        error: 'Execution timed out. Simplify the program and try again.',
      );
    } catch (_) {
      return const RunResult(
        '',
        error: 'The practice runner could not start. Try again.',
      );
    } finally {
      worker?.kill(priority: Isolate.immediate);
      port.close();
    }
  }

  static void _run((SendPort, String) message) {
    message.$1.send(PythonVm().run(message.$2));
  }
}
