# Ledger template

Copy to `.sota/<slug>/LEDGER.md`, unless the project has its own convention. Every section is append-only, except each round's State and finding status, which are updated in place, and a replaced Decision, which is marked as replaced with the new one above it. If the work is published, keep this file out of it unless the owner agrees. Write in the owner's language.

```markdown
# Ledger: <subject>

## Subject
- Objective:
- Surface: <what is in scope: screens, sections, audiences, roles>
- Profile: <from profiles.md, with its reality surface, matrix, gate and guard spelled out for this subject>
- Criterion of "state of the art" (checkable):
  1. ...
- Must not: <what each audience must not receive; what must not change>
- Sources to measure against: <standards, comparables, literature>

## Release contract
- Level: local | shared | public
- Action:
- Proof:
- Rollback:
- Needs separate consent each time:
- Approved by the owner on: <date>

## Rounds
### Round 0 — <date>
- Version:
- What changed:
- Gate: <result, read from where>
- Release: <id and proof, or "local only">

### Round N — <date>
- Council: <mode, seats, reality surface measured> · Report: <path>
- Findings: F<n> <severity> — <one-line evidence> — <proposed fix> — open | fixed | deferred (D#) | inherited (H#)
- New blockers and majors: <n> (of which regressions of earlier fixes: <n>)
- Owner's answer at the pause: <quoted literally>
- Fixes: ... · Version: ... · Gate: ... · Release: ...

State: paused-awaiting-owner | fixing | closed

Trajectory: 5 → 3 → 1

## Decisions
Decided, and not reopened without new evidence. Includes the owner's notes verbatim.
- D1 (<date>, owner): ...

## Out of scope
Refused on purpose, and why.
- O1: ...

## Inherited
Real defects whose cause lies outside the declared surface. A record for the owner.
- H1: <defect> — <evidence> — <who could fix it>

## Guards
- G1: <what it protects> — <where it lives> — <the failure that proved it red>

## Verdict
Converged at round N | No new majors, N open by owner decision | Stopped by the owner at round N | Stopped by condition 3, 4, 5 or 6 at round N. Pending: ...
```
