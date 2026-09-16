"""Course-specific advanced modules appended without changing existing IDs."""

TOPICS = {
    'python': [
        ('Protocols, descriptors, and metaprogramming', 'define stable behavioral contracts and control attribute access without fragile inheritance', 'from typing import Protocol\nclass Priced(Protocol):\n    price: int\ndef total(items: list[Priced]) -> int:\n    return sum(item.price for item in items)', 'design a protocol-based pricing service and test two unrelated implementations.'),
        ('Async services, packaging, and secure delivery', 'coordinate bounded asynchronous work, package reproducibly, and protect local inputs and secrets', 'import asyncio\nasync def report(values):\n    await asyncio.sleep(0)\n    return sum(values)\nprint(asyncio.run(report([20, 30])))', 'build an offline asynchronous report pipeline with timeouts, cancellation, tests, and a reproducible package.'),
    ],
    'web-design': [
        ('Design systems and component architecture', 'turn tokens, components, states, and content rules into a maintainable interface system', ':root { --space-2: .5rem; --brand: #087c89; }\n.button { padding: var(--space-2) 1rem; }\n.button:focus-visible { outline: 3px solid currentColor; }', 'create a documented local design system with accessible default, hover, focus, error, and disabled states.'),
        ('Advanced accessibility and performance', 'audit semantics, keyboard flow, contrast, motion, responsive images, and rendering cost under real constraints', '@media (prefers-reduced-motion: reduce) {\n  *, *::before, *::after { animation-duration: .01ms !important; }\n}', 'audit and repair a multi-page site for keyboard, screen-reader, large-text, reduced-motion, and offline performance.'),
    ],
    'web-development': [
        ('Distributed system boundaries', 'design versioned contracts, idempotent operations, retries, and failure isolation between client and server', 'POST /loans HTTP/1.1\nIdempotency-Key: loan-42\nContent-Type: application/json\n\n{"bookId": 7}', 'design an idempotent lending workflow and prove that retrying cannot create duplicate records.'),
        ('Security, observability, and deployment', 'apply threat modeling, least privilege, structured logs, health checks, migrations, and reversible releases', 'request_id=8f2 action=create_loan outcome=accepted duration_ms=12', 'ship a locally deployable service with a threat model, redacted logs, health checks, migration rollback, and recovery drill.'),
    ],
    'java': [
        ('Concurrency and the Java memory model', 'reason about visibility, atomicity, executors, immutable messages, and structured task lifecycles', 'try (var executor = java.util.concurrent.Executors.newVirtualThreadPerTaskExecutor()) {\n  var future = executor.submit(() -> 40 + 2);\n  System.out.println(future.get());\n}', 'build a bounded concurrent importer and test cancellation, ordering, failure propagation, and clean shutdown.'),
        ('JVM architecture, profiling, and delivery', 'measure allocation and latency, define module boundaries, and create reproducible runtime images', 'module school.reports {\n  exports school.reports.api;\n}', 'profile a modular reporting service, remove one measured bottleneck, and package it with repeatable offline build instructions.'),
    ],
    'kotlin': [
        ('Coroutines, Flow, and structured concurrency', 'model cancellation, backpressure, lifecycle ownership, and deterministic coroutine tests', 'suspend fun total(values: List<Int>) = kotlinx.coroutines.coroutineScope {\n    values.map { async { it } }.awaitAll().sum()\n}', 'implement a cancellable report stream with bounded work, failure tests, and no orphaned coroutines.'),
        ('DSLs, multiplatform boundaries, and performance', 'use receivers and sealed models carefully while separating common logic from platform adapters', 'sealed interface Result<out T> {\n data class Ok<T>(val value:T): Result<T>\n data class Error(val message:String): Result<Nothing>\n}', 'design a typed validation DSL shared by two platform adapters and benchmark the critical transformation.'),
    ],
    'android': [
        ('Offline-first synchronization architecture', 'model local truth, conflict resolution, work scheduling, retries, and observable sync state', 'data class SyncState(val pending: Int, val lastError: String?)\n// Room remains the source of truth; workers reconcile later.', 'build a local-first queue with deterministic conflict rules and tests for restart, duplicate work, and interrupted synchronization.'),
        ('Performance, security, and production delivery', 'profile startup and rendering, protect stored data, minimize permissions, and verify signed release behavior', '<uses-permission android:name="android.permission.INTERNET" />\n<!-- Remove this permission when the product is fully offline. -->', 'produce a release audit covering startup, jank, accessibility, backup policy, permissions, secrets, signing, and offline acceptance.'),
    ],
    'ios': [
        ('Offline data, background work, and conflict handling', 'coordinate SwiftData or Core Data transactions, background tasks, migrations, and merge policies', '@Model final class Note {\n var title: String\n init(title: String) { self.title = title }\n}', 'build a migration-tested local store with background import, deterministic conflict handling, and restart recovery.'),
        ('Privacy, performance, and App Store delivery', 'measure launch and UI responsiveness, apply data minimization, signing, entitlements, and release checks', 'let started = ContinuousClock.now\n// Measure a defined operation, then compare against a budget.', 'prepare a privacy manifest, performance budget, accessibility audit, signed archive checklist, and offline release evidence.'),
    ],
    'swift': [
        ('Actors and advanced concurrency', 'use actors, task groups, cancellation, Sendable values, and isolation boundaries safely', 'actor Counter {\n private var value = 0\n func increment() { value += 1 }\n func read() -> Int { value }\n}', 'implement a cancellable actor-based batch processor and test isolation, partial failure, and deterministic output.'),
        ('Protocols, generics, macros, and package design', 'create expressive compile-time contracts while keeping APIs small, testable, and source compatible', 'protocol Repository<Item> {\n associatedtype Item\n func load() throws -> [Item]\n}', 'publish a local Swift package with protocol-based storage adapters, semantic version notes, documentation, and tests.'),
    ],
    'cpp': [
        ('Templates, concepts, and compile-time design', 'constrain generic algorithms, understand instantiation cost, and expose clear diagnostics and ownership contracts', '#include <concepts>\ntemplate<std::integral T>\nT total(T a, T b) { return a + b; }', 'design a constrained statistics library and test signed, unsigned, overflow, empty, and invalid cases.'),
        ('Concurrency, profiling, and systems reliability', 'apply race-free ownership, atomics or locks, sanitizers, profiling, and failure-safe resource control', 'std::jthread worker([](std::stop_token stop) {\n  while (!stop.stop_requested()) { break; }\n});', 'build a bounded worker queue, verify it with thread/address sanitizers, profile it, and document shutdown guarantees.'),
    ],
    'javascript': [
        ('Event loop, workers, and performance', 'reason about tasks and microtasks, move CPU work to workers, and measure responsiveness', 'console.log("A");\nqueueMicrotask(() => console.log("microtask"));\nsetTimeout(() => console.log("task"), 0);', 'build a responsive local data processor using a worker, cancellation, progress messages, and performance measurements.'),
        ('Language internals, security, and package design', 'apply prototypes, iterators, typed boundaries, input safety, modules, and reproducible dependency policy', 'export function* valid(records) {\n  for (const record of records) if (record?.id != null) yield record;\n}', 'design a dependency-light module with a threat model, strict validation, public API documentation, and compatibility tests.'),
    ],
    'reactjs': [
        ('Concurrent rendering and application architecture', 'design transitions, suspense boundaries, server-state ownership, and predictable feature boundaries', 'const [isPending, startTransition] = useTransition();\nstartTransition(() => setQuery(nextQuery));', 'build a large searchable local catalog that stays responsive and has explicit loading, empty, error, and recovery states.'),
        ('Performance, accessibility, and secure delivery', 'profile renders and bundles, test keyboard and screen-reader flows, and defend browser boundaries', 'const visible = useMemo(() => filter(items, query), [items, query]);', 'measure and repair a real render bottleneck, complete an accessibility audit, and produce a reproducible offline build.'),
    ],
    'reactnative': [
        ('Native modules, threads, and performance', 'understand the new architecture boundary, avoid JS-thread stalls, and measure startup, lists, and memory', '<FlatList data={items} keyExtractor={item => item.id} renderItem={renderItem} />', 'profile a large offline list, repair measured frame drops, and document when native code is justified.'),
        ('Offline-first mobile delivery', 'design durable local state, migrations, conflict policies, accessibility, signing, and reproducible Android/iOS releases', 'type PendingChange = { id: string; operation: "upsert" | "delete"; version: number };', 'deliver a local-first mobile feature with migration tests, interrupted-write recovery, platform accessibility checks, and release evidence.'),
    ],
    'nodejs': [
        ('Streams, workers, and backpressure', 'process large inputs with bounded memory, worker isolation, cancellation, and explicit error propagation', 'import { pipeline } from "node:stream/promises";\nawait pipeline(source, transform, destination);', 'build a bounded CSV pipeline and prove backpressure, cleanup, cancellation, and malformed-record handling.'),
        ('Diagnostics, security, and production operations', 'measure event-loop delay, trace requests, constrain privileges, and operate graceful startup and shutdown', 'process.on("SIGTERM", async () => {\n  await server.close();\n  process.exitCode = 0;\n});', 'package a loopback service with structured diagnostics, resource limits, threat model, graceful shutdown, and recovery test.'),
    ],
    'expressjs': [
        ('Service architecture and resilient workflows', 'separate HTTP, application, and persistence concerns while applying idempotency and transaction boundaries', 'app.post("/loans", validate, asyncHandler(async (req, res) => {\n  res.status(201).json(await service.create(req.body));\n}));', 'implement an idempotent transactional workflow with stable errors and contract tests through real HTTP.'),
        ('API security, observability, and operations', 'apply authentication boundaries, authorization policy, rate and size limits, redacted logs, and graceful operation', 'app.use(express.json({ limit: "16kb" }));\napp.use((err, req, res, next) => res.status(500).json({code:"INTERNAL"}));', 'threat-model and harden a local API, then verify limits, policy failures, redaction, health, and clean shutdown.'),
    ],
    'flutter-dart': [
        ('Rendering, isolates, and performance engineering', 'measure frames, rebuilds, memory, startup, and isolate transfer before applying targeted optimizations', 'final result = await Isolate.run(() => expensiveReport(records));\n// Transfer immutable results and enforce a timeout.', 'profile a large offline screen, repair one measured bottleneck, and verify responsiveness on a low-resource device.'),
        ('Platform integration, security, and release automation', 'design plugin boundaries, migrations, permissions, signing, reproducible builds, and rollback evidence', 'abstract interface class SecureStore {\n  Future<void> write(String key, String value);\n}', 'deliver a platform adapter with fakes and integration tests plus signed-build, offline-install, backup, migration, and rollback checks.'),
    ],
    'database-foundations': [
        ('Distributed data and consistency models', 'compare replication, partitioning, consistency, availability, and conflict resolution using explicit failure scenarios', 'Node A: version 4, value 12\nNode B: version 5, value 10\nPolicy: reject blind overwrite; reconcile with domain rules.', 'model a partition and recovery scenario, state the chosen consistency guarantee, and test conflict outcomes.'),
        ('Data governance, security, and lifecycle', 'apply classification, least privilege, auditability, retention, backup, restoration, and responsible deletion', 'classification: internal\nretention_days: 365\nbackup_tested: true\nrestore_point: 2026-01-15', 'create a governance and disaster-recovery plan with access matrix, retention rules, restore drill, and audit evidence.'),
    ],
    'sql': [
        ('Window functions and analytical SQL', 'use partitions, frames, common table expressions, and execution plans to express auditable analytics', 'SELECT category, amount,\n SUM(amount) OVER (PARTITION BY category ORDER BY day) AS running_total\nFROM expenses;', 'write analytical queries using ranking and running totals, then verify ties, nulls, empty groups, and plan cost.'),
        ('Transactions, isolation, and query optimization', 'reason about locks, isolation anomalies, indexing, statistics, plans, and safe schema evolution', 'BEGIN;\nUPDATE stock SET quantity = quantity - 1 WHERE id = 7 AND quantity > 0;\n-- require exactly one affected row\nCOMMIT;', 'design a concurrent sale transaction, reproduce an anomaly, choose isolation and indexes, and justify the resulting plan.'),
    ],
    'sqlite': [
        ('Query planning, indexes, and full-text search', 'inspect query plans, design selective indexes, use FTS carefully, and measure write/read tradeoffs', 'EXPLAIN QUERY PLAN\nSELECT * FROM loans WHERE student_id = 7 ORDER BY loaned_at DESC;', 'optimize a measured search workload with indexes or FTS and retain before-and-after plans and timing evidence.'),
        ('WAL, migrations, backup, and recovery', 'configure concurrent readers, execute atomic migrations, verify integrity, and test online backup and corruption recovery', 'PRAGMA journal_mode=WAL;\nPRAGMA integrity_check;\nPRAGMA user_version;', 'build a versioned migration and backup/restore drill that survives interruption without losing the previous valid database.'),
    ],
    'postgresql': [
        ('Advanced indexing, plans, and partitioning', 'interpret EXPLAIN ANALYZE, choose index families, maintain statistics, and partition only for measured needs', 'EXPLAIN (ANALYZE, BUFFERS)\nSELECT * FROM loans WHERE returned_at IS NULL AND student_id = 7;', 'tune a representative workload using measured plans and justify indexes, statistics, and any partition boundary.'),
        ('Concurrency, replication, and operations', 'apply MVCC isolation, advisory locks, roles, backup, point-in-time recovery, monitoring, and failover reasoning', 'BEGIN ISOLATION LEVEL SERIALIZABLE;\n-- read invariant, apply change, retry serialization failures\nCOMMIT;', 'design a retry-safe transaction and complete a role, backup, restore, monitoring, and simulated failover exercise.'),
    ],
    'mongodb': [
        ('Aggregation and schema evolution', 'design bounded pipelines, indexes, validation, denormalization policy, and compatible document migrations', 'db.loans.aggregate([\n {$match:{returned:false}},\n {$group:{_id:"$bookId", total:{$sum:1}}}\n])', 'build and explain an indexed aggregation, then migrate mixed document versions without breaking old readers.'),
        ('Transactions, replication, and operations', 'choose transaction boundaries, read/write concerns, shard keys, backup, restore, and observable failure handling', 'session.withTransaction(async () => {\n  // update loan and inventory with retry-safe identifiers\n});', 'design a retry-safe multi-document workflow and document replica failure, recovery, backup, restore, and consistency evidence.'),
    ],
}

