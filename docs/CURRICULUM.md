# Learn By Marifat Team — Curriculum and lesson plans

Original curriculum, edition 3. Bloom means the revised cognitive taxonomy, not an accreditation or a fixed rule requiring every lesson to traverse six levels. These are guided lesson plans and project assignments, not a claim that every toolchain is embedded in the app.

Every course has sixteen modules, thirty-two planned sessions (40 guided hours), and three projects (6 + 12 + 24 estimated hours). Modules seven through sixteen progress through advanced technology and applied software engineering. Allow additional practice and remediation. “Zero to Hero” names the Python pathway; competence requires demonstrated work, not seat time.

## Lesson delivery protocol

Guided session (60 min): retrieval 5, explanation and worked trace 15, guided practice 20, evidence assessment 15, reflection 5. Independent studio (90 min): retrieval 10, design 15, implementation 35, testing/review 20, reflection 10. Read the module explanation and example before the activity. Examples marked as fragments belong inside a provisioned project; they are not all standalone programs.

Remediation: return to the worked trace, reduce the input to one record, explain the failure, then retry with a different input. Extension: add a justified requirement and regression tests. Pair work is optional; a paper trace and self-review provide an offline alternative. Plans, evidence prompts, and examples are bundled in the app; toolchains are separately provisioned.

## Project assessment rubric

Score each dimension from 0 to 3: correctness, design, verification, usability/accessibility, and reproducibility. 0 = absent; 1 = partial with major gaps; 2 = meets requirements with recorded evidence; 3 = meets requirements plus justified edge-case improvements. Recommended readiness: every requirement demonstrated and every dimension at least 2. Self-ratings are provisional until a peer or teacher reviews the evidence. No automatic certification.

## Python Course Zero to Hero

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Python basics run in the app’s limited sandbox. Advanced modules require a separately installed CPython 3 interpreter; use only the standard library. Save local .py files and run python filename.py. No pip packages are needed for these projects.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

No programming experience is needed. Open Code lab. Replace its sample with the two lines below. Type straight quotes, not decorative quotation marks. Press Run code. You can also trace the example on paper.

Vocabulary:

- Program: a sequence of instructions a computer follows.
- String: text enclosed in quotes.
- Variable: a name that refers to a value.
- Output: the result a program displays.

```text
name = "Salam"
print(name)
```

- Line 1 stores the string Salam under the name name. The equals sign assigns a value; it does not ask a question.
- Line 2 reads that value and displays Salam. The quotes and variable name are not printed.
- Change Salam to Kabul and run again. Only the displayed word changes.

Readiness check: What will print(name) display after name = "Salam"?

Answer: Salam

Guided practice: Store Kabul in a variable named city, then display city on one line.

Hint: Replace both uses of name with city. Keep the text inside quotes.

Reference solution:

```text
city = "Kabul"
print(city)
```

Expected result: Kabul

### Values, decisions, and loops

Variables name values; conditionals select a branch and loops repeat a rule. Trace one iteration at a time. Validate that a quantity is nonnegative before calculating a total. Complete the seven interactive Python foundation lessons before this studio.

```text
prices = [20, 35, 15]
total = 0
for price in prices:
    total = total + price
print(total)
```

#### Values, decisions, and loops: guided investigation (60 min; Remember)

ID: `python-m1-l1`

Objective: Identify the key terms and syntax in values, decisions, and loops without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a shopping total that rejects negative quantities. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Values, decisions, and loops: independent studio (90 min; Understand)

ID: `python-m1-l2`

Objective: Explain how values, decisions, and loops changes program behavior using a traced example.

Activity: a shopping total that rejects negative quantities. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Functions and data structures

Separate calculation from input and output. Lists preserve sequence; dictionaries associate unique keys with values; sets remove duplicates. A pure function produces a result without modifying shared state.

```text
def total(items):
    return sum(item["price"] * item["quantity"] for item in items)
assert total([]) == 0
```

#### Functions and data structures: guided investigation (60 min; Understand)

ID: `python-m2-l1`

Objective: Explain how functions and data structures changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an inventory summary using dictionaries and functions with tests for duplicate item names. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Functions and data structures: independent studio (90 min; Apply)

ID: `python-m2-l2`

Objective: Implement an inventory summary using dictionaries and functions with tests for duplicate item names.

Activity: an inventory summary using dictionaries and functions with tests for duplicate item names. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Files, exceptions, and modules

Use context managers to close files even when reading fails. JSON carries structured data, but parsing does not validate its business meaning. Catch a specific exception and preserve the previous valid file when a write fails.

```text
import json
from pathlib import Path
path = Path("items.json")
path.write_text(json.dumps([{ "name": "Notebook", "stock": 4 }]), encoding="utf-8")
print(json.loads(path.read_text(encoding="utf-8")))
```

#### Files, exceptions, and modules: guided investigation (60 min; Apply)

ID: `python-m3-l1`

Objective: Implement a JSON importer that reports malformed data without erasing the last valid records.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a JSON importer that reports malformed data without erasing the last valid records. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Files, exceptions, and modules: independent studio (90 min; Analyze)

ID: `python-m3-l2`

Objective: Locate a failing assumption in files, exceptions, and modules and isolate it with a minimal reproduction.

Activity: a JSON importer that reports malformed data without erasing the last valid records. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Objects, typing, and iterators

A class groups state and invariants. Prefer composition when behavior can be delegated. Type hints communicate contracts; they do not enforce values at runtime. Generators yield records incrementally instead of building an entire result list.

```text
from dataclasses import dataclass
@dataclass(frozen=True)
class Item:
    name: str
    stock: int

def available(items):
    for item in items:
        if item.stock > 0:
            yield item
```

#### Objects, typing, and iterators: guided investigation (60 min; Analyze)

ID: `python-m4-l1`

Objective: Locate a failing assumption in objects, typing, and iterators and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an immutable item model and a generator that filters available stock without altering the source. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Objects, typing, and iterators: independent studio (90 min; Evaluate)

ID: `python-m4-l2`

Objective: Judge two approaches to objects, typing, and iterators against correctness, maintainability, and offline operation.

Activity: an immutable item model and a generator that filters available stock without altering the source. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### SQLite, testing, and architecture

Put persistence behind a repository interface so calculations can be tested without a database. SQL placeholders separate values from commands. A transaction groups related changes; rollback prevents a half-recorded sale. Use unittest for boundary and regression cases.

```text
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE stock (name TEXT PRIMARY KEY, quantity INTEGER)")
    db.execute("INSERT INTO stock VALUES (?, ?)", ("Notebook", 4))
    assert db.execute("SELECT quantity FROM stock").fetchone()[0] == 4
```

#### SQLite, testing, and architecture: guided investigation (60 min; Evaluate)

ID: `python-m5-l1`

Objective: Judge two approaches to sqlite, testing, and architecture against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a transactional stock sale that rolls back when requested quantity exceeds availability. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### SQLite, testing, and architecture: independent studio (90 min; Create)

ID: `python-m5-l2`

Objective: Design and deliver an original extension using sqlite, testing, and architecture with explicit acceptance tests.

Activity: a transactional stock sale that rolls back when requested quantity exceeds availability. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Concurrency, profiling, and delivery

A worker can keep an interface responsive, but shared mutable data introduces races. Compare sequential work with an executor using measured timings. Profile before optimizing, keep SQLite ownership explicit, and distribute a README and reproducible standard-library tests.

```text
from concurrent.futures import ThreadPoolExecutor
def summarize(values):
    return sum(values)
with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(summarize, [[1, 2], [3, 4]])))
```

#### Concurrency, profiling, and delivery: guided investigation (60 min; Create)

ID: `python-m6-l1`

Objective: Design and deliver an original extension using concurrency, profiling, and delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a batch report with sequential and worker implementations, measuring time and checking equal results. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Concurrency, profiling, and delivery: independent studio (90 min; Evaluate)

ID: `python-m6-l2`

Objective: Judge two approaches to concurrency, profiling, and delivery against correctness, maintainability, and offline operation.

Activity: a batch report with sequential and worker implementations, measuring time and checking equal results. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Protocols, descriptors, and metaprogramming

This Python module teaches you to define stable behavioral contracts and control attribute access without fragile inheritance. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
from typing import Protocol
class Priced(Protocol):
    price: int
def total(items: list[Priced]) -> int:
    return sum(item.price for item in items)
```

#### Protocols, descriptors, and metaprogramming: guided investigation (60 min; Create)

ID: `python-m7-l1`

Objective: Design and deliver an original extension using protocols, descriptors, and metaprogramming with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design a protocol-based pricing service and test two unrelated implementations. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Protocols, descriptors, and metaprogramming: independent studio (90 min; Evaluate)

ID: `python-m7-l2`

Objective: Judge two approaches to protocols, descriptors, and metaprogramming against correctness, maintainability, and offline operation.

Activity: Design a protocol-based pricing service and test two unrelated implementations. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Async services, packaging, and secure delivery

This Python module teaches you to coordinate bounded asynchronous work, package reproducibly, and protect local inputs and secrets. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
import asyncio
async def report(values):
    await asyncio.sleep(0)
    return sum(values)
print(asyncio.run(report([20, 30])))
```

#### Async services, packaging, and secure delivery: guided investigation (60 min; Create)

ID: `python-m8-l1`

Objective: Design and deliver an original extension using async services, packaging, and secure delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build an offline asynchronous report pipeline with timeouts, cancellation, tests, and a reproducible package. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Async services, packaging, and secure delivery: independent studio (90 min; Evaluate)

ID: `python-m8-l2`

Objective: Judge two approaches to async services, packaging, and secure delivery against correctness, maintainability, and offline operation.

Activity: Build an offline asynchronous report pipeline with timeouts, cancellation, tests, and a reproducible package. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Python module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `python-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `python-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Python module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `python-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `python-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Python module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `python-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `python-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Python module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `python-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `python-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Python module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `python-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `python-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Python module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `python-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `python-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Python module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `python-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `python-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Python module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `python-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `python-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Household expense ledger (6 hours)

Help a fictional family understand weekly spending in AFN.

Acceptance conditions:

- Add dated expenses in integer AFN with a category.
- Reject negative amounts and blank categories.
- Produce category totals and a weekly total from local JSON.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: School attendance analyst (12 hours)

Help a teacher summarize attendance from a local CSV file.

Acceptance conditions:

- Validate student IDs, dates, and duplicate rows.
- Calculate attendance percentages with a defined zero-session rule.
- Export a UTF-8 report and test malformed CSV cases.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Community shop inventory (24 hours)

Build an offline stock and sales tool for a small stationery shop.

Acceptance conditions:

- Persist items and sales in SQLite; use an atomic sale transaction.
- Prevent overselling and retain stock after restart.
- Provide low-stock reports, JSON export, and automated regression tests.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Web Design

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Use a local text editor and browser. Open index.html directly; bundle CSS, images, and fonts locally. No CDN, online design service, or package manager is required.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

No programming experience is needed. Create a folder named first-page. In a plain-text editor save a file named index.html, not index.html.txt. Paste the example, save it, and open it in a browser. No internet is needed.

Vocabulary:

- HTML: markup that gives a document structure.
- Element: a piece of a page, usually marked by opening and closing tags.
- Heading: a title that describes the following content.
- Browser: the application that displays a web document.

```text
<!doctype html>
<html lang="en">
  <h1>School library</h1>
  <p>Open today</p>
</html>
```

- The doctype asks the browser to use modern HTML rules.
- The h1 tags mark the main heading; they are not visible text.
- The p tags mark a paragraph. Edit Open today, save the file, then refresh the browser.

Readiness check: Which element marks the main heading?

Answer: h1

Guided practice: Create a page with the heading My first page and a paragraph reading I can learn.

Hint: Keep the tags in pairs and change the text between them.

Reference solution:

```text
<!doctype html>
<html lang="en">
<h1>My first page</h1>
<p>I can learn.</p>
</html>
```

Expected result: The browser shows My first page as a heading and I can learn. as a paragraph.

### Semantic HTML

A page is a document before it is a visual composition. Landmarks, headings, lists, and labels express relationships to browsers and assistive tools. Choose elements by meaning, then style them.

```text
<main>
  <h1>Community library</h1>
  <nav aria-label="Sections"><a href="#hours">Opening hours</a></nav>
  <section id="hours"><h2>Hours</h2><p>Saturday–Thursday, 9–4</p></section>
</main>
```

#### Semantic HTML: guided investigation (60 min; Remember)

ID: `web-design-m1-l1`

Objective: Identify the key terms and syntax in semantic html without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a library page with a meaningful heading hierarchy and working internal navigation. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Semantic HTML: independent studio (90 min; Understand)

ID: `web-design-m1-l2`

Objective: Explain how semantic html changes program behavior using a traced example.

Activity: a library page with a meaningful heading hierarchy and working internal navigation. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### CSS cascade and typography

The cascade resolves competing declarations; inheritance passes selected values to descendants. Use a small spacing and color system instead of unrelated numbers. Relative units support larger text settings.

```text
body { font: 1rem/1.6 system-ui, sans-serif; margin: 0; }
main { max-width: 65ch; margin-inline: auto; padding: 1.5rem; }
a:focus-visible { outline: 3px solid #175c40; }
```

#### CSS cascade and typography: guided investigation (60 min; Understand)

ID: `web-design-m2-l1`

Objective: Explain how css cascade and typography changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a readable type and spacing system with visible keyboard focus. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### CSS cascade and typography: independent studio (90 min; Apply)

ID: `web-design-m2-l2`

Objective: Implement a readable type and spacing system with visible keyboard focus.

Activity: a readable type and spacing system with visible keyboard focus. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Responsive layout

Flexbox aligns a row or column; Grid coordinates two dimensions. Let content choose breakpoints. Avoid fixed heights that clip translated or enlarged text, and test the narrowest supported viewport.

```text
.cards { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }
```

#### Responsive layout: guided investigation (60 min; Apply)

ID: `web-design-m3-l1`

Objective: Implement a card layout that reflows at 320, 768, and 1280 CSS pixels without horizontal overflow.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a card layout that reflows at 320, 768, and 1280 CSS pixels without horizontal overflow. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Responsive layout: independent studio (90 min; Analyze)

ID: `web-design-m3-l2`

Objective: Locate a failing assumption in responsive layout and isolate it with a minimal reproduction.

Activity: a card layout that reflows at 320, 768, and 1280 CSS pixels without horizontal overflow. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Forms and accessibility

Labels identify fields; instructions and error messages explain how to recover. Native controls provide useful keyboard behavior. Do not use color alone to indicate an error. HTML validation helps users but is not server-side security.

```text
<label for="name">Student name</label>
<input id="name" name="name" required aria-describedby="name-help">
<p id="name-help">Enter the name used on your school record.</p>
```

#### Forms and accessibility: guided investigation (60 min; Analyze)

ID: `web-design-m4-l1`

Objective: Locate a failing assumption in forms and accessibility and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a registration form with labels, keyboard access, and understandable required-field errors. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Forms and accessibility: independent studio (90 min; Evaluate)

ID: `web-design-m4-l2`

Objective: Judge two approaches to forms and accessibility against correctness, maintainability, and offline operation.

Activity: a registration form with labels, keyboard access, and understandable required-field errors. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### RTL and inclusive design

Set direction on the relevant document or region. Logical properties such as margin-inline adapt to direction; source-code blocks remain left-to-right. Test mixed numbers, names, and long translations with native readers before release.

```text
<article lang="fa" dir="rtl"><h1>کتابخانه</h1><p>ساعت کار: ۹ تا ۴</p></article>
<pre dir="ltr">print("Salam")</pre>
```

#### RTL and inclusive design: guided investigation (60 min; Evaluate)

ID: `web-design-m5-l1`

Objective: Judge two approaches to rtl and inclusive design against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an English and Dari page pair with logical spacing and a documented translation review checklist. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### RTL and inclusive design: independent studio (90 min; Create)

ID: `web-design-m5-l2`

Objective: Design and deliver an original extension using rtl and inclusive design with explicit acceptance tests.

Activity: an English and Dari page pair with logical spacing and a documented translation review checklist. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Design systems and usability

Reusable tokens and components reduce accidental variation. Evaluate a design through tasks: can a learner locate hours, navigate with a keyboard, and read at 200% zoom? Record observed difficulties and revise one component at a time.

```text
:root { --space: 1rem; --ink: #162f28; --surface: #fffdf5; }
.card { padding: var(--space); color: var(--ink); background: var(--surface); }
```

#### Design systems and usability: guided investigation (60 min; Create)

ID: `web-design-m6-l1`

Objective: Design and deliver an original extension using design systems and usability with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a small component guide and a usability report with three observed issues and fixes. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Design systems and usability: independent studio (90 min; Evaluate)

ID: `web-design-m6-l2`

Objective: Judge two approaches to design systems and usability against correctness, maintainability, and offline operation.

Activity: a small component guide and a usability report with three observed issues and fixes. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Design systems and component architecture

