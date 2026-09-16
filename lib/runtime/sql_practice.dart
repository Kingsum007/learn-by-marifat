import 'dart:isolate';

import 'package:sqlite3/sqlite3.dart';

/// Read-only, bounded SQL teaching on fresh fictional data. Never opens a file
/// or shares a connection with learner storage. This is intentionally a subset.
const sqlFixture = '''
CREATE TABLE books(id INTEGER PRIMARY KEY,title TEXT NOT NULL,price INTEGER NOT NULL);
INSERT INTO books VALUES(1,'Python',100),(2,'Databases',150),(3,'Web',100);
CREATE TABLE students(id INTEGER PRIMARY KEY,name TEXT NOT NULL);
INSERT INTO students VALUES(1,'Amina'),(2,'Omid');
CREATE TABLE loans(id INTEGER PRIMARY KEY,book_id INTEGER,student_id INTEGER);
INSERT INTO loans VALUES(1,1,1),(2,1,2),(3,2,1);
''';
const sqlStarter = 'SELECT title, price FROM books ORDER BY id;';
const sqlSchema = '''books(id, title, price)
students(id, name)
loans(id, book_id, student_id)

books: (1, Python, 100), (2, Databases, 150), (3, Web, 100)
students: (1, Amina), (2, Omid)
loans: (1, 1, 1), (2, 1, 2), (3, 2, 1)''';

class SqlPracticeResult {
  const SqlPracticeResult({
    this.columns = const [],
    this.rows = const [],
    this.error,
  });
  final List<String> columns;
  final List<List<String>> rows;
  final String? error;
}

Future<SqlPracticeResult> runSqlPractice(String query) =>
    Isolate.run(() => runSqlPracticeSync(query));

SqlPracticeResult runSqlPracticeSync(String source) {
  const unsupported =
      'Use one SELECT query on books, students, or loans. This practice does not change stored data.';
  var query = source.trim();
  if (query.endsWith(';')) query = query.substring(0, query.length - 1);
  if (query.isEmpty || query.length > 2000) {
    return const SqlPracticeResult(
      error: 'Write a query of 1 to 2000 characters.',
    );
  }
  // Tokenize rather than searching raw strings: keywords inside string literals
  // are data. No comments, quoted identifiers, parameters or extra statements.
  final token = RegExp(
    r"\s+|'(?:''|[^'])*'|[A-Za-z_][A-Za-z_0-9]*|[0-9]+(?:\.[0-9]+)?|<>|!=|<=|>=|[(),.*+/<>=%-]",
  );
  final tokens = <String>[];
  var position = 0;
  while (position < query.length) {
    final match = token.matchAsPrefix(query, position);
    if (match == null) return const SqlPracticeResult(error: unsupported);
    final value = match.group(0)!;
    if (value.trim().isNotEmpty) tokens.add(value);
    position = match.end;
  }
  const keywords = {
    'select',
    'from',
    'where',
    'order',
    'by',
    'asc',
    'desc',
    'group',
    'having',
    'limit',
    'offset',
    'as',
    'distinct',
    'join',
    'inner',
    'left',
    'outer',
    'on',
    'and',
    'or',
    'not',
    'null',
    'is',
    'in',
    'like',
    'between',
    'case',
    'when',
    'then',
    'else',
    'end',
    'true',
    'false',
  };
  const functions = {
    'count',
    'sum',
    'avg',
    'min',
    'max',
    'coalesce',
    'round',
    'length',
    'lower',
    'upper',
    'abs',
  };
  const fields = {'id', 'title', 'price', 'name', 'book_id', 'student_id'};
  const tables = {'books', 'students', 'loans'};
  final aliases = {
    'a',
    'b',
    'c',
    's',
    'l',
    'total',
    'copies',
    'book_name',
    'loan_count',
    'amount',
    'result',
  };
  for (var i = 1; i < tokens.length; i++) {
    final previous = tokens[i - 1].toLowerCase();
    final value = tokens[i].toLowerCase();
    if ((previous == 'as' || tables.contains(previous)) &&
        RegExp(r'^[a-z_][a-z_0-9]*$').hasMatch(value) &&
        !keywords.contains(value)) {
      aliases.add(value);
    }
  }
  if (tokens.first.toLowerCase() != 'select') {
    return const SqlPracticeResult(error: unsupported);
  }
  var tableTokens = 0;
  var selects = 0;
  for (var i = 0; i < tokens.length; i++) {
    final value = tokens[i].toLowerCase();
    if (!RegExp(r'^[a-z_]').hasMatch(value)) continue;
    if (value == 'select') selects++;
    if (tables.contains(value) &&
        (i + 1 == tokens.length || tokens[i + 1] != '.')) {
      tableTokens++;
    }
    if (!keywords.contains(value) &&
        !functions.contains(value) &&
        !fields.contains(value) &&
        !tables.contains(value) &&
        !aliases.contains(value)) {
      return const SqlPracticeResult(
        error: 'Use the displayed table and column names. Supported functions include COUNT, SUM, AVG, MIN, MAX, and COALESCE.',
      );
    }
    if (i + 1 < tokens.length &&
        tokens[i + 1] == '(' &&
        !functions.contains(value) &&
        value != 'in') {
      return const SqlPracticeResult(error: unsupported);
    }
  }
  // At most four references to these tiny tables, no subqueries/CTEs/unions:
  // joins, aggregation and sorting therefore have a small bounded input.
  if (selects != 1 ||
      tableTokens < 1 ||
      tableTokens > 4 ||
      tokens.length > 300 ||
      query.contains('--') ||
      query.contains('/*')) {
    return const SqlPracticeResult(error: unsupported);
  }
  final database = sqlite3.openInMemory();
  try {
    database.execute(sqlFixture);
    database.execute('PRAGMA query_only=ON');
    final result = database.select('SELECT * FROM ($query) LIMIT 100');
    return SqlPracticeResult(
      columns: List<String>.from(result.columnNames),
      rows: [
        for (final row in result)
          [
            for (var i = 0; i < result.columnNames.length; i++)
              row.values.elementAt(i)?.toString() ?? 'NULL',
          ],
      ],
    );
  } on SqliteException {
    return const SqlPracticeResult(
      error: 'The query could not run. Check column names, commas, quotes, and the order of SELECT, FROM, WHERE, GROUP BY, and ORDER BY.',
    );
  } finally {
    database.close();
  }
}
