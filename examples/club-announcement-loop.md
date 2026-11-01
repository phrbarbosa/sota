# Example: round 0 and the first pause of a paper-only loop

Real output on the 1.0.0 protocol. The announcement and the club are invented test input. Measured cost: USD 7.25 at API prices on an Opus-class model, in about 16 minutes. The run stopped at the pause, as a loop must, so no fix has been applied and nothing was sent. The clipped style of the pause message comes from an output setting on the author's machine and is not part of the skill. The files are otherwise unedited.

Prompt:

> /sota:sota loop announcement.md, paper only. Goal: every member knows what changes, when, and what to do. The criterion you write is approved. Release contract approved in advance: level local, action = save as a new version file, proof = file exists, rollback = previous version file, sending is always mine. Run round 0 and stop at the first Pause, then end your turn with the pause message.

## The input: `announcement.md`

```text
Hi all, the club is changing some things next month. Fees are going up and the
gym hours will be different. Please take note and contact us if needed.

Facts (from the treasurer's note, 2026-10-28): monthly fee goes from $40 to $46 on 1 December.
Weekday gym hours become 6:00-21:00 (were 6:00-22:00). Weekend hours do not change.
Members who pay annually keep their current price until renewal. Questions: desk@riverside-club.example.
```

## What the owner saw at the pause

# Pause: round 0 done, v0 not ready to send

Slug `announcement`. Resume: `/sota:sota continue announcement`.

**What changed:** nothing. `announcement.md` existed, so it became baseline. Facts paragraph may or may not go to members, so council measured both: first paragraph only (R1), whole file (R2).

**Proof**
- Version: `announcement.v0.md`, byte-identical to `announcement.md`.
- Gate: fails on 3 claims in first paragraph, all predating loop, so no block. Gym hours have no sourced date, and "fees" and "gym hours" overstate scope.
- Release: skipped, nothing changed. Sending stays yours.
- Rollback: none needed yet.

**Council found 8 blockers and majors, all new.** Reader tasks answered, out of 13: R1 0, R2 9 (8 if dead address counts as fail).

| Severity | Finding | Evidence | Fix |
|---|---|---|---|
| Blocker | Paragraph 1 alone useless (R1 only) | No figure, date or address in 29 words | Don't send it |
| Blocker | Gym change has no start date | "1 December" belongs to fee sentence only | **You supply date** |
| Blocker | No action for any change | Only "take note and contact us if needed" | **You supply action** |
| Blocker in R1, major in R2 | Lead misleads annual and weekend members | "Fees are going up"; corrections start at word 53 | Scoped lead |
| Major | "next month" goes stale | Right for the fee only if read in November | Absolute dates |
| Major | Club never named | Only trace is the email domain | **You supply name** |
| Major | Skim test fails | R2's first 34 words hold no specifics | Lead with the changes |
| Major | Question address dead (R2 only) | `.example` not in root zone, authoritative NXDOMAIN | **You supply address** |

- **Minors:** 7. One is the "treasurer's note" prefix: all five seats said major, fresh verifier said minor, I applied minor. It still breaks a must-not, and proposed text removes it.
- **Inherited:** none. Missing facts stay open because the defect sits in the text.
- **Dissent:** gym date stays blocker, though major was argued. Fix same either way.
- **Council limit:** reports not anonymized under letters; rulings rest on checked evidence.

**Trajectory:** `8`, first count, no trend yet. Four of the eight need your facts, so more rounds can't close them.

**Proposed v1 (not applied):**

```
[CLUB NAME]: changes to the monthly fee and weekday gym hours.

Monthly fee: rises from $40 to $46 on 1 December [2026]. Members who pay annually keep their current price until renewal.

Weekday gym: closes at 21:00 instead of 22:00, from [GYM START DATE]. Opening stays at 6:00. Weekend hours do not change.

What to do: [ACTION FOR MONTHLY PAYERS, ANNUAL PAYERS AND WEEKDAY GYM USERS, OR CONFIRMED "NO ACTION NEEDED"]

Questions: [CONFIRMED ADDRESS]
```

Fresh verifier checked earlier wording. I then fixed two issues it raised; word positions re-measured, new wording not re-read fresh.

