---
name: sota
description: Bring anything to its state of the art — code, a UI, an API, a document, a message, a plan, a business idea, a decision, a prompt, a research claim. Two modes. Review convenes Curia, an evidence-driven council of 5 method-differentiated seats plus a Chair, and returns a verdict with stated confidence and evidence, prioritized fixes and a curated version. Loop repeats review, fix, verify and release in rounds, pausing after each so the owner can inspect the result and decide whether to continue. Use for "sota", "state of the art", "estado da arte", "iterate until it converges", "curia", "council", "conselho", "red team", "stress test", "pre-mortem", "second opinion", "what am I missing", "is this good enough", "review this properly", "critique and improve", or any serious multi-perspective evaluation of something consequential or hard to reverse, even if no name is used. Not for quick factual questions or trivial edits.
license: MIT
compatibility: Works best where the agent can start subagents or a headless CLI for fresh contexts. Falls back to a weaker single-context mode and says so.
metadata:
  version: "1.0.0"
  repository: https://github.com/phrbarbosa/sota
---

# sota

Takes one subject toward its state of the art by scrutiny from fresh eyes, contact with reality, and a human decision at every step.

**Authority, in both modes.** Invoking this skill never authorizes sending, publishing, deploying or purchasing. The run itself uses the user's model allowance, and it says how much it will start before starting.

## Choose the mode

| The user wants | Mode | Changes the subject? |
|---|---|---|
| A verdict, a critique, a second opinion, one curated pass | **Review** | No. The curated version goes in the report |
| The thing improved in repeated rounds until it stops yielding | **Loop** | Yes, inside the scope and release contract the owner approved |
| To resume an earlier loop (`continue <slug>`) | **Loop**, from the ledger | Yes |

If the request does not say which, use Review and offer the Loop in one line. Review costs less and touches nothing.

```
/sota review the rollout plan in docs/rollout.md
/sota review deep: should we migrate to UUID primary keys this sprint?
/sota loop our signup page feels generic; goal: a first-time user finishes in under a minute
/sota loop the grant proposal in proposal.md, paper only
/sota continue signup-page
```

When installed as a plugin the command is `/sota:sota`. Plain language works as well as the command.

## Review mode

Read `references/council.md` and follow it. That file is the complete protocol: brief, independent seats, triage, contention, verification, verdict. Modes are `standard` (default), `deep` and `lite`.

## Loop mode

Why it has this shape, from real runs: reviewing a description converges slowly, while reviewing the running thing finds what matters. Every fix can break something elsewhere, so without checks that survive the round the loop oscillates. And an owner who sees the work only at the end cannot veto anything along the way.

### Guarantees

1. **Fresh eyes, always.** Every council round uses fresh contexts, never `lite`. The work was produced in this session, and a model does not reliably find errors in its own trace.
2. **Reality from round 1.** Each round reviews the thing as its audience meets it, not a description of it. `references/profiles.md` says what that means per kind of subject.
3. **Every regression fix gets a guard that failed without it.** See `references/guards.md`. A guard that has never been red guards nothing.
4. **Nothing is released failing the gate.** A failure that predates the loop is measured, stated and recorded, and does not block.
5. **Every pause asks, unless the round converged.** The council on the released version runs as part of the Pause, so the owner decides on evidence. No fix starts without the owner's "continue".
6. **Outward action comes only from the release contract** (round 0), and an irreversible step needs its own consent at the moment it happens.

If there is no human to answer, stop at the pause and leave the ledger ready for `continue`. Never answer for the owner.

The Loop requires fresh contexts. Without subagents or a headless CLI it does not run: say so, and offer a Review of material not made in this session.

### The ledger

The state that crosses rounds, so decisions are not reopened and another session can resume. Use `references/ledger-template.md`. It lives at `.sota/<slug>/LEDGER.md` unless the project has its own convention, and it is versioned with the work when the work is versioned. If the work is published, keep the ledger out of it unless the owner agrees, because it quotes the owner verbatim. Round briefs reference it and do not copy it. Tell the owner the slug and the resume command at round 0.

**Resuming.** Find the ledger in the working directory, or ask; a bare `continue` lists `.sota/*`. Read its State. If paused, present the pause again and ask. Re-run the council only if the subject changed.

### Round 0 — contract, then first version

