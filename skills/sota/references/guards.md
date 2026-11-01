# Guards

A guard is a check that survives the round and goes red if the defect returns. In code it is usually a test. In writing or planning it is a fact-table row, a recomputation or a checklist item with a quoted failing case. These rules came from guards that were green while the defect was present.

## The proof: see it red

1. Write the guard.
2. Remove the fix, or use the previous version. **See the guard fail.**
3. Restore the fix. See it pass.
4. Record the failure in the ledger.

**Check the mutation itself.** A mutation that landed in the wrong place produces a false "survived" result, which looks rigorous and points you at an imaginary hole. Confirm the diff is the intended change and nothing else. A one-line diff is the proof. A ten-thousand-line diff is the alarm.

## Six ways a guard lies

| Failure | What it looks like | Rule |
|---|---|---|
| **Half-truth** | Proves "the slot starts empty" and cannot notice that it stayed empty | Write the sentence the guard proves, then its temporal negation. If the second half has no case, it is not guarded |
| **Copied list** | Coverage comes from a list inside the test, so it is green for the item added afterwards | Derive the list from the source (the enum, the routes, the screen's definition), and add an anchor item known to exist |
| **Tautology** | Compares two outputs of the same function | Compare what the audience sees and can do: the visible controls, the sentence as rendered |
| **Empty pass** | Loops over zero cases and succeeds | Require a minimum case count |
| **Wrong data** | Passes on a sample that lacks the fields that expose the defect | Add a fixture shaped like the real thing |
| **Blind medium** | A pixel diff of 0 while behavior is wrong; a spellcheck that passes while the fact is false | Check the property that failed, in the medium where it failed |

## Measure the matrix

One guard that measures the whole matrix beats ten that measure one point each. When findings are regressions of the previous round's fixes, the missing thing is usually a matrix guard and not another round. A component that hosts others needs a guard that opens each hosted thing inside it, because measuring only the host misses what is clipped or trapped.

## Reading results

**A plausible partial reading is worse than an absurd one.** An absurd number stops you. "Zero failures" read from a progress stream does not. Before accepting a number that confirms what you hoped, ask which slice of the output it came from and what the discarded part could contain. Prefer a structured report to progress text. Read the start of a provisioning log, not only its tail, because an early failure is what makes the later steps report nonsense. Read volatile state, such as the current branch, in the same command that acts on it. A pipe can hide an exit code, so check the code of the command you care about.

## Non-code guards

| Subject | Guard |
|---|---|
| Message or report | Fact table: claim, source, date checked. Plus one reader-simulation task with an expected answer |
| Plan | Recomputed model from inputs; assumptions labeled measured or hypothesis; a falsifier with a date |
| Analysis | An assertion on the recomputed headline number; a planted error that the pipeline catches |
| Prompt | An eval case that fails on the previous version, run several times |
| Concept | A recorded observation from a real probe, with who and when |

The same proof applies. Show that the check would have caught the earlier version: re-run it against that version and record the failing line.
