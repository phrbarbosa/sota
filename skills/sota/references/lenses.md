# Lenses

Short checklists the Chair attaches to the brief according to artifact type. They give the seats a shared map of what "good" means for this kind of thing, so findings are comparable across seats. They are starting points; seats may add items.

## Code / PR / architecture
- Correctness: does it do what the description says? Edge inputs (empty, null, huge, concurrent, unicode, negative, time zones)? Error paths tested, not just the happy path?
- Safety: input validation, injection, auth/authz, secrets, data exposure, unsafe defaults, resource exhaustion.
- Reliability: failure modes of dependencies (timeouts, retries, idempotency, partial failure), migrations reversible, observability (logs/metrics for the failure the Red Team predicts).
- Maintainability: naming, size of units, hidden coupling, duplicated logic, dead code, tests as documentation.
- Performance: the operation that scales badly; the query without an index; the N+1.
- Change hygiene: scope creep in the diff, unrelated changes, missing docs/changelog, blast radius.
- Verifier priority: run the tests; run the new code path with adversarial input; check the dependency's actual API.

## Plan / strategy / business idea
- Problem: is it real, frequent, painful, and for whom? Evidence beyond the author's intuition?
- Mechanism: why would this work — what is the causal story from action to outcome?
- Economics: unit economics, CAC/LTV or equivalent, time to value, what has to be true for it to pay.
- Competition and substitutes: what people do today instead; why switch.
- Execution: team, time, sequencing, the first milestone that de-risks the most.
- Assumptions ledger: the three assumptions the plan dies without; cheapest test for each.
- Reversibility: what is committed at each stage; where the one-way doors are.
- Outside View priority: base rate for this class of venture/initiative; comparables and how they went.

## Document / argument / essay / report
- Thesis: stated in one sentence? Is the document actually about that?
- Support: each major claim backed by evidence of the right kind; citations say what they're cited for.
- Logic: valid inferences, no equivocation, no motte-and-bailey, counter-arguments engaged rather than ignored.
- Audience fit: register, assumed knowledge, length, what the reader needs to do after reading.
- Structure: can a skimmer get the point; does every section earn its place.
- Verifier priority: spot-check the five most load-bearing factual claims.

## Product / feature / UX
- Job to be done: whose, how often, what they do today.
- Flow: first-use walkthrough; where it breaks, confuses, or demands effort disproportionate to value.
- Scope: smallest version that tests the hypothesis; what is in the release that doesn't need to be.
- Metrics: how we will know it worked; the leading indicator; the guardrail metric.
- Edge users: accessibility, low-end devices, non-native language, abuse.
- Pragmatist priority: narrate the walkthrough for each stakeholder.

## Decision between options (A vs B vs C)
- Criteria: explicit, weighted by the objective, agreed before scoring.
- Each option assessed on each criterion separately before any overall ranking.
- Reversibility of each option; the option that preserves the most optionality.
- The conditions under which the losing option would win.
- The cheapest experiment that would discriminate between the top two.

## Prompt / skill / agent instructions
- Objective and success criteria stated; the model can tell when it is done.
- Ambiguity: instructions that can be read two ways; conflicting rules; MUSTs without reasons.
- Coverage: the edge cases the prompt will meet in practice; what happens on bad input.
- Length and load: does every section change behavior; can it be shorter.
- Testability: 3 realistic inputs where the current prompt would fail.
- Safety: does it ask the model to do anything it shouldn't; does it degrade gracefully.

## Research claim / analysis / data result
- Question clearly posed; the result actually answers it.
- Data provenance, sample, missingness, leakage; the analysis reproducible from what is given.
- Alternative explanations considered (confounding, selection, multiple comparisons, p-hacking).
- Effect size and uncertainty reported, not just significance.
- Generalization: to what population/conditions does the claim extend.
- Verifier priority: recompute at least one headline number from the raw inputs.

## Personal plan (study plan, routine, financial plan, career move)
- Objective concrete and dated; the plan's steps actually sum to it.
- Realism: hours per week vs available hours; dependencies on willpower vs on structure.
- Feedback loops: how the person will know they are on/off track each week.
- Failure recovery: what happens after a bad week; does the plan survive it.
- Outside View priority: how people in this situation typically fare; what the successful ones did differently.

## Creative work (design, copy, naming, visual identity)
- The brief's constraints are met, and each is checked separately.
- Legible and usable at real size, in the real context of use.
- Distinct from what the audience already sees.
- Rights and factual claims are checked.
- Taste is left to the owner: name defects and options, and do not rule on preference.
