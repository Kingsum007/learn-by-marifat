import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/runtime/sql_practice.dart';

void main() {
  test(
    'SQL practice executes filters, left joins, grouping and empty results',
    () {
      final filter = runSqlPracticeSync(
        'SELECT title FROM books WHERE price=100 ORDER BY title;',
      );
      expect(filter.error, isNull);
      expect(filter.rows, [
        ['Python'],
        ['Web'],
      ]);
      final join = runSqlPracticeSync(
        'SELECT b.title, COUNT(l.id) AS loan_count FROM books b LEFT JOIN loans l ON l.book_id=b.id GROUP BY b.id,b.title ORDER BY b.id',
      );
      expect(join.error, isNull);
      expect(join.rows, [
        ['Python', '2'],
        ['Databases', '1'],
        ['Web', '0'],
      ]);
      final empty = runSqlPracticeSync(
        'SELECT title FROM books WHERE price>200',
      );
      expect(empty.error, isNull);
      expect(empty.rows, isEmpty);
      expect(
        runSqlPracticeSync('SELECT SUM(price) AS total_price FROM books').rows,
        [
          ['350'],
        ],
      );
    },
  );
  test('SQL practice blocks mutations, extra statements, files and expensive functions', () {
    for (final query in [
      "ATTACH DATABASE 'learner.db' AS a",
      'DELETE FROM books',
      'SELECT title FROM books; DELETE FROM books',
      "SELECT load_extension('x') FROM books",
      'SELECT randomblob(1000000000) FROM books',
      'WITH RECURSIVE a AS (SELECT 1) SELECT * FROM a',
      'SELECT * FROM sqlite_master',
      'SELECT * FROM books a,books b,books c,books s,books l',
      'SELECT (SELECT title FROM books) FROM books',
    ]) {
      expect(runSqlPracticeSync(query).error, isNotNull, reason: query);
    }
    expect(runSqlPracticeSync('SELECT COUNT(*) FROM books').rows, [
      ['3'],
    ]);
  });
  test(
    'SQL literals are data and a fresh run still has the original fixture',
    () async {
      final result = await runSqlPractice(
        "SELECT 'DELETE' AS result FROM books WHERE id=1",
      );
      expect(result.error, isNull);
      expect(result.rows, [
        ['DELETE'],
      ]);
      expect(runSqlPracticeSync(sqlStarter).rows.length, 3);
      expect(
        runSqlPracticeSync('SELECT title, title FROM books WHERE id=1').rows,
        [
          ['Python', 'Python'],
        ],
      );
    },
  );
}