**Risks outside the text**
- **Facts unchecked:** all second-hand. Treasurer's note not available, so only you can compare.
- **Reach:** one send will miss members. Association email opens about 36% in 2024 (vendor data); small club may differ.
- **Notice:** 1 December is 30 days away. Membership terms not seen, so any required notice period unknown.

Report: `.sota/announcement/round-1-report.md`. Ledger: `.sota/announcement/LEDGER.md`, state `paused-awaiting-owner`.

## Your call: continue, continue with notes, or stop?

- **Continue:** I apply fixes and save `announcement.v1.md`, then next council reads it. Without your facts, v1 keeps visible brackets and is not sendable.
- **Continue with notes:** same, plus what not to fix or what to prioritize, recorded verbatim.
- **Stop here:** close with findings listed as pending.

Answer what you can with it, or attach the treasurer's note, which may settle some:
1. What date does 21:00 closing start? Also 1 December?
2. What must monthly payers, annual payers and weekday gym users each do? If nothing, confirm "no action needed".
3. Club's name as members know it?
4. Real address for questions, or is this one a stand-in?
5. Does "1 December" mean 2026?
6. Are these the only changes?

## The ledger

````markdown
# Ledger: club announcement

Slug: `announcement` · Resume: `/sota:sota continue announcement`

## Subject
- Objective: every member knows what changes, when, and what to do.
- Surface: the text of `announcement.md` as members receive it. The owner has not stated whether the "Facts" paragraph goes to members, so both renderings are measured: R1 = first paragraph only; R2 = whole file.
- Profile: Writing (paper only).
  - Reality surface: the text as received; seats simulate each recipient with no outside context.
  - Matrix: audiences (monthly payer, annual payer, weekday-evening gym user, weekend-only gym user, member who does not use the gym) × tasks (what changes, when, what to do) × reading conditions (skim, phone, forwarded without context).
  - Gate: fact table in `FACTS.md`; every number, date, name and address checked against it.
  - Guard: a fact-table row, or a reader-simulation task with an expected answer, shown to fail on the earlier version.
- Criterion of "state of the art" (checkable). Approved by the owner in advance ("The criterion you write is approved"):
  1. **Reader tasks.** Given only the text, with no inference or outside context, a reader answers correctly:
     - monthly payer: the new fee, the old fee, the date it starts, what to do;
     - annual payer: that their price holds until renewal, what to do;
     - weekday gym user: the new closing time, the old closing time, that opening time is unchanged, the date it starts, what to do;
     - weekend-only gym user: that their hours do not change;
     - any member: where to send questions.
  2. **Complete per change.** Each change states what, when as an absolute date, and the action, or a sourced statement that no action is needed.
  3. **Skim.** Both changes and their dates appear in the first 50 words. The whole message is at most 150 words.
  4. **Forwarded.** The text stands alone: it names the club and contains no time reference that depends on when it is read.
  5. **Facts.** Every number, date, name, address and promise traces to a row in `FACTS.md`. Summaries do not overstate or understate scope.
  6. **Gaps stay visible.** A fact a reader needs that the sources lack is reported to the owner and is never filled in by the text.
- Must not:
  - any member must not receive an invented reason, an invented annual renewal price, an invented "no action needed", an invented date, or an apology or justification the sources do not hold;
  - annual payers must not be led to think their price rises on 1 December;
  - weekend-only users must not be led to think their hours change;
  - no member should receive internal provenance such as "from the treasurer's note".
- Sources to measure against: the Facts paragraph in `announcement.md`. The treasurer's note of 2026-10-28 is not available here.

## Release contract
- Level: local
- Action: save as a new version file (`announcement.vN.md`, next to the original)
- Proof: the file exists
- Rollback: the previous version file
- Needs separate consent each time: sending, which is always the owner's act
- Approved by the owner on: 2026-11-01, in advance

## Rounds
### Round 0 — 2026-11-01
- Version: `announcement.v0.md`, byte-identical copy of `announcement.md` (sha256 49a67382…96ad)
- What changed: nothing. The subject exists and the owner supplied no new facts and no rewrite request, so it is the baseline.
- Gate: fails on A2, A3, A4 in `FACTS.md`. Predates the loop: recorded, does not block.
- Release: skipped, nothing changed. The baseline copy is local only.

