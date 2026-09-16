# Offline learning adventure — version 2.1

## Inspiration and adaptation

The reference patterns are short, focused lessons and hands-on practice from [Sololearn's explanation of its teaching approach](https://www.sololearn.com/en/how-sololearn-teaches), and interactive lessons/coding challenges from [Programming Hub](https://programminghub.io/). Reviewed 13 September 2026. The official Sololearn search result was available; a direct fetch returned HTTP 403. These references informed the learning flow, not a pixel-for-pixel copy or an effectiveness claim.

Marifat keeps its own supplied logo and navy/teal identity. Its course entry is now a mission map, with lesson stops, a next-challenge marker, visible solved counts, completed stars, XP, levels, badges, and animated success feedback. Python opens the seven playable foundation lessons directly. Other courses use a short explanation/example/task workshop. Long syllabus material and advanced tool setup remain reachable through a clearly named reference library.

## Reward contract

- 10 XP per unique correctly solved foundation exercise.
- 20 bonus XP when all exercises in a foundation lesson are solved.
- Level = 1 + floor(XP / 100), with progress toward the next hundred. After every available foundation mission is complete, a completion message replaces the next-level target.
- First spark: 1 solved challenge. Problem solver: 5 solved challenges. Lesson champion: 1 completed lesson. Python explorer: all 7 foundation lessons completed.
- Rewards derive from persisted solved IDs and known lesson exercise sets. No extra XP counter, database migration, clock dependence or reward duplication on replay.
- Wrong answers do not remove points or access. Failed writes do not award points. Learners may freely revisit any lesson.
- No hearts, paid retries, artificial wait timers, online leaderboard, or invented daily streak is implemented. Existing backups reproduce the same rewards.

Automatic XP currently covers the 21 graded Python foundation exercises. Workshop plans, self-reported portfolio work and reference projects do not award automatic XP. These points represent practice progress, not a verified credential or proof of mastery. Editing a local backup is not prevented cryptographically.

## Validation

Reward tests cover thresholds, lesson bonuses, unknown IDs, concurrent replay, wrong answers, persistence reopening, and failed saves. Course-map widget checks render Dari and Pashto in dark desktop layouts and open a playable lesson from the map. Existing phone and larger-text checks remain in the suite. Completion markers use actual saved results.

Native-speaker review and a study with beginner students remain pending. Full language-runtime and curriculum coverage remains as documented in IMPLEMENTATION_STATUS.md.
