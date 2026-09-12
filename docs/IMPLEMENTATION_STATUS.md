# Version 2.0 implementation status

The Marifat redesign introduces a simpler home, three navigation destinations, short foundation lesson views, and progressive project guidance; see UX_REDESIGN.md.

The learner app reads bundled content and saves work without a network. This is an education implementation in progress, not a guarantee of mastery or full IDE support.

| Capability | Verified implementation | Remaining work |
|---|---|---|
| Curriculum | 15 courses, 90 module explanations/examples, 180 Bloom-aligned session plans | Turn every session into a full scaffolded beginner lesson, reviewed by educators |
| Beginner teaching | 15 entry lessons with vocabulary, prediction checks, trace, task, hint, and small solution; 7 interactive Python lessons / 21 exercises | Complete advanced progression and prerequisite diagnostics |
| Projects | 45 briefs with requirements, milestones, rubric, editable source and notes; 3 complete Python CLI references, 15 regression tests, and 3 runnable core exercises | Remaining 42 reference applications; embedded full-runtime execution; broader project-specific checks |
| In-app work | 225 local workspaces, four files each, explicit save, dirty-state guard, backup/restore | Full project trees, export to SDK project folders, HTML preview, embedded supported-language engines |
| Execution | Real bounded Python teaching interpreter | Full CPython and other language/framework runtimes; native iOS compilation still needs Apple tools |
| Localization | Inventoried prose in English/Dari/Pashto, RTL controls, original code, local font; Pashto adaptive-control delegate | Native-speaker and accessibility review; OS dialogs follow OS language |
| Assessment | Python output grading and choice/order checks; project rubrics are self-assessment | Reviewed mastery assessments and instructional effectiveness study |
| Platforms | Windows release build | Android release/device acceptance and iOS build testing |

## Persistence contract

Backup payload version 3 retains the stable kohi-backup marker and accepts versions 1 and 2. Version 2 entries without files restore with empty workspaces. SQLite table schema stays at version 1. Every change validates and commits before visible state is updated. Workspace writes preserve evidence; evidence writes preserve workspace files. Limits: 16 MB UTF-8 backup, four files per workspace, 12,000 characters per file, flat filenames up to 80 ASCII characters. Invalid writes leave the previous saved aggregate unchanged.

## Content authoring and verification

Run `python tool/build_project_guides.py`, `python tool/build_curriculum.py`, `dart run tool/export_foundations.dart`, `dart run tool/translation_audit.dart`, then `python tool/build_translations.py`. The last command fails if inventoried prose lacks Dari or Pashto text. The Dart localization test checks nonempty translations and placeholder parity. Technical IDs, source code, learner input and license notices are intentionally outside translation scope. Initial project seeds are explicitly labelled teaching examples, never finished projects.

Translation sources: tool/translation_content.py and tool/translation_ui.py. Beginner guides: tool/beginner_lessons.py. Generated dictionaries ship in the binary; no network translation service is used.