### Round 1 — 2026-11-01
- Council: standard; Verifier, Red Team, Steelman, Outside View, Pragmatist; 2 contention pairs; 1 fresh verifier. Measured v0 as R1 and R2 across the matrix. Report: `round-1-report.md`
- Findings:
  - F1 blocker (R1) — R1 scores 0 of 13 reader tasks — do not send paragraph 1 — open
  - F2 blocker — no start date for the gym change anywhere in the file — owner supplies the date — open, severity in dissent
  - F3 blocker — no action or sourced "no action needed" for any change — owner supplies per audience — open
  - F4 blocker in R1, major in R2 — "Fees are going up", "the gym hours will be different" unscoped; corrections at words 53 and 58 — scoped lead — open
  - F5 major — "next month" true only if read in November 2026 — absolute dates — open
  - F6 major — club never named — owner supplies the name — open
  - F7 major — skim criterion fails in both renderings — lead with the changes — open
  - F8 major (R2) — `.example` absent from the root zone, authoritative NXDOMAIN — owner supplies the real address or confirms a stand-in — open
  - Minors, 7: provenance prefix (downgraded from major by the fresh verifier), no year, opening must be deduced, summary hides the cut, renewal silence, no reason, fragile word-50 position — open
- New blockers and majors: 8 (of which regressions of earlier fixes: 0)
- Owner's answer at the pause: (awaited)
- Fixes: none. Version: v0 unchanged (sha256 re-checked identical). Gate: unchanged, fails on A2, A3, A4, predates the loop. Release: skipped at round 0, nothing changed.

State: paused-awaiting-owner

Trajectory: 8

## Decisions
Decided, and not reopened without new evidence. Includes the owner's notes verbatim.
- D1 (2026-11-01, owner): "loop announcement.md, paper only. Goal: every member knows what changes, when, and what to do. The criterion you write is approved. Release contract approved in advance: level local, action = save as a new version file, proof = file exists, rollback = previous version file, sending is always mine."

## Out of scope
Refused on purpose, and why.
- O1: Whether the fee rise and the shorter hours are good decisions. The announcement reports them and does not set them.
- O2: Sending, and the choice of channel. The owner's act under D1.

## Inherited
Real defects whose cause lies outside the declared surface. A record for the owner.
- (none yet)

## Guards
- G1: reader tasks, 13 answers with expected values from `FACTS.md` — the task list in criterion 1 above, to be run on every version — red on v0: R1 0 of 13, R2 9 of 13 (8 if the dead address counts as a fail). Checked by the fresh verifier; on any fix, the expected answers come from the owner's facts.

## Verdict
(open)
````

## The round's council report

# Curia verdict: club announcement, v0 (loop round 1)

**Verdict:** NEEDS REWORK, fix named
**Why, in one line:** Neither rendering tells every member what changes, when and what to do. Text edits fix part of this, and four defects need facts only the owner has.
**Confidence:** high on the text defects (word positions computed, every anchor opened, root DNS queried). The facts themselves are unchecked, because the treasurer's note was not available.
**Mode:** standard · Seats: Verifier, Red Team, Steelman, Outside View, Pragmatist · 2 contention pairs · 1 fresh verifier
**Model families:** 1. Seats ran in separate contexts with different methods; this is not independent human review.

## Objective evaluated against
Owner, verbatim: "every member knows what changes, when, and what to do." Criterion and must-nots are in `LEDGER.md`.

## Must change

Blockers:

1. **R1 alone gives members nothing usable.** `verified` · `convergent`
   Evidence: R1 scores 0 of 13 reader tasks. It has no digit, no `$` and no `@` in 29 words, and never states the annual hold, the unchanged opening or the weekend hours.
   Fix: do not send paragraph 1. Use the proposed text.
2. **The gym change has no start date.** `verified` · `convergent` · severity contested (see Dissent)
   Evidence: the only dates in the file are "next month", "2026-10-28" and "1 December", and "1 December" belongs to the fee sentence. The gym sentence, "Weekday gym hours become 6:00-21:00 (were 6:00-22:00).", has none.
   Fix: needs the date from the owner. Do not extend "1 December" to it by inference.
3. **No change has an action or a sourced "no action needed".** `verified` · `convergent`
   Evidence: the only instruction is "Please take note and contact us if needed".
   Fix: needs the action for monthly payers, annual payers and weekday gym users, or the owner's confirmation that none is needed.