1. **Read the subject yourself**, then write the council brief (`references/council.md`, Phase 0).
2. **Pick the profile** from `references/profiles.md`, or compose one. It fixes the reality surface, the matrix, the gate, the guards and the release.
3. **Write the criterion of "state of the art" so it can be checked.** Without one the council always finds one more thing. Name the surfaces, the audiences, the conditions and the sources you will measure against. State what each audience must *not* receive, not only what it must.
4. **Propose the criterion and the release contract** (below) together and get the owner's approval. This is the one question round 0 must ask.
5. **Check the size.** If the subject needs a new system, or work other sessions must continue over weeks, say so and propose splitting it. The loop refines one subject and does not replace planning.
6. **Get to a first version.**
   - **The subject exists:** it is the first version. Change nothing, version it as the baseline, and go to the Pause, skipping its Release step because nothing changed. If the owner asked for a rewrite or supplied new facts, draft under the fix discipline, pass the gate, and treat that draft as the first version.
   - **It does not exist, and a real version can exist:** write a one-page proposal and run at most two paper councils, to remove blockers of direction and not to polish wording. Show their blockers to the owner with the Pause's three answers. Then build under the fix discipline, pass the gate, and go to the Pause.
   - **Paper only** (no running version can exist, or the owner asks for none): draft the document under the fix discipline, pass the gate, and go to the Pause. Rounds still apply, and the reality surface is whatever the profile gives: reader tasks, recomputed numbers, sources opened. Expect slower convergence and read the stop signals.

### The release contract

```
Release level:  local | shared | public   (default: local)
Action:         the exact command or step
Proof:          how we confirm it worked
Rollback:       how we undo it, or "irreversible"
Needs separate consent each time: <anything irreversible or outward-facing>
```

Each version is released before its council reads it, so say that when proposing the contract.

- `local`: a new file or an unpushed branch, never the default branch. Nobody else sees it.
- `shared`: a preview, a staging environment, a draft handed to the owner to pass on.
- `public`: production, a publication, a message that gets sent.

Sending messages, charging money, running production data migrations, filing documents and posting publicly stay with the owner unless they name that action in the contract. Even then, an irreversible action is confirmed again when it comes due.

### Round N (N ≥ 1) — review the real thing

1. **Stand up the reality surface for this exact version.** Do not change it while a round is reading it.
2. **Write the round brief**:
   - the version, and the whole change since the loop began, not only the last step;
   - last round's fixes, each with "verify it, and look for what this fix broke";
   - the criterion of a **new major**: a major that violates the written criterion on the declared surface and is not in the ledger, or a declared fix that is only half done. Changing something shared puts everything that depends on it in scope;
   - **inherited** means the cause lies outside the declared surface;
   - the ledger's Decisions and Out of scope, with "do not reopen without new evidence";
   - the order to measure the whole matrix before concluding.

   State facts in the brief. Keep your own interpretation and any reframing out of it, because the council follows whatever frame it is handed. Pass source material whole, because summaries generate false findings.
3. **Run the council's Phases 1–4 in `standard` mode**, fresh contexts, in parallel, plus a domain seat when warranted. Count majors after Phase 4. Proposed fixes take the place of the curated version. For a subject with many parts, add a seat that audits consistency across parts (every shared name, number and promise, against who produces and who consumes it). Part-by-part review misses these.
4. **Triage** (council Phase 2). For each major, decide whether it is in scope or inherited, by measuring. Inherited goes in the ledger and not in the round.
5. **Decide the exit.** If triage pruned, downgraded or marked inherited any major this round, first send those items to one fresh verifier. Then:
   - no new blocker or major, and none left open → at the Pause say "converged", skip the question, then Closing;
   - the only open majors stand by the owner's decision → show them, skip the question, and close as "no new majors, N open by owner decision", never "converged";
   - otherwise → this is what the Pause presents.
6. **Do not fix anything before the pause**, because that takes away the veto the pause exists to give.
7. **On "continue":** fix under the discipline below, pass the gate, go to the Pause.

### Fix discipline

- State the check first, see it fail on the current version, then fix.
- Smallest fix that resolves the finding. Check every fix across the whole matrix, not only where the defect appeared.
- A new claim introduced by a fix needs a source like any other. In writing, fixes are where unsourced sentences come from.
- When consolidating versions, copy what still applies in full. "As before" silently drops content.
- Check premises against the source itself, not a summary of it.
- Never calibrate against your own earlier hypothesis. A number that originated as an assumption stays an assumption however many rounds repeat it.