LOCAL_TITLES = {
 'Protocols, descriptors, and metaprogramming': ('پروتکل‌ها، توصیف‌گرها و فرابرنامه‌نویسی','پروتوکولونه، توصیفګرونه او مېټاپروګرام‌لیکنه'),
 'Async services, packaging, and secure delivery': ('خدمات ناهمگام، بسته‌بندی و تحویل امن','نامتقارن خدمتونه، بسته کول او خوندي سپارل'),
 'Design systems and component architecture': ('سیستم طراحی و معماری اجزا','ډیزاین سیسټم او د اجزاوو معماري'),
 'Advanced accessibility and performance': ('دسترس‌پذیری و کارایی پیشرفته','پرمختللی لاسرسی او کړنه'),
 'Distributed system boundaries': ('مرزهای سیستم توزیع‌شده','د وېشل شوي سیسټم پولې'),
 'Security, observability, and deployment': ('امنیت، مشاهده‌پذیری و استقرار','امنیت، څارنه او ځای پر ځای کول'),
 'Concurrency and the Java memory model': ('هم‌زمانی و مدل حافظهٔ جاوا','هممهالي او د جاوا حافظې موډل'),
 'JVM architecture, profiling, and delivery': ('معماری JVM، پروفایل و تحویل','د JVM معماري، پروفایل او سپارل'),
 'Coroutines, Flow, and structured concurrency': ('کوروتین، Flow و هم‌زمانی ساختاری','کوروتین، Flow او جوړښتي هممهالي'),
 'DSLs, multiplatform boundaries, and performance': ('DSL، مرزهای چندسکویی و کارایی','DSL، څو پلاتفورمي پولې او کړنه'),
 'Offline-first synchronization architecture': ('معماری همگام‌سازی با اولویت آفلاین','آفلاین لومړیتوب همغږۍ معماري'),
 'Performance, security, and production delivery': ('کارایی، امنیت و تحویل تولید','کړنه، امنیت او تولیدي سپارل'),
 'Offline data, background work, and conflict handling': ('دادهٔ آفلاین، کار پس‌زمینه و حل تعارض','آفلاین معلومات، شالید کار او د ټکر حل'),
 'Privacy, performance, and App Store delivery': ('حریم خصوصی، کارایی و تحویل اپ‌استور','محرمیت، کړنه او اپ‌سټور سپارل'),
 'Actors and advanced concurrency': ('Actorها و هم‌زمانی پیشرفته','Actor او پرمختللی هممهالي'),
 'Protocols, generics, macros, and package design': ('پروتکل، جنریک، ماکرو و طراحی بسته','پروتوکول، جنریک، ماکرو او بسته ډیزاین'),
 'Templates, concepts, and compile-time design': ('قالب‌ها، conceptها و طراحی زمان ترجمه','ټیمپلېټونه، concept او د کمپایل وخت ډیزاین'),
 'Concurrency, profiling, and systems reliability': ('هم‌زمانی، پروفایل و قابلیت اعتماد سیستم','هممهالي، پروفایل او د سیسټم باوري‌توب'),
 'Event loop, workers, and performance': ('حلقهٔ رویداد، workerها و کارایی','د پېښو کړۍ، worker او کړنه'),
 'Language internals, security, and package design': ('درون‌ساخت زبان، امنیت و طراحی بسته','د ژبې دنننی جوړښت، امنیت او بسته ډیزاین'),
 'Concurrent rendering and application architecture': ('رندر هم‌زمان و معماری برنامه','هممهالی رینډر او د اپ معماري'),
 'Performance, accessibility, and secure delivery': ('کارایی، دسترس‌پذیری و تحویل امن','کړنه، لاسرسی او خوندي سپارل'),
 'Native modules, threads, and performance': ('ماژول بومی، thread و کارایی','اصلي ماډیولونه، thread او کړنه'),
 'Offline-first mobile delivery': ('تحویل موبایل با اولویت آفلاین','آفلاین لومړیتوب موبایل سپارل'),
 'Streams, workers, and backpressure': ('جریان‌ها، workerها و فشار معکوس','جریانونه، worker او شاتګ فشار'),
 'Diagnostics, security, and production operations': ('تشخیص، امنیت و عملیات تولید','تشخیص، امنیت او تولیدي عملیات'),
 'Service architecture and resilient workflows': ('معماری خدمت و گردش‌کار پایدار','د خدمت معماري او زغم لرونکی کاري بهیر'),
 'API security, observability, and operations': ('امنیت API، مشاهده‌پذیری و عملیات','د API امنیت، څارنه او عملیات'),
 'Rendering, isolates, and performance engineering': ('رندر، isolate و مهندسی کارایی','رینډر، isolate او د کړنې انجنیري'),
 'Platform integration, security, and release automation': ('یکپارچه‌سازی پلتفرم، امنیت و خودکارسازی انتشار','د پلاتفورم یوځای کول، امنیت او اتومات خپرول'),
 'Distributed data and consistency models': ('دادهٔ توزیع‌شده و مدل‌های سازگاری','وېشل شوي معلومات او د سازګارۍ موډلونه'),
 'Data governance, security, and lifecycle': ('حاکمیت داده، امنیت و چرخهٔ عمر','د معلوماتو حاکمیت، امنیت او ژوند پړاو'),
 'Window functions and analytical SQL': ('تابع‌های پنجره‌ای و SQL تحلیلی','کړکۍ دندې او تحلیلي SQL'),
 'Transactions, isolation, and query optimization': ('تراکنش، جداسازی و بهینه‌سازی پرس‌وجو','معاملې، جلاوالی او د پوښتنې سمون'),
 'Query planning, indexes, and full-text search': ('برنامهٔ پرس‌وجو، نمایه و جستجوی تمام‌متن','د پوښتنې پلان، شاخصونه او بشپړمتن لټون'),
 'WAL, migrations, backup, and recovery': ('WAL، مهاجرت، پشتیبان و بازیابی','WAL، کډون، شاتړ او بېرته راګرځول'),
 'Advanced indexing, plans, and partitioning': ('نمایه‌سازی، پلان و بخش‌بندی پیشرفته','پرمختللي شاخصونه، پلانونه او وېش'),
 'Concurrency, replication, and operations': ('هم‌زمانی، تکثیر و عملیات','هممهالي، نقل او عملیات'),
 'Aggregation and schema evolution': ('تجمیع و تکامل شِما','راټولونه او د سکیما بدلون'),
 'Transactions, replication, and operations': ('تراکنش، تکثیر و عملیات','معاملې، نقل او عملیات'),
 'Requirements and domain discovery': ('کشف نیازها و حوزهٔ مسئله','د اړتیاوو او مسئلې ساحې موندنه'),
 'Models, interfaces, and contracts': ('مدل‌ها، رابط‌ها و قراردادها','موډلونه، اړیک‌مخونه او تړونونه'),
 'Validation and failure recovery': ('اعتبارسنجی و بازیابی از شکست','ارزونه او له ناکامۍ رغونه'),
 'Testing strategy and quality gates': ('راهبرد آزمون و دروازه‌های کیفیت','د ازموینې تګلاره او د کیفیت پړاوونه'),
 'Architecture and dependency boundaries': ('معماری و مرزهای وابستگی','معماري او د تړاو پولې'),
 'Security, privacy, and inclusive access': ('امنیت، حریم خصوصی و دسترسی فراگیر','امنیت، محرمیت او ټولشموله لاسرسی'),
 'Performance and resource budgets': ('کارایی و بودجهٔ منابع','کړنه او د سرچینو بودجه'),
 'Capstone delivery and maintenance': ('تحویل و نگه‌داری پروژهٔ نهایی','د وروستۍ پروژې سپارل او ساتنه'),
}