4. **The lead misleads annual payers and weekend-only users.** Blocker in R1, major in R2. `verified` · `convergent`
   Evidence: "Fees are going up" and "the gym hours will be different" carry no scope limit. R1 never corrects them. R2's explicit corrections begin at word 53 ("Weekend") and word 58 ("Members"), past the 50-word skim window.
   Fix: delete the lead and use a scoped one, with the annual and weekend sentences beside the change they qualify.

Majors:

5. **"next month" depends on the reading date.** `verified` · `convergent`
   Evidence: it matches the 1 December fee only if read in November 2026.
   Fix: delete it and use absolute dates.
6. **The club is never named.** `verified` · `convergent`
   Evidence: "the club" at word 4, and `riverside-club` only inside the address, in R2 only. Fails criterion 4 when forwarded.
   Fix: needs the name as members know it. Do not derive it from the domain.
7. **The skim test fails.** `verified` · `convergent`
   Evidence: R1 has no absolute date. R2's first 34 words hold no specifics and its first 50 end at "6:00-21:00", with no gym date. Length passes (29 and 69 words). The missing gym date is a shared cause with finding 2; the empty lead is its own cause.
   Fix: lead with the changes.
8. **The only question address cannot receive mail on the public internet.** R2 only. `verified` · severity contested, upheld
   Evidence: `.example` is absent from the IANA TLD list (version 2026110100). `dig NS example. @a.root-servers.net` returns authoritative NXDOMAIN; the control `com.` returns a delegation. The full club domain was not queried and no mail was sent. Nothing in the text marks it as a placeholder.
   Fix: needs the real address, or the owner's confirmation that this is a stand-in.

## Should change (minors, 7)
1. Provenance prefix in R2, "Facts (from the treasurer's note, 2026-10-28):". Breaches a must-not. Downgraded from major (see Dissent). Effort: small. The proposed text removes it.
2. "1 December" has no year. The only year in the file sits in that prefix. Effort: small; owner confirms.
3. Opening time must be worked out by comparing two ranges. Effort: small.
4. "some things" and "will be different" hide that the gym change is an hour less. Effort: small.
5. "until renewal" invites "and what then?", and the source holds no renewal date or price. The text must stay silent. Report to the owner, and the desk needs an answer.
6. No reason for the fee rise. Published guidance recommends giving one; the source has none, so the text must not supply it. Optional fact from the owner.
7. R2's new hours fall exactly on word 50, so its partial skim result is fragile. Effort: none once finding 7 is fixed.

## Keep
- Old values beside new: "$40 to $46", "(were 6:00-22:00)".
- "Weekend hours do not change." and "Members who pay annually keep their current price until renewal." Carried word for word.
- No invented reason, apology, renewal price or "no action needed" appears anywhere. Any rewrite must preserve this.
- Length: 69 words against a limit of 150.

## Proposed text (replaces the curated version; nothing is applied before the owner answers)
**Status:** checked by a fresh context, which found one real change of meaning ("two changes" closed the list) and one fill risk (actions were per change, tasks are per audience). The Chair corrected both afterwards. The word positions below were re-measured by script; a fresh context has not re-read the corrected wording. Not sendable until the brackets are filled.

```
[CLUB NAME]: changes to the monthly fee and weekday gym hours.

Monthly fee: rises from $40 to $46 on 1 December [2026]. Members who pay annually keep their current price until renewal.

Weekday gym: closes at 21:00 instead of 22:00, from [GYM START DATE]. Opening stays at 6:00. Weekend hours do not change.

What to do: [ACTION FOR MONTHLY PAYERS, ANNUAL PAYERS AND WEEKDAY GYM USERS, OR CONFIRMED "NO ACTION NEEDED"]

Questions: [CONFIRMED ADDRESS]
```

74 words with brackets as written. Fee and date end at word 22, gym date slot ends at word 44, opening at 45-48, "Weekend" at 49. A long gym date or club name could push the gym date slot toward word 50; re-measure once filled.

Changelog: lead and "next month" removed (findings 1, 4, 5, 7); gym date, action, club and address slots (2, 3, 6, 8); provenance removed, year slot, opening stated, direction stated (minors 1-4).

