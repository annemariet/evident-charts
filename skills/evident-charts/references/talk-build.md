# Talk build mode (Altair, one question per step)

Use when the user wants a **step-by-step Altair build** like the Compute! talk flow: **one question per turn**, wait for the answer, then show only the smallest code delta for that grammar step. This does not replace the default workflow; it layers the interrogation style from a fixed step order onto evident-charts defaults.

## When to switch

- User asks to build a chart step by step, be grilled before each encoding choice, or follow a grammar-of-graphics walkthrough in Altair.
- A separate `build-my-chart` skill may exist in another repo; this mode keeps **one stack** (evident-charts rules + checks) without copying that skill's text.

## Rules (talk mode only)

- **One step per turn.** Ask the step question, stop until the user answers. No full-spec dump.
- **Read the data yourself** after step 1; report rows, types, missingness, and distinct counts.
- **Brief first:** one line `Takeaway | Audience | Destination` (default workflow step 2), but split intent across step 0 questions: explore vs communicate, message, audience, comparison (at most one question each turn).
- **Fixed step order** (skip with one line when N/A): Data → Transform → Views plan → Mark → Encodings → Overlap → Field details → Scales/guides → Facet → Map → Wiring → Text → Check.
- **After each answer:** reply with: step name, grammar element, smallest Altair snippet, one cited rule from this skill (ID or chart default), user's decision, next step question.
- **Stack:** Altair 6.x + `assets/themes/evident_vegalite.json` when theming; export PNG for checks. Run `check_svg.py` on exported SVG when Chrome is available.
- **Step 13 (Check):** run automated checks and name one misread risk; do not skip integrity analysis because the walk was slow.

## Step questions (templates)

Adapt field names to the dataset. Do not read these verbatim.

| Step | Ask |
| --- | --- |
| 0 | Explore or communicate? Then message, audience, main comparison (one question per turn). |
| 1 | Dataset path or table; which columns matter? |
| 2 | Counts, means, bins, filters, or shares—and computed where? |
| 3 | One view or several; how linked? |
| 4 | Which mark supports the comparison from step 0? |
| 5 | Which channel for each field (x, y, color, …)? |
| 6 | Stack, normalize, dodge, or opacity? |
| 7 | Category order, number format, time unit? |
| 8 | Zero baseline, colour domain/scheme, legend needed? |
| 9 | Facet or repeat? |
| 10 | Projection (maps only). |
| 11 | Layer, concat, brush, or shared scales? |
| 12 | Title states the takeaway; subtitle has units and source publisher. |
| 13 | What could a careless reader misread? Run checks. |

## Finish

- One final code block, recap of user decisions only, list checks run/failed/skipped, optional suggestion to critique a finished chart with `references/critique.md`.