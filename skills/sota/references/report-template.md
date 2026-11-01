# Review report template

Use this structure. Write in the user's language. Keep sections proportional to the stakes; a good artifact gets a short report.

```
# Curia verdict: <artifact name>

**Verdict:** GO | GO WITH CHANGES | NOT YET | NO-GO   (or SOUND | SOUND WITH FIXES | NEEDS REWORK)
**Why, in one line:** ...
**Confidence:** high | medium | low — <reason>
**Mode:** standard | deep | lite · Seats: Verifier, Red Team, Steelman, Outside View, Pragmatist[, <domain> source check (not a professional)][, consistency]
**Model families:** <n> — seats ran in separate contexts with different methods; this is not independent human review.
**For a qualified professional** (law, medicine, finance, safety only): this prepares you and does not replace them. They must decide: ...

## Objective Curia evaluated against
<one or two lines from the brief; label assumed parts>

### Challenge to the objective  (include only when seats raised one)
<what the seats converged on; the proposed corrected objective; the cheaper or smaller thing that would satisfy it if there is one; "the verdict below assumes <X>"; offer to re-run against the corrected objective>

## Must change (blockers / majors)
1. **<finding>** — `verified|plausible` · `converged|contested|unique`
   Evidence: <anchor>
   Fix: <concrete>
2. ...

## Should change (highest impact ÷ effort)
1. <improvement> — effort: small|medium|large — why it matters to the objective
2. ...

## Could change
- ...

## Keep (strengths with evidence)
- ...

## Curated version
**Status:** checked by a fresh context: <result> | curated, unchecked

<full improved artifact, or patch list for large artifacts; changelog mapping changes → finding IDs>

## Dissent register
- <finding>: *For* — ... / *Against* — ... (unresolved because ...)

## What would change this verdict
- <falsifier 1> — cheapest test: ...
- <falsifier 2> — cheapest test: ...

**Pre-mortem:** If this fails in 12 months, the most likely reason is ___.

## Dimension assessment
| Correctness | Fit | Risk | Cost/simplicity | Execution | Stakeholders | Outside view |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

<details><summary>Finding registry and process notes</summary>

| ID | Finding | Seats | Class | Severity | Status | Evidence |
|----|---------|-------|-------|----------|--------|----------|
| ... |

Process notes: what could not be verified; limitations of the mode; any sign of seat collapse; contention outcomes.
</details>
```
