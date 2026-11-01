# Curia: the council protocol

Curia is an evaluation council. It exists because one judge is noisy, biased toward its own work, and blind to its own errors. The protocol follows what research on group judgment, LLM debate and LLM-as-judge shows (`evidence.md`): independent judgments before discussion, forced dissent, seats that differ in **method** rather than costume, debate only on real disagreement, verification by something outside the model, and a Chair who judges each dimension separately before forming a verdict.

The goal is a **verdict the user can check**, a **better version of the thing**, and an honest statement of **what would change the verdict**. A long list of complaints is not the goal.

## Modes

| Mode | When | Mechanics |
|---|---|---|
| `standard` (default) | Anything consequential: a feature, a plan, an idea, a design doc, a decision | 5 seats as parallel fresh contexts + Chair; one targeted contention round |
| `deep` | Hard to reverse, high cost of error, or the user asks | `standard` + web research for the outside view + a second contention round + independent re-verification by a fresh context that has not seen the deliberation; a second model family for at least one seat if available |
| `lite` | Small artifact, low stakes, the user asks for a quick pass | The Chair runs the five seat briefs in sequence in one context, in clearly separate sections, re-reading only the brief and artifact before each. Weaker, since there is no true independence. Say so in the report |

The seats need **fresh contexts**, and the mechanism is secondary. Use subagents when present. Otherwise use any headless CLI that runs a prompt in a new process, such as `claude -p "<prompt>"`, `codex exec "<prompt>"` or `gemini -p "<prompt>"`, in parallel from the shell. This satisfies the protocol fully. Only when neither exists fall back to `lite`, and state the limitation.

`lite` is not acceptable for one-way doors or high-stakes artifacts. Say a proper run is needed and do your best meanwhile. **Never use `lite` on the council's own output or on anything produced in this session**: a model does not reliably find errors in its own trace, but finds them readily when the same content arrives from outside.

**Before starting**, tell the user in one line what the run will start, for example "5 fresh agents, plus up to 10 for contention and 2 checkers". If they named this skill or a council, proceed. If they asked in plain language, state the run and the cheaper option (`lite`, or one careful read), and wait for a yes.

**If a seat fails** or hits a usage limit, retry once, then name the missing seat on the verdict line and cap confidence at medium. Never give `GO` or `SOUND` with the Verifier or Red Team missing.

## Phase 0 — Brief (Chair)

Write a short brief before convening anyone. A council evaluating against the wrong objective produces confident, well-argued noise.

1. **What is the thing?** Type, scope, where it lives. Read it yourself first.
2. **What is it for?** The objective in one sentence and the success criteria as the user would state them. If none were given, infer the most plausible and label them `assumed`.
3. **Constraints**: time, money, team, tech, legal, non-negotiables.
4. **Stakeholders**: who uses it, who pays, who is harmed if it fails.
5. **Reversibility and stakes**: one-way or two-way door; cost of a wrong verdict in each direction.
6. **Open questions** you cannot resolve from the material.
7. **Data boundary.** If the subject holds personal, health, legal, financial, client or secret material, do not pass it to another provider's CLI or model family without a yes from the user. State in the process notes where the material went.

If the objective is truly unknowable and a wrong guess would waste the run, ask **one** question. Otherwise proceed with labeled assumptions, since seats may challenge the frame.

Keep your own interpretation out of the brief. Seats follow whatever frame they are handed, so a reframing written into the brief comes back as false agreement.

Pick the mode. Attach the matching checklist from `lenses.md`. Read the subject's row in `profiles.md`, including its high-stakes rules. Decide whether a 6th **source-check seat** for a domain is warranted (security for auth code, clinical for a health protocol, legal for a contract); for law, medicine, finance or safety it is mandatory. For an artifact with many parts, add a consistency seat as well. Both briefs are in `seats.md`.

## Phase 1 — Independent assessments

Start the five seats **at the same time**, each in a fresh context. Each receives the brief, the artifact or its path, its seat brief from `seats.md`, the lens and the output contract below. **No seat sees another's output.** Independence is what makes later agreement mean something.

| Seat | Method | Core question |
|---|---|---|
| **Verifier** | Tests claims against reality: runs, reads sources, searches, recomputes | What here is true, false or unverifiable? |
| **Red Team** | Attacks: strongest case against, pre-mortem, failure enumeration, adversarial use | How does this fail, and what is the most damaging way? |
| **Steelman & Upside** | Builds the strongest version: best case for, what makes it 10x better, what to protect | What is most valuable here, and how do we get more? |
| **Outside View** | Reference class, base rates, prior art, how comparable things went | How often does this work, and what do existing solutions do? |
| **Pragmatist** | Simulates real users and operators; cost/benefit, simplest alternative, second-order effects, ethics, common sense | Would a sensible affected person accept this, and is there a simpler way? |

**Tool allocation is part of the method.** If every seat runs the same experiment, you get five copies of one finding.

- **Verifier**: full tools: execute, test, fetch, recompute.
- **Outside View**: search and read. No experiments on the artifact.
- **Red Team**: read-only; at most three targeted checks to substantiate its top attacks.
- **Steelman & Upside**, **Pragmatist**: read-only. If they want something measured, they list it under "what I would need".
- **Domain seat**: as the domain requires.

Seats report and never change the artifact. A seat that needs to experiment works on a copy.

