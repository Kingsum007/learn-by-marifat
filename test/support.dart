import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/domain/portfolio.dart';
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

// Seed completed prerequisites for tests that inspect already-unlocked screens.
Future<void> seedCourseProgress(
  LearningController controller,
  String id, {
  int projects = 0,
}) async {
  final course = controller.curriculum.catalog.firstWhere((c) => c.id == id);
  await controller.importBackup(
    controller.state
        .copyWith(
          completedIntros: {...controller.state.completedIntros, id},
          solved: id == 'python'
              ? controller.lessons
                    .expand((l) => l.exercises)
                    .map((e) => e.id)
                    .toSet()
              : controller.state.solved,
          portfolio: {
            ...controller.state.portfolio,
            for (final module in course.modules)
              for (final plan in module.plans)
                plan.id: PortfolioEntry(
                  evidence: 'Completed and checked example.',
                  milestones: {0},
                ),
            for (final project in course.projects.take(projects))
              project.id: PortfolioEntry(
                evidence: 'Completed project.',
                milestones: {0, 1, 2, 3, 4},
              ),
          },
        )
        .encode(),
  );
}
