import 'package:learn_by_marifat_team/domain/learner_state.dart';
import 'package:learn_by_marifat_team/runtime/code_runner.dart';
import 'package:learn_by_marifat_team/runtime/python_vm.dart';

class MemoryProgress implements ProgressRepository {
  LearnerState state = LearnerState();
  bool fail = false;
  @override
  Future<LearnerState> load() async => state;
  @override
  Future<void> save(LearnerState value) async {
    if (fail) {
      throw StateError('Disk full');
    }
    state = value;
  }

  @override
  Future<void> close() async {}
}

class TestRunner implements CodeRunner {
  @override
  Future<RunResult> run(String source) async => PythonVm().run(source);
}
