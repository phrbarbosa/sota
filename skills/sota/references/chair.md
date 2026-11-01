# Chair protocol

The Chair is the strongest reasoner available in the session and the only participant who sees everything. The quality of a council is bottlenecked by its aggregation step: diverse seats only help when the judge can tell a good finding from a plausible-sounding one. Everything below exists to make that judgment less noisy.

## 1. Triage (Phase 2)

Work through these in order. Do not skip ahead to the verdict; forming a holistic impression early is the single most common way a reviewer's judgment gets corrupted.

### 1.0 Keep working notes separate from the report
The Chair produces two things: private **working notes** (per-report summaries, the registry draft, the dimension table before the verdict, contention rulings) and the **report**. Keep the notes in a scratch file or a clearly separate block; only the registry, the dimension table and process notes are carried into the report's appendix. The notes exist to discipline your reading order, not to be published.

### 1.1 Anonymize and shuffle
The seat reports arrive unlabeled by design (the output contract forbids the seat naming itself). Assign them letters A–E in a random order and judge them under those letters; keep the letter→seat mapping aside and consult it only when a finding's method matters (e.g. "was this checked by the seat with tools?"). Judge the reports, not the seats' reputations. (This reduces position and reputation effects when the order is truly shuffled. It does not stop a same-model Chair favoring text like its own.)

### 1.2 Read one report at a time, fully
Before opening the next report, write a 3-line summary of the one you just read in your working notes: its top finding, its weakest finding, its confidence. This forces each report to be processed on its own evidence before being blended.

### 1.3 Build the finding registry
One row per distinct finding. Merge duplicates across seats; keep every evidence anchor.

| ID | Finding | Seats | Class | Severity | Status | Evidence | Fix |
|----|---------|-------|-------|----------|--------|----------|-----|

- **Class**: `convergent` (2+ seats, independently), `contested`, `unique`.
- **Severity**, judged on the artifact **as written** (ask "if nobody touched it, what happens?"): `blocker` (objective fails / unacceptable harm), `major` (objective materially degraded or significant risk created), `minor` (real but contained), `nit` (polish). Ease of fixing never changes the label; it changes the verdict (§4). When seats dispute severity over ease of fixing, rule on it yourself. Disputes about consequence go to contention.
- **Status**: `verified` (a seat or you actually checked), `plausible` (coherent, unchecked), `speculative` (no anchor).

### 1.4 Prune and downgrade
- Open every evidence anchor on blockers and majors. If the anchor does not say what the finding claims, downgrade to `speculative` and note "anchor failed".
- A `speculative` blocker is a contradiction: either verify it in Phase 4 or demote it.
- If two or more seats produced near-identical findings *and* near-identical phrasing, the run partially collapsed into one perspective. Record it in process notes; weight those findings as one voice, not two.

### 1.5 Decide what goes to contention
Send to Phase 3: all `contested` items of severity ≥ major, and all `unique` blockers. Cap at five; pick by stakes. Everything else goes straight to Phase 4 verification or to synthesis.

## 2. Judging contention (Phase 3)

For each exchange:
1. List the evidence each side produced that was **new** relative to the registry.
2. The position supported by the stronger new evidence wins. Rhetoric, confidence and length are not evidence.
3. If neither side produced evidence, the finding stays `plausible` at its original severity and goes to the dissent register.
4. Record the outcome in one line: "F3 upheld as major: challenger could not show the retry path handles 5xx; advocate reproduced with test X."

A seat that changed position is credible only if it named the evidence that moved it.

## 3. Dimension-by-dimension assessment (Phase 5, before the verdict)

Score each dimension separately and write one sentence of justification per dimension **before** thinking about the overall verdict. Use the discrete scale; never numbers.

| Dimension | Question | Scale |
|---|---|---|
| Correctness | Is it true / does it work? | sound · mostly sound · unsound |
| Fit to objective | Does it achieve what the brief says it is for? | strong · partial · weak · wrong target |
| Risk | What is the worst plausible outcome, and how reversible? | contained · material · severe |
| Cost & simplicity | Is the effort proportional; is there a simpler path? | lean · acceptable · bloated |
| Execution quality | Craft: clarity, structure, maintainability, polish | high · adequate · poor |
| Stakeholder acceptability | Would the affected people accept it (incl. ethics/legal)? | yes · with reservations · no |
| Outside-view alignment | Does it respect what the reference class teaches? | aligned · partially · ignores |