**Anchors**: for prose cite the step, section or quoted phrase, since line numbers drift. For code cite `file:line`. For images, a described region and the viewing condition.

**Output contract for every seat.** The body does not name the seat, which is what lets the Chair anonymize honestly in Phase 2.

```
## Report
### Findings
- F1 [severity: blocker|major|minor|nit] [status: verified|plausible|speculative]
  Claim: <one sentence>
  Evidence: <file:line / quote / test output / URL / computation — mandatory>
  Impact if true: <one sentence>
  Suggested fix: <concrete: a rewrite, a diff, a replacement>
### Strengths worth protecting
- S1 ... (with evidence)
### Improvements beyond fixes
- I1 ... (with effort: small|medium|large)
### Challenge to the brief (optional)
### What I could not verify and would need
### Confidence in my overall read: low|medium|high — why
```

Rules for every seat:

- A finding with no evidence anchor is `speculative`, and the Chair may discard it.
- "Verified" means the seat checked it.
- No manufactured findings. If the thing is good, say so and spend the effort on improvements.

**Severity is judged on the artifact as written, never on how easy the fix is.** `blocker`: the objective fails or unacceptable harm occurs. `major`: the objective is materially degraded or a significant risk is created. `minor`: real but contained. `nit`: polish. Settle severity arguments by asking "if nobody touched it, what happens?"

## Phase 2 — Chair triage

Read the reports **separately, one at a time**, and build a **finding registry** (details in `chair.md`).

- **Anonymize and shuffle**: Seat A–E in random order while judging.
- **Classify**: `convergent` (2+ seats; on one model family this raises a finding's priority for verification, not its credibility), `contested` (disagreement on existence, severity or fix), `unique` (one seat). **Never discard a finding for being unique**: groups lose exactly the information only one member holds. Verify it instead.
- **Discrete labels, no averaging.** Averaging hides the disagreement that carries information.
- **Select, do not blend.** Keep the best-supported finding and fix rather than an average of the proposals.
- **Prune**: downgrade to `speculative` any finding whose anchor does not hold when opened. Hallucinated critiques are the most common failure of LLM reviewers.

## Phase 3 — Targeted contention

Debate alone does not improve answers. What helps is adversarial argument before a judge on a specific disagreement.

- Skip this phase if the registry has no `contested` items and no `unique` blockers. The Chair rules directly on disputes about ease of fixing; disputes about consequence go here. `lite` skips this phase and lists such items in the dissent register.
- For each contested item (cap of 5, highest stakes first) start **two fresh contexts**: one argues the finding is real and serious, the other that it is wrong or overstated. Each gets the brief, the artifact, the finding and its evidence, and must respond **with evidence**. One round each; a second only in `deep` and only if the first produced new evidence.
- A position changes only on new evidence, and you record which. Discard conformity flips.

## Phase 4 — Verification sweep

For every `blocker` and `major` still standing, run the **cheapest decisive test**: execute it, reproduce the number, open the source, check the base rate, draft the counterexample. Prefer signals the model did not generate. Downgrade whatever fails.

The Chair may verify the seats' majors directly, since that is checking others' work. But the Chair must not treat its own synthesis as verified. If any `blocker` survives triage, or in `deep` for all blockers and majors, start **one fresh verifier** (`seats.md`) that gets only the brief, the artifact and the findings. In real runs this step caught what several seats missed. In `lite`, the Chair checks what it can and marks the rest `plausible`.

## Phase 5 — Verdict and report

Read `chair.md`, then produce the report from `report-template.md`.

1. **Verdict**: `GO` · `GO WITH CHANGES` · `NOT YET` · `NO-GO`, or for non-decisions `SOUND` · `SOUND WITH FIXES` · `NEEDS REWORK`. One line of justification. Confidence in a word and a reason.
2. **What must change**: blockers and majors, with evidence and a concrete fix.
3. **What would make it better**, ranked by impact ÷ effort. Prefer the smallest intervention that captures most of the value.
4. **What to keep**, with evidence.
5. **Curated version**: the improved thing in full if small; a patch list if large. Review mode puts it in the report and does not edit the original unless the user asks. Before reporting, give one fresh context the brief, the original, the curated version and the must-change list. It executes the curated version if it can run; otherwise it walks it against each finding and looks for what the fix broke and for new unsourced claims. Report the result beside the version, or label it `curated, unchecked`.
6. **Dissent register**: every unresolved contested item, each side at full strength.
7. **Falsifiers**: the two or three pieces of evidence that would flip the verdict, and the cheapest test for each.
8. **Pre-mortem line**: "If this fails in 12 months, the most likely reason is ___."
9. **Process notes**: mode, seats, what could not be verified, limitations.

Write in the user's language, as short as the stakes allow. For law, medicine, finance or safety, say what a qualified professional must still decide.

## Anti-patterns

- **Costume diversity**: five personas, one method. If two seats produced near-identical findings, the run collapsed. Say so.
- **Debate as theater**: rounds of agreement-seeking that converge on the first confident claim.
- **Severity inflation**: calling nits majors to look thorough.
- **Complexity ratchet**: recommending the elaborate fix when a small one captures the value.
- **Sycophancy**: softening a NO-GO because the user is invested. The job is to be right, kindly.
- **Self-grading**: counting the Chair's own synthesis as verified.
- **Circular calibration**: judging a number against a range that the input itself labeled a hypothesis.
- **Finding count as quality**: a good artifact deserves a short report and a strong GO.