## Dissent register
- **Gym date, blocker or major (R2).** *Blocker:* the objective says "every member" and criterion 1 bars inference, so one cohort without a "when" means the objective fails. *Major:* a criterion breach alone sets major; "next month" plus the December fee line gives a month, the natural guess is 1 December, and the worst case is a wasted trip. Neither side produced new evidence, so it stays blocker at its original level. The fix is the same either way.
- **Provenance prefix, major or minor.** *Major (all five seats):* a written must-not, and its date competes with "1 December". *Minor (fresh verifier):* no member loses what, when or what to do, and no significant risk is shown. The Chair applied the verifier's result.

## What would change this verdict
- The treasurer's note holds the gym date and an action. Then findings 2 and 3 close with one edit. Cheapest test: the owner opens the note.
- The address is a deliberate stand-in. Then finding 8 closes at once. Cheapest test: the owner says so.

**Pre-mortem:** If this fails in 12 months, the most likely reason is a rewrite attached "1 December" to the gym line because it reads naturally, and the real date differed.

## Beyond the criterion
- **Reach.** "Every member knows" also depends on the channel, which is the owner's (O2). Association email open rates were reported at about 36% for 2024 (Higher Logic, vendor data on 1,500+ organisations; a small club may differ). A perfect text sent once will still miss members. Passing the criterion is not the same as the objective being met.
- **Notice.** 1 December is 30 days from 2026-11-01. Membership terms and jurisdiction were not available, so any required notice period is unknown. The owner should check.
- **Source.** All facts are second-hand from the file's paragraph, so "traces to a source" means "traces to that paragraph". Only the owner can compare it with the note.

## Dimension assessment
| Correctness | Fit | Risk | Cost/simplicity | Execution | Stakeholders | Outside view |
|---|---|---|---|---|---|---|
| mostly sound: paragraph 2 consistent, paragraph 1 overstates, address dead | weak | contained: correctable by a second message | lean | poor as a member message | with reservations | partially: has the old-and-new format, lacks lead and action |

<details><summary>Finding registry and process notes</summary>

| ID | Finding | Seats | Class | Severity | Status | Outcome |
|----|---------|-------|-------|----------|--------|---------|
| 1 | R1 carries no facts | 5 of 5 | convergent | blocker (R1) | verified | open |
| 2 | Gym start date absent | 5 of 5 | contested on severity | blocker | verified | open, fact needed |
| 3 | No action per change | 5 of 5 | convergent | blocker | verified | open, fact needed |
| 4 | Lead misleads two audiences | 5 of 5 | convergent | blocker R1 / major R2 | verified | open |
| 5 | "next month" relative | 5 of 5 | convergent | major | verified | open |
| 6 | Club unnamed | 5 of 5 | convergent | major | verified | open, fact needed |
| 7 | Skim fails | 3 of 5 as a finding, 5 of 5 in scoring | convergent | major | verified | open |
| 8 | Address cannot receive mail | 3 of 5 flagged; severity split | contested | major | verified | open, fact needed |
| m1-7 | Minors listed above | various | | minor | verified or plausible | open |

Process notes:
- Limitation: reports were read in sequence but not anonymized under letters, and each report's method was evident from its content. Rulings rest on checked anchors, not on which seat said what.
- Contention, gym date: real in both renderings. The stated cause fits R2 only, since R1 has no date at all; R1's failure is finding 1. No new evidence on severity, so it stands as blocker and goes to dissent. Contention, address: the challenger conceded on the text-as-written rule, and new evidence was the root NXDOMAIN. Upheld as major, R2 only.
- Fresh verifier: verified items 2-4, 6-9. Corrected the reason on item 1 (R1 also fails tasks it simply never states, not only for lack of figures). Rejected major for provenance. Found the "two changes" and per-change issues in the proposed text.
- Inherited: three seats suggested marking the missing facts inherited. Triage keeps them in the round, since the defect is in the text, which is the declared surface, and the fix lands in the text. Only the fact comes from the owner.
- Downgrade: provenance. It went to the fresh verifier, whose result produced the downgrade, so no second verifier was run.
- Scoring: R2's 9 of 13 counts the address on the text alone; it is 8 of 13 if the dead address counts as a fail.
- Data: seats were same-provider subagents. Web queries were reported as general questions; DNS checks touched only the TLD. One seat's sources included some read through a summariser, and it listed which sources it opened and which it saw only as search results. Figures cited here come from sources it reported opening.
- The owner's first paragraph was treated as not a source, because the brief said so. Two seats questioned this. It would give a month at most, so the gym finding stands either way.
</details>