Only after the table is complete, form the holistic judgment. Intuition is allowed at this point — it is just not allowed to come first.

## 4. Verdict rules

A decision is something a person will do or not do (a plan, a change, an option). Everything else (a text, a claim, an analysis) is a non-decision. Take the first row that applies, from the top.

| Situation | Decision | Non-decision |
|---|---|---|
| Objective wrong, corrected objective exists | `NOT YET`, reframed | `NEEDS REWORK`, reframed |
| Objective unachievable or harmful | `NO-GO` | `NEEDS REWORK` |
| Verified blocker, fix clear and within the current shape | `NOT YET` | `NEEDS REWORK`, fix named |
| Verified blocker needing a different approach | `NO-GO` | `NEEDS REWORK` |
| Plausible blocker, one-way door | `NOT YET` | `NEEDS REWORK` |
| Plausible blocker, two-way door | `GO WITH CHANGES`, its test first | `SOUND WITH FIXES`, its test first |
| Majors fixable within scope | `GO WITH CHANGES` | `SOUND WITH FIXES` |
| Majors not fixable within scope | `NOT YET` | `NEEDS REWORK` |
| Minors or none | `GO` | `SOUND` |

**Confidence** is stated in words with a reason: "high — the Verifier reproduced the failure by execution" or "low — core claim is unverifiable without production data". Do not report percentages unless you can say what they are calibrated against. Confidence may cite only execution, opened external sources or a second model family. Agreement alone cannot lift it above medium when all seats share a family.

## 5. Ranking improvements

Rank by impact on the stated objective divided by effort. Tie-break toward the smaller, more reversible change. Prefer the fix that changes words or configuration over the one that changes structure, unless the structure is the finding. Group as:

1. **Must** (blockers/majors) — numbered, each with evidence and the concrete fix.
2. **Should** (high impact/effort ratio) — numbered, with effort.
3. **Could** — a short list; do not pad.

If the Steelman seat's "protect list" conflicts with a proposed fix, surface the conflict explicitly instead of silently choosing.

## 6. The curated version

The user asked for the thing to be *curated*, not merely judged. Deliver:
- Small artifact (≤ ~2 pages / ≤ ~200 lines / a single prompt or plan): the full improved version, with a short changelog mapping each change to a finding ID.
- Large artifact: a patch list (file/section → change → finding ID), plus full rewrites of the two or three passages that matter most.
- Decisions between options: the recommended option, the conditions under which the other option wins, and the cheapest experiment to tell them apart.

Do not alter what the protect list says to protect without flagging it.

## 7. Dissent register, falsifiers, pre-mortem

- **Dissent**: every contested item that stayed unresolved, each side in its strongest one-sentence form. Resist the urge to resolve them by fiat.
- **Falsifiers**: the 2-3 observations that would flip the verdict (both directions), and the cheapest way to obtain each.
- **Pre-mortem line**: a single sentence — if this fails, the most likely reason is ___. Take it from the Red Team's post-mortems, filtered by what survived verification.

## 8. Calibration language

Use these consistently so the user learns to read the council:

- "verified" — someone ran the check; evidence is attached.
- "plausible" — coherent and unrefuted, but unchecked.
- "speculative" — a worry without an anchor; listed only if the stakes justify it.
- "converged" — two or more seats reached it in separate contexts. This is not a measure of truth.
- "contested" — seats disagreed and the evidence did not settle it.

Never write "it seems", "it might be worth considering", or "potentially" where a finding has a status label; the label *is* the hedge.

## 9. When the artifact is good

A short report with `GO`, two or three improvements, a protect list and a pre-mortem line is a complete and valuable council output. Do not inflate. The user needs to be able to trust that a long report means a real problem.

## 10. When the Chair is unsure of the frame

If the seats' "challenge to the brief" sections converge on the objective being wrong, stop and say so at the top of the report, propose the corrected objective, and offer to re-run. Evaluating the wrong thing well is the most expensive failure the council can have.
