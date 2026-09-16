# Sequential learning — 2.5.0

Each course starts with its first topic. Python foundation lessons require every exercise in every preceding lesson. Python workshops follow completion of all seven foundations. Other courses begin with their first workshop.

Every non-Python course now begins with a persisted zero-knowledge introduction. It defines four essential terms, explains the first example step by step, checks one prediction, and provides guided practice. Topic 1 remains locked until the learner answers the readiness check correctly and explicitly completes this introduction.

The catalogue also enforces its authored prerequisite graph. A dependent course stays locked until every required course has all workshops complete (and, for Python, all foundation challenges). Its card names the unfinished prerequisite. Courses with no prerequisites remain valid starting points, so learners may choose Python, Java, Kotlin, Swift, C++, Flutter/Dart, Web Design, or Database Foundations according to their goal.

Workshops unlock in order. Each of their two practice activities requires saved, nonempty evidence and the learner's completion checkbox; the second activity follows the first. This is self-reported completion, not automatic code assessment. Projects unlock after all workshops and then follow the preceding project's saved evidence and all milestone confirmations.

The same policy protects direct lesson, assessment, workshop, activity, project, and workspace routes. The reference library opens after the course workshops. Code Lab remains available for independent practice. Course choice remains free; locking is within each course.

Progress is derived from existing validated solved exercises and portfolio records, so it survives restarts and backups without a new storage schema. Existing incomplete records do not count as completion. Failed saves do not change locks. Removing completion evidence can relock dependent topics; no work is deleted.

New regression tests cover gaps in historical Python progress, workshop activity order, failed saves, persisted progress, project gates, and direct-route protection. Existing unlocked-screen tests now seed prerequisite completion explicitly.
