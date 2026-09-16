import 'package:sqflite/sqflite.dart';

import '../domain/course.dart';
import '../domain/learner_state.dart';
import '../domain/curriculum.dart';
import 'bundled_curriculum.dart';

class SqliteProgressRepository implements ProgressRepository {
  SqliteProgressRepository._(this._database, this._courses, this._curriculum);
  final Database _database;
  final CourseRepository _courses;
  final CurriculumRepository _curriculum;

  static Future<SqliteProgressRepository> open(
    DatabaseFactory factory,
    String path,
    CourseRepository courses, {
    CurriculumRepository curriculum = const BundledCurriculum(),
  }) async {
    final database = await factory.openDatabase(
      path,
      options: OpenDatabaseOptions(
        version: 1,
        onConfigure: (db) async {
          await db.execute('PRAGMA foreign_keys = ON');
        },
        onCreate: (db, version) async {
          await db.execute(
            'CREATE TABLE learner (id INTEGER PRIMARY KEY CHECK (id = 1), payload TEXT NOT NULL)',
          );
        },
      ),
    );
    return SqliteProgressRepository._(database, courses, curriculum);
  }

  @override
  Future<LearnerState> load() async {
    final rows = await _database.query(
      'learner',
      where: 'id = ?',
      whereArgs: [1],
    );
    if (rows.isEmpty) {
      return LearnerState();
    }
    return LearnerState.decode(
      rows.single['payload'] as String,
      portfolioIds: portfolioIds(_curriculum),
      exerciseIds: _courses.lessons
          .expand((l) => l.exercises)
          .map((e) => e.id)
          .toSet(),
      lessonIds: _courses.lessons.map((l) => l.id).toSet(),
      courseIds: _curriculum.catalog.map((course) => course.id).toSet(),
    );
  }

  @override
  Future<void> save(LearnerState state) async {
    await _database.transaction((txn) async {
      await txn.insert('learner', {
        'id': 1,
        'payload': state.encode(),
      }, conflictAlgorithm: ConflictAlgorithm.replace);
    });
  }

  @override
  Future<void> close() => _database.close();
}
