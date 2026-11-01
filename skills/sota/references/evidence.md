# Evidence base

Each entry: what a source found → the rule it motivates. Read this when someone asks why the protocol works this way or wants to change it. arXiv IDs were checked against the arXiv API on 2026-11-01, and each description was checked against its abstract for that ID. Classic works are cited from the literature and were not re-read for this file. Many of the 2025–2026 entries are recent preprints on narrow benchmarks, so read them as motivation for a design choice and not as settled findings.

## A. Independent judgment before interaction

- **Nominal groups beat interacting groups at idea generation** (Diehl & Stroebe 1987; Dennis & Valacich 1999). → Seats work in isolation and only the Chair pools.
- **Hidden profiles** (Stasser & Titus 1985; Schulz-Hardt et al.): groups fail to surface information held by one member. → `unique` findings are verified, never discarded for being unique.
- **Decision hygiene** (Kahneman, Sibony & Sunstein, *Noise*, 2021; Kahneman, Lovallo & Sibony, MIT Sloan Management Review 2019): keep assessments independent, review each separately, delay holistic intuition. → One report at a time; dimension table before the verdict.
- **Crowds need independent errors** (Condorcet 1785; Hong & Page 2004; Dietrich & Spiekermann 2019 as a critique): correlated errors collapse a crowd into one voice. → Seats differ by method and inputs; the Chair checks for collapse.

## B. Forced dissent beats consensus-seeking

- **Devil's advocacy and dialectical inquiry beat consensus approaches** (Schweiger, Sandberg & Ragan 1986; Schwenk 1990; Valacich & Schwenk 1995). → A standing Red Team and a standing Steelman.
- **Authentic dissent beats role-played dissent** (Nemeth, Brown & Rogers 2001; Schulz-Hardt et al. 2002). → Attacks must be anchored in evidence the seat can substantiate.
- **Groupthink** (Janis 1972). → The Chair shares no preliminary view; the dissent register is mandatory.

## C. What LLM multi-agent debate does