ENGINEERING_STUDIOS = [
    ('Requirements and domain discovery', 'turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples', 'User: a learner with an older device\nNeed: finish work without internet\nAcceptance: saved work survives restart\nOut of scope: cloud accounts', 'interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope.'),
    ('Models, interfaces, and contracts', 'model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors', 'Input contract: non-empty learner_id\nRule: progress can only move forward\nResult: saved progress or a specific error\nAdapter: local file or database', 'draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary.'),
    ('Validation and failure recovery', 'validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand', 'normal: 3 valid records -> save\nedge: empty list -> valid empty result\ninvalid: negative score -> reject\ninterruption: old data remains readable', 'build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery.'),
    ('Testing strategy and quality gates', 'combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation', 'Given saved progress at lesson 2\nWhen the app restarts offline\nThen lesson 2 remains complete\nAnd lesson 3 is the next available step', 'create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch.'),
    ('Architecture and dependency boundaries', 'apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable', 'presentation -> application -> domain\ndata implements domain ports\nplatform code stays behind adapters\nDecision: local storage is the source of truth', 'refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network.'),
    ('Security, privacy, and inclusive access', 'threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs', 'Asset: learner progress\nThreat: unintended disclosure\nControl: local minimum data\nAccess check: keyboard + 200% text\nRecovery: explicit local backup', 'produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data.'),
    ('Performance and resource budgets', 'measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices', 'startup budget: 2 seconds\ninteraction budget: 100 ms\nstorage budget: 50 MB\noffline check: airplane mode from first launch', 'choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass.'),
    ('Capstone delivery and maintenance', 'plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release', 'Release evidence:\n- acceptance checks pass\n- migration and rollback tested\n- offline install documented\n- known limits published\n- next improvement prioritized', 'deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration.'),
]

COURSE_LABELS = {
    'python':'Python', 'web-design':'web design', 'web-development':'web development',
    'java':'Java', 'kotlin':'Kotlin', 'android':'Android', 'ios':'iOS', 'swift':'Swift',
    'cpp':'C++', 'javascript':'JavaScript', 'reactjs':'React', 'reactnative':'React Native',
    'nodejs':'Node.js', 'expressjs':'Express', 'flutter-dart':'Flutter and Dart',
    'database-foundations':'database foundations', 'sql':'SQL', 'sqlite':'SQLite',
    'postgresql':'PostgreSQL', 'mongodb':'MongoDB',
}

def advanced_for(course_id):
    label = COURSE_LABELS[course_id]
    return [
        (
            title,
            f'This {label} module teaches you to {focus}. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.\n\nHint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.',
            example,
            f'{challenge[0].upper() + challenge[1:]} Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback.',
        )
        for title, focus, example, challenge in [*TOPICS[course_id], *ENGINEERING_STUDIOS]
    ]

def local_title(title, language):
    return LOCAL_TITLES[title][0 if language == 'fa' else 1]