### The Pause — version, release, review, show, ask

In this order:

1. **Version** the round's work and the updated ledger. Re-run the gate.
2. **Release** exactly as the contract says, and prove it. If the contract does not cover something the round now needs, stop and ask. If a defect has already reached a shared line that others can release from, holding back your own release does not contain it: fix or revert it there.
3. **Run the next round's council** (Round N, steps 1–5) on what was just released. That is what makes item 4c possible.
4. **Show**, briefly, in the owner's language:
   - a. **What changed**, in the words of someone who uses it, and where to look: exact location, conditions, role;
   - b. **The proof**: version, gate result, release result, rollback;
   - c. **What the next round found**: each new blocker or major with one line of evidence and the proposed fix; minors in aggregate; what became inherited. If nothing, say "converged" (see Round N, step 5);
   - d. **The trajectory**: majors per round, such as `5 → 3 → 1 → 0`. If it has not fallen for two rounds, or the findings are regressions of earlier fixes, say so. That signals a missing guard, not a missing round.
5. **Save the report and version the ledger again**, with its State set to `paused-awaiting-owner`.
6. **Ask one question** (a structured question tool if there is one, otherwise a plain message, and then stop):
   - *Continue*: fix what the round found and go again;
   - *Continue with notes*: the owner says what not to fix, what to prioritize, what changed. Record it literally as a Decision, and it enters the next brief;
   - *Stop here*: go to Closing with the pending findings listed;
   - *Roll back*, when a new blocker is live: undo the release per the contract, then choose again.

   Facts only the owner knows go in this question as well. They turn a hedge into a statement.

A note that contradicts an earlier Decision replaces it: record both, newest on top. A note that exceeds the scope gets a plain statement that it does not fit, and what would.

### Closing

- The last round is released and proven as the contract requires, and the ledger holds the verdict and what stays pending.
- Temporary branches, previews and processes are removed.
- Report: the trajectory, what is live and where, inherited items for the owner, and new guards.

### Stop conditions

Never force another round.

1. The owner chose *Stop*.
2. A round found no new blocker or major. Show it and do not ask whether to continue. For a high-risk subject, offer one `deep` review in a line.
3. Three rounds in a row whose majors are regressions of earlier fixes. Stop fixing, propose the guard that measures the whole matrix, and ask.
4. The gate still fails because of the loop's changes after two attempts. Do not release. Pause with the failure.
5. The release proof failed. Roll back and pause with the diagnosis.
6. The subject has outgrown the loop. Say so and name what fits.

Signals worth saying out loud at the pause, even when the count has not reached zero:

- **The majors changed nature** (concept → promise → legal, say). The concept has stabilized. Stop rounding and write it down.
- **A round was spent undoing the previous round's excesses.** The council has started to regress.
- **The count holds but the severity keeps falling** until findings are word swaps. The remaining value is small.

Counts rarely reach zero fast. Three earlier loops, run on this protocol's predecessor, went `9 → 4 → 5 → 2`, `9 → 7 → 7 → 7` and `13 → 15 → 14`, and none reached zero. Stopping on evidence is a normal ending.

### Anti-patterns

- Fixing before the pause what the next round found.
- Counting minors as non-convergence. The criterion is a new blocker or major.
- A brief that forgets the ledger, so the council reopens decisions and the round spins.
- Testing a fix only where the defect appeared.
- "State of the art" with no written criterion.
- Treating "add more detail" as a major when the criterion is what the audience needs.

## Reference files

- `references/council.md`: the Review protocol, phases 0–5
- `references/seats.md`: seat briefs, contention and verifier prompts
- `references/chair.md`: triage, dimensions, verdict rules, calibration language
- `references/report-template.md`: the review report skeleton
- `references/lenses.md`: checklists by kind of artifact
- `references/profiles.md`: how the loop maps onto code, writing, plans, data, prompts and more
- `references/guards.md`: how to write a check that actually guards
- `references/ledger-template.md`: the loop's state file
- `references/evidence.md`: the research behind the rules, read when someone asks why or wants to change them