- **Positive results**: Du et al. 2023 ([2305.14325](https://arxiv.org/abs/2305.14325)); Liang et al. 2023 ([2305.19118](https://arxiv.org/abs/2305.19118)); ReConcile ([2309.13007](https://arxiv.org/abs/2309.13007)); ChatEval ([2308.07201](https://arxiv.org/abs/2308.07201)).
- **Critical re-examinations**: Smit et al. 2023, "Should we be going MAD?" ([2311.17371](https://arxiv.org/abs/2311.17371)); "Debate or Vote" ([2508.17536](https://arxiv.org/abs/2508.17536)); "Talk Isn't Always Cheap" ([2509.05396](https://arxiv.org/abs/2509.05396)); "Can LLM Agents Really Debate?" ([2511.07784](https://arxiv.org/abs/2511.07784)). → Contention is targeted, adversarial, evidence-gated, short, and skipped when nothing is contested.
- **"What Does Multi-Agent Debate Actually Change?"** ([2609.08016](https://arxiv.org/abs/2609.08016)): on opinion questions, instructions shifted reported agreement a great deal, while the selected option stayed the same in over 90% of comparisons. Expressed disagreement need not mean revised positions. → A position change only counts with named new evidence.
- **The Interaction Tax** ([2608.23541](https://arxiv.org/abs/2608.23541)): when agents read each other's full outputs, proposals converge within one round; independent generation avoids this. → No cross-talk before Phase 2.
- **Representational collapse** ([2604.03809](https://arxiv.org/abs/2604.03809)): three same-model agents with different role prompts on 100 GSM8K questions gave rationales with mean cosine similarity 0.888 and effective rank 2.17 of 3. → Seats are procedures, not personas; the Chair records signs of collapse.
- **The selection bottleneck** ([2603.20324](https://arxiv.org/abs/2603.20324)): diversity helps or hurts depending on aggregation quality. Win rate against a single-model baseline with judge-based selection: diverse team 0.810, homogeneous team 0.512. Selection strongly beat synthesis. → A strong Chair under an explicit protocol, and "select, do not blend".
- **Debate as oversight** (Khan et al. 2024, [2402.06782](https://arxiv.org/abs/2402.06782)): two persuasive debaters arguing opposite answers raised judge accuracy (humans 60% → 88%, LLM judges 48% → 76%). From the paper's body rather than its abstract: a single consultant gained less (78% and 54%), and with LLM judges, consultants optimized for persuasion lowered accuracy. → Contention uses paired advocate and challenger, never one unopposed summary.
- **Societies of thought** ([2601.10825](https://arxiv.org/abs/2601.10825)): reasoning models generate internal multi-perspective dialogue. → Explains why `lite` is weaker and not useless.

**Not established.** No source here tests method-differentiated seats on one model against a single reviewer or a persona panel. That remedy is this project's inference. Sources showing a benefit from diversity vary the model family (2603.20324, 2404.18796). Even across families, judge panels lose most of their independence ([2605.29800](https://arxiv.org/abs/2605.29800), on judging tasks with known answers). → Agreement raises priority for verification, and only external checks raise confidence.

## D. Persona prompting

- **Personas do not reliably improve accuracy**: Zheng et al. ([2311.10054](https://arxiv.org/abs/2311.10054)); "Persona is a Double-edged Sword" ([2408.08631](https://arxiv.org/abs/2408.08631)); "Playing Pretend" ([2512.05858](https://arxiv.org/abs/2512.05858)); "When Does Persona Prompting Actually Help?" ([2605.29420](https://arxiv.org/abs/2605.29420)). → Seat briefs are procedures, not identities.

## E. LLM-as-judge

- **Known biases**: Zheng et al. 2023 ([2306.05685](https://arxiv.org/abs/2306.05685)); "Judging the Judges" on position bias ([2406.07791](https://arxiv.org/abs/2406.07791)); surveys ([2411.15594](https://arxiv.org/abs/2411.15594), [2412.05579](https://arxiv.org/abs/2412.05579)); "Reliability without Validity" ([2606.19544](https://arxiv.org/abs/2606.19544)). → Anonymize and shuffle; judge content rather than length.
- **Panels beat a single judge** (Verga et al. 2024, [2404.18796](https://arxiv.org/abs/2404.18796)). Inter-judge disagreement can be treated as a signal that calls for human arbitration ([2605.24737](https://arxiv.org/abs/2605.24737), in a compliance setting). → Several seats, no averaging, and a dissent register.
- **Rubric interference** ([2608.14684](https://arxiv.org/abs/2608.14684)): judging several criteria in one pass shifts each verdict depending on the others present. Autorubric ([2603.00077](https://arxiv.org/abs/2603.00077)) catalogues criterion conflation and forced judgments. → Dimension table scored one row at a time, with discrete labels.
- **Evidence-grounded judging** (Rulers, [2601.08654](https://arxiv.org/abs/2601.08654)): fixed criteria with traceable evidence improved agreement with human scores. → Mandatory evidence anchors, opened during triage.

## F. Self-correction and the external signal

- **LLMs struggle to correct themselves without feedback**: Huang et al. 2023 ([2310.01798](https://arxiv.org/abs/2310.01798)); Kamoi et al. 2024 ([2406.01297](https://arxiv.org/abs/2406.01297)); Tyen et al. ([2311.08516](https://arxiv.org/abs/2311.08516)), who find models can correct an error once told where it is but cannot find it.
- **The Self-Correction Illusion** ([2606.05976](https://arxiv.org/abs/2606.05976)): presenting a byte-identical erroneous claim under an external role instead of the agent's own thought raised explicit correction by 23–93 percentage points, significant in 10 of 12 settings. → Fresh contexts, never `lite` on the session's own work.
- **Self-Refine** (Madaan et al. 2023, [2303.17651](https://arxiv.org/abs/2303.17651)): iterative refinement with feedback improves outputs. → The loop is built on refinement, and its feedback comes from fresh contexts and external checks.

## G. Forecasting and decision quality

- **Outside view** (Kahneman & Tversky; Tetlock & Gardner, *Superforecasting*, 2015). → The Outside View seat and the falsifiers.
- **Pre-mortem** (Klein 2007; Mitchell, Russo & Pennington 1989): assuming failure has happened yields more and more specific reasons. → Red Team step 1, and the pre-mortem line.
- **Reversibility** as a decision variable. → The brief records it, and one-way doors raise the bar.

## H. Lessons from real loop runs

These are field notes from about ten loops and a few council sessions on one production product, run before this public version took its current shape (screens, flows, a concept document, stakeholder messages). They are observations from a single owner's practice, not controlled results.

| Observation | Rule |
|---|---|
| Paper review took 6 rounds to converge; the first 2 rounds on the build found focus, layout and failure-state defects paper could not show | Reality from round 1; at most two paper rounds when a build can exist |
| 13 rounds with no pause meant 13 rounds of decisions the owner could not veto | Every pause asks |
| The last 4 of those rounds found only regressions, each from the previous fix, each at another width | Measure the whole matrix; stop condition 3 |
| In a message loop, 4 of 7 majors were new unsourced sentences introduced by fixes | New claims need a source |
| A Chair calibrated a "15×" promise against a range the input had labeled a hypothesis, and all seats rejected it the next round | Never calibrate against your own hypothesis |
| A consolidated revision inherited an earlier one "by reference", and its metrics disappeared | Copy what still applies in full |
| A shared component's change had a pixel diff of zero and was wrong in behavior | Blind medium, in `guards.md` |
| A guard proved a slot started empty and stayed green while it remained empty through many later changes | Half-truth, in `guards.md` |
| A guard whose list was copied into the test missed the newest item, three times | Copied list, in `guards.md` |
| Part-by-part reviewers checked 43 anchors against the code with no error, and the next round still found about 30 majors between parts | Consistency seat |
| A brief containing a reframing was followed by all five seats, which reviewers flagged as conformity | Keep interpretation out of the brief |
| A held-back release went out anyway when someone else published the shared line | Holding back does not contain a defect |
| A defect slipped past six seats and was caught by the final fresh verifier | Keep the fresh verifier |

## I. Prior art

Curia took ideas from these projects and combined them with the rules above:

- [karpathy/llm-council](https://github.com/karpathy/llm-council): anonymized peer review, chairman synthesis.
- [hex/claude-council](https://github.com/hex/claude-council): heterogeneous model seats; agreement and split as output.
- [amgadelgamal/claude-council](https://github.com/amgadelgamal/claude-council): a council built on subagents with no extra API keys.
- [wan-huiyan/agent-review-panel](https://github.com/wan-huiyan/agent-review-panel): domain checklists, anti-groupthink measures, the warning against a complexity ratchet.
- [brandonsimpson/devils-advocate](https://github.com/brandonsimpson/devils-advocate): evidence-located adversarial critique.
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills): criterion-bound judgments and "do not average".
- [MrLesk/agents-council](https://github.com/MrLesk/agents-council): cross-tool transport, compatible for heterogeneous seats.

The combination is the contribution: enforced independence, method-differentiated seats, debate gated on disagreement, evidence anchors that are opened, verification in a fresh context, dimension-by-dimension judgment, and a curated version with falsifiers. The loop adds to that: a written criterion, guards proven red, an explicit release contract, and an owner decision at every round.