This web design module teaches you to turn tokens, components, states, and content rules into a maintainable interface system. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
:root { --space-2: .5rem; --brand: #087c89; }
.button { padding: var(--space-2) 1rem; }
.button:focus-visible { outline: 3px solid currentColor; }
```

#### Design systems and component architecture: guided investigation (60 min; Create)

ID: `web-design-m7-l1`

Objective: Design and deliver an original extension using design systems and component architecture with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a documented local design system with accessible default, hover, focus, error, and disabled states. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Design systems and component architecture: independent studio (90 min; Evaluate)

ID: `web-design-m7-l2`

Objective: Judge two approaches to design systems and component architecture against correctness, maintainability, and offline operation.

Activity: Create a documented local design system with accessible default, hover, focus, error, and disabled states. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Advanced accessibility and performance

This web design module teaches you to audit semantics, keyboard flow, contrast, motion, responsive images, and rendering cost under real constraints. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; }
}
```

#### Advanced accessibility and performance: guided investigation (60 min; Create)

ID: `web-design-m8-l1`

Objective: Design and deliver an original extension using advanced accessibility and performance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Audit and repair a multi-page site for keyboard, screen-reader, large-text, reduced-motion, and offline performance. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Advanced accessibility and performance: independent studio (90 min; Evaluate)

ID: `web-design-m8-l2`

Objective: Judge two approaches to advanced accessibility and performance against correctness, maintainability, and offline operation.

Activity: Audit and repair a multi-page site for keyboard, screen-reader, large-text, reduced-motion, and offline performance. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This web design module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `web-design-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `web-design-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This web design module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `web-design-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `web-design-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This web design module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `web-design-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `web-design-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This web design module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `web-design-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `web-design-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This web design module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `web-design-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `web-design-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This web design module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `web-design-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `web-design-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This web design module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `web-design-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `web-design-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This web design module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `web-design-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `web-design-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Student portfolio (6 hours)

Present a fictional student’s work in an accessible local website.

Acceptance conditions:

- Use semantic sections and local images with appropriate alternative text.
- Provide keyboard navigation and a printable résumé.
- Remain readable at 320px width and 200% zoom.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Bilingual school information site (12 hours)

Make school schedules understandable in English and Dari.

Acceptance conditions:

- Create two local language pages with correct direction.
- Include timetables with table headings and clear dates.
- Use no external fonts, scripts, or image requests.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Community services design system (24 hours)

Create an accessible site for library, training, and community events.

Acceptance conditions:

- Deliver reusable navigation, cards, forms, and typography tokens.
- Document responsive states and error states.
- Conduct three task-based usability checks and record revisions.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Web Development

Prerequisites: web-design, javascript, nodejs, expressjs

Offline tools: Provision a browser, Node.js, Express, and the package cache in advance. Run client and server on the same computer using loopback. Localhost is used for practice; no internet service is required.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

First complete Web Design, JavaScript, NodeJs, and ExpressJs. If these words are new, open the prerequisites below. This first example is a paper trace; it does not require a running server.

Vocabulary:

- Client: the program that asks for a resource.
- Server: the program that receives and answers a request.
- HTTP: a set of rules for web requests and responses.
- Status: a number describing the result of a request.

```text
Client: GET /books
Server: 200 OK
Body: [{"title":"Algorithms"}]
```

- The client asks for the resource named /books.
- The server reports 200 to indicate success.
- The response body carries data. The browser still needs instructions to render that data on a page.

Readiness check: Which participant sends the response?

Answer: The server

Guided practice: Write a request and a successful response for a local /courses resource with one course.

Hint: Use the same three-part trace and change the resource and JSON data.

Reference solution:

```text
Client: GET /courses
Server: 200 OK
Body: [{"title":"Python"}]
```

Expected result: A request, a success status, and a JSON array containing one course are present.

### Client, server, and HTTP

The browser requests resources; a server returns a status, headers, and a body. A local server is still a server, even without internet. Distinguish persistent data from the rendered document.

```text
GET /books HTTP/1.1
Host: 127.0.0.1:3000

HTTP/1.1 200 OK
Content-Type: application/json

[{"id":1,"title":"Algorithms"}]
```

#### Client, server, and HTTP: guided investigation (60 min; Remember)

ID: `web-development-m1-l1`

Objective: Identify the key terms and syntax in client, server, and http without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a sequence diagram connecting a search interaction to a local HTTP response. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Client, server, and HTTP: independent studio (90 min; Understand)

ID: `web-development-m1-l2`

Objective: Explain how client, server, and http changes program behavior using a traced example.

Activity: a sequence diagram connecting a search interaction to a local HTTP response. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Forms and API contracts

Agree on request and response shapes before wiring the interface. Validate at the server boundary and render field errors near their controls. A successful HTTP transport does not imply a valid business operation.

```text
const response = await fetch("/api/books");
if (!response.ok) throw new Error("Could not load books");
const books = await response.json();
```

#### Forms and API contracts: guided investigation (60 min; Understand)

ID: `web-development-m2-l1`

Objective: Explain how forms and api contracts changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a book form with both client hints and server validation errors. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Forms and API contracts: independent studio (90 min; Apply)

ID: `web-development-m2-l2`

Objective: Implement a book form with both client hints and server validation errors.

Activity: a book form with both client hints and server validation errors. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Relational modeling and transactions

Model entities with stable IDs and constraints. A loan links a member and a book; an atomic transaction must prevent two active loans for the same copy. Schema changes need migrations and rollback plans.

```text
CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL);
CREATE TABLE loans (id INTEGER PRIMARY KEY, book_id INTEGER NOT NULL REFERENCES books(id), returned_at TEXT);
```

#### Relational modeling and transactions: guided investigation (60 min; Apply)

ID: `web-development-m3-l1`

Objective: Implement a library schema and a transaction design that prevents duplicate active loans.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a library schema and a transaction design that prevents duplicate active loans. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Relational modeling and transactions: independent studio (90 min; Analyze)

ID: `web-development-m3-l2`

Objective: Locate a failing assumption in relational modeling and transactions and isolate it with a minimal reproduction.

Activity: a library schema and a transaction design that prevents duplicate active loans. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Security boundaries

Treat all input as untrusted. Authorization belongs on the server for each operation. Escape text when rendering HTML, parameterize database queries, and never store plaintext passwords. For this offline learning project, use fictional roles without claiming production authentication.

```text
const titleNode = document.createElement("span");
titleNode.textContent = userSuppliedTitle;
```

#### Security boundaries: guided investigation (60 min; Analyze)

ID: `web-development-m4-l1`

Objective: Locate a failing assumption in security boundaries and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a threat model covering stored script injection, unauthorized edits, and unsafe file paths. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Security boundaries: independent studio (90 min; Evaluate)

ID: `web-development-m4-l2`

Objective: Judge two approaches to security boundaries against correctness, maintainability, and offline operation.

Activity: a threat model covering stored script injection, unauthorized edits, and unsafe file paths. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing and fault recovery

Test contracts between layers, not only isolated helpers. Simulate a failed write and an unavailable server. Display recoverable errors while preserving the user’s unsaved input. A retry must not silently create duplicate records.

```text
const operation = { id: "request-001", bookId: 7 };
// Persist and deduplicate operation.id in the same transaction as the loan.
```

#### Testing and fault recovery: guided investigation (60 min; Evaluate)

ID: `web-development-m5-l1`

Objective: Judge two approaches to testing and fault recovery against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an idempotent loan request and tests for retry after an ambiguous response. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Testing and fault recovery: independent studio (90 min; Create)

ID: `web-development-m5-l2`

Objective: Design and deliver an original extension using testing and fault recovery with explicit acceptance tests.

Activity: an idempotent loan request and tests for retry after an ambiguous response. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Offline packaging and maintainability

An offline package includes the client, server, database initialization, dependencies, and instructions. Separate domain rules from HTTP and storage. Build on a clean provisioned machine without fetching assets; document installation separately from runtime.

```text
project/
  domain/loan.js
  adapters/http.js
  adapters/storage.js
  public/index.html
  test/loan.test.js
```

#### Offline packaging and maintainability: guided investigation (60 min; Create)

ID: `web-development-m6-l1`

Objective: Design and deliver an original extension using offline packaging and maintainability with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a reproducible local release with seed data, migration instructions, and an airplane-mode acceptance report. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Offline packaging and maintainability: independent studio (90 min; Evaluate)

ID: `web-development-m6-l2`

Objective: Judge two approaches to offline packaging and maintainability against correctness, maintainability, and offline operation.

Activity: a reproducible local release with seed data, migration instructions, and an airplane-mode acceptance report. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Distributed system boundaries

This web development module teaches you to design versioned contracts, idempotent operations, retries, and failure isolation between client and server. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
POST /loans HTTP/1.1
Idempotency-Key: loan-42
Content-Type: application/json

{"bookId": 7}
```

#### Distributed system boundaries: guided investigation (60 min; Create)

ID: `web-development-m7-l1`

Objective: Design and deliver an original extension using distributed system boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design an idempotent lending workflow and prove that retrying cannot create duplicate records. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Distributed system boundaries: independent studio (90 min; Evaluate)

ID: `web-development-m7-l2`

Objective: Judge two approaches to distributed system boundaries against correctness, maintainability, and offline operation.

Activity: Design an idempotent lending workflow and prove that retrying cannot create duplicate records. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, observability, and deployment

This web development module teaches you to apply threat modeling, least privilege, structured logs, health checks, migrations, and reversible releases. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
request_id=8f2 action=create_loan outcome=accepted duration_ms=12
```

#### Security, observability, and deployment: guided investigation (60 min; Create)

ID: `web-development-m8-l1`

Objective: Design and deliver an original extension using security, observability, and deployment with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Ship a locally deployable service with a threat model, redacted logs, health checks, migration rollback, and recovery drill. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, observability, and deployment: independent studio (90 min; Evaluate)

ID: `web-development-m8-l2`

Objective: Judge two approaches to security, observability, and deployment against correctness, maintainability, and offline operation.

Activity: Ship a locally deployable service with a threat model, redacted logs, health checks, migration rollback, and recovery drill. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This web development module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `web-development-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `web-development-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This web development module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `web-development-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `web-development-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This web development module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `web-development-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `web-development-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This web development module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `web-development-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `web-development-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This web development module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `web-development-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `web-development-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This web development module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `web-development-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `web-development-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This web development module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `web-development-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `web-development-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This web development module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `web-development-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `web-development-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Local event registration (6 hours)

Manage seats for a fictional workshop on one local computer.

Acceptance conditions:

- Validate attendee input and capacity.
- Show inline errors without discarding form values.
- Export a registration list using fictional data.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Library lending system (12 hours)

Track books and loans through a browser and local service.

Acceptance conditions:

- Prevent duplicate active loans and support returns.
- Persist records and provide search and pagination.
- Test API contracts and database rollback behavior.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Training center administration (24 hours)

Integrate courses, enrollments, and attendance in a local full-stack app.

Acceptance conditions:

- Separate domain, API, and persistence responsibilities.
- Enforce capacity and role rules on the server.
- Ship installation instructions, migration tests, and a local backup workflow.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Java

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Install a JDK before going offline. Use javac Main.java and java Main for plain examples. Provision build tools and any test libraries beforehand; initial projects can use Java assertions with java -ea Main.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

No prior programming is required. A classroom computer needs an installed JDK. Save the example as Main.java. In that folder run javac Main.java, then java Main. Keep capital letters exactly as shown.

Vocabulary:

- Source file: a text file containing program instructions.
- Compiler: a tool that checks and translates source code.
- Method: a named group of instructions.
- println: a method that displays a value followed by a new line.

```text
public class Main {
  public static void main(String[] args) {
    System.out.println("Salam");
  }
}
```

- Main is the class name and matches the file name. The outer braces enclose the class.
- main is the entry method Java starts. Its braces enclose the instructions.
- println displays Salam. The semicolon ends this statement. Do not delete the surrounding structure yet.

Readiness check: Which text is displayed by this program?

Answer: Salam

Guided practice: Change the program so it displays Kabul instead of Salam.

Hint: Only change the characters inside the quoted string.

Reference solution:

```text
public class Main {
  public static void main(String[] args) {
    System.out.println("Kabul");
  }
}
```

Expected result: Kabul

### Types and control flow

Java checks declared types at compile time. Use integers for whole quantities and choose explicit rounding for money. A loop invariant states what remains true after every iteration.

```text
public class Main { public static void main(String[] args) { int total = 0; for (int value : new int[]{10,20,30}) total += value; System.out.println(total); } }
```

#### Types and control flow: guided investigation (60 min; Remember)

ID: `java-m1-l1`

Objective: Identify the key terms and syntax in types and control flow without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a marks summary with bounds checks and a stated loop invariant. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Types and control flow: independent studio (90 min; Understand)

ID: `java-m1-l2`

Objective: Explain how types and control flow changes program behavior using a traced example.

Activity: a marks summary with bounds checks and a stated loop invariant. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Classes and encapsulation

Keep mutable fields private and expose operations that preserve invariants. Constructors establish valid state. An interface describes a capability without fixing its implementation.

```text
final class Stock { private int quantity; Stock(int q) { if(q < 0) throw new IllegalArgumentException(); quantity=q; } int quantity() { return quantity; } }
```

#### Classes and encapsulation: guided investigation (60 min; Understand)

ID: `java-m2-l1`

Objective: Explain how classes and encapsulation changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a stock object that cannot be initialized with a negative quantity. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Classes and encapsulation: independent studio (90 min; Apply)

ID: `java-m2-l2`

Objective: Implement a stock object that cannot be initialized with a negative quantity.

Activity: a stock object that cannot be initialized with a negative quantity. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Collections and generics

List preserves order, Set expresses uniqueness, and Map associates keys with values. Generics reject incompatible element types during compilation. Define equality deliberately when objects become map keys.

```text
java.util.Map<String,Integer> stock = new java.util.HashMap<>();
stock.put("Notebook", 5);
stock.merge("Notebook", 2, Integer::sum);
```

#### Collections and generics: guided investigation (60 min; Apply)

ID: `java-m3-l1`

Objective: Implement a catalog with unique IDs, duplicate detection, and sorted reports.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a catalog with unique IDs, duplicate detection, and sorted reports. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Collections and generics: independent studio (90 min; Analyze)

ID: `java-m3-l2`

Objective: Locate a failing assumption in collections and generics and isolate it with a minimal reproduction.

Activity: a catalog with unique IDs, duplicate detection, and sorted reports. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Exceptions and file persistence

A checked exception makes a failure path visible in an API. Try-with-resources closes owned resources. Separate malformed user data from unavailable storage so recovery messages are specific.

```text
try (var lines = java.nio.file.Files.lines(java.nio.file.Path.of("items.txt"))) { lines.filter(s -> !s.isBlank()).forEach(System.out::println); }
```

#### Exceptions and file persistence: guided investigation (60 min; Analyze)

ID: `java-m4-l1`

Objective: Locate a failing assumption in exceptions and file persistence and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a file importer that reports line numbers and preserves valid existing records. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Exceptions and file persistence: independent studio (90 min; Evaluate)

ID: `java-m4-l2`

Objective: Judge two approaches to exceptions and file persistence against correctness, maintainability, and offline operation.

Activity: a file importer that reports line numbers and preserves valid existing records. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Streams, concurrency, and tests

Streams express transformations but side effects make reasoning harder. Executors separate task submission from thread creation. Protect shared state or avoid it; test deterministic domain functions separately from scheduling.

```text
var names = java.util.List.of("Kabul", "Herat", "Bamyan");
var sorted = names.stream().sorted().toList();
assert sorted.size() == 3;
```

#### Streams, concurrency, and tests: guided investigation (60 min; Evaluate)

ID: `java-m5-l1`

Objective: Judge two approaches to streams, concurrency, and tests against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a report pipeline and compare sequential and concurrent results under repeated runs. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Streams, concurrency, and tests: independent studio (90 min; Create)

ID: `java-m5-l2`

Objective: Design and deliver an original extension using streams, concurrency, and tests with explicit acceptance tests.

Activity: a report pipeline and compare sequential and concurrent results under repeated runs. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### SOLID and delivery

Dependency inversion lets business rules depend on a repository contract. A memory adapter supports fast tests; a file adapter supports persistence. Keep interfaces small and package a command-line entry point with reproducible execution instructions.

```text
interface ItemRepository { java.util.List<String> allNames(); }
final class Report { private final ItemRepository repository; Report(ItemRepository r) { repository=r; } int count() { return repository.allNames().size(); } }
```

#### SOLID and delivery: guided investigation (60 min; Create)

ID: `java-m6-l1`

Objective: Design and deliver an original extension using solid and delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a repository-backed report with fake storage and failure-path tests. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### SOLID and delivery: independent studio (90 min; Evaluate)

ID: `java-m6-l2`

Objective: Judge two approaches to solid and delivery against correctness, maintainability, and offline operation.

Activity: a repository-backed report with fake storage and failure-path tests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Concurrency and the Java memory model

This Java module teaches you to reason about visibility, atomicity, executors, immutable messages, and structured task lifecycles. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
try (var executor = java.util.concurrent.Executors.newVirtualThreadPerTaskExecutor()) {
  var future = executor.submit(() -> 40 + 2);
  System.out.println(future.get());
}
```

#### Concurrency and the Java memory model: guided investigation (60 min; Create)

ID: `java-m7-l1`

Objective: Design and deliver an original extension using concurrency and the java memory model with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a bounded concurrent importer and test cancellation, ordering, failure propagation, and clean shutdown. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Concurrency and the Java memory model: independent studio (90 min; Evaluate)

ID: `java-m7-l2`

Objective: Judge two approaches to concurrency and the java memory model against correctness, maintainability, and offline operation.

Activity: Build a bounded concurrent importer and test cancellation, ordering, failure propagation, and clean shutdown. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### JVM architecture, profiling, and delivery

This Java module teaches you to measure allocation and latency, define module boundaries, and create reproducible runtime images. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
module school.reports {
  exports school.reports.api;
}
```

#### JVM architecture, profiling, and delivery: guided investigation (60 min; Create)

ID: `java-m8-l1`

Objective: Design and deliver an original extension using jvm architecture, profiling, and delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Profile a modular reporting service, remove one measured bottleneck, and package it with repeatable offline build instructions. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### JVM architecture, profiling, and delivery: independent studio (90 min; Evaluate)

ID: `java-m8-l2`

Objective: Judge two approaches to jvm architecture, profiling, and delivery against correctness, maintainability, and offline operation.

Activity: Profile a modular reporting service, remove one measured bottleneck, and package it with repeatable offline build instructions. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Java module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `java-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `java-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Java module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `java-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `java-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Java module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `java-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `java-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Java module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `java-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `java-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Java module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `java-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `java-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Java module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `java-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `java-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Java module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `java-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `java-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Java module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `java-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `java-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Student gradebook (6 hours)

Produce course results from fictional marks.

Acceptance conditions:

- Validate marks from 0 to 100.
- Calculate averages with a documented rounding rule.
- Test empty classes and boundary marks.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Library desktop core (12 hours)

Implement the domain and command-line interface of a library.

Acceptance conditions:

- Use stable IDs for books and members.
- Reject borrowing an unavailable copy.
- Persist to local files and report malformed records.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Warehouse ledger (24 hours)

Maintain stock movements for a small warehouse.

Acceptance conditions:

- Encapsulate stock invariants and provide repository adapters.
- Generate sorted reports and reconcile movement totals.
- Test failure recovery and document the build and packaging steps.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Kotlin

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Provision Kotlin/JVM and a JDK. Compile local code with kotlinc Main.kt -include-runtime -d main.jar, then java -jar main.jar. Coroutine libraries and Gradle dependencies, if used, must be cached before offline study.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

No prior programming is required. On a provisioned computer save Main.kt. Compile with kotlinc Main.kt -include-runtime -d main.jar, then run java -jar main.jar. The app cannot run Kotlin code.

Vocabulary:

- Function: a named group of instructions.
- main: the starting function of this example.
- val: a binding that cannot be reassigned.
- String: a text value enclosed in quotes.

```text
fun main() {
  val city = "Kabul"
  println(city)
}
```

- fun introduces a function. The braces surround its body.
- val gives the text Kabul a name, city.
- println reads city and displays Kabul. It does not print the word city.

Readiness check: What is the value referred to by city?

Answer: Kabul

Guided practice: Use a val named greeting to display Salam.

Hint: Change the binding name and the quoted value, then update println.

Reference solution:

```text
fun main() {
  val greeting = "Salam"
  println(greeting)
}
```

Expected result: Salam

### Values, expressions, and nullability

Prefer val for bindings that do not change. A nullable type makes absence explicit; a safe call propagates null, while the Elvis operator supplies a fallback. Avoid force-unwrapping input that can be absent.

```text
fun main() { val name: String? = null; println(name?.uppercase() ?: "Guest") }
```

#### Values, expressions, and nullability: guided investigation (60 min; Remember)

ID: `kotlin-m1-l1`

Objective: Identify the key terms and syntax in values, expressions, and nullability without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a greeting and fee calculator that handles missing optional input. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Values, expressions, and nullability: independent studio (90 min; Understand)

ID: `kotlin-m1-l2`

Objective: Explain how values, expressions, and nullability changes program behavior using a traced example.

Activity: a greeting and fee calculator that handles missing optional input. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Functions and collections

Small functions can transform immutable lists. map changes each element, filter retains matching elements, and fold accumulates a result. Explain when a sequence avoids intermediate collections and when it adds overhead.

```text
val total = listOf(10, 20, 30).filter { it > 10 }.fold(0) { sum, n -> sum + n }
```

#### Functions and collections: guided investigation (60 min; Understand)

ID: `kotlin-m2-l1`

Objective: Explain how functions and collections changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a purchase report using collection transformations and an empty-list test. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Functions and collections: independent studio (90 min; Apply)

ID: `kotlin-m2-l2`

Objective: Implement a purchase report using collection transformations and an empty-list test.

Activity: a purchase report using collection transformations and an empty-list test. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Data classes and sealed results

A data class represents values; a sealed hierarchy enumerates alternatives. A when expression can handle each result explicitly, making missing cases visible when the model changes.

```text
sealed interface SaveResult
data class Saved(val id: Int) : SaveResult
data class Rejected(val reason: String) : SaveResult
```

#### Data classes and sealed results: guided investigation (60 min; Apply)

ID: `kotlin-m3-l1`

Objective: Implement a validation API that returns a typed success or failure instead of ambiguous null.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a validation API that returns a typed success or failure instead of ambiguous null. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Data classes and sealed results: independent studio (90 min; Analyze)

ID: `kotlin-m3-l2`

Objective: Locate a failing assumption in data classes and sealed results and isolate it with a minimal reproduction.

Activity: a validation API that returns a typed success or failure instead of ambiguous null. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Extensions, interfaces, and generics

Extensions add convenient syntax without changing a type’s actual members. Interfaces define replaceable behavior. Keep transformations separate from storage and pass dependencies to constructors for testability.

```text
interface Repository<T> { fun all(): List<T> }
fun String.normalizedName(): String = trim().lowercase()
```

#### Extensions, interfaces, and generics: guided investigation (60 min; Analyze)

ID: `kotlin-m4-l1`

Objective: Locate a failing assumption in extensions, interfaces, and generics and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a generic repository and duplicate-name detection with explicit normalization rules. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Extensions, interfaces, and generics: independent studio (90 min; Evaluate)

ID: `kotlin-m4-l2`

Objective: Judge two approaches to extensions, interfaces, and generics against correctness, maintainability, and offline operation.

Activity: a generic repository and duplicate-name detection with explicit normalization rules. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Coroutines and structured concurrency

Suspending is not the same as blocking a thread. A coroutine scope owns child work and cancellation. Dispatch blocking IO appropriately and propagate cancellation; do not swallow it inside a broad failure handler.

```text
// Requires a provisioned kotlinx-coroutines dependency.
suspend fun loadNames(repository: NameRepository): List<String> = repository.load()
interface NameRepository { suspend fun load(): List<String> }
```

#### Coroutines and structured concurrency: guided investigation (60 min; Evaluate)

ID: `kotlin-m5-l1`

Objective: Judge two approaches to coroutines and structured concurrency against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a cancellable report operation with deterministic fake-repository tests. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Coroutines and structured concurrency: independent studio (90 min; Create)

ID: `kotlin-m5-l2`

Objective: Design and deliver an original extension using coroutines and structured concurrency with explicit acceptance tests.

Activity: a cancellable report operation with deterministic fake-repository tests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Testing and JVM interoperability

Kotlin can call Java APIs, but platform types weaken null guarantees. Validate values at the boundary. Separate a functional core from file operations, and test both pure rules and persistence round trips.

```text
fun validStock(value: Int): Boolean = value >= 0
fun main() { check(validStock(0)); check(!validStock(-1)) }
```

#### Testing and JVM interoperability: guided investigation (60 min; Create)

ID: `kotlin-m6-l1`

Objective: Design and deliver an original extension using testing and jvm interoperability with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a command-line release with boundary tests, persistence checks, and a Java API adapter. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing and JVM interoperability: independent studio (90 min; Evaluate)

ID: `kotlin-m6-l2`

Objective: Judge two approaches to testing and jvm interoperability against correctness, maintainability, and offline operation.

Activity: a command-line release with boundary tests, persistence checks, and a Java API adapter. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Coroutines, Flow, and structured concurrency

This Kotlin module teaches you to model cancellation, backpressure, lifecycle ownership, and deterministic coroutine tests. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
suspend fun total(values: List<Int>) = kotlinx.coroutines.coroutineScope {
    values.map { async { it } }.awaitAll().sum()
}
```

#### Coroutines, Flow, and structured concurrency: guided investigation (60 min; Create)

ID: `kotlin-m7-l1`

Objective: Design and deliver an original extension using coroutines, flow, and structured concurrency with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Implement a cancellable report stream with bounded work, failure tests, and no orphaned coroutines. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Coroutines, Flow, and structured concurrency: independent studio (90 min; Evaluate)

ID: `kotlin-m7-l2`

Objective: Judge two approaches to coroutines, flow, and structured concurrency against correctness, maintainability, and offline operation.

Activity: Implement a cancellable report stream with bounded work, failure tests, and no orphaned coroutines. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### DSLs, multiplatform boundaries, and performance

This Kotlin module teaches you to use receivers and sealed models carefully while separating common logic from platform adapters. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
sealed interface Result<out T> {
 data class Ok<T>(val value:T): Result<T>
 data class Error(val message:String): Result<Nothing>
}
```

#### DSLs, multiplatform boundaries, and performance: guided investigation (60 min; Create)

ID: `kotlin-m8-l1`

Objective: Design and deliver an original extension using dsls, multiplatform boundaries, and performance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design a typed validation DSL shared by two platform adapters and benchmark the critical transformation. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### DSLs, multiplatform boundaries, and performance: independent studio (90 min; Evaluate)

ID: `kotlin-m8-l2`

Objective: Judge two approaches to dsls, multiplatform boundaries, and performance against correctness, maintainability, and offline operation.

Activity: Design a typed validation DSL shared by two platform adapters and benchmark the critical transformation. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Kotlin module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `kotlin-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `kotlin-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Kotlin module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `kotlin-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `kotlin-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Kotlin module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `kotlin-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `kotlin-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Kotlin module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `kotlin-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `kotlin-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Kotlin module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `kotlin-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `kotlin-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Kotlin module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `kotlin-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `kotlin-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Kotlin module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `kotlin-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `kotlin-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Kotlin module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `kotlin-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `kotlin-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Study planner (6 hours)

Organize weekly study tasks.

Acceptance conditions:

- Model optional deadlines safely.
- Filter tasks by course and completion.
- Test empty and duplicate task input.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Expense categorizer (12 hours)

Summarize local expense records.

Acceptance conditions:

- Use typed validation results and immutable models.
- Import a local file with useful errors.
- Generate category totals and test malformed records.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Offline inventory core (24 hours)

Create a reusable Kotlin inventory library and CLI.

Acceptance conditions:

- Expose repository contracts and typed operations.
- Support cancellation for long reports with provisioned coroutine tools.
- Deliver tests, local persistence, and JVM execution instructions.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Android

Prerequisites: kotlin

Offline tools: Provision Android Studio, JDK, Android SDK, emulator image or device drivers, and all Gradle/Compose/Room dependencies. Use Gradle offline mode after provisioning. The learning app cannot compile Android projects itself.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

Complete Kotlin first. Use a provisioned Android Studio Empty Activity project with Compose. Keep the generated project structure. Replace only the starter greeting composable with the example. Run on a prepared emulator or device.

Vocabulary:

- Activity: an Android entry point for a user interaction.
- Composable: a function that describes part of a Compose interface.
- State: data that determines what the interface displays.
- Emulator: software that simulates an Android device.

```text
@Composable
fun Greeting() {
  Text("Salam")
}
// Call Greeting() inside the generated setContent block.
```

- The annotation marks a Compose UI function.
- Greeting describes one small part of the screen.
- Text displays Salam. Text and Composable require the imports supplied by the Compose project. This fragment is not a standalone Kotlin file.

Readiness check: What does Text("Salam") describe?

Answer: Visible text

Guided practice: Change the greeting so the screen displays Welcome.

Hint: Keep the composable function and change the string passed to Text.

Reference solution:

```text
@Composable
fun Greeting() {
  Text("Welcome")
}
```

Expected result: The app screen displays Welcome.

### Android project and lifecycle

An Activity is a platform entry point, not a permanent store. Configuration changes can recreate it. Identify manifest declarations, resources, build variants, and the difference between app process lifetime and screen lifetime.

```text
class MainActivity : androidx.activity.ComponentActivity() {
 override fun onCreate(state: android.os.Bundle?) {
  super.onCreate(state)
  setContent { androidx.compose.material3.Text("Salam") }
 }
}
// In a Compose project, import androidx.activity.compose.setContent.
```

#### Android project and lifecycle: guided investigation (60 min; Remember)

ID: `android-m1-l1`

Objective: Identify the key terms and syntax in android project and lifecycle without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a local Android screen and describe what survives rotation and process recreation. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Android project and lifecycle: independent studio (90 min; Understand)

ID: `android-m1-l2`

Objective: Explain how android project and lifecycle changes program behavior using a traced example.

Activity: a local Android screen and describe what survives rotation and process recreation. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Compose state and layouts

Composable functions describe UI from state. Hoist state when multiple components need one source of truth. remember holds state across recomposition; persistent and restorable state require a deliberate owner.

```text
@Composable
fun Counter() {
 var count by rememberSaveable { mutableIntStateOf(0) }
 Button(onClick = { count++ }) { Text("Count: $count") }
}
// Import Compose runtime, saveable, and Material3 symbols.
```

#### Compose state and layouts: guided investigation (60 min; Understand)

ID: `android-m2-l1`

Objective: Explain how compose state and layouts changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a counter and form that preserve appropriate fields after rotation. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Compose state and layouts: independent studio (90 min; Apply)

ID: `android-m2-l2`

Objective: Implement a counter and form that preserve appropriate fields after rotation.

Activity: a counter and form that preserve appropriate fields after rotation. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Navigation and ViewModel

Navigation identifies destinations and arguments; a ViewModel owns screen logic. Expose UI state and accept user actions. Pass stable IDs between destinations instead of serializing mutable database entities.

```text
data class UiState(val names: List<String> = emptyList(), val error: String? = null)
// A ViewModel exposes StateFlow<UiState>; the UI collects with lifecycle awareness.
```

#### Navigation and ViewModel: guided investigation (60 min; Apply)

ID: `android-m3-l1`

Objective: Implement a list-to-detail flow with loading, empty, content, and error states.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a list-to-detail flow with loading, empty, content, and error states. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Navigation and ViewModel: independent studio (90 min; Analyze)

ID: `android-m3-l2`

Objective: Locate a failing assumption in navigation and viewmodel and isolate it with a minimal reproduction.

Activity: a list-to-detail flow with loading, empty, content, and error states. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Room and repository boundaries

Room maps structured data to SQLite. Entities express storage, DAOs express queries, and repositories expose application operations. Use migrations when schemas change and keep writes off the UI thread.

```text
@Entity
data class Note(@PrimaryKey val id: Long, val text: String)
@Dao
interface Notes { @Query("SELECT * FROM Note ORDER BY id") fun observe(): Flow<List<Note>> }
// Requires Room and Flow imports and provisioned code generation.
```

#### Room and repository boundaries: guided investigation (60 min; Analyze)

ID: `android-m4-l1`

Objective: Locate a failing assumption in room and repository boundaries and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a note repository with a migration test and a restart persistence check. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Room and repository boundaries: independent studio (90 min; Evaluate)

ID: `android-m4-l2`

Objective: Judge two approaches to room and repository boundaries against correctness, maintainability, and offline operation.

Activity: a note repository with a migration test and a restart persistence check. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Background work and permissions

Request only capabilities needed for an explicit feature. Long deferred work and immediate screen work have different owners. A background task may retry, so its effects must be idempotent. A local-only app needs no internet permission.

```text
// Background export state: queued -> running -> succeeded | failed.
// Store an operation ID; a repeated export must not duplicate ledger entries.
```

#### Background work and permissions: guided investigation (60 min; Evaluate)

ID: `android-m5-l1`

Objective: Judge two approaches to background work and permissions against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an export workflow that reports cancellation and retries without duplicating data. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Background work and permissions: independent studio (90 min; Create)

ID: `android-m5-l2`

Objective: Design and deliver an original extension using background work and permissions with explicit acceptance tests.

Activity: an export workflow that reports cancellation and retries without duplicating data. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Accessibility, testing, and release

Test domain rules, Compose interactions, and device lifecycle behavior separately. Provide labels and adequate touch targets. An unsigned or debug build is not a production release; document signing ownership and test an installed build in airplane mode.

```text
@Test fun emptyNameIsRejected() { assertFalse(validateName("")) }
fun validateName(name: String) = name.isNotBlank()
```

#### Accessibility, testing, and release: guided investigation (60 min; Create)

ID: `android-m6-l1`

Objective: Design and deliver an original extension using accessibility, testing, and release with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an accessible release candidate with lifecycle tests and a documented offline installation path. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Accessibility, testing, and release: independent studio (90 min; Evaluate)

ID: `android-m6-l2`

Objective: Judge two approaches to accessibility, testing, and release against correctness, maintainability, and offline operation.

Activity: an accessible release candidate with lifecycle tests and a documented offline installation path. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Offline-first synchronization architecture

This Android module teaches you to model local truth, conflict resolution, work scheduling, retries, and observable sync state. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
data class SyncState(val pending: Int, val lastError: String?)
// Room remains the source of truth; workers reconcile later.
```

#### Offline-first synchronization architecture: guided investigation (60 min; Create)

ID: `android-m7-l1`

Objective: Design and deliver an original extension using offline-first synchronization architecture with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a local-first queue with deterministic conflict rules and tests for restart, duplicate work, and interrupted synchronization. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Offline-first synchronization architecture: independent studio (90 min; Evaluate)

ID: `android-m7-l2`

Objective: Judge two approaches to offline-first synchronization architecture against correctness, maintainability, and offline operation.

Activity: Build a local-first queue with deterministic conflict rules and tests for restart, duplicate work, and interrupted synchronization. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance, security, and production delivery

This Android module teaches you to profile startup and rendering, protect stored data, minimize permissions, and verify signed release behavior. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
<uses-permission android:name="android.permission.INTERNET" />
<!-- Remove this permission when the product is fully offline. -->
```

#### Performance, security, and production delivery: guided investigation (60 min; Create)

ID: `android-m8-l1`

Objective: Design and deliver an original extension using performance, security, and production delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a release audit covering startup, jank, accessibility, backup policy, permissions, secrets, signing, and offline acceptance. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance, security, and production delivery: independent studio (90 min; Evaluate)

ID: `android-m8-l2`

Objective: Judge two approaches to performance, security, and production delivery against correctness, maintainability, and offline operation.

Activity: Produce a release audit covering startup, jank, accessibility, backup policy, permissions, secrets, signing, and offline acceptance. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Android module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `android-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `android-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Android module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `android-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `android-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Android module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `android-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `android-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Android module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `android-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `android-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Android module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `android-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `android-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Android module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `android-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `android-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Android module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `android-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `android-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Android module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `android-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `android-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Campus timetable (6 hours)

Help students view a local weekly timetable.

Acceptance conditions:

- Build accessible Compose day and class views.
- Preserve selected day through rotation.
- Bundle all timetable data locally.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Study notes (12 hours)

Create searchable notes on a device.

Acceptance conditions:

- Persist with Room and edit by stable ID.
- Handle empty content and migration failures.
- Test search, restart, rotation, and larger font sizes.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Community inventory Android app (24 hours)

Track goods on one shared learning device using fictional data.

Acceptance conditions:

- Separate ViewModel, domain operations, and repository adapters.
- Prevent invalid stock adjustments and persist transaction history.
- Support local export and demonstrate installed airplane-mode operation.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## iOS

Prerequisites: swift

Offline tools: Native iOS development requires a compatible Mac with Xcode, SDKs, and simulator runtimes provisioned beforehand. Simulator exercises can be local; physical-device signing and distribution have separate Apple requirements. Windows or Android alone cannot build these native projects.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

Complete Swift first. Use a compatible Mac with provisioned Xcode. Create an iOS SwiftUI app. Replace the generated ContentView with this example and run the prepared simulator. This cannot be compiled on an Android phone.

Vocabulary:

- Scene: one instance of an app interface.
- View: a description of visible interface content.
- SwiftUI: Apple’s declarative interface framework.
- Simulator: a tool for running a simulated device on a Mac.

```text
import SwiftUI
struct ContentView: View {
  var body: some View {
    Text("Salam")
  }
}
```

- The import makes SwiftUI types available.
- ContentView conforms to View and supplies a body.
- The body describes one text element. Xcode’s generated app entry point displays ContentView.

Readiness check: What is displayed by the view?

Answer: Salam

Guided practice: Display Welcome using the same view structure.

Hint: Change only the string inside Text.

Reference solution:

```text
import SwiftUI
struct ContentView: View {
  var body: some View { Text("Welcome") }
}
```

Expected result: The simulator displays Welcome.

### Xcode and app lifecycle

An iOS app has scenes and lifecycle transitions. Treat backgrounding as a normal event, not an error. Separate the application entry point from feature views and inspect the project’s target settings.

```text
import SwiftUI
@main struct LearningApp: App { var body: some Scene { WindowGroup { Text("Salam") } } }
```

#### Xcode and app lifecycle: guided investigation (60 min; Remember)

ID: `ios-m1-l1`

Objective: Identify the key terms and syntax in xcode and app lifecycle without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a simulator app and a diagram of active, inactive, and background transitions. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Xcode and app lifecycle: independent studio (90 min; Understand)

ID: `ios-m1-l2`

Objective: Explain how xcode and app lifecycle changes program behavior using a traced example.

Activity: a simulator app and a diagram of active, inactive, and background transitions. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### SwiftUI state and composition

A view describes a value-dependent interface. State has an owner, bindings allow controlled editing, and child views should receive only what they need. Keep calculations outside the body when they represent domain policy.

```text
struct Counter: View { @State private var count = 0; var body: some View { Button("Count: \(count)") { count += 1 } } }
```

#### SwiftUI state and composition: guided investigation (60 min; Understand)

ID: `ios-m2-l1`

Objective: Explain how swiftui state and composition changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a composed form with validation and one clear owner for each mutable value. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### SwiftUI state and composition: independent studio (90 min; Apply)

ID: `ios-m2-l2`

Objective: Implement a composed form with validation and one clear owner for each mutable value.

Activity: a composed form with validation and one clear owner for each mutable value. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Navigation and accessible forms

NavigationStack models a navigation path. Stable identifiers connect list and detail screens. VoiceOver labels and Dynamic Type are design inputs; use system controls before inventing custom interaction patterns.

```text
NavigationStack { List(["Algorithms", "Databases"], id: \.self) { name in NavigationLink(name) { Text(name) } } }
```

#### Navigation and accessible forms: guided investigation (60 min; Apply)

ID: `ios-m3-l1`

Objective: Implement a course list and detail flow that remains usable with VoiceOver and large text.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a course list and detail flow that remains usable with VoiceOver and large text. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Navigation and accessible forms: independent studio (90 min; Analyze)

ID: `ios-m3-l2`

Objective: Locate a failing assumption in navigation and accessible forms and isolate it with a minimal reproduction.

Activity: a course list and detail flow that remains usable with VoiceOver and large text. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Local persistence and migrations

Choose storage by data shape. Codable files fit small documents; structured persistence fits related records and queries. Decode into validated models, preserve the last good file, and test version changes with real fixtures.

```text
struct Note: Codable { let id: UUID; var text: String }
let data = try JSONEncoder().encode([Note(id: UUID(), text: "Study")])
// Persist data atomically in the application documents directory.
```

#### Local persistence and migrations: guided investigation (60 min; Analyze)

ID: `ios-m4-l1`

Objective: Locate a failing assumption in local persistence and migrations and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a local note store with corrupted-file recovery and a schema-version fixture. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Local persistence and migrations: independent studio (90 min; Evaluate)

ID: `ios-m4-l2`

Objective: Judge two approaches to local persistence and migrations against correctness, maintainability, and offline operation.

Activity: a local note store with corrupted-file recovery and a schema-version fixture. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Concurrency and platform boundaries

UI updates belong to the main actor. Asynchronous work should cancel when its owner no longer needs the result. Wrap platform file operations behind a protocol so failure and cancellation can be tested without the UI.

```text
protocol NoteStore { func load() async throws -> [Note] }
@MainActor final class NoteModel { var notes: [Note] = []; func refresh(using store: NoteStore) async throws { notes = try await store.load() } }
```

#### Concurrency and platform boundaries: guided investigation (60 min; Evaluate)

ID: `ios-m5-l1`

Objective: Judge two approaches to concurrency and platform boundaries against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a cancellable load flow with visible recovery and a fake failing store. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Concurrency and platform boundaries: independent studio (90 min; Create)

ID: `ios-m5-l2`

Objective: Design and deliver an original extension using concurrency and platform boundaries with explicit acceptance tests.

Activity: a cancellable load flow with visible recovery and a fake failing store. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Testing and distribution planning

Use unit tests for policy and UI tests for critical flows. Verify background/foreground transitions and offline relaunch. Build archives, signing, and distribution are separate from coding; record the environment and limits of what was tested.

```text
import XCTest
final class TitleTests: XCTestCase { func testBlankTitle() { XCTAssertTrue(" ".trimmingCharacters(in: .whitespaces).isEmpty) } }
```

#### Testing and distribution planning: guided investigation (60 min; Create)

ID: `ios-m6-l1`

Objective: Design and deliver an original extension using testing and distribution planning with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a tested simulator release with an explicit signing and physical-device verification checklist. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing and distribution planning: independent studio (90 min; Evaluate)

ID: `ios-m6-l2`

Objective: Judge two approaches to testing and distribution planning against correctness, maintainability, and offline operation.

Activity: a tested simulator release with an explicit signing and physical-device verification checklist. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Offline data, background work, and conflict handling

This iOS module teaches you to coordinate SwiftData or Core Data transactions, background tasks, migrations, and merge policies. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
@Model final class Note {
 var title: String
 init(title: String) { self.title = title }
}
```

#### Offline data, background work, and conflict handling: guided investigation (60 min; Create)

ID: `ios-m7-l1`

Objective: Design and deliver an original extension using offline data, background work, and conflict handling with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a migration-tested local store with background import, deterministic conflict handling, and restart recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Offline data, background work, and conflict handling: independent studio (90 min; Evaluate)

ID: `ios-m7-l2`

Objective: Judge two approaches to offline data, background work, and conflict handling against correctness, maintainability, and offline operation.

Activity: Build a migration-tested local store with background import, deterministic conflict handling, and restart recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Privacy, performance, and App Store delivery

This iOS module teaches you to measure launch and UI responsiveness, apply data minimization, signing, entitlements, and release checks. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
let started = ContinuousClock.now
// Measure a defined operation, then compare against a budget.
```

#### Privacy, performance, and App Store delivery: guided investigation (60 min; Create)

ID: `ios-m8-l1`

Objective: Design and deliver an original extension using privacy, performance, and app store delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Prepare a privacy manifest, performance budget, accessibility audit, signed archive checklist, and offline release evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Privacy, performance, and App Store delivery: independent studio (90 min; Evaluate)

ID: `ios-m8-l2`

Objective: Judge two approaches to privacy, performance, and app store delivery against correctness, maintainability, and offline operation.

Activity: Prepare a privacy manifest, performance budget, accessibility audit, signed archive checklist, and offline release evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This iOS module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `ios-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `ios-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This iOS module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `ios-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `ios-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This iOS module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `ios-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `ios-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This iOS module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `ios-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `ios-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This iOS module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `ios-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `ios-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This iOS module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `ios-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `ios-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This iOS module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `ios-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `ios-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This iOS module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `ios-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `ios-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Campus guide for iOS (6 hours)

Provide local campus information without maps or web services.

Acceptance conditions:

- Bundle place descriptions and accessibility information.
- Support Dynamic Type and VoiceOver.
- Use local navigation without network requests.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Reading journal (12 hours)

Track books and reading notes.

Acceptance conditions:

- Persist Codable documents atomically.
- Support edit, search, and safe delete confirmation.
- Test corrupted files and app relaunch.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Workshop organizer (24 hours)

Manage fictional workshops and attendance locally.

Acceptance conditions:

- Enforce capacities through domain logic.
- Provide accessible list, detail, and attendance flows.
- Use repository tests and demonstrate simulator operation offline.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Swift

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Provision a supported Swift toolchain. Use swift main.swift for basic programs and swift test for package tests. Foundation availability varies by platform; iOS UI work belongs to the iOS course and requires Xcode on macOS.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

No programming experience is required. On a computer with Swift provisioned, save main.swift and run swift main.swift from its folder. This language lesson does not require an iOS interface.

Vocabulary:

- let: a constant binding.
- Variable: a named value that can change when declared with var.
- String: text enclosed in quotes.
- print: a function that displays a value.

```text
let city = "Kabul"
print(city)
```

- let creates a binding named city containing a string.
- print reads city and displays its value.
- Trying to assign another value to city later fails because this binding uses let. Use var only when reassignment is required.

Readiness check: Which word declares the constant binding?

Answer: let

Guided practice: Declare greeting as a constant and display Salam.

Hint: Keep let, choose a new name, and pass that name to print.

Reference solution:

```text
let greeting = "Salam"
print(greeting)
```

Expected result: Salam

### Values, control flow, and optionals

Swift distinguishes absent values with Optional. Use conditional binding or guard to handle absence. let prevents rebinding, while value types help avoid accidental shared mutation.

```text
let input = "42"
if let amount = Int(input) { print(amount + 1) } else { print("Invalid amount") }
```

#### Values, control flow, and optionals: guided investigation (60 min; Remember)

ID: `swift-m1-l1`

Objective: Identify the key terms and syntax in values, control flow, and optionals without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an integer parser with explicit invalid-input behavior. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Values, control flow, and optionals: independent studio (90 min; Understand)

ID: `swift-m1-l2`

Objective: Explain how values, control flow, and optionals changes program behavior using a traced example.

Activity: an integer parser with explicit invalid-input behavior. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Functions and collections

Functions state parameter and return types. Arrays preserve order, dictionaries map keys, and sets express uniqueness. Separate transformations from IO and prefer readable intermediate names over dense chains.

```text
func total(_ values: [Int]) -> Int { values.reduce(0, +) }
assert(total([]) == 0)
```

#### Functions and collections: guided investigation (60 min; Understand)

ID: `swift-m2-l1`

Objective: Explain how functions and collections changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a grade summary with empty and boundary cases. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Functions and collections: independent studio (90 min; Apply)

ID: `swift-m2-l2`

Objective: Implement a grade summary with empty and boundary cases.

Activity: a grade summary with empty and boundary cases. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Structs, enums, and protocols

Structs have value semantics; classes share reference identity. Enums can carry associated values to model outcomes. Protocols express capabilities and let code depend on behavior instead of a concrete implementation.

```text
enum Validation { case accepted(Int); case rejected(String) }
struct Item { let id: Int; var quantity: Int }
```

#### Structs, enums, and protocols: guided investigation (60 min; Apply)

ID: `swift-m3-l1`

Objective: Implement a stock validation result and compare copied structs with shared class instances.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a stock validation result and compare copied structs with shared class instances. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Structs, enums, and protocols: independent studio (90 min; Analyze)

ID: `swift-m3-l2`

Objective: Locate a failing assumption in structs, enums, and protocols and isolate it with a minimal reproduction.

Activity: a stock validation result and compare copied structs with shared class instances. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Errors, Codable, and generics

Throwing functions make failure explicit. Codable handles representation, not domain validity. Generic algorithms share behavior across types while retaining compiler checks. Validate decoded values before accepting them.

```text
import Foundation
struct Expense: Codable { let amount: Int }
let bytes = try JSONEncoder().encode(Expense(amount: 20))
print(try JSONDecoder().decode(Expense.self, from: bytes).amount)
```

#### Errors, Codable, and generics: guided investigation (60 min; Analyze)

ID: `swift-m4-l1`

Objective: Locate a failing assumption in errors, codable, and generics and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a JSON import that distinguishes malformed bytes from invalid amounts. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Errors, Codable, and generics: independent studio (90 min; Evaluate)

ID: `swift-m4-l2`

Objective: Judge two approaches to errors, codable, and generics against correctness, maintainability, and offline operation.

Activity: a JSON import that distinguishes malformed bytes from invalid amounts. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### ARC and concurrency

Automatic reference counting manages object lifetimes, but strong reference cycles can keep objects alive. Actors isolate mutable state; async does not guarantee parallel work. Choose ownership before adding weak references or detached tasks.

```text
actor Counter { private var value = 0; func increment() { value += 1 }; func read() -> Int { value } }
```

#### ARC and concurrency: guided investigation (60 min; Evaluate)

ID: `swift-m5-l1`

Objective: Judge two approaches to arc and concurrency against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an actor-based counter and an ownership diagram for a callback retaining its owner. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### ARC and concurrency: independent studio (90 min; Create)

ID: `swift-m5-l2`

Objective: Design and deliver an original extension using arc and concurrency with explicit acceptance tests.

Activity: an actor-based counter and an ownership diagram for a callback retaining its owner. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Packages, tests, and design

Swift packages organize modules and tests. Hide file access behind a protocol, keep domain models independent, and document public contracts. Compare alternative abstractions with a concrete change request instead of counting patterns.

```text
protocol LedgerStore { func amounts() throws -> [Int] }
func balance(_ store: LedgerStore) throws -> Int { try store.amounts().reduce(0, +) }
```

#### Packages, tests, and design: guided investigation (60 min; Create)

ID: `swift-m6-l1`

Objective: Design and deliver an original extension using packages, tests, and design with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a package with a fake store, tested failure paths, and a local usage example. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Packages, tests, and design: independent studio (90 min; Evaluate)

ID: `swift-m6-l2`

Objective: Judge two approaches to packages, tests, and design against correctness, maintainability, and offline operation.

Activity: a package with a fake store, tested failure paths, and a local usage example. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Actors and advanced concurrency

This Swift module teaches you to use actors, task groups, cancellation, Sendable values, and isolation boundaries safely. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
actor Counter {
 private var value = 0
 func increment() { value += 1 }
 func read() -> Int { value }
}
```

#### Actors and advanced concurrency: guided investigation (60 min; Create)

ID: `swift-m7-l1`

Objective: Design and deliver an original extension using actors and advanced concurrency with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Implement a cancellable actor-based batch processor and test isolation, partial failure, and deterministic output. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Actors and advanced concurrency: independent studio (90 min; Evaluate)

ID: `swift-m7-l2`

Objective: Judge two approaches to actors and advanced concurrency against correctness, maintainability, and offline operation.

Activity: Implement a cancellable actor-based batch processor and test isolation, partial failure, and deterministic output. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Protocols, generics, macros, and package design

This Swift module teaches you to create expressive compile-time contracts while keeping APIs small, testable, and source compatible. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
protocol Repository<Item> {
 associatedtype Item
 func load() throws -> [Item]
}
```

#### Protocols, generics, macros, and package design: guided investigation (60 min; Create)

ID: `swift-m8-l1`

Objective: Design and deliver an original extension using protocols, generics, macros, and package design with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Publish a local Swift package with protocol-based storage adapters, semantic version notes, documentation, and tests. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Protocols, generics, macros, and package design: independent studio (90 min; Evaluate)

ID: `swift-m8-l2`

Objective: Judge two approaches to protocols, generics, macros, and package design against correctness, maintainability, and offline operation.

Activity: Publish a local Swift package with protocol-based storage adapters, semantic version notes, documentation, and tests. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Swift module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `swift-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `swift-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Swift module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `swift-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `swift-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Swift module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `swift-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `swift-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Swift module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `swift-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `swift-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Swift module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `swift-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `swift-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Swift module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `swift-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `swift-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Swift module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `swift-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `swift-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Swift module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `swift-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `swift-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: AFN budget calculator (6 hours)

Calculate a fictional household budget.

Acceptance conditions:

- Use integer amounts and validated input.
- Report remaining budget and overspending.
- Test zero and negative input policies.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Book catalog CLI (12 hours)

Maintain a local reading catalog.

Acceptance conditions:

- Model books with stable identifiers and Codable.
- Support search and duplicate rejection.
- Preserve previous data on import failure.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Reusable ledger package (24 hours)

Deliver a Swift package for financial record exercises using fictional data.

Acceptance conditions:

- Separate domain rules and storage protocols.
- Handle concurrent operations with explicit isolation.
- Provide tests, API documentation, and a local command-line client.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## C++

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Provision a C++17-capable compiler and local standard library. Compile with g++ -std=c++17 -Wall -Wextra main.cpp -o app or the equivalent MSVC/Clang command. Sanitizers are optional and must be provisioned; no external libraries are required.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

No prior programming is required. Use a provisioned C++ compiler. Save main.cpp and compile with g++ -std=c++17 -Wall -Wextra main.cpp -o app. Run ./app, or app.exe on Windows. The app itself cannot compile C++.

Vocabulary:

- Header: a declaration file included before compilation.
- main: the function where this program begins.
- Stream: a sequence of input or output data.
- Statement: one instruction, often ending with a semicolon.

```text
#include <iostream>
int main() {
  std::cout << "Salam" << "\n";
  return 0;
}
```

- iostream declares standard input and output facilities.
- main contains the program statements between braces.
- cout sends Salam and a newline to the output. return 0 reports successful completion to the operating system.

Readiness check: Which expression sends text to standard output?

Answer: std::cout

Guided practice: Display Kabul followed by a newline.

Hint: Replace Salam inside the quotes; keep the stream operators and semicolon.

Reference solution:

```text
#include <iostream>
int main() {
  std::cout << "Kabul" << "\n";
  return 0;
}
```

Expected result: Kabul

### Types, expressions, and loops

C++ types affect ranges and operations. Integer division discards fractional parts. Initialize values before reading them, check input failures, and avoid assuming signed overflow wraps predictably.

```text
#include <iostream>
int main() { int total = 0; for (int n : {10,20,30}) total += n; std::cout << total << "\n"; }
```

#### Types, expressions, and loops: guided investigation (60 min; Remember)

ID: `cpp-m1-l1`

Objective: Identify the key terms and syntax in types, expressions, and loops without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a marks calculator that checks input and documents its numeric range. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Types, expressions, and loops: independent studio (90 min; Understand)

ID: `cpp-m1-l2`

Objective: Explain how types, expressions, and loops changes program behavior using a traced example.

Activity: a marks calculator that checks input and documents its numeric range. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Functions, references, and const

Pass small values by value and large read-only objects by const reference. A reference refers to an existing object; it must not outlive that object. Express whether a function can mutate its input.

```text
#include <vector>
int sum(const std::vector<int>& values) { int result=0; for(int value:values) result+=value; return result; }
```

#### Functions, references, and const: guided investigation (60 min; Understand)

ID: `cpp-m2-l1`

Objective: Explain how functions, references, and const changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a report function with a clear ownership and mutation contract. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Functions, references, and const: independent studio (90 min; Apply)

ID: `cpp-m2-l2`

Objective: Implement a report function with a clear ownership and mutation contract.

Activity: a report function with a clear ownership and mutation contract. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### RAII and object lifetimes

RAII ties resource release to object lifetime. Prefer standard containers and smart pointers to manual new/delete. Destructors run during stack unwinding; a dangling pointer remains invalid even if its old bytes look plausible.

```text
#include <memory>
struct Item { int stock=0; };
auto item = std::make_unique<Item>();
// The unique owner releases the Item when it leaves scope.
```

#### RAII and object lifetimes: guided investigation (60 min; Apply)

ID: `cpp-m3-l1`

Objective: Implement a resource ownership diagram and replace manual allocation with an RAII owner.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a resource ownership diagram and replace manual allocation with an RAII owner. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### RAII and object lifetimes: independent studio (90 min; Analyze)

ID: `cpp-m3-l2`

Objective: Locate a failing assumption in raii and object lifetimes and isolate it with a minimal reproduction.

Activity: a resource ownership diagram and replace manual allocation with an RAII owner. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### STL algorithms and complexity

Choose a container based on required operations and measured scale. Sorting generally costs more than one linear scan. Algorithms accept iterator ranges; invalidating an iterator while using it can introduce subtle defects.

```text
#include <algorithm>
#include <vector>
std::vector<int> values{3,1,2};
// Inside a function:
// std::sort(values.begin(), values.end());
```

#### STL algorithms and complexity: guided investigation (60 min; Analyze)

ID: `cpp-m4-l1`

Objective: Locate a failing assumption in stl algorithms and complexity and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a sorted inventory search and compare linear search with binary search on ordered data. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### STL algorithms and complexity: independent studio (90 min; Evaluate)

ID: `cpp-m4-l2`

Objective: Judge two approaches to stl algorithms and complexity against correctness, maintainability, and offline operation.

Activity: a sorted inventory search and compare linear search with binary search on ordered data. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Files, exceptions, and testing

Check stream state after IO and preserve the last good data when parsing fails. Assertions are useful in tests, but release builds may disable them; never use assert as the only user-input validation.

```text
#include <sstream>
#include <stdexcept>
int parse(const std::string& text) { std::istringstream in(text); int n; if(!(in >> n)) throw std::invalid_argument("integer required"); in >> std::ws; if(!in.eof()) throw std::invalid_argument("trailing data"); return n; }
```

#### Files, exceptions, and testing: guided investigation (60 min; Evaluate)

ID: `cpp-m5-l1`

Objective: Judge two approaches to files, exceptions, and testing against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a strict record parser with empty, overflow, and trailing-data cases. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Files, exceptions, and testing: independent studio (90 min; Create)

ID: `cpp-m5-l2`

Objective: Design and deliver an original extension using files, exceptions, and testing with explicit acceptance tests.

Activity: a strict record parser with empty, overflow, and trailing-data cases. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Templates, boundaries, and profiling

Templates reuse type-safe algorithms; keep diagnostics and interfaces understandable. Separate file storage from calculations, inspect compiler warnings, and measure before optimizing. Use sanitizers where available to investigate lifetime errors.

```text
template<class T> T larger(T a, T b) { return a < b ? b : a; }
// Define domain rules in a library and inject storage through an interface.
```

#### Templates, boundaries, and profiling: guided investigation (60 min; Create)

ID: `cpp-m6-l1`

Objective: Design and deliver an original extension using templates, boundaries, and profiling with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a modular release with warning-clean builds, test evidence, and a measured optimization decision. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Templates, boundaries, and profiling: independent studio (90 min; Evaluate)

ID: `cpp-m6-l2`

Objective: Judge two approaches to templates, boundaries, and profiling against correctness, maintainability, and offline operation.

Activity: a modular release with warning-clean builds, test evidence, and a measured optimization decision. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Templates, concepts, and compile-time design

This C++ module teaches you to constrain generic algorithms, understand instantiation cost, and expose clear diagnostics and ownership contracts. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
#include <concepts>
template<std::integral T>
T total(T a, T b) { return a + b; }
```

#### Templates, concepts, and compile-time design: guided investigation (60 min; Create)

ID: `cpp-m7-l1`

Objective: Design and deliver an original extension using templates, concepts, and compile-time design with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design a constrained statistics library and test signed, unsigned, overflow, empty, and invalid cases. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Templates, concepts, and compile-time design: independent studio (90 min; Evaluate)

ID: `cpp-m7-l2`

Objective: Judge two approaches to templates, concepts, and compile-time design against correctness, maintainability, and offline operation.

Activity: Design a constrained statistics library and test signed, unsigned, overflow, empty, and invalid cases. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Concurrency, profiling, and systems reliability

This C++ module teaches you to apply race-free ownership, atomics or locks, sanitizers, profiling, and failure-safe resource control. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
std::jthread worker([](std::stop_token stop) {
  while (!stop.stop_requested()) { break; }
});
```

#### Concurrency, profiling, and systems reliability: guided investigation (60 min; Create)

ID: `cpp-m8-l1`

Objective: Design and deliver an original extension using concurrency, profiling, and systems reliability with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a bounded worker queue, verify it with thread/address sanitizers, profile it, and document shutdown guarantees. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Concurrency, profiling, and systems reliability: independent studio (90 min; Evaluate)

ID: `cpp-m8-l2`

Objective: Judge two approaches to concurrency, profiling, and systems reliability against correctness, maintainability, and offline operation.

Activity: Build a bounded worker queue, verify it with thread/address sanitizers, profile it, and document shutdown guarantees. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This C++ module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `cpp-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `cpp-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This C++ module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `cpp-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `cpp-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This C++ module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `cpp-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `cpp-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This C++ module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `cpp-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `cpp-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This C++ module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `cpp-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `cpp-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This C++ module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `cpp-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `cpp-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This C++ module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `cpp-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `cpp-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This C++ module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `cpp-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `cpp-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Exam statistics CLI (6 hours)

Summarize fictional exam scores.

Acceptance conditions:

- Reject out-of-range marks and invalid tokens.
- Calculate minimum, maximum, and mean with an empty-input rule.
- Compile with warnings enabled and retain test results.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Library search index (12 hours)

Search a local catalog efficiently.

Acceptance conditions:

- Load and validate records from a file.
- Compare linear and sorted search using the same fixture.
- Avoid dangling references during updates.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Warehouse stock engine (24 hours)

Build a C++ inventory core and CLI.

Acceptance conditions:

- Use RAII and clear ownership contracts.
- Prevent invalid stock transitions and preserve files after errors.
- Deliver modular source, boundary tests, and profiling notes.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## JavaScript

Prerequisites: web-design

Offline tools: Use a browser’s developer tools for pure language examples and local HTML with classic scripts. ES modules and fetch may require a provisioned local server. Node.js is optional for node --test; no remote scripts are needed.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

Begin with Web Design so you can create local files. Open a browser’s developer tools and its Console. Enter the two lines below. No website account or internet service is needed.

Vocabulary:

- Script: instructions executed by a JavaScript runtime.
- const: a binding that cannot be reassigned.
- Console: a developer tool that displays messages.
- Expression: code that produces a value.

```text
const amount = 20;
console.log(amount + 5);
```

- const gives the number 20 the name amount.
- The addition expression calculates 25 before console.log displays it.
- The semicolon ends a statement. Numbers are not quoted here; quoted values would be strings.

Readiness check: What number does the example display?

Answer: 25

Guided practice: Store 30 in price and display price plus 10.

Hint: Use a numeric value without quotes and pass the addition expression to console.log.

Reference solution:

```text
const price = 30;
console.log(price + 10);
```

Expected result: 40

### Values, scope, and control flow

const prevents rebinding; it does not freeze an object. Use strict equality to avoid implicit coercion surprises. Block scope limits where a binding exists. Distinguish undefined from a deliberately absent null.

```text
const prices = [10, 20, 30];
let total = 0;
for (const price of prices) total += price;
console.log(total);
```

#### Values, scope, and control flow: guided investigation (60 min; Remember)

ID: `javascript-m1-l1`

Objective: Identify the key terms and syntax in values, scope, and control flow without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a budget calculation with explicit numeric conversion and invalid-input handling. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Values, scope, and control flow: independent studio (90 min; Understand)

ID: `javascript-m1-l2`

Objective: Explain how values, scope, and control flow changes program behavior using a traced example.

Activity: a budget calculation with explicit numeric conversion and invalid-input handling. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Functions, arrays, and objects

Functions can receive other functions. Array methods express transformations; avoid mutating shared input when a calculation can return a new value. Object spread copies only one level, so nested objects may still be shared.

```text
const expenses = [{category:"books", amount:20}, {category:"travel", amount:10}];
const total = expenses.reduce((sum, item) => sum + item.amount, 0);
```

#### Functions, arrays, and objects: guided investigation (60 min; Understand)

ID: `javascript-m2-l1`

Objective: Explain how functions, arrays, and objects changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a category report without mutating the original expense array. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Functions, arrays, and objects: independent studio (90 min; Apply)

ID: `javascript-m2-l2`

Objective: Implement a category report without mutating the original expense array.

Activity: a category report without mutating the original expense array. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### DOM, events, and forms

The DOM is a mutable document tree. Respond to user events, validate input, then render from your data model. Use textContent for user text; inserting untrusted HTML creates an injection boundary.

```text
const button = document.querySelector("button");
button.addEventListener("click", () => { document.querySelector("output").textContent = "Saved locally"; });
```

#### DOM, events, and forms: guided investigation (60 min; Apply)

ID: `javascript-m3-l1`

Objective: Implement an accessible task form that rejects blank input and renders text safely.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an accessible task form that rejects blank input and renders text safely. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### DOM, events, and forms: independent studio (90 min; Analyze)

ID: `javascript-m3-l2`

Objective: Locate a failing assumption in dom, events, and forms and isolate it with a minimal reproduction.

Activity: an accessible task form that rejects blank input and renders text safely. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Promises and the event loop

Promises represent eventual results. await pauses the async function, not the whole browser. Handle rejection and stale responses; the last request started may not be the last one completed.

```text
async function load(read) { try { return await read(); } catch { return []; } }
load(() => Promise.resolve(["Algorithms"])).then(console.log);
```

#### Promises and the event loop: guided investigation (60 min; Analyze)

ID: `javascript-m4-l1`

Objective: Locate a failing assumption in promises and the event loop and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a simulated asynchronous search that discards outdated results. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Promises and the event loop: independent studio (90 min; Evaluate)

ID: `javascript-m4-l2`

Objective: Judge two approaches to promises and the event loop against correctness, maintainability, and offline operation.

Activity: a simulated asynchronous search that discards outdated results. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Modules and browser storage

Modules define explicit dependencies. Browser storage is local but can be cleared or unavailable. JSON decoding needs schema checks; store a version and offer an export before changing a format.

```text
const snapshot = {version:1, tasks:[{id:1, title:"Study"}]};
localStorage.setItem("tasks", JSON.stringify(snapshot));
```

#### Modules and browser storage: guided investigation (60 min; Evaluate)

ID: `javascript-m5-l1`

Objective: Judge two approaches to modules and browser storage against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a versioned task store that handles malformed JSON without replacing good data. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Modules and browser storage: independent studio (90 min; Create)

ID: `javascript-m5-l2`

Objective: Design and deliver an original extension using modules and browser storage with explicit acceptance tests.

Activity: a versioned task store that handles malformed JSON without replacing good data. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Testing and maintainable design

Keep domain functions independent of the DOM so edge cases are easy to test. Test events and storage separately through adapters. A passing sample is insufficient: include empty input, duplicates, and failures.

```text
function add(a, b) { if (!Number.isFinite(a) || !Number.isFinite(b)) throw new Error("finite numbers required"); return a+b; }
console.assert(add(2,3) === 5);
```

#### Testing and maintainable design: guided investigation (60 min; Create)

ID: `javascript-m6-l1`

Objective: Design and deliver an original extension using testing and maintainable design with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a tested task app with a storage adapter and reproducible local instructions. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing and maintainable design: independent studio (90 min; Evaluate)

ID: `javascript-m6-l2`

Objective: Judge two approaches to testing and maintainable design against correctness, maintainability, and offline operation.

Activity: a tested task app with a storage adapter and reproducible local instructions. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Event loop, workers, and performance

This JavaScript module teaches you to reason about tasks and microtasks, move CPU work to workers, and measure responsiveness. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
console.log("A");
queueMicrotask(() => console.log("microtask"));
setTimeout(() => console.log("task"), 0);
```

#### Event loop, workers, and performance: guided investigation (60 min; Create)

ID: `javascript-m7-l1`

Objective: Design and deliver an original extension using event loop, workers, and performance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a responsive local data processor using a worker, cancellation, progress messages, and performance measurements. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Event loop, workers, and performance: independent studio (90 min; Evaluate)

ID: `javascript-m7-l2`

Objective: Judge two approaches to event loop, workers, and performance against correctness, maintainability, and offline operation.

Activity: Build a responsive local data processor using a worker, cancellation, progress messages, and performance measurements. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Language internals, security, and package design

This JavaScript module teaches you to apply prototypes, iterators, typed boundaries, input safety, modules, and reproducible dependency policy. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
export function* valid(records) {
  for (const record of records) if (record?.id != null) yield record;
}
```

#### Language internals, security, and package design: guided investigation (60 min; Create)

ID: `javascript-m8-l1`

Objective: Design and deliver an original extension using language internals, security, and package design with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design a dependency-light module with a threat model, strict validation, public API documentation, and compatibility tests. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Language internals, security, and package design: independent studio (90 min; Evaluate)

ID: `javascript-m8-l2`

Objective: Judge two approaches to language internals, security, and package design against correctness, maintainability, and offline operation.

Activity: Design a dependency-light module with a threat model, strict validation, public API documentation, and compatibility tests. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This JavaScript module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `javascript-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `javascript-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This JavaScript module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `javascript-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `javascript-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This JavaScript module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `javascript-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `javascript-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This JavaScript module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `javascript-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `javascript-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This JavaScript module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `javascript-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `javascript-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This JavaScript module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `javascript-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `javascript-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This JavaScript module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `javascript-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `javascript-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This JavaScript module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `javascript-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `javascript-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: AFN expense calculator (6 hours)

Summarize daily expenses in the browser.

Acceptance conditions:

- Validate finite nonnegative amounts.
- Render categories using safe text APIs.
- Provide keyboard-accessible controls.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Study task board (12 hours)

Organize local learning tasks.

Acceptance conditions:

- Create, edit, filter, and complete tasks with stable IDs.
- Persist a versioned snapshot and handle corrupted data.
- Export and import a validated JSON backup.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Local quiz studio (24 hours)

Author and take quizzes without a service.

Acceptance conditions:

- Separate question data, scoring, and rendering.
- Support keyboard interaction and accessible feedback.
- Test scoring boundaries, persistence, and malformed imports.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## ReactJs

Prerequisites: javascript

Offline tools: Provision Node.js and a React project with pinned dependencies and a populated package cache. Use local development/build scripts from that project. All data, fonts, and images must be local; do not depend on a CDN.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

Complete JavaScript first. Open a provisioned local React starter project. In its App.jsx file use this example, keeping the project’s generated entry point. Run the starter project’s documented local command.

Vocabulary:

- Component: a reusable function describing interface content.
- JSX: syntax for describing elements inside JavaScript.
- Prop: an input passed to a component.
- Render: calculate the interface description from data.

```text
export default function App() {
  return <h1>Salam</h1>;
}
```

- App is a JavaScript function used as a component.
- The returned JSX describes a heading containing Salam.
- export default allows the starter entry point to import this component. JSX needs the project’s build tools and is not ordinary HTML pasted into a browser console.

Readiness check: What does this component return?

Answer: A heading description

Guided practice: Return a heading containing Welcome.

Hint: Change only the text between the h1 tags.

Reference solution:

```text
export default function App() {
  return <h1>Welcome</h1>;
}
```

Expected result: The local React page shows a Welcome heading.

### Components, JSX, and props

Components describe reusable UI. Props are inputs owned by a parent; do not mutate them. Break a design into components by responsibility and identify the minimum data required for each one.

```text
function CourseCard({title}) { return <article><h2>{title}</h2></article>; }
```

#### Components, JSX, and props: guided investigation (60 min; Remember)

ID: `reactjs-m1-l1`

Objective: Identify the key terms and syntax in components, jsx, and props without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a component tree for a course catalog with explicit props. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Components, JSX, and props: independent studio (90 min; Understand)

ID: `reactjs-m1-l2`

Objective: Explain how components, jsx, and props changes program behavior using a traced example.

Activity: a component tree for a course catalog with explicit props. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### State, events, and controlled inputs

State drives rendering. Use a state update function when the next value depends on the previous one. Controlled inputs keep the current value in state; validate without losing what the user typed.

```text
function Counter() { const [count,setCount] = useState(0); return <button onClick={() => setCount(c => c+1)}>{count}</button>; }
// import {useState} from "react";
```

#### State, events, and controlled inputs: guided investigation (60 min; Understand)

ID: `reactjs-m2-l1`

Objective: Explain how state, events, and controlled inputs changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a controlled expense form with validation and a derived total. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### State, events, and controlled inputs: independent studio (90 min; Apply)

ID: `reactjs-m2-l2`

Objective: Implement a controlled expense form with validation and a derived total.

Activity: a controlled expense form with validation and a derived total. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Lists, keys, and reducers

Keys preserve identity between renders; array positions are unstable when rows move. A reducer centralizes state transitions and can reject invalid actions. Derived values usually do not need separate state.

```text
function reducer(state, action) { if(action.type === "add") return [...state, action.item]; return state; }
```

#### Lists, keys, and reducers: guided investigation (60 min; Apply)

ID: `reactjs-m3-l1`

Objective: Implement a task reducer and test add, edit, delete, and duplicate-ID actions.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a task reducer and test add, edit, delete, and duplicate-ID actions. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Lists, keys, and reducers: independent studio (90 min; Analyze)

ID: `reactjs-m3-l2`

Objective: Locate a failing assumption in lists, keys, and reducers and isolate it with a minimal reproduction.

Activity: a task reducer and test add, edit, delete, and duplicate-ID actions. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Effects and external systems

Effects synchronize with systems outside rendering, such as storage or subscriptions. Clean up subscriptions and avoid using effects for values that can be calculated during render. Treat asynchronous completion after unmount as a lifecycle concern.

```text
useEffect(() => { const handler = () => setOnline(navigator.onLine); window.addEventListener("online",handler); return () => window.removeEventListener("online",handler); }, []);
```

#### Effects and external systems: guided investigation (60 min; Analyze)

ID: `reactjs-m4-l1`

Objective: Locate a failing assumption in effects and external systems and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a storage adapter and explain which updates require an effect and which are derived. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Effects and external systems: independent studio (90 min; Evaluate)

ID: `reactjs-m4-l2`

Objective: Judge two approaches to effects and external systems against correctness, maintainability, and offline operation.

Activity: a storage adapter and explain which updates require an effect and which are derived. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Composition, accessibility, and tests

Composition often avoids a large configuration-heavy component. Test behavior through labels and roles. Keep focus predictable when dialogs open and close, and test forms with a keyboard instead of only a mouse.

```text
function Field({label, id, children}) { return <div><label htmlFor={id}>{label}</label>{children}</div>; }
```

#### Composition, accessibility, and tests: guided investigation (60 min; Evaluate)

ID: `reactjs-m5-l1`

Objective: Judge two approaches to composition, accessibility, and tests against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an accessible edit dialog with focus restoration and behavior tests. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Composition, accessibility, and tests: independent studio (90 min; Create)

ID: `reactjs-m5-l2`

Objective: Design and deliver an original extension using composition, accessibility, and tests with explicit acceptance tests.

Activity: an accessible edit dialog with focus restoration and behavior tests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Architecture and offline builds

Separate components, domain rules, and persistence adapters. A production build must bundle assets locally. Test the built artifact through a local server with internet disconnected; cached development assets can hide missing dependencies.

```text
src/
  features/tasks/
  domain/taskReducer.js
  adapters/localStore.js
  components/Field.jsx
```

#### Architecture and offline builds: guided investigation (60 min; Create)

ID: `reactjs-m6-l1`

Objective: Design and deliver an original extension using architecture and offline builds with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a production build with local data, failure states, and an architecture decision record. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and offline builds: independent studio (90 min; Evaluate)

ID: `reactjs-m6-l2`

Objective: Judge two approaches to architecture and offline builds against correctness, maintainability, and offline operation.

Activity: a production build with local data, failure states, and an architecture decision record. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Concurrent rendering and application architecture

This React module teaches you to design transitions, suspense boundaries, server-state ownership, and predictable feature boundaries. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
const [isPending, startTransition] = useTransition();
startTransition(() => setQuery(nextQuery));
```

#### Concurrent rendering and application architecture: guided investigation (60 min; Create)

ID: `reactjs-m7-l1`

Objective: Design and deliver an original extension using concurrent rendering and application architecture with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a large searchable local catalog that stays responsive and has explicit loading, empty, error, and recovery states. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Concurrent rendering and application architecture: independent studio (90 min; Evaluate)

ID: `reactjs-m7-l2`

Objective: Judge two approaches to concurrent rendering and application architecture against correctness, maintainability, and offline operation.

Activity: Build a large searchable local catalog that stays responsive and has explicit loading, empty, error, and recovery states. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance, accessibility, and secure delivery

This React module teaches you to profile renders and bundles, test keyboard and screen-reader flows, and defend browser boundaries. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
const visible = useMemo(() => filter(items, query), [items, query]);
```

#### Performance, accessibility, and secure delivery: guided investigation (60 min; Create)

ID: `reactjs-m8-l1`

Objective: Design and deliver an original extension using performance, accessibility, and secure delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Measure and repair a real render bottleneck, complete an accessibility audit, and produce a reproducible offline build. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance, accessibility, and secure delivery: independent studio (90 min; Evaluate)

ID: `reactjs-m8-l2`

Objective: Judge two approaches to performance, accessibility, and secure delivery against correctness, maintainability, and offline operation.

Activity: Measure and repair a real render bottleneck, complete an accessibility audit, and produce a reproducible offline build. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This React module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `reactjs-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `reactjs-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This React module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `reactjs-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `reactjs-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This React module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `reactjs-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `reactjs-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This React module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `reactjs-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `reactjs-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This React module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `reactjs-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `reactjs-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This React module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `reactjs-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `reactjs-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This React module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `reactjs-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `reactjs-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This React module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `reactjs-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `reactjs-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Course catalog UI (6 hours)

Help students browse a local course list.

Acceptance conditions:

- Filter by topic without modifying source data.
- Use stable keys and accessible controls.
- Show an intentional no-results state.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Attendance dashboard (12 hours)

Record attendance for a fictional class.

Acceptance conditions:

- Use reducer-driven updates and stable student IDs.
- Persist local snapshots and compute derived percentages.
- Test toggling, empty classes, and storage failures.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Learning portfolio dashboard (24 hours)

Display projects and student reflections locally.

Acceptance conditions:

- Separate domain rules, UI, and storage.
- Provide accessible editing and validated backup import.
- Build a local production bundle and test with internet disconnected.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## ReactNative

Prerequisites: reactjs

Offline tools: Provision Node.js, a native React Native project, native SDKs, and all packages. Android uses Android Studio/JDK; iOS requires macOS/Xcode. Do not require an online Expo service or cloud build. Local native builds need their complete dependency cache.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

Complete ReactJs first. Open a fully provisioned local React Native starter project. Replace its App component with this example. Use the starter’s native build command and prepared emulator; a cloud build is not required.

Vocabulary:

- Native component: an interface element provided by the mobile platform.
- View: a container for native layout.
- Text: a native component used to display text.
- Prop: an input supplied to a component.

```text
import {View, Text} from "react-native";
export default function App() {
  return <View><Text>Salam</Text></View>;
}
```

- The import brings native components into this module.
- View contains the Text component.
- Visible words belong inside Text. Browser elements such as h1 are not native components here.

Readiness check: Which component displays the word Salam?

Answer: Text

Guided practice: Display Welcome inside a native Text component.

Hint: Keep the import and View wrapper; edit the word inside Text.

Reference solution:

```text
import {View, Text} from "react-native";
export default function App() {
  return <View><Text>Welcome</Text></View>;
}
```

Expected result: The native app displays Welcome.

### Native components and layout

React Native renders native platform components rather than browser DOM elements. Use View and Text, learn Flexbox defaults, and account for safe areas and different screen sizes.

```text
import {View, Text} from "react-native";
function Greeting() { return <View style={{padding:24}}><Text>Salam</Text></View>; }
```

#### Native components and layout: guided investigation (60 min; Remember)

ID: `reactnative-m1-l1`

Objective: Identify the key terms and syntax in native components and layout without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a native information card that adapts to small and large screens. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Native components and layout: independent studio (90 min; Understand)

ID: `reactnative-m1-l2`

Objective: Explain how native components and layout changes program behavior using a traced example.

Activity: a native information card that adapts to small and large screens. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Input, state, and lists

TextInput emits text changes and FlatList renders large collections efficiently. Stable keys preserve item identity. Keep domain data separate from presentation and avoid nesting large scrolling lists unnecessarily.

```text
<FlatList data={items} keyExtractor={item => item.id} renderItem={({item}) => <Text>{item.title}</Text>} />
```

#### Input, state, and lists: guided investigation (60 min; Understand)

ID: `reactnative-m2-l1`

Objective: Explain how input, state, and lists changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a searchable list with controlled input and a meaningful empty state. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Input, state, and lists: independent studio (90 min; Apply)

ID: `reactnative-m2-l2`

Objective: Implement a searchable list with controlled input and a meaningful empty state.

Activity: a searchable list with controlled input and a meaningful empty state. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Navigation and lifecycle

A screen may remain mounted when it loses focus. Distinguish component lifecycle from navigation focus. Pass stable IDs to detail screens and preserve appropriate form drafts when moving between screens.

```text
// Navigation contract: Catalog -> Detail({itemId}) -> Edit({itemId}).
// The repository owns records; route parameters carry IDs only.
```

#### Navigation and lifecycle: guided investigation (60 min; Apply)

ID: `reactnative-m3-l1`

Objective: Implement a three-screen flow with predictable back behavior and draft preservation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a three-screen flow with predictable back behavior and draft preservation. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Navigation and lifecycle: independent studio (90 min; Analyze)

ID: `reactnative-m3-l2`

Objective: Locate a failing assumption in navigation and lifecycle and isolate it with a minimal reproduction.

Activity: a three-screen flow with predictable back behavior and draft preservation. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Local storage and repository adapters

React Native does not provide browser localStorage. Choose a provisioned native storage adapter and validate serialized data. Expose async repository operations and show failures without discarding user edits.

```text
async function saveItem(store, item) { if(!item.title.trim()) throw new Error("Title required"); await store.save(item); }
```

#### Local storage and repository adapters: guided investigation (60 min; Analyze)

ID: `reactnative-m4-l1`

Objective: Locate a failing assumption in local storage and repository adapters and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a replaceable local store with save-failure and restart tests. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Local storage and repository adapters: independent studio (90 min; Evaluate)

ID: `reactnative-m4-l2`

Objective: Judge two approaches to local storage and repository adapters against correctness, maintainability, and offline operation.

Activity: a replaceable local store with save-failure and restart tests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Platform APIs and accessibility

Permissions depend on the feature and platform. Ask in context and support denial. Accessibility labels, roles, and scalable text need native testing; a web accessibility result does not prove a native screen works.

```text
<Pressable accessibilityRole="button" accessibilityLabel="Save note" onPress={save}><Text>Save</Text></Pressable>
```

#### Platform APIs and accessibility: guided investigation (60 min; Evaluate)

ID: `reactnative-m5-l1`

Objective: Judge two approaches to platform apis and accessibility against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an accessible export action that handles unavailable platform support. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Platform APIs and accessibility: independent studio (90 min; Create)

ID: `reactnative-m5-l2`

Objective: Design and deliver an original extension using platform apis and accessibility with explicit acceptance tests.

Activity: an accessible export action that handles unavailable platform support. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Testing and native packaging

Test pure rules in JavaScript and critical flows on a device or simulator. Native dependencies can behave differently across platforms. Produce a local build, record its platform, and verify the installed app without internet.

```text
// Test matrix: Android/iOS, small/large text, empty/populated store, save failure, relaunch.
```

#### Testing and native packaging: guided investigation (60 min; Create)

ID: `reactnative-m6-l1`

Objective: Design and deliver an original extension using testing and native packaging with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a native release candidate with documented platform gaps and reproducible offline build prerequisites. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing and native packaging: independent studio (90 min; Evaluate)

ID: `reactnative-m6-l2`

Objective: Judge two approaches to testing and native packaging against correctness, maintainability, and offline operation.

Activity: a native release candidate with documented platform gaps and reproducible offline build prerequisites. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Native modules, threads, and performance

This React Native module teaches you to understand the new architecture boundary, avoid JS-thread stalls, and measure startup, lists, and memory. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
<FlatList data={items} keyExtractor={item => item.id} renderItem={renderItem} />
```

#### Native modules, threads, and performance: guided investigation (60 min; Create)

ID: `reactnative-m7-l1`

Objective: Design and deliver an original extension using native modules, threads, and performance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Profile a large offline list, repair measured frame drops, and document when native code is justified. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Native modules, threads, and performance: independent studio (90 min; Evaluate)

ID: `reactnative-m7-l2`

Objective: Judge two approaches to native modules, threads, and performance against correctness, maintainability, and offline operation.

Activity: Profile a large offline list, repair measured frame drops, and document when native code is justified. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Offline-first mobile delivery

This React Native module teaches you to design durable local state, migrations, conflict policies, accessibility, signing, and reproducible Android/iOS releases. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
type PendingChange = { id: string; operation: "upsert" | "delete"; version: number };
```

#### Offline-first mobile delivery: guided investigation (60 min; Create)

ID: `reactnative-m8-l1`

Objective: Design and deliver an original extension using offline-first mobile delivery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a local-first mobile feature with migration tests, interrupted-write recovery, platform accessibility checks, and release evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Offline-first mobile delivery: independent studio (90 min; Evaluate)

ID: `reactnative-m8-l2`

Objective: Judge two approaches to offline-first mobile delivery against correctness, maintainability, and offline operation.

Activity: Deliver a local-first mobile feature with migration tests, interrupted-write recovery, platform accessibility checks, and release evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This React Native module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `reactnative-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `reactnative-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This React Native module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `reactnative-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `reactnative-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This React Native module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `reactnative-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `reactnative-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This React Native module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `reactnative-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `reactnative-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This React Native module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `reactnative-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `reactnative-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This React Native module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `reactnative-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `reactnative-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This React Native module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `reactnative-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `reactnative-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This React Native module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `reactnative-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `reactnative-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Campus directory (6 hours)

Browse fictional campus contacts and places.

Acceptance conditions:

- Bundle records and local imagery.
- Provide accessible search and detail views.
- Handle narrow screens and larger text.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Personal study tracker (12 hours)

Record study sessions on one device.

Acceptance conditions:

- Validate durations and preserve local records.
- Summarize by subject without duplicate counting.
- Test relaunch and storage failure.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Field survey notebook (24 hours)

Collect fictional community survey records locally.

Acceptance conditions:

- Separate form validation and native storage.
- Provide edit, export, and permission-denial behavior.
- Verify a locally built native app in airplane mode.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## NodeJs

Prerequisites: javascript

Offline tools: Provision a Node.js runtime. The examples and initial projects use built-in modules; run node filename.mjs and node --test. Bind demonstration services to 127.0.0.1. No external network calls are required.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

Complete JavaScript first. On a computer with Node.js installed, save hello.mjs. Open a terminal in its folder and run node hello.mjs. A browser and internet connection are not required.

Vocabulary:

- Runtime: software that executes a language.
- Terminal: an interface for entering operating-system commands.
- Argument: a value supplied to a program or function.
- Module: a file with explicitly shared code.

```text
const city = "Kabul";
console.log(city);
```

- Node executes the file outside the browser.
- The first line binds Kabul to city.
- console.log writes the value to the terminal. No DOM or document object is provided by Node.

Readiness check: Where does this example show its output?

Answer: The terminal

Guided practice: Write a local script that displays Salam.

Hint: Use console.log with a quoted string and run the saved .mjs file.

Reference solution:

```text
console.log("Salam");
```

Expected result: Salam

### Runtime and modules

Node.js runs JavaScript outside the browser and provides platform APIs. ES modules define imports and exports. Use explicit file extensions for local module paths and separate CLI input from domain logic.

```text
import {parseArgs} from "node:util";
const {positionals} = parseArgs({allowPositionals:true});
console.log(positionals);
```

#### Runtime and modules: guided investigation (60 min; Remember)

ID: `nodejs-m1-l1`

Objective: Identify the key terms and syntax in runtime and modules without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a CLI that validates arguments and prints a useful usage message. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Runtime and modules: independent studio (90 min; Understand)

ID: `nodejs-m1-l2`

Objective: Explain how runtime and modules changes program behavior using a traced example.

Activity: a CLI that validates arguments and prints a useful usage message. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Async filesystem operations

Promise-based IO avoids blocking while waiting, but CPU-heavy loops still block the event loop. Resolve file paths deliberately and handle missing or malformed data with specific errors.

```text
import {readFile} from "node:fs/promises";
const text = await readFile("records.json", "utf8");
const records = JSON.parse(text);
```

#### Async filesystem operations: guided investigation (60 min; Understand)

ID: `nodejs-m2-l1`

Objective: Explain how async filesystem operations changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a local report generator with missing-file and invalid-JSON cases. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Async filesystem operations: independent studio (90 min; Apply)

ID: `nodejs-m2-l2`

Objective: Implement a local report generator with missing-file and invalid-JSON cases.

Activity: a local report generator with missing-file and invalid-JSON cases. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Streams and backpressure

Streams process chunks instead of loading entire files. Backpressure prevents a producer from overwhelming a consumer. pipeline connects error handling and completion across a chain; always handle its rejection.

```text
import {pipeline} from "node:stream/promises";
import {createReadStream, createWriteStream} from "node:fs";
await pipeline(createReadStream("input.txt"), createWriteStream("copy.txt"));
```

#### Streams and backpressure: guided investigation (60 min; Apply)

ID: `nodejs-m3-l1`

Objective: Implement a bounded-memory file copy with error handling and byte-for-byte verification.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a bounded-memory file copy with error handling and byte-for-byte verification. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Streams and backpressure: independent studio (90 min; Analyze)

ID: `nodejs-m3-l2`

Objective: Locate a failing assumption in streams and backpressure and isolate it with a minimal reproduction.

Activity: a bounded-memory file copy with error handling and byte-for-byte verification. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### HTTP and event-loop behavior

An HTTP handler must finish each response. Validate route, method, and body size; a slow CPU task delays other requests. Listen on loopback for local exercises and close the server cleanly after tests.

```text
import {createServer} from "node:http";
createServer((req,res) => { res.writeHead(200,{"Content-Type":"application/json"}); res.end(JSON.stringify({status:"ok"})); }).listen(3000,"127.0.0.1");
```

#### HTTP and event-loop behavior: guided investigation (60 min; Analyze)

ID: `nodejs-m4-l1`

Objective: Locate a failing assumption in http and event-loop behavior and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a local health endpoint and measure how a CPU-heavy handler affects latency. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### HTTP and event-loop behavior: independent studio (90 min; Evaluate)

ID: `nodejs-m4-l2`

Objective: Judge two approaches to http and event-loop behavior against correctness, maintainability, and offline operation.

Activity: a local health endpoint and measure how a CPU-heavy handler affects latency. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing, workers, and contracts

Use node:test for deterministic domain checks. Workers can isolate CPU-heavy work, but messages must be bounded and lifecycle cleanup matters. Inject filesystem and clock dependencies when tests need controlled failures.

```text
import test from "node:test";
import assert from "node:assert/strict";
test("empty total", () => assert.equal([].reduce((a,b)=>a+b,0),0));
```

#### Testing, workers, and contracts: guided investigation (60 min; Evaluate)

ID: `nodejs-m5-l1`

Objective: Judge two approaches to testing, workers, and contracts against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a report worker with timeout handling and tests for malformed requests. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Testing, workers, and contracts: independent studio (90 min; Create)

ID: `nodejs-m5-l2`

Objective: Design and deliver an original extension using testing, workers, and contracts with explicit acceptance tests.

Activity: a report worker with timeout handling and tests for malformed requests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Packaging and operational recovery

Document runtime requirements and command-line contracts. Avoid logging sensitive records. Atomic file replacement and explicit backup restoration reduce data-loss risk; a clean shutdown must finish or reject in-flight work predictably.

```text
app/
  cli.mjs
  domain/report.mjs
  adapters/files.mjs
  test/report.test.mjs
```

#### Packaging and operational recovery: guided investigation (60 min; Create)

ID: `nodejs-m6-l1`

Objective: Design and deliver an original extension using packaging and operational recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a standard-library-only release with bounded inputs, local backup, and failure recovery tests. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Packaging and operational recovery: independent studio (90 min; Evaluate)

ID: `nodejs-m6-l2`

Objective: Judge two approaches to packaging and operational recovery against correctness, maintainability, and offline operation.

Activity: a standard-library-only release with bounded inputs, local backup, and failure recovery tests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Streams, workers, and backpressure

This Node.js module teaches you to process large inputs with bounded memory, worker isolation, cancellation, and explicit error propagation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
import { pipeline } from "node:stream/promises";
await pipeline(source, transform, destination);
```

#### Streams, workers, and backpressure: guided investigation (60 min; Create)

ID: `nodejs-m7-l1`

Objective: Design and deliver an original extension using streams, workers, and backpressure with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a bounded CSV pipeline and prove backpressure, cleanup, cancellation, and malformed-record handling. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Streams, workers, and backpressure: independent studio (90 min; Evaluate)

ID: `nodejs-m7-l2`

Objective: Judge two approaches to streams, workers, and backpressure against correctness, maintainability, and offline operation.

Activity: Build a bounded CSV pipeline and prove backpressure, cleanup, cancellation, and malformed-record handling. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Diagnostics, security, and production operations

This Node.js module teaches you to measure event-loop delay, trace requests, constrain privileges, and operate graceful startup and shutdown. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
process.on("SIGTERM", async () => {
  await server.close();
  process.exitCode = 0;
});
```

#### Diagnostics, security, and production operations: guided investigation (60 min; Create)

ID: `nodejs-m8-l1`

Objective: Design and deliver an original extension using diagnostics, security, and production operations with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Package a loopback service with structured diagnostics, resource limits, threat model, graceful shutdown, and recovery test. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Diagnostics, security, and production operations: independent studio (90 min; Evaluate)

ID: `nodejs-m8-l2`

Objective: Judge two approaches to diagnostics, security, and production operations against correctness, maintainability, and offline operation.

Activity: Package a loopback service with structured diagnostics, resource limits, threat model, graceful shutdown, and recovery test. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Node.js module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `nodejs-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `nodejs-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Node.js module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `nodejs-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `nodejs-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Node.js module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `nodejs-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `nodejs-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Node.js module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `nodejs-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `nodejs-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Node.js module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `nodejs-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `nodejs-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Node.js module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `nodejs-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `nodejs-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Node.js module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `nodejs-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `nodejs-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Node.js module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `nodejs-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `nodejs-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: CSV report CLI (6 hours)

Summarize fictional attendance data.

Acceptance conditions:

- Validate the documented CSV dialect and record schema.
- Report malformed rows with line numbers.
- Write deterministic summaries and test empty files.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Local file catalog (12 hours)

Index a selected exercise directory.

Acceptance conditions:

- Restrict traversal to the chosen root and handle unreadable files.
- Process large files without loading them all into memory.
- Export a catalog and test interrupted operations.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Offline reporting service (24 hours)

Serve local reports from fictional datasets.

Acceptance conditions:

- Bind to loopback and limit request and file sizes.
- Separate HTTP, report rules, and persistence.
- Test timeouts, invalid input, graceful shutdown, and backup recovery.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## ExpressJs

Prerequisites: nodejs

Offline tools: Provision Node.js and a pinned Express installation plus any testing dependencies. Use a local package cache and a lockfile. Bind to loopback and use fictional data; no cloud database or hosted API is required.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

Complete NodeJs first. Use a provisioned project with Express installed and an ES-module entry file named app.mjs. Run node app.mjs, then open http://127.0.0.1:3000/ in a browser on the same computer. This local address does not require internet.

Vocabulary:

- Route: a rule matching a request method and path.
- Request: a client’s message to a server.
- Response: the server’s reply.
- Loopback: an address that refers to the same computer.

```text
import express from "express";
const app = express();
app.get("/", (req, res) => res.send("Salam"));
app.listen(3000, "127.0.0.1");
```

- express() creates an application with a route table.
- The GET route answers requests for / by sending Salam.
- listen starts the local service. Stop it with Ctrl+C in its terminal after practicing. This example has no database or authentication.

Readiness check: What does a GET request to / receive?

Answer: Salam

Guided practice: Change the route response to Welcome.

Hint: Edit the string passed to res.send and restart the local service.

Reference solution:

```text
import express from "express";
const app = express();
app.get("/", (req, res) => res.send("Welcome"));
app.listen(3000, "127.0.0.1");
```

Expected result: The local browser displays Welcome.

### Routing and middleware order

Express matches requests through an ordered middleware chain. A handler must respond or delegate. Put general parsing before routes and error handling after routes; middleware order changes behavior.

```text
import express from "express";
const app = express();
app.use(express.json({limit:"16kb"}));
app.get("/health", (req,res) => res.json({status:"ok"}));
app.listen(3000,"127.0.0.1");
```

#### Routing and middleware order: guided investigation (60 min; Remember)

ID: `expressjs-m1-l1`

Objective: Identify the key terms and syntax in routing and middleware order without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a loopback service with health, not-found, and JSON routes. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Routing and middleware order: independent studio (90 min; Understand)

ID: `expressjs-m1-l2`

Objective: Explain how routing and middleware order changes program behavior using a traced example.

Activity: a loopback service with health, not-found, and JSON routes. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Validation and REST contracts

Validate types and business constraints at the boundary. Use status codes consistently and return structured errors without stack traces. An ID in the URL does not prove a caller may modify that resource.

```text
app.post("/items", (req,res) => { if(typeof req.body?.name !== "string" || !req.body.name.trim()) return res.status(400).json({error:"name_required"}); res.status(201).json({name:req.body.name.trim()}); });
```

#### Validation and REST contracts: guided investigation (60 min; Understand)

ID: `expressjs-m2-l1`

Objective: Explain how validation and rest contracts changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a create-item contract with missing, malformed, and valid request tests. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Validation and REST contracts: independent studio (90 min; Apply)

ID: `expressjs-m2-l2`

Objective: Implement a create-item contract with missing, malformed, and valid request tests.

Activity: a create-item contract with missing, malformed, and valid request tests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Service and repository layers

Routes translate HTTP; services enforce rules; repositories persist state. Dependency injection allows an in-memory repository in tests. Avoid storing business policy in middleware that unrelated routes accidentally inherit.

```text
function createItemService(repository) { return { list: () => repository.list() }; }
```

#### Service and repository layers: guided investigation (60 min; Apply)

ID: `expressjs-m3-l1`

Objective: Implement a replaceable item repository and keep domain tests independent of Express.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a replaceable item repository and keep domain tests independent of Express. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Service and repository layers: independent studio (90 min; Analyze)

ID: `expressjs-m3-l2`

Objective: Locate a failing assumption in service and repository layers and isolate it with a minimal reproduction.

Activity: a replaceable item repository and keep domain tests independent of Express. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Errors, authorization, and input limits

Handle known errors explicitly and hide internal details. Enforce authorization for each operation and bound request sizes. Offline operation does not make local input trustworthy. Authentication design needs vetted libraries and separate security review before real deployment.

```text
app.use((error,req,res,next) => { if(res.headersSent) return next(error); res.status(500).json({error:"internal_error"}); });
```

#### Errors, authorization, and input limits: guided investigation (60 min; Analyze)

ID: `expressjs-m4-l1`

Objective: Locate a failing assumption in errors, authorization, and input limits and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a fictional-role authorization matrix and tests for denied operations and oversized requests. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Errors, authorization, and input limits: independent studio (90 min; Evaluate)

ID: `expressjs-m4-l2`

Objective: Judge two approaches to errors, authorization, and input limits against correctness, maintainability, and offline operation.

Activity: a fictional-role authorization matrix and tests for denied operations and oversized requests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Integration tests and transactions

Exercise the service through HTTP with a temporary store. Assert response and resulting state, including failures. Related persistence operations must commit together; retries need a stable operation identifier to avoid duplicate writes.

```text
// Test: POST loan -> 201; repeat operation ID -> same result;
// conflicting loan -> 409; storage failure -> no partial loan.
```

#### Integration tests and transactions: guided investigation (60 min; Evaluate)

ID: `expressjs-m5-l1`

Objective: Judge two approaches to integration tests and transactions against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an integration suite for atomic lending and idempotent retries. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Integration tests and transactions: independent studio (90 min; Create)

ID: `expressjs-m5-l2`

Objective: Design and deliver an original extension using integration tests and transactions with explicit acceptance tests.

Activity: an integration suite for atomic lending and idempotent retries. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Local release and observability

Separate app construction from listen so tests can own ports and cleanup. Log operation IDs and outcomes without dumping personal data. Document runtime, dependency cache, fixtures, and restoration procedures for a disconnected machine.

```text
export function createApp(service) { const app = express(); app.get("/items", async (req,res,next) => { try { res.json(await service.list()); } catch(error) { next(error); } }); return app; }
```

#### Local release and observability: guided investigation (60 min; Create)

ID: `expressjs-m6-l1`

Objective: Design and deliver an original extension using local release and observability with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a release package with controlled startup, shutdown, and an offline smoke test. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Local release and observability: independent studio (90 min; Evaluate)

ID: `expressjs-m6-l2`

Objective: Judge two approaches to local release and observability against correctness, maintainability, and offline operation.

Activity: a release package with controlled startup, shutdown, and an offline smoke test. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Service architecture and resilient workflows

This Express module teaches you to separate HTTP, application, and persistence concerns while applying idempotency and transaction boundaries. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
app.post("/loans", validate, asyncHandler(async (req, res) => {
  res.status(201).json(await service.create(req.body));
}));
```

#### Service architecture and resilient workflows: guided investigation (60 min; Create)

ID: `expressjs-m7-l1`

Objective: Design and deliver an original extension using service architecture and resilient workflows with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Implement an idempotent transactional workflow with stable errors and contract tests through real HTTP. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Service architecture and resilient workflows: independent studio (90 min; Evaluate)

ID: `expressjs-m7-l2`

Objective: Judge two approaches to service architecture and resilient workflows against correctness, maintainability, and offline operation.

Activity: Implement an idempotent transactional workflow with stable errors and contract tests through real HTTP. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### API security, observability, and operations

This Express module teaches you to apply authentication boundaries, authorization policy, rate and size limits, redacted logs, and graceful operation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
app.use(express.json({ limit: "16kb" }));
app.use((err, req, res, next) => res.status(500).json({code:"INTERNAL"}));
```

#### API security, observability, and operations: guided investigation (60 min; Create)

ID: `expressjs-m8-l1`

Objective: Design and deliver an original extension using api security, observability, and operations with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Threat-model and harden a local API, then verify limits, policy failures, redaction, health, and clean shutdown. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### API security, observability, and operations: independent studio (90 min; Evaluate)

ID: `expressjs-m8-l2`

Objective: Judge two approaches to api security, observability, and operations against correctness, maintainability, and offline operation.

Activity: Threat-model and harden a local API, then verify limits, policy failures, redaction, health, and clean shutdown. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Express module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `expressjs-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `expressjs-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Express module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `expressjs-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `expressjs-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Express module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `expressjs-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `expressjs-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Express module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `expressjs-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `expressjs-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Express module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `expressjs-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `expressjs-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Express module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `expressjs-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `expressjs-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Express module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `expressjs-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `expressjs-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Express module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `expressjs-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `expressjs-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Course catalog API (6 hours)

Expose a fictional training catalog locally.

Acceptance conditions:

- Implement list, detail, and filtered search routes.
- Return consistent validation and not-found errors.
- Test contracts through HTTP on a temporary port.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Library lending API (12 hours)

Enforce loan rules behind HTTP endpoints.

Acceptance conditions:

- Use service and repository boundaries.
- Prevent duplicate active loans and validate IDs.
- Test rollback and idempotent retry behavior.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Training enrollment service (24 hours)

Manage local enrollments for fictional courses.

Acceptance conditions:

- Enforce capacity and explicit role policies.
- Bound requests and avoid leaking internal errors.
- Ship integration tests, seed data, and offline operation instructions.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Flutter and Dart

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Provision Flutter/Dart, target SDKs, fonts, and all pub/native dependency caches. Use flutter pub get --offline after provisioning. Android and Windows need their native build tools; iOS builds require macOS/Xcode. The app’s Python sandbox does not execute Dart.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

No programming experience is required. Start with Dart before widgets. On a computer with Flutter/Dart provisioned, save main.dart and run dart run main.dart. This first lesson uses the console, not a mobile screen.

Vocabulary:

- Dart: the programming language used here.
- Function: a named group of instructions.
- Widget: a description of part of a Flutter interface.
- print: a Dart function that writes a value to the console.

```text
void main() {
  final city = "Kabul";
  print(city);
}
```

- main is where this program starts. void means it returns no value to its caller.
- final creates a binding that is assigned once.
- print displays Kabul in the console. In a Flutter interface, use a Text widget instead when the user should see text on screen.

Readiness check: Where does print(city) display Kabul?

Answer: The console

Guided practice: Declare greeting with final and display Salam.

Hint: Keep the main function and change both the binding and print argument.

Reference solution:

```text
void main() {
  final greeting = "Salam";
  print(greeting);
}
```

Expected result: Salam

### Dart types and asynchronous code

Sound null safety makes absent values explicit. Futures represent eventual results and streams represent multiple events. Validate inputs at boundaries and keep calculation functions independent of widgets.

```text
int total(List<int> values) => values.fold(0, (sum, value) => sum + value);
void main() { assert(total([]) == 0); print(total([10,20])); }
```

#### Dart types and asynchronous code: guided investigation (60 min; Remember)

ID: `flutter-dart-m1-l1`

Objective: Identify the key terms and syntax in dart types and asynchronous code without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a typed expense model and pure validation functions with boundary tests. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Dart types and asynchronous code: independent studio (90 min; Understand)

ID: `flutter-dart-m1-l2`

Objective: Explain how dart types and asynchronous code changes program behavior using a traced example.

Activity: a typed expense model and pure validation functions with boundary tests. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Widgets, constraints, and layout

Flutter layout passes constraints down, sizes up, and positions children. A widget describes configuration; state belongs to an appropriate owner. Avoid unbounded flex children in scrolling layouts and test long labels.

```text
class Greeting extends StatelessWidget { const Greeting({super.key}); @override Widget build(BuildContext context) => const Padding(padding: EdgeInsets.all(24), child: Text("Salam")); }
```

#### Widgets, constraints, and layout: guided investigation (60 min; Understand)

ID: `flutter-dart-m2-l1`

Objective: Explain how widgets, constraints, and layout changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a responsive course card that supports narrow screens and larger text. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Widgets, constraints, and layout: independent studio (90 min; Apply)

ID: `flutter-dart-m2-l2`

Objective: Implement a responsive course card that supports narrow screens and larger text.

Activity: a responsive course card that supports narrow screens and larger text. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### State, navigation, and forms

Choose one owner for shared state and expose explicit actions. Navigation should carry stable IDs. Validate before saving and show progress while work is pending; only display success after persistence succeeds.

```text
final formKey = GlobalKey<FormState>();
// Form(key: formKey, child: TextFormField(validator: (v) => v == null || v.trim().isEmpty ? "Required" : null));
```

#### State, navigation, and forms: guided investigation (60 min; Apply)

ID: `flutter-dart-m3-l1`

Objective: Implement a list-detail-edit flow with validation and preserved input after a failed save.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a list-detail-edit flow with validation and preserved input after a failed save. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### State, navigation, and forms: independent studio (90 min; Analyze)

ID: `flutter-dart-m3-l2`

Objective: Locate a failing assumption in state, navigation, and forms and isolate it with a minimal reproduction.

Activity: a list-detail-edit flow with validation and preserved input after a failed save. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Clean architecture and local storage

Domain rules depend on contracts, and adapters implement SQLite or file storage. Inject repositories into application services. Transactions protect related writes; migrations and validated backup formats protect data across releases.

```text
abstract interface class NoteRepository { Future<List<String>> load(); Future<void> save(List<String> notes); }
class LoadNotes { LoadNotes(this.repository); final NoteRepository repository; Future<List<String>> call() => repository.load(); }
```

#### Clean architecture and local storage: guided investigation (60 min; Analyze)

ID: `flutter-dart-m4-l1`

Objective: Locate a failing assumption in clean architecture and local storage and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a local repository with memory and persistent adapters plus migration fixtures. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Clean architecture and local storage: independent studio (90 min; Evaluate)

ID: `flutter-dart-m4-l2`

Objective: Judge two approaches to clean architecture and local storage against correctness, maintainability, and offline operation.

Activity: a local repository with memory and persistent adapters plus migration fixtures. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Isolates, accessibility, and testing

An isolate has separate memory and communicates with messages. Bound work and terminate a worker on timeout. Unit tests check rules, widget tests check interaction, and integration tests check real plugins and startup.

```text
final result = await Isolate.run(() => [1,2,3].fold(0, (a,b) => a+b));
// Import dart:isolate; use explicit worker lifecycle control for cancellable work.
```

#### Isolates, accessibility, and testing: guided investigation (60 min; Evaluate)

ID: `flutter-dart-m5-l1`

Objective: Judge two approaches to isolates, accessibility, and testing against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. a bounded report worker and accessible UI tests with large text and storage failures. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Isolates, accessibility, and testing: independent studio (90 min; Create)

ID: `flutter-dart-m5-l2`

Objective: Design and deliver an original extension using isolates, accessibility, and testing with explicit acceptance tests.

Activity: a bounded report worker and accessible UI tests with large text and storage failures. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Release engineering and offline guarantees

A release must include assets and native libraries for its target. Separate developer provisioning from learner runtime. Verify first launch, learning, saving, restart, and backup with internet disabled; keep signing secrets out of source control.

```text
lib/
  domain/
  application/
  data/
  presentation/
  runtime/
test/
integration_test/
```

#### Release engineering and offline guarantees: guided investigation (60 min; Create)

ID: `flutter-dart-m6-l1`

Objective: Design and deliver an original extension using release engineering and offline guarantees with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. an offline release candidate with dependency documentation, CI checks, and real-device acceptance evidence. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Release engineering and offline guarantees: independent studio (90 min; Evaluate)

ID: `flutter-dart-m6-l2`

Objective: Judge two approaches to release engineering and offline guarantees against correctness, maintainability, and offline operation.

Activity: an offline release candidate with dependency documentation, CI checks, and real-device acceptance evidence. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Rendering, isolates, and performance engineering

This Flutter and Dart module teaches you to measure frames, rebuilds, memory, startup, and isolate transfer before applying targeted optimizations. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
final result = await Isolate.run(() => expensiveReport(records));
// Transfer immutable results and enforce a timeout.
```

#### Rendering, isolates, and performance engineering: guided investigation (60 min; Create)

ID: `flutter-dart-m7-l1`

Objective: Design and deliver an original extension using rendering, isolates, and performance engineering with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Profile a large offline screen, repair one measured bottleneck, and verify responsiveness on a low-resource device. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Rendering, isolates, and performance engineering: independent studio (90 min; Evaluate)

ID: `flutter-dart-m7-l2`

Objective: Judge two approaches to rendering, isolates, and performance engineering against correctness, maintainability, and offline operation.

Activity: Profile a large offline screen, repair one measured bottleneck, and verify responsiveness on a low-resource device. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Platform integration, security, and release automation

This Flutter and Dart module teaches you to design plugin boundaries, migrations, permissions, signing, reproducible builds, and rollback evidence. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
abstract interface class SecureStore {
  Future<void> write(String key, String value);
}
```

#### Platform integration, security, and release automation: guided investigation (60 min; Create)

ID: `flutter-dart-m8-l1`

Objective: Design and deliver an original extension using platform integration, security, and release automation with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a platform adapter with fakes and integration tests plus signed-build, offline-install, backup, migration, and rollback checks. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Platform integration, security, and release automation: independent studio (90 min; Evaluate)

ID: `flutter-dart-m8-l2`

Objective: Judge two approaches to platform integration, security, and release automation against correctness, maintainability, and offline operation.

Activity: Deliver a platform adapter with fakes and integration tests plus signed-build, offline-install, backup, migration, and rollback checks. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This Flutter and Dart module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `flutter-dart-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `flutter-dart-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This Flutter and Dart module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `flutter-dart-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `flutter-dart-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This Flutter and Dart module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `flutter-dart-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `flutter-dart-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This Flutter and Dart module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `flutter-dart-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `flutter-dart-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This Flutter and Dart module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `flutter-dart-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `flutter-dart-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This Flutter and Dart module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `flutter-dart-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `flutter-dart-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This Flutter and Dart module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `flutter-dart-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `flutter-dart-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This Flutter and Dart module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `flutter-dart-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `flutter-dart-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Student timetable (6 hours)

Build a responsive local timetable.

Acceptance conditions:

- Use typed data and accessible day navigation.
- Bundle content and fonts.
- Test narrow layout and large text.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Offline expense journal (12 hours)

Record fictional expenses across app restarts.

Acceptance conditions:

- Inject a local repository and validate amounts.
- Persist atomically and implement validated JSON backup.
- Test failed saves and backup round trips.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Mini learning platform (24 hours)

Create a small offline education app using the architecture taught here.

Acceptance conditions:

- Separate curriculum, assessment, portfolio, storage, and UI responsibilities.
- Bundle lessons and track progress without accounts or network calls.
- Deliver unit, widget, integration tests and a verified target-specific release.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## Database Foundations

Prerequisites: No prior programming required; basic device and file use.

Offline tools: Use the in-app SQL practice for read-only queries on fictional data. The worked scripts can also be run in a separately prepared SQLite tool. Each example starts with a fresh database; no internet or account is needed.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

A database organizes information so it can be found and checked. Imagine a library register: each book is one row, and title and price are columns. A table describes the fields every record uses. SQL is a language for asking the database to create, read, and change records. Keeping data in a table is different from displaying it on a screen.

Vocabulary:

- Database: organized information that a program can read and change.
- Record: one stored item, represented by a row or a document.
- Query: a request describing which information you want.
- Constraint: a rule that rejects invalid stored data.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT title, price FROM books ORDER BY id;
```

- CREATE TABLE defines the structure but adds no books. INSERT adds three rows. SELECT asks for two columns and ORDER BY id fixes the display order. The rows are Python/100, Databases/150, and Web/100. A result table is a view of stored data, not a second saved copy.

Readiness check: What should you do before changing training data?

Answer: Predict the result and identify the target records.

Guided practice: Read only the title column and keep the rows ordered by id.

Hint: Use a fresh fictional fixture. Read the worked trace and change only the requested fields or query.

Reference solution:

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT title FROM books ORDER BY id;
```

Expected result: Three titles appear in this order: Python, Databases, Web. No price column is returned.

### Tables, rows, and columns

A database organizes information so it can be found and checked. Imagine a library register: each book is one row, and title and price are columns. A table describes the fields every record uses. SQL is a language for asking the database to create, read, and change records. Keeping data in a table is different from displaying it on a screen.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT title, price FROM books ORDER BY id;
```

#### Tables, rows, and columns: guided investigation (60 min; Remember)

ID: `database-foundations-m1-l1`

Objective: Identify the key terms and syntax in tables, rows, and columns without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Read only the title column and keep the rows ordered by id. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Tables, rows, and columns: independent studio (90 min; Understand)

ID: `database-foundations-m1-l2`

Objective: Explain how tables, rows, and columns changes program behavior using a traced example.

Activity: Read only the title column and keep the rows ordered by id. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Identity and primary keys

Two students may share a name, so a name is a poor identity. A primary key uniquely identifies a row. Other records can refer to that stable key even after a title changes. Choose identity independently of display order: the first visible row is not necessarily record 1.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
UPDATE books SET title='Python basics' WHERE id=1;
SELECT id,title FROM books ORDER BY id;
```

#### Identity and primary keys: guided investigation (60 min; Understand)

ID: `database-foundations-m2-l1`

Objective: Explain how identity and primary keys changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Rename book 2 without changing either its id or the other books. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Identity and primary keys: independent studio (90 min; Apply)

ID: `database-foundations-m2-l2`

Objective: Implement rename book 2 without changing either its id or the other books.

Activity: Rename book 2 without changing either its id or the other books. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Relationships and foreign keys

A loan belongs to a book, so store the book id on the loan instead of copying all book fields. This is a relationship. A foreign key rejects references to missing books when enforcement is enabled. It does not automatically limit a book to one active loan; that is another rule.

```text
PRAGMA foreign_keys=ON;
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
CREATE TABLE loans(id INTEGER PRIMARY KEY, book_id INTEGER NOT NULL REFERENCES books(id));
INSERT INTO loans VALUES(1,2);
SELECT b.title FROM loans l JOIN books b ON b.id=l.book_id;
```

#### Relationships and foreign keys: guided investigation (60 min; Apply)

ID: `database-foundations-m3-l1`

Objective: Implement add a second loan for book 1 and list both referenced titles.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Add a second loan for book 1 and list both referenced titles. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Relationships and foreign keys: independent studio (90 min; Analyze)

ID: `database-foundations-m3-l2`

Objective: Locate a failing assumption in relationships and foreign keys and isolate it with a minimal reproduction.

Activity: Add a second loan for book 1 and list both referenced titles. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Reducing duplicate facts

Repeating a category name on every book makes renaming error-prone. Put each category in its own row and reference its key. This is one step toward normalization: store one fact in one appropriate place. Separate tables when they represent independent facts, not merely because more tables look advanced.

```text
CREATE TABLE categories(id INTEGER PRIMARY KEY,name TEXT NOT NULL);
CREATE TABLE titles(id INTEGER PRIMARY KEY,title TEXT,category_id INTEGER);
INSERT INTO categories VALUES(1,'Computing');
INSERT INTO titles VALUES(1,'Python',1),(2,'Web',1);
SELECT title,name FROM titles JOIN categories ON categories.id=titles.category_id ORDER BY titles.id;
```

#### Reducing duplicate facts: guided investigation (60 min; Analyze)

ID: `database-foundations-m4-l1`

Objective: Locate a failing assumption in reducing duplicate facts and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Rename the shared category once and explain why both result rows change. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Reducing duplicate facts: independent studio (90 min; Evaluate)

ID: `database-foundations-m4-l2`

Objective: Judge two approaches to reducing duplicate facts against correctness, maintainability, and offline operation.

Activity: Rename the shared category once and explain why both result rows change. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Constraints and valid records

Validation in a screen can be bypassed by another writer. Database constraints provide a second boundary. NOT NULL rejects missing values and CHECK enforces a stated condition. A non-null title can still be blank, so encode the actual rule rather than assuming the type says everything.

```text
CREATE TABLE students(id INTEGER PRIMARY KEY,name TEXT NOT NULL CHECK(length(trim(name))>0),age INTEGER NOT NULL CHECK(age>=0));
INSERT INTO students VALUES(1,'Amina',20);
SELECT name,age FROM students;
```

#### Constraints and valid records: guided investigation (60 min; Evaluate)

ID: `database-foundations-m5-l1`

Objective: Judge two approaches to constraints and valid records against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Add a check that rejects a blank book title and test a spaces-only title. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Constraints and valid records: independent studio (90 min; Create)

ID: `database-foundations-m5-l2`

Objective: Design and deliver an original extension using constraints and valid records with explicit acceptance tests.

Activity: Add a check that rejects a blank book title and test a spaces-only title. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Transactions and recovery

Some changes must succeed together. A transaction groups them so a rollback can undo unfinished work. Think of transferring stock between shelves: subtracting without adding loses inventory. COMMIT accepts the changes; ROLLBACK cancels them. A backup is separate: it protects against loss beyond one unfinished transaction.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
BEGIN;
UPDATE books SET price=0 WHERE id=1;
ROLLBACK;
SELECT price FROM books WHERE id=1;
```

#### Transactions and recovery: guided investigation (60 min; Create)

ID: `database-foundations-m6-l1`

Objective: Design and deliver an original extension using transactions and recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Compare committed and rolled-back price changes and record both final values. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Transactions and recovery: independent studio (90 min; Evaluate)

ID: `database-foundations-m6-l2`

Objective: Judge two approaches to transactions and recovery against correctness, maintainability, and offline operation.

Activity: Compare committed and rolled-back price changes and record both final values. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Distributed data and consistency models

This database foundations module teaches you to compare replication, partitioning, consistency, availability, and conflict resolution using explicit failure scenarios. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Node A: version 4, value 12
Node B: version 5, value 10
Policy: reject blind overwrite; reconcile with domain rules.
```

#### Distributed data and consistency models: guided investigation (60 min; Create)

ID: `database-foundations-m7-l1`

Objective: Design and deliver an original extension using distributed data and consistency models with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Model a partition and recovery scenario, state the chosen consistency guarantee, and test conflict outcomes. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Distributed data and consistency models: independent studio (90 min; Evaluate)

ID: `database-foundations-m7-l2`

Objective: Judge two approaches to distributed data and consistency models against correctness, maintainability, and offline operation.

Activity: Model a partition and recovery scenario, state the chosen consistency guarantee, and test conflict outcomes. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Data governance, security, and lifecycle

This database foundations module teaches you to apply classification, least privilege, auditability, retention, backup, restoration, and responsible deletion. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
classification: internal
retention_days: 365
backup_tested: true
restore_point: 2026-01-15
```

#### Data governance, security, and lifecycle: guided investigation (60 min; Create)

ID: `database-foundations-m8-l1`

Objective: Design and deliver an original extension using data governance, security, and lifecycle with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a governance and disaster-recovery plan with access matrix, retention rules, restore drill, and audit evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Data governance, security, and lifecycle: independent studio (90 min; Evaluate)

ID: `database-foundations-m8-l2`

Objective: Judge two approaches to data governance, security, and lifecycle against correctness, maintainability, and offline operation.

Activity: Create a governance and disaster-recovery plan with access matrix, retention rules, restore drill, and audit evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This database foundations module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `database-foundations-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `database-foundations-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This database foundations module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `database-foundations-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `database-foundations-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This database foundations module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `database-foundations-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `database-foundations-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This database foundations module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `database-foundations-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `database-foundations-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This database foundations module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `database-foundations-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `database-foundations-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This database foundations module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `database-foundations-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `database-foundations-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This database foundations module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `database-foundations-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `database-foundations-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This database foundations module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `database-foundations-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `database-foundations-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Library data model (6 hours)

Design books, members, and loans for a fictional community library.

Acceptance conditions:

- Use stable keys and enforce references to existing books and members.
- Demonstrate valid loans and rejected missing references.
- Explain how returned loans remain as history.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Training enrollment model (12 hours)

Model students attending several courses without duplicating student details.

Acceptance conditions:

- Separate students, courses, and enrollments.
- Prevent the same student enrolling twice in the same course.
- Test renaming a course without breaking its enrollments.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Shop stock transfer (24 hours)

Model stock transfers between two fictional shelves with no lost units.

Acceptance conditions:

- Reject negative stock and invalid shelf references.
- Group subtraction and addition in one transaction.
- Force a failure and prove both shelf quantities remain unchanged.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## SQL from Zero

Prerequisites: database-foundations

Offline tools: Use the in-app SQL practice for read-only queries on fictional data. The worked scripts can also be run in a separately prepared SQLite tool. Each example starts with a fresh database; no internet or account is needed.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

SELECT describes the columns you want; FROM names their table. Start with one table before joining several. Selecting columns does not modify stored rows. ORDER BY makes result order explicit; without it, do not rely on whichever order the database happens to return.

Vocabulary:

- Database: organized information that a program can read and change.
- Record: one stored item, represented by a row or a document.
- Query: a request describing which information you want.
- Constraint: a rule that rejects invalid stored data.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT title AS book_name FROM books ORDER BY id;
```

- The alias book_name labels the result column without renaming the stored title field. Three titles appear in id order. SELECT * would request every column, making the output contract depend on later schema changes. Prefer the fields your caller actually uses.

Readiness check: What should you do before changing training data?

Answer: Predict the result and identify the target records.

Guided practice: Return id and title with clear result column names.

Hint: Use a fresh fictional fixture. Read the worked trace and change only the requested fields or query.

Reference solution:

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT id,title AS book_name FROM books ORDER BY id;
```

Expected result: The columns are id and book_name. The ordered rows are 1/Python, 2/Databases, and 3/Web.

### SELECT and column names

SELECT describes the columns you want; FROM names their table. Start with one table before joining several. Selecting columns does not modify stored rows. ORDER BY makes result order explicit; without it, do not rely on whichever order the database happens to return.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT title AS book_name FROM books ORDER BY id;
```

#### SELECT and column names: guided investigation (60 min; Remember)

ID: `sql-m1-l1`

Objective: Identify the key terms and syntax in select and column names without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Return id and title with clear result column names. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### SELECT and column names: independent studio (90 min; Understand)

ID: `sql-m1-l2`

Objective: Explain how select and column names changes program behavior using a traced example.

Activity: Return id and title with clear result column names. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Filtering and ordering

WHERE keeps rows whose condition is true. Compare prices as numbers, not text. ORDER BY can sort the filtered rows, and LIMIT can bound a preview. Filtering happens before the final limit, so a preview should state both its condition and its ordering.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT title,price FROM books WHERE price>=100 ORDER BY price DESC,id LIMIT 2;
```

#### Filtering and ordering: guided investigation (60 min; Understand)

ID: `sql-m2-l1`

Objective: Explain how filtering and ordering changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. List books costing exactly 100, ordered by title. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Filtering and ordering: independent studio (90 min; Apply)

ID: `sql-m2-l2`

Objective: Implement list books costing exactly 100, ordered by title.

Activity: List books costing exactly 100, ordered by title. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Totals and grouping

COUNT counts records and SUM adds numeric values. GROUP BY computes a result for each group rather than one grand total. WHERE filters individual rows before grouping; HAVING filters groups after aggregation. Decide which question you are asking before choosing either filter.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT price,COUNT(*) AS copies FROM books GROUP BY price ORDER BY price;
```

#### Totals and grouping: guided investigation (60 min; Apply)

ID: `sql-m3-l1`

Objective: Implement calculate total price and explain the difference from the book count.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Calculate total price and explain the difference from the book count. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Totals and grouping: independent studio (90 min; Analyze)

ID: `sql-m3-l2`

Objective: Locate a failing assumption in totals and grouping and isolate it with a minimal reproduction.

Activity: Calculate total price and explain the difference from the book count. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Joining related tables

A join combines rows according to a relationship. INNER JOIN keeps matching pairs; LEFT JOIN also keeps left-side rows without a match. A book with two loans can produce two result rows. That is expected relationship behavior, not automatically a duplicate-data bug.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
CREATE TABLE loans(id INTEGER PRIMARY KEY,book_id INTEGER);
INSERT INTO loans VALUES(1,1),(2,1);
SELECT b.title,COUNT(l.id) AS loans FROM books b LEFT JOIN loans l ON l.book_id=b.id GROUP BY b.id,b.title ORDER BY b.id;
```

#### Joining related tables: guided investigation (60 min; Analyze)

ID: `sql-m4-l1`

Objective: Locate a failing assumption in joining related tables and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Return only books with no loans using the left-join result. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Joining related tables: independent studio (90 min; Evaluate)

ID: `sql-m4-l2`

Objective: Judge two approaches to joining related tables against correctness, maintainability, and offline operation.

Activity: Return only books with no loans using the left-join result. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### NULL and missing information

NULL represents missing or unknown information; it is not zero or an empty string. Use IS NULL rather than = NULL. Comparisons with unknown values do not behave like ordinary true/false arithmetic. COALESCE can provide a display fallback, but it should not silently replace unknown business facts.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
ALTER TABLE books ADD COLUMN note TEXT;
SELECT title,COALESCE(note,'No note') AS note FROM books WHERE note IS NULL ORDER BY id;
```

#### NULL and missing information: guided investigation (60 min; Evaluate)

ID: `sql-m5-l1`

Objective: Judge two approaches to null and missing information against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Compare a NULL note and an empty note without treating them as equal. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### NULL and missing information: independent studio (90 min; Create)

ID: `sql-m5-l2`

Objective: Design and deliver an original extension using null and missing information with explicit acceptance tests.

Activity: Compare a NULL note and an empty note without treating them as equal. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Safe changes and parameters

UPDATE changes existing rows and DELETE removes them. A missing WHERE can affect the whole table. Preview the intended rows first and use a transaction for related changes. In application code bind user values as parameters instead of assembling them into SQL command text.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
BEGIN;
UPDATE books SET price=120 WHERE id=1;
COMMIT;
SELECT id,price FROM books ORDER BY id;
```

#### Safe changes and parameters: guided investigation (60 min; Create)

ID: `sql-m6-l1`

Objective: Design and deliver an original extension using safe changes and parameters with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Preview book 3, change its price in a transaction, and verify other rows. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Safe changes and parameters: independent studio (90 min; Evaluate)

ID: `sql-m6-l2`

Objective: Judge two approaches to safe changes and parameters against correctness, maintainability, and offline operation.

Activity: Preview book 3, change its price in a transaction, and verify other rows. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Window functions and analytical SQL

This SQL module teaches you to use partitions, frames, common table expressions, and execution plans to express auditable analytics. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
SELECT category, amount,
 SUM(amount) OVER (PARTITION BY category ORDER BY day) AS running_total
FROM expenses;
```

#### Window functions and analytical SQL: guided investigation (60 min; Create)

ID: `sql-m7-l1`

Objective: Design and deliver an original extension using window functions and analytical sql with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Write analytical queries using ranking and running totals, then verify ties, nulls, empty groups, and plan cost. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Window functions and analytical SQL: independent studio (90 min; Evaluate)

ID: `sql-m7-l2`

Objective: Judge two approaches to window functions and analytical sql against correctness, maintainability, and offline operation.

Activity: Write analytical queries using ranking and running totals, then verify ties, nulls, empty groups, and plan cost. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Transactions, isolation, and query optimization

This SQL module teaches you to reason about locks, isolation anomalies, indexing, statistics, plans, and safe schema evolution. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
BEGIN;
UPDATE stock SET quantity = quantity - 1 WHERE id = 7 AND quantity > 0;
-- require exactly one affected row
COMMIT;
```

#### Transactions, isolation, and query optimization: guided investigation (60 min; Create)

ID: `sql-m8-l1`

Objective: Design and deliver an original extension using transactions, isolation, and query optimization with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design a concurrent sale transaction, reproduce an anomaly, choose isolation and indexes, and justify the resulting plan. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Transactions, isolation, and query optimization: independent studio (90 min; Evaluate)

ID: `sql-m8-l2`

Objective: Judge two approaches to transactions, isolation, and query optimization against correctness, maintainability, and offline operation.

Activity: Design a concurrent sale transaction, reproduce an anomaly, choose isolation and indexes, and justify the resulting plan. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This SQL module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `sql-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `sql-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This SQL module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `sql-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `sql-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This SQL module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `sql-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `sql-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This SQL module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `sql-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `sql-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This SQL module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `sql-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `sql-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This SQL module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `sql-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `sql-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This SQL module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `sql-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `sql-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This SQL module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `sql-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `sql-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Library query workbook (6 hours)

Produce useful reports from fictional books and loans.

Acceptance conditions:

- Write ordered title and price filters.
- Include books with zero loans in a loan-count report.
- Explain every join and test duplicate matching rows.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: AFN expense reports (12 hours)

Report fictional household spending by category and date.

Acceptance conditions:

- Store amounts as integer AFN and reject negative expenses.
- Test empty periods and inclusive date boundaries.
- Reconcile grouped totals with the overall total.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Enrollment reporting desk (24 hours)

Answer course enrollment questions without losing courses that have no students.

Acceptance conditions:

- Use a left join to retain empty courses.
- Count enrollments without counting NULL placeholders.
- Document query inputs, expected rows, and ordering.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## SQLite for Offline Apps

Prerequisites: sql

Offline tools: Use the in-app SQL practice for read-only queries on fictional data. The worked scripts can also be run in a separately prepared SQLite tool. Each example starts with a fresh database; no internet or account is needed.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

SQLite runs inside a program rather than requiring a separate database server. A file database can survive restart; an in-memory database disappears when its connection closes. Choose deliberately. Lessons use fresh temporary data so an experiment cannot alter the learner progress database.

Vocabulary:

- Database: organized information that a program can read and change.
- Record: one stored item, represented by a row or a document.
- Query: a request describing which information you want.
- Constraint: a rule that rejects invalid stored data.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT COUNT(*) AS book_count FROM books;
```

- The fresh fixture contains three books, so the count is 3. Reopening a memory connection would start empty, while reopening a saved file should retain committed rows. Test those lifetimes separately; seeing data in one open connection is not evidence of restart persistence.

Readiness check: What should you do before changing training data?

Answer: Predict the result and identify the target records.

Guided practice: Count the books in the fresh fixture and explain what closing an in-memory connection does.

Hint: Use a fresh fictional fixture. Read the worked trace and change only the requested fields or query.

Reference solution:

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT COUNT(*) AS book_count FROM books;
```

Expected result: The fresh fixture contains three books, so the count is 3. Reopening a memory connection would start empty, while reopening a saved file should retain committed rows. Test those lifetimes separately; seeing data in one open connection is not evidence of restart persistence.

### Embedded storage and connections

SQLite runs inside a program rather than requiring a separate database server. A file database can survive restart; an in-memory database disappears when its connection closes. Choose deliberately. Lessons use fresh temporary data so an experiment cannot alter the learner progress database.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT COUNT(*) AS book_count FROM books;
```

#### Embedded storage and connections: guided investigation (60 min; Remember)

ID: `sqlite-m1-l1`

Objective: Identify the key terms and syntax in embedded storage and connections without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Compare a temporary database and a file database after closing their connections. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Embedded storage and connections: independent studio (90 min; Understand)

ID: `sqlite-m1-l2`

Objective: Explain how embedded storage and connections changes program behavior using a traced example.

Activity: Compare a temporary database and a file database after closing their connections. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Types and application constraints

SQLite type affinity is flexible; a declared column type is not a complete validation policy. Combine suitable types, NOT NULL, CHECK, and application validation. For integer AFN, reject fractional and negative inputs before storage. A database schema should express the data contract that the app actually needs.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
SELECT title,typeof(price) AS stored_type FROM books ORDER BY id;
```

#### Types and application constraints: guided investigation (60 min; Understand)

ID: `sqlite-m2-l1`

Objective: Explain how types and application constraints changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Require integer nonnegative prices and test text and fractional values. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Types and application constraints: independent studio (90 min; Apply)

ID: `sqlite-m2-l2`

Objective: Implement require integer nonnegative prices and test text and fractional values.

Activity: Require integer nonnegative prices and test text and fractional values. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Transactions and competing writers

SQLite allows only one writer at a time. Keep transactions short and avoid waiting for user input while holding a write transaction. A conditional update can enforce available stock at the point of change. Check affected rows; a completed command that changed zero rows is not a successful sale.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
BEGIN IMMEDIATE;
UPDATE books SET price=price-10 WHERE id=1 AND price>=10;
COMMIT;
SELECT price FROM books WHERE id=1;
```

#### Transactions and competing writers: guided investigation (60 min; Apply)

ID: `sqlite-m3-l1`

Objective: Implement test an update whose condition matches no rows and report that outcome accurately.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Test an update whose condition matches no rows and report that outcome accurately. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Transactions and competing writers: independent studio (90 min; Analyze)

ID: `sqlite-m3-l2`

Objective: Locate a failing assumption in transactions and competing writers and isolate it with a minimal reproduction.

Activity: Test an update whose condition matches no rows and report that outcome accurately. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Indexes and query plans

An index keeps an additional searchable structure. It can speed some reads but costs space and write work. Start from a real query and inspect its plan. A tiny table may be faster to scan; do not force an index merely because indexes sound advanced.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
CREATE INDEX books_price ON books(price);
EXPLAIN QUERY PLAN SELECT title FROM books WHERE price=100;
```

#### Indexes and query plans: guided investigation (60 min; Analyze)

ID: `sqlite-m4-l1`

Objective: Locate a failing assumption in indexes and query plans and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Compare query plans before and after a price index without changing query results. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Indexes and query plans: independent studio (90 min; Evaluate)

ID: `sqlite-m4-l2`

Objective: Judge two approaches to indexes and query plans against correctness, maintainability, and offline operation.

Activity: Compare query plans before and after a price index without changing query results. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Schema migrations

A new app release may need another column while retaining old records. A migration is an ordered transformation of an older schema. Version it and test it on real old fixtures, not only a fresh empty database. Never erase a user database as a shortcut for a failed migration.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
BEGIN;
ALTER TABLE books ADD COLUMN active INTEGER NOT NULL DEFAULT 1;
COMMIT;
SELECT id,active FROM books ORDER BY id;
```

#### Schema migrations: guided investigation (60 min; Evaluate)

ID: `sqlite-m5-l1`

Objective: Judge two approaches to schema migrations against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Migrate an old fixture and verify all titles, prices, and defaults after reopening. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Schema migrations: independent studio (90 min; Create)

ID: `sqlite-m5-l2`

Objective: Design and deliver an original extension using schema migrations with explicit acceptance tests.

Activity: Migrate an old fixture and verify all titles, prices, and defaults after reopening. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Backup verification and recovery

A backup is useful only if it restores correctly. Use a supported backup mechanism or export from a consistent snapshot. Copying one live database file while a journal or WAL is active may miss data. Validate restored structure and business totals in a separate training copy before replacing anything.

```text
CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, price INTEGER NOT NULL CHECK(price >= 0));
INSERT INTO books VALUES (1,'Python',100),(2,'Databases',150),(3,'Web',100);
PRAGMA integrity_check;
SELECT COUNT(*) AS rows,SUM(price) AS total FROM books;
```

#### Backup verification and recovery: guided investigation (60 min; Create)

ID: `sqlite-m6-l1`

Objective: Design and deliver an original extension using backup verification and recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Restore a training backup and compare its row count and total with the source. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Backup verification and recovery: independent studio (90 min; Evaluate)

ID: `sqlite-m6-l2`

Objective: Judge two approaches to backup verification and recovery against correctness, maintainability, and offline operation.

Activity: Restore a training backup and compare its row count and total with the source. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Query planning, indexes, and full-text search

This SQLite module teaches you to inspect query plans, design selective indexes, use FTS carefully, and measure write/read tradeoffs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
EXPLAIN QUERY PLAN
SELECT * FROM loans WHERE student_id = 7 ORDER BY loaned_at DESC;
```

#### Query planning, indexes, and full-text search: guided investigation (60 min; Create)

ID: `sqlite-m7-l1`

Objective: Design and deliver an original extension using query planning, indexes, and full-text search with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Optimize a measured search workload with indexes or FTS and retain before-and-after plans and timing evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Query planning, indexes, and full-text search: independent studio (90 min; Evaluate)

ID: `sqlite-m7-l2`

Objective: Judge two approaches to query planning, indexes, and full-text search against correctness, maintainability, and offline operation.

Activity: Optimize a measured search workload with indexes or FTS and retain before-and-after plans and timing evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### WAL, migrations, backup, and recovery

This SQLite module teaches you to configure concurrent readers, execute atomic migrations, verify integrity, and test online backup and corruption recovery. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
PRAGMA journal_mode=WAL;
PRAGMA integrity_check;
PRAGMA user_version;
```

#### WAL, migrations, backup, and recovery: guided investigation (60 min; Create)

ID: `sqlite-m8-l1`

Objective: Design and deliver an original extension using wal, migrations, backup, and recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a versioned migration and backup/restore drill that survives interruption without losing the previous valid database. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### WAL, migrations, backup, and recovery: independent studio (90 min; Evaluate)

ID: `sqlite-m8-l2`

Objective: Judge two approaches to wal, migrations, backup, and recovery against correctness, maintainability, and offline operation.

Activity: Build a versioned migration and backup/restore drill that survives interruption without losing the previous valid database. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This SQLite module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `sqlite-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `sqlite-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This SQLite module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `sqlite-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `sqlite-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This SQLite module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `sqlite-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `sqlite-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This SQLite module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `sqlite-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `sqlite-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This SQLite module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `sqlite-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `sqlite-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This SQLite module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `sqlite-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `sqlite-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This SQLite module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `sqlite-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `sqlite-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This SQLite module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `sqlite-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `sqlite-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Offline notes database (6 hours)

Persist fictional notes and restore them after restarting a local app.

Acceptance conditions:

- Validate titles and use parameterized writes.
- Test save failure without losing the previous note.
- Migrate a populated older schema.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Transactional stock ledger (12 hours)

Record a sale and stock reduction as one local operation.

Acceptance conditions:

- Prevent overselling with a conditional update.
- Roll back the stock change if sale insertion fails.
- Test two competing connections and a repeated request.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Migration and restore kit (24 hours)

Deliver fixtures and a repeatable upgrade-and-restore procedure.

Acceptance conditions:

- Keep versioned fixtures for each supported schema.
- Compare row counts and totals after restore.
- Document a failed migration without erasing the original.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## PostgreSQL Development

Prerequisites: sql

Offline tools: Lessons and practice traces are bundled offline. Executing PostgreSQL-specific scripts requires a separately installed local PostgreSQL server and psql. Use a disposable training database and a restricted local user. The in-app SQL practice runs SQLite, not PostgreSQL.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

PostgreSQL is a database server. A client such as psql connects to a particular database as a role. Schemas organize objects inside that database. A local server can work without internet, but it must already be installed and running. A connection failure is not corrected by rewriting a valid SELECT.

Vocabulary:

- Database: organized information that a program can read and change.
- Record: one stored item, represented by a row or a document.
- Query: a request describing which information you want.
- Constraint: a rule that rejects invalid stored data.

```text
SELECT current_database(),current_user;
CREATE TEMP TABLE books(id integer PRIMARY KEY,title text NOT NULL);
INSERT INTO books VALUES(1,'Python');
SELECT title FROM books;
```

- The first query identifies the actual connection, so its values depend on your setup. The temporary table belongs to this session. Inserting one book and selecting its title returns Python. Ending the session removes the temporary table; use a deliberate persistent schema for a real application.

Readiness check: What should you do before changing training data?

Answer: Predict the result and identify the target records.

Guided practice: Identify the connected database and create a disposable one-row table.

Hint: Use a fresh fictional fixture. Read the worked trace and change only the requested fields or query.

Reference solution:

```text
SELECT current_database(),current_user;
CREATE TEMP TABLE books(id integer PRIMARY KEY,title text NOT NULL);
INSERT INTO books VALUES(1,'Python');
SELECT title FROM books;
```

Expected result: The first query identifies the actual connection, so its values depend on your setup. The temporary table belongs to this session. Inserting one book and selecting its title returns Python. Ending the session removes the temporary table; use a deliberate persistent schema for a real application.

### Server, database, and schema

PostgreSQL is a database server. A client such as psql connects to a particular database as a role. Schemas organize objects inside that database. A local server can work without internet, but it must already be installed and running. A connection failure is not corrected by rewriting a valid SELECT.

```text
SELECT current_database(),current_user;
CREATE TEMP TABLE books(id integer PRIMARY KEY,title text NOT NULL);
INSERT INTO books VALUES(1,'Python');
SELECT title FROM books;
```

#### Server, database, and schema: guided investigation (60 min; Remember)

ID: `postgresql-m1-l1`

Objective: Identify the key terms and syntax in server, database, and schema without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Identify the connected database and create a disposable one-row table. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Server, database, and schema: independent studio (90 min; Understand)

ID: `postgresql-m1-l2`

Objective: Explain how server, database, and schema changes program behavior using a traced example.

Activity: Identify the connected database and create a disposable one-row table. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Typed schemas and constraints

Choose column types for meaning, not appearance. Integer quantities and numeric monetary values have different contracts. A generated identity creates identifiers; it does not validate other fields. Put required and nonnegative rules into constraints and handle their failures in the client without losing the draft.

```text
CREATE TEMP TABLE expenses(id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,amount numeric(12,2) NOT NULL CHECK(amount>=0));
INSERT INTO expenses(amount) VALUES(20.50) RETURNING id,amount;
```

#### Typed schemas and constraints: guided investigation (60 min; Understand)

ID: `postgresql-m2-l1`

Objective: Explain how typed schemas and constraints changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Insert a valid expense and demonstrate rejection of a negative one. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Typed schemas and constraints: independent studio (90 min; Apply)

ID: `postgresql-m2-l2`

Objective: Implement insert a valid expense and demonstrate rejection of a negative one.

Activity: Insert a valid expense and demonstrate rejection of a negative one. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Joins and window calculations

An aggregate can collapse rows into groups. A window calculation instead attaches a result while retaining individual rows. For a running total, specify ordering and the frame so the business meaning is clear. Unique ordering avoids ambiguity when several records share a date.

```text
SELECT id,amount,SUM(amount) OVER(ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total FROM (VALUES(1,10),(2,20),(3,5)) AS e(id,amount) ORDER BY id;
```

#### Joins and window calculations: guided investigation (60 min; Apply)

ID: `postgresql-m3-l1`

Objective: Implement add a fourth amount and predict its running total before execution.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Add a fourth amount and predict its running total before execution. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Joins and window calculations: independent studio (90 min; Analyze)

ID: `postgresql-m3-l2`

Objective: Locate a failing assumption in joins and window calculations and isolate it with a minimal reproduction.

Activity: Add a fourth amount and predict its running total before execution. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Transactions and row locks

Concurrent clients can read the same old quantity. A row lock can protect a read-then-write operation while its transaction is active. Locks must be released by commit or rollback. Keep the transaction short and plan how to report a conflict or retry; waiting indefinitely is not a usable interface.

```text
CREATE TEMP TABLE stock(id integer PRIMARY KEY,quantity integer CHECK(quantity>=0));
INSERT INTO stock VALUES(1,5);
BEGIN;
SELECT quantity FROM stock WHERE id=1 FOR UPDATE;
UPDATE stock SET quantity=quantity-2 WHERE id=1;
COMMIT;
SELECT quantity FROM stock;
```

#### Transactions and row locks: guided investigation (60 min; Analyze)

ID: `postgresql-m4-l1`

Objective: Locate a failing assumption in transactions and row locks and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Demonstrate lock waiting with two sessions on a disposable shared table. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Transactions and row locks: independent studio (90 min; Evaluate)

ID: `postgresql-m4-l2`

Objective: Judge two approaches to transactions and row locks against correctness, maintainability, and offline operation.

Activity: Demonstrate lock waiting with two sessions on a disposable shared table. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Indexes and EXPLAIN

EXPLAIN describes a planned execution strategy. EXPLAIN ANALYZE actually runs the statement and measures it, so it is not a harmless description for a modifying query. Begin with read-only queries and realistic fixtures. More indexes can slow inserts and updates, so compare both read and write costs.

```text
CREATE TEMP TABLE products(id integer PRIMARY KEY,price integer);
INSERT INTO products SELECT n,n%100 FROM generate_series(1,1000) AS n;
CREATE INDEX ON products(price);
ANALYZE products;
EXPLAIN SELECT id FROM products WHERE price=42;
```

#### Indexes and EXPLAIN: guided investigation (60 min; Evaluate)

ID: `postgresql-m5-l1`

Objective: Judge two approaches to indexes and explain against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Compare a selective query with and without an index on a training fixture. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Indexes and EXPLAIN: independent studio (90 min; Create)

ID: `postgresql-m5-l2`

Objective: Design and deliver an original extension using indexes and explain with explicit acceptance tests.

Activity: Compare a selective query with and without an index on a training fixture. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Roles, backup, and restore

A role controls permissions; an application should not connect with unrestricted administrative power. Backups need a tested restore procedure and protected local storage. Logical export and restore are separate tools, not SQL SELECT statements. Use fictional data and restore into a different training database before trusting the process.

```text
-- Shell commands, not SQL. Replace names with disposable training databases.
pg_dump -Fc training_source -f training.dump
pg_restore --no-owner --dbname=training_restore training.dump
```

#### Roles, backup, and restore: guided investigation (60 min; Create)

ID: `postgresql-m6-l1`

Objective: Design and deliver an original extension using roles, backup, and restore with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Restore a fictional database to a separate target and test a restricted reader role. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Roles, backup, and restore: independent studio (90 min; Evaluate)

ID: `postgresql-m6-l2`

Objective: Judge two approaches to roles, backup, and restore against correctness, maintainability, and offline operation.

Activity: Restore a fictional database to a separate target and test a restricted reader role. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Advanced indexing, plans, and partitioning

This PostgreSQL module teaches you to interpret EXPLAIN ANALYZE, choose index families, maintain statistics, and partition only for measured needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM loans WHERE returned_at IS NULL AND student_id = 7;
```

#### Advanced indexing, plans, and partitioning: guided investigation (60 min; Create)

ID: `postgresql-m7-l1`

Objective: Design and deliver an original extension using advanced indexing, plans, and partitioning with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Tune a representative workload using measured plans and justify indexes, statistics, and any partition boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Advanced indexing, plans, and partitioning: independent studio (90 min; Evaluate)

ID: `postgresql-m7-l2`

Objective: Judge two approaches to advanced indexing, plans, and partitioning against correctness, maintainability, and offline operation.

Activity: Tune a representative workload using measured plans and justify indexes, statistics, and any partition boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Concurrency, replication, and operations

This PostgreSQL module teaches you to apply MVCC isolation, advisory locks, roles, backup, point-in-time recovery, monitoring, and failover reasoning. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
BEGIN ISOLATION LEVEL SERIALIZABLE;
-- read invariant, apply change, retry serialization failures
COMMIT;
```

#### Concurrency, replication, and operations: guided investigation (60 min; Create)

ID: `postgresql-m8-l1`

Objective: Design and deliver an original extension using concurrency, replication, and operations with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design a retry-safe transaction and complete a role, backup, restore, monitoring, and simulated failover exercise. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Concurrency, replication, and operations: independent studio (90 min; Evaluate)

ID: `postgresql-m8-l2`

Objective: Judge two approaches to concurrency, replication, and operations against correctness, maintainability, and offline operation.

Activity: Design a retry-safe transaction and complete a role, backup, restore, monitoring, and simulated failover exercise. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This PostgreSQL module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `postgresql-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `postgresql-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This PostgreSQL module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `postgresql-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `postgresql-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This PostgreSQL module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `postgresql-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `postgresql-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This PostgreSQL module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `postgresql-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `postgresql-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This PostgreSQL module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `postgresql-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `postgresql-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This PostgreSQL module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `postgresql-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `postgresql-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This PostgreSQL module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `postgresql-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `postgresql-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This PostgreSQL module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `postgresql-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `postgresql-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Local enrollment service database (6 hours)

Enforce course capacity with two competing local clients.

Acceptance conditions:

- Use stable enrollment keys and constraints.
- Test the last available seat with two sessions.
- Explain rollback and retry behavior.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Expense reporting database (12 hours)

Produce grouped and running totals for fictional expenses.

Acceptance conditions:

- Use an exact numeric amount contract.
- Use deterministic window ordering.
- Compare query plans without changing totals.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Restore rehearsal (24 hours)

Deliver a local dump and verified restoration using restricted roles.

Acceptance conditions:

- Restore into a separate training database.
- Verify constraints and report totals after restore.
- Show that the reader cannot modify records.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

## MongoDB and Document Databases

Prerequisites: database-foundations

Offline tools: Lessons and document traces work offline. Executing these commands requires a separately provisioned local MongoDB server and mongosh. No Atlas account or cloud service is required. Use a disposable training database; the in-app SQLite editor cannot execute MongoDB commands.

### Start here: first guided lesson

This is the true starting point for this course. No vocabulary from this course is assumed. You will first learn what the example is for, the meaning of its four key terms, and how to follow it one step at a time. Read the prerequisite course shown in the catalog first when one is required.

A document stores named fields together, while a collection groups documents. Think of one library book with a title and a list of tags. MongoDB stores BSON documents; the shell uses JavaScript-like notation to express them. Flexible fields do not mean that a program can safely accept any shape.

Vocabulary:

- Database: organized information that a program can read and change.
- Record: one stored item, represented by a row or a document.
- Query: a request describing which information you want.
- Constraint: a rule that rejects invalid stored data.

```text
db.books.insertOne({_id:1,title:"Python",tags:["coding","beginner"]});
db.books.find({_id:1},{_id:0,title:1,tags:1});
```

- insertOne creates one document with a fixed training id. find matches that id and the projection hides _id while returning title and tags. Repeating the insert unchanged fails on the duplicate id. Use a fresh training collection rather than silently overwriting someone else's data.

Readiness check: What should you do before changing training data?

Answer: Predict the result and identify the target records.

Guided practice: Create a second book with a distinct id and find only its title.

Hint: Use a fresh fictional fixture. Read the worked trace and change only the requested fields or query.

Reference solution:

```text
db.books.insertOne({_id:2,title:"Databases",tags:["data"]});
db.books.find({_id:2},{_id:0,title:1});
```

Expected result: One result document contains title: Databases. The first book is unchanged.

### Documents and collections

A document stores named fields together, while a collection groups documents. Think of one library book with a title and a list of tags. MongoDB stores BSON documents; the shell uses JavaScript-like notation to express them. Flexible fields do not mean that a program can safely accept any shape.

```text
db.books.insertOne({_id:1,title:"Python",tags:["coding","beginner"]});
db.books.find({_id:1},{_id:0,title:1,tags:1});
```

#### Documents and collections: guided investigation (60 min; Remember)

ID: `mongodb-m1-l1`

Objective: Identify the key terms and syntax in documents and collections without consulting the example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a second book with a distinct id and find only its title. Compare the actual result with your prediction.

Assessment evidence: Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.

#### Documents and collections: independent studio (90 min; Understand)

ID: `mongodb-m1-l2`

Objective: Explain how documents and collections changes program behavior using a traced example.

Activity: Create a second book with a distinct id and find only its title. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

### Filters and targeted updates

A filter describes which documents match. An update operator changes selected fields rather than replacing the whole document. Match by a stable identity when editing one record. Check matched and modified counts; a command that matched nothing is not evidence that the intended book changed.

```text
db.items.insertOne({_id:1,name:"Notebook",stock:5});
db.items.updateOne({_id:1,stock:{$gte:2}},{$inc:{stock:-2}});
db.items.find({_id:1});
```

#### Filters and targeted updates: guided investigation (60 min; Understand)

ID: `mongodb-m2-l1`

Objective: Explain how filters and targeted updates changes program behavior using a traced example.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Attempt an oversized decrement and verify the stock remains unchanged. Compare the actual result with your prediction.

Assessment evidence: Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.

#### Filters and targeted updates: independent studio (90 min; Apply)

ID: `mongodb-m2-l2`

Objective: Implement attempt an oversized decrement and verify the stock remains unchanged.

Activity: Attempt an oversized decrement and verify the stock remains unchanged. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

### Embedding and references

Embed data read together when its size and lifetime fit the parent. Use references for independent or growing records. Copying a student name into every enrollment can make updates inconsistent. There is no universal rule that every relationship should be embedded; start from access patterns and update behavior.

```text
db.courses.insertOne({_id:1,title:"SQL",lessons:[{title:"Tables"},{title:"Queries"}]});
db.courses.find({_id:1},{lessons:1,_id:0});
```

#### Embedding and references: guided investigation (60 min; Apply)

ID: `mongodb-m3-l1`

Objective: Implement compare embedded lesson summaries with referenced full lesson documents.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Compare embedded lesson summaries with referenced full lesson documents. Compare the actual result with your prediction.

Assessment evidence: Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.

#### Embedding and references: independent studio (90 min; Analyze)

ID: `mongodb-m3-l2`

Objective: Locate a failing assumption in embedding and references and isolate it with a minimal reproduction.

Activity: Compare embedded lesson summaries with referenced full lesson documents. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

### Aggregation pipelines

A pipeline passes documents through ordered stages. Match narrows the input, group produces summaries, and sort orders the result. Each stage changes what the next stage receives. Write down an intermediate result after each stage instead of guessing from the final pipeline alone.

```text
db.expenses.insertMany([{category:"books",amount:20},{category:"books",amount:10},{category:"travel",amount:5}]);
db.expenses.aggregate([{$group:{_id:"$category",total:{$sum:"$amount"}}},{$sort:{_id:1}}]);
```

#### Aggregation pipelines: guided investigation (60 min; Analyze)

ID: `mongodb-m4-l1`

Objective: Locate a failing assumption in aggregation pipelines and isolate it with a minimal reproduction.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Add a category filter before grouping and trace which records remain. Compare the actual result with your prediction.

Assessment evidence: Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.

#### Aggregation pipelines: independent studio (90 min; Evaluate)

ID: `mongodb-m4-l2`

Objective: Judge two approaches to aggregation pipelines against correctness, maintainability, and offline operation.

Activity: Add a category filter before grouping and trace which records remain. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and indexes

Flexible documents still need a contract. Validation can require fields and types. A unique index rejects duplicate key values, while an ordinary index only helps access. Existing invalid or duplicate data can prevent adding a new rule; inspect a training copy before changing a real collection.

```text
db.members.createIndex({studentId:1},{unique:true});
db.members.insertOne({studentId:"S1",name:"Amina"});
db.members.find({studentId:"S1"});
```

#### Validation and indexes: guided investigation (60 min; Evaluate)

ID: `mongodb-m5-l1`

Objective: Judge two approaches to validation and indexes against correctness, maintainability, and offline operation.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Test duplicate identities and missing required fields as separate failures. Compare the actual result with your prediction.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

#### Validation and indexes: independent studio (90 min; Create)

ID: `mongodb-m5-l2`

Objective: Design and deliver an original extension using validation and indexes with explicit acceptance tests.

Activity: Test duplicate identities and missing required fields as separate failures. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

### Atomicity and local backup

A single-document update is atomic. Changes across several documents need a different design or a supported transaction deployment. A standalone server does not support multi-document transactions; a local replica set can be provisioned for that lesson. Backups still need restore testing, even when individual writes are atomic.

```text
// Shell commands, not mongosh JavaScript; training databases only.
mongodump --db training_source --out training_backup
mongorestore --nsFrom="training_source.*" --nsTo="training_restore.*" training_backup
```

#### Atomicity and local backup: guided investigation (60 min; Create)

ID: `mongodb-m6-l1`

Objective: Design and deliver an original extension using atomicity and local backup with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Restore fictional documents to a separate database and explain consistency limits. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Atomicity and local backup: independent studio (90 min; Evaluate)

ID: `mongodb-m6-l2`

Objective: Judge two approaches to atomicity and local backup against correctness, maintainability, and offline operation.

Activity: Restore fictional documents to a separate database and explain consistency limits. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Aggregation and schema evolution

This MongoDB module teaches you to design bounded pipelines, indexes, validation, denormalization policy, and compatible document migrations. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
db.loans.aggregate([
 {$match:{returned:false}},
 {$group:{_id:"$bookId", total:{$sum:1}}}
])
```

#### Aggregation and schema evolution: guided investigation (60 min; Create)

ID: `mongodb-m7-l1`

Objective: Design and deliver an original extension using aggregation and schema evolution with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build and explain an indexed aggregation, then migrate mixed document versions without breaking old readers. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Aggregation and schema evolution: independent studio (90 min; Evaluate)

ID: `mongodb-m7-l2`

Objective: Judge two approaches to aggregation and schema evolution against correctness, maintainability, and offline operation.

Activity: Build and explain an indexed aggregation, then migrate mixed document versions without breaking old readers. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Transactions, replication, and operations

This MongoDB module teaches you to choose transaction boundaries, read/write concerns, shard keys, backup, restore, and observable failure handling. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
session.withTransaction(async () => {
  // update loan and inventory with retry-safe identifiers
});
```

#### Transactions, replication, and operations: guided investigation (60 min; Create)

ID: `mongodb-m8-l1`

Objective: Design and deliver an original extension using transactions, replication, and operations with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Design a retry-safe multi-document workflow and document replica failure, recovery, backup, restore, and consistency evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Transactions, replication, and operations: independent studio (90 min; Evaluate)

ID: `mongodb-m8-l2`

Objective: Judge two approaches to transactions, replication, and operations against correctness, maintainability, and offline operation.

Activity: Design a retry-safe multi-document workflow and document replica failure, recovery, backup, restore, and consistency evidence. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Requirements and domain discovery

This MongoDB module teaches you to turn a learner or client problem into user stories, a shared vocabulary, scope boundaries, and testable acceptance examples. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
User: a learner with an older device
Need: finish work without internet
Acceptance: saved work survives restart
Out of scope: cloud accounts
```

#### Requirements and domain discovery: guided investigation (60 min; Create)

ID: `mongodb-m9-l1`

Objective: Design and deliver an original extension using requirements and domain discovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Requirements and domain discovery: independent studio (90 min; Evaluate)

ID: `mongodb-m9-l2`

Objective: Judge two approaches to requirements and domain discovery against correctness, maintainability, and offline operation.

Activity: Interview a fictional learner, write three user stories and acceptance examples, then reject one attractive feature that violates the offline scope. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Models, interfaces, and contracts

This MongoDB module teaches you to model domain rules separately from screens and frameworks, define small interfaces, and state preconditions, results, and errors. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Input contract: non-empty learner_id
Rule: progress can only move forward
Result: saved progress or a specific error
Adapter: local file or database
```

#### Models, interfaces, and contracts: guided investigation (60 min; Create)

ID: `mongodb-m10-l1`

Objective: Design and deliver an original extension using models, interfaces, and contracts with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Models, interfaces, and contracts: independent studio (90 min; Evaluate)

ID: `mongodb-m10-l2`

Objective: Judge two approaches to models, interfaces, and contracts against correctness, maintainability, and offline operation.

Activity: Draw the domain, application, storage, and interface boundaries for a small attendance feature; define one contract at every boundary. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Validation and failure recovery

This MongoDB module teaches you to validate at trust boundaries, preserve the last valid state, use atomic changes, and design recovery users can understand. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
normal: 3 valid records -> save
edge: empty list -> valid empty result
invalid: negative score -> reject
interruption: old data remains readable
```

#### Validation and failure recovery: guided investigation (60 min; Create)

ID: `mongodb-m11-l1`

Objective: Design and deliver an original extension using validation and failure recovery with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Validation and failure recovery: independent studio (90 min; Evaluate)

ID: `mongodb-m11-l2`

Objective: Judge two approaches to validation and failure recovery against correctness, maintainability, and offline operation.

Activity: Build a validation table for normal, empty, boundary, malformed, duplicate, and interrupted operations, then implement or simulate safe recovery. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Testing strategy and quality gates

This MongoDB module teaches you to combine focused unit tests, boundary tests, integration checks, and user-visible acceptance evidence without mirroring the implementation. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Given saved progress at lesson 2
When the app restarts offline
Then lesson 2 remains complete
And lesson 3 is the next available step
```

#### Testing strategy and quality gates: guided investigation (60 min; Create)

ID: `mongodb-m12-l1`

Objective: Design and deliver an original extension using testing strategy and quality gates with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Testing strategy and quality gates: independent studio (90 min; Evaluate)

ID: `mongodb-m12-l2`

Objective: Judge two approaches to testing strategy and quality gates against correctness, maintainability, and offline operation.

Activity: Create a test pyramid for one real feature, write at least five meaningful cases, and explain which failure each test would catch. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Architecture and dependency boundaries

This MongoDB module teaches you to apply separation of concerns, dependency inversion, cohesive modules, and architecture decision records to keep change affordable. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
presentation -> application -> domain
data implements domain ports
platform code stays behind adapters
Decision: local storage is the source of truth
```

#### Architecture and dependency boundaries: guided investigation (60 min; Create)

ID: `mongodb-m13-l1`

Objective: Design and deliver an original extension using architecture and dependency boundaries with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Architecture and dependency boundaries: independent studio (90 min; Evaluate)

ID: `mongodb-m13-l2`

Objective: Judge two approaches to architecture and dependency boundaries against correctness, maintainability, and offline operation.

Activity: Refactor or redesign one feature so its business rule can be tested without its UI, database, framework, or network. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Security, privacy, and inclusive access

This MongoDB module teaches you to threat-model assets and trust boundaries, minimize data and permissions, and include keyboard, screen-reader, contrast, language, and large-text needs. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Asset: learner progress
Threat: unintended disclosure
Control: local minimum data
Access check: keyboard + 200% text
Recovery: explicit local backup
```

#### Security, privacy, and inclusive access: guided investigation (60 min; Create)

ID: `mongodb-m14-l1`

Objective: Design and deliver an original extension using security, privacy, and inclusive access with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Security, privacy, and inclusive access: independent studio (90 min; Evaluate)

ID: `mongodb-m14-l2`

Objective: Judge two approaches to security, privacy, and inclusive access against correctness, maintainability, and offline operation.

Activity: Produce a compact threat and accessibility review, repair the two highest-impact findings, and record evidence with fictional data. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Performance and resource budgets

This MongoDB module teaches you to measure startup, responsiveness, memory, storage, and expensive operations before optimizing for realistic low-resource devices. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
startup budget: 2 seconds
interaction budget: 100 ms
storage budget: 50 MB
offline check: airplane mode from first launch
```

#### Performance and resource budgets: guided investigation (60 min; Create)

ID: `mongodb-m15-l1`

Objective: Design and deliver an original extension using performance and resource budgets with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Performance and resource budgets: independent studio (90 min; Evaluate)

ID: `mongodb-m15-l2`

Objective: Judge two approaches to performance and resource budgets against correctness, maintainability, and offline operation.

Activity: Choose three measurable budgets, capture a baseline, improve one proven bottleneck, and verify that behavior and accessibility still pass. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Capstone delivery and maintenance

This MongoDB module teaches you to plan incremental delivery, version data safely, document offline setup, review risks, and maintain the product after its first release. Use the idea in the course project or in a small offline records feature. Read the example line by line and identify its input, rule, result, and possible failure. Then test a normal case, an empty or boundary case, and an invalid case. Record the actual results instead of claiming that the design works.

Hint: begin with one input and one expected result. Make that case work, add the failure case, and only then extend the design. Keep the smallest solution you can explain and reproduce.

```text
Release evidence:
- acceptance checks pass
- migration and rollback tested
- offline install documented
- known limits published
- next improvement prioritized
```

#### Capstone delivery and maintenance: guided investigation (60 min; Create)

ID: `mongodb-m16-l1`

Objective: Design and deliver an original extension using capstone delivery and maintenance with explicit acceptance tests.

Activity: Read the explanation. Trace the worked example on paper, record each state change, then run it using the course toolchain. Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Compare the actual result with your prediction.

Assessment evidence: Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.

#### Capstone delivery and maintenance: independent studio (90 min; Evaluate)

ID: `mongodb-m16-l2`

Objective: Judge two approaches to capstone delivery and maintenance against correctness, maintainability, and offline operation.

Activity: Deliver a course-specific capstone increment with requirements, architecture decision, implementation evidence, tests, usability review, migration or rollback plan, and a short demonstration. Use fictional data, explain each important step in your own words, test normal and failure paths, and record one improvement you would make after feedback. Change one requirement, implement your own solution, then deliberately introduce an edge-case failure. Diagnose and repair it without copying the worked example.

Assessment evidence: Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.

### Project: Learning resource catalog (6 hours)

Store fictional learning resources with tags and searchable titles.

Acceptance conditions:

- Validate required fields and stable identifiers.
- Compare embedding and referencing for lesson metadata.
- Demonstrate tag filters and deterministic result ordering.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Document expense reports (12 hours)

Aggregate fictional expenses and keep invalid records out.

Acceptance conditions:

- Validate amount types and nonnegative values.
- Trace every stage of a grouped report.
- Test empty categories and repeated fixture setup.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.

### Project: Local document recovery lab (24 hours)

Practice consistent local backup and restore with fictional collections.

Acceptance conditions:

- Restore to a separate target namespace.
- Compare document counts and report totals.
- Document standalone and replica-set transaction differences.

Milestones:

- Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.
- Design: sketch components and data flow; justify one tradeoff in an architecture decision record.
- Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.
- Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.
- Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.
