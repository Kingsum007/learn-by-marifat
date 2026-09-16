# Course expansion — version 2.3

The catalog now has 20 courses, 320 modules, 640 planned sessions, 60 project
assignments, and 380 saved portfolio/workspace destinations. Existing IDs and
backup formats are preserved. The five added pathways are Database Foundations,
SQL from Zero, SQLite for Offline Apps, PostgreSQL Development, and MongoDB and
Document Databases. Each course has sixteen modules and three practical project briefs. Modules seven through sixteen form a course-specific advanced technology and applied software-engineering stage.

All 304 modules outside Python now have an authored explanation of their actual
example, its outcome, and relevant failure cases. Workshop pages present the
concept, worked example, and concrete practice with review criteria. First
modules also show introductory instructions and vocabulary. Language coverage
includes English, Dari, and Pashto. The seven previously expanded playable
Python lessons are retained.

## What students can execute inside the app

The existing bounded Python interpreter remains available. SQL practice adds
real SQLite SELECT execution over fresh fictional books, students and loans.
Filters, supported aggregates, grouping, ordering and small joins are supported.
Its token validator limits query length to 2,000 characters, table references
to four, and output to 100 rows. Only an explicit function set is allowed;
additional statements, CTEs, subqueries, arbitrary functions and mutations are
rejected. SQLite also enables query-only mode. Every run opens and closes its
own in-memory database in a worker isolate. No learner database connection or
file path is passed to this tool.

The editor explains that queries are temporary and asks before discarding
changed text. Students can copy queries to retain them; automatic portfolio
saving and SQL grading/XP are not implemented. The three displayed tables are
a shared practice fixture, not the exact final state of every lesson script.
Full scripts that create/update tables are readable in lessons and run in a
separately prepared SQLite tool. The 18 relational lesson scripts are tested
with real SQLite, including expected results, rollback and constraints.

PostgreSQL and MongoDB lessons contain server-specific scripts and traces.
Their local servers must be prepared separately; the app does not emulate them
using SQLite. Likewise, framework and native app examples still require their
listed SDKs. Diagrams, comments, and incomplete project fragments are explained
as such instead of being represented as fully running programs.

## Scope of completion

This release expands teaching and adds database pathways. It does not ship 60
finished project applications, add graded exercises for every language, certify
mastery, or prove that all advanced material is sufficient for unsupervised
beginners. The 60 projects are briefs with requirements, milestones, review
criteria and editable workspaces; only the existing three Python projects have
complete reference applications. Native-speaker educational review of Dari and
Pashto remains pending. Automated translation checks establish coverage, not
fluency or teaching effectiveness.

## Authoring and checks

1. Edit `tool/module_walkthroughs.py` for the 84 existing non-Python module traces.
2. Edit `tool/database_courses.py` for the 30 database modules, examples, practice,
   entry lessons, project briefs and parallel translations.
3. Run `python tool/build_curriculum.py` then `python tool/build_module_guides.py`.
4. Run the Dart translation audit, then `python tool/build_translations.py`.
5. Format generated Dart and run Flutter tests and `python tool/test_database_content.py`.

Translation generation includes every new guide field in its completeness
inventory. Coverage tests require every non-Python module to have a guide in
both local languages. SQL tests exercise real results and rejected commands;
widget tests check translated workshops, navigation, error feedback and the
temporary-query exit guard. PostgreSQL/MongoDB servers and all external SDK
fragments have not been executed as part of this release's verification.

## Primary technical references

The examples and prose are original. These references were consulted for the
relevant database and lifecycle rules; opening them requires internet, but
reading the bundled lessons does not.

Code typography uses bundled Noto Sans Mono from the
[Google Fonts source distribution](https://github.com/google/fonts/tree/main/ofl/notosansmono),
with its unmodified SIL Open Font License included in the app.

- [SQLite SELECT documentation](https://www.sqlite.org/lang_select.html): querying and grouping semantics.
- [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html): enforcement and references.
- [SQLite transactions](https://www.sqlite.org/lang_transaction.html): transactions and competing writers.
- [SQLite backup API](https://www.sqlite.org/backup.html): consistent backup mechanisms.
- [PostgreSQL transaction tutorial](https://www.postgresql.org/docs/16/tutorial-transactions.html): commit and rollback.
- [PostgreSQL window functions](https://www.postgresql.org/docs/current/tutorial-window.html): results retaining individual rows.
- [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/): embedding and access patterns.
- [MongoDB transaction deployment considerations](https://www.mongodb.com/docs/manual/core/transactions-production-consideration/): standalone and replica-set limits.
- [React effect synchronization](https://react.dev/learn/synchronizing-with-effects): external subscriptions and cleanup.
