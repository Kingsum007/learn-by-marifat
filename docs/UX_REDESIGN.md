# Marifat UX redesign — version 2.0

## Learner journey

Home now offers one prominent action: start or continue the next Python foundation lesson. Native language choices are visible before starting. The navigation has three destinations: Home, Courses, Practice. Settings remain reachable from the top bar. A plain-language three-part introduction explains what the learner will do.

Foundation lessons use three short views: understand the idea, see an example, try an activity. The next action stays at the bottom of the screen. Returning to a partially practiced lesson opens its practice view, using saved exercise results. Reading tabs do not award completion. The learner can revisit an explanation or example at any time.

Projects reveal their walkthrough in short expandable sections. Bloom metadata remains in the curriculum/domain for instructional design and validation, but learner-facing level badges and terminology were removed. No academic theory labels are needed to use the app. Course entry puts the first lesson before optional time/tool details; requirements remain available and advanced-tool needs are still disclosed.

## Brand and accessibility

The supplied Marifat PNG is bundled unchanged, with navy/teal surfaces and consistent cards and controls. It is loaded locally without an image service. The former mountain identity was removed. Dari/Pashto use bundled Arabic typography and RTL layout, while code blocks/editors and inline technical fragments preserve LTR order. Phone and desktop layouts, larger text, translated screens and the supplied logo are covered by widget/visual checks.

## Engineering changes

- Course search includes translated course, module, and project names as well as original text.
- The code lab now has a dedicated route. PopScope protects unsaved edits with Keep editing, Discard changes, and Save and leave. A failed save leaves the editor open with its source intact.
- Existing controller persistence, stable exercise/project IDs, backup format and stored learner data remain compatible. No destructive migration is introduced.
- Resume actions use persisted solved exercises; a new tab or a read explanation cannot mark an exercise complete.
- Translation inventory checks continue to cover newly authored interface prose. User code, filenames and the original logo remain unchanged.

## Verification and remaining scope

This is an implemented redesign, not a claim of a completed usability study. Test it with Afghan students who have never used a programming tool, especially reading comprehension, finding help, recovering from errors, and understanding save/backup behavior. Native-speaker review remains pending.

The redesign does not add missing compilers or complete the remaining curriculum/reference projects. The bounded Python interpreter and existing offline execution limits still apply. Android device/release acceptance remains unverified. See IMPLEMENTATION_STATUS.md for content and runtime coverage.
