import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/sqlite_progress_repository.dart';
import 'package:learn_by_marifat_team/domain/learner_state.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

import 'support.dart';

void main() {
  late MemoryProgress repository;
  late LearningController controller;
  setUp(() {
    repository = MemoryProgress();
    controller = LearningController(
      courses: BundledCourse(),
      curriculum: const BundledCurriculum(),
      progress: repository,
      runner: TestRunner(),
    );
  });
  tearDown(() => controller.dispose());
  test('concurrent commands cannot lose updates', () async {
    await Future.wait([
      controller.toggleBookmark('hello'),
      controller.toggleBookmark('loops'),
      controller.preferences(dark: true),
    ]);
    expect(controller.state.bookmarks, {'hello', 'loops'});
    expect(controller.state.dark, isTrue);
  });
  test('failed writes preserve state and queue recovers', () async {
    repository.fail = true;
    await expectLater(controller.toggleBookmark('hello'), throwsStateError);
    expect(controller.state.bookmarks, isEmpty);
    repository.fail = false;
    await controller.toggleBookmark('loops');
    expect(controller.state.bookmarks, {'loops'});
  });
  test('wrong retries never erase mastery; completion is idempotent', () async {
    final exercise = controller.lessons.first.exercises.first;
    await controller.submitChoice(exercise, exercise.answer);
    await controller.submitChoice(exercise, exercise.answer);
    await controller.submitChoice(exercise, 0);
    expect(controller.state.solved, {exercise.id});
    expect(controller.state.attempts[exercise.id], 3);
  });
  test('invalid choices cannot alter progress', () async {
    await expectLater(
      controller.submitChoice(controller.lessons.first.exercises.first, -1),
      throwsArgumentError,
    );
    expect(controller.state.attempts, isEmpty);
  });
  test(
    'coding result records only successful execution with expected output',
    () async {
      final exercise = controller.lessons.first.exercises.last;
      final failed = await controller.submitCode(
        exercise,
        'print("Salam")\nprint("Kabul")\nprint(1/0)',
      );
      expect(failed.$2.correct, isFalse);
      expect(controller.state.solved, isEmpty);
      final passed = await controller.submitCode(
        exercise,
        'print("Salam")\nprint("Kabul")',
      );
      expect(passed.$2.correct, isTrue);
      expect(controller.state.solved, {exercise.id});
    },
  );
  test('backup round-trip preserves all state', () async {
    await controller.toggleBookmark('hello');
    await controller.saveDraft('playground', 'print("سلام")');
    await controller.preferences(language: 'fa', dark: true);
    final json = await controller.exportBackup();
    final decoded = controller.validateBackup(json);
    expect(decoded.bookmarks, {'hello'});
    expect(decoded.drafts['playground'], 'print("سلام")');
    expect(decoded.language, 'fa');
    expect(decoded.dark, true);
  });
  for (final entry in <String, Object?>{
    'version': 99,
    'solved': ['not-real'],
    'bookmarks': ['not-real'],
    'attempts': {'hello-q': -1},
    'drafts': {'playground': 9},
    'language': 'invalid',
    'dark': 'true',
  }.entries) {
    test('rejects invalid backup ${entry.key} without writes', () async {
      final data = jsonDecode(LearnerState().encode()) as Map<String, dynamic>;
      data[entry.key] = entry.value;
      await expectLater(
        controller.importBackup(jsonEncode(data)),
        throwsFormatException,
      );
      expect(controller.state.solved, isEmpty);
      expect(controller.state.bookmarks, isEmpty);
    });
  }
  test(
    'oversized backup is rejected',
    () => expect(
      () => controller.validateBackup('a' * 1000001),
      throwsFormatException,
    ),
  );
  test('unknown IDs rejected in application writes', () async {
    await expectLater(
      controller.toggleBookmark('invalid'),
      throwsFormatException,
    );
  });
  test('SQLite survives close and reopen', () async {
    sqfliteFfiInit();
    final directory = await Directory.systemTemp.createTemp('kohi-test-');
    final file = '${directory.path}/progress.db';
    var db = await SqliteProgressRepository.open(
      databaseFactoryFfi,
      file,
      BundledCourse(),
    );
    try {
      await db.save(
        LearnerState(
          solved: {'hello-q'},
          bookmarks: {'hello'},
          drafts: {'playground': 'print(1)'},
        ),
      );
      await db.close();
      db = await SqliteProgressRepository.open(
        databaseFactoryFfi,
        file,
        BundledCourse(),
      );
      final restored = await db.load();
      expect(restored.solved, {'hello-q'});
      expect(restored.drafts['playground'], 'print(1)');
    } finally {
      await db.close();
      await directory.delete(recursive: true);
    }
  });
}
