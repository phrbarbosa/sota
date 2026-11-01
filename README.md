# sota

**An agent skill that reviews anything against a written objective, shows its evidence, and improves it in rounds you approve: code, a UI, a document, a plan, a decision, a prompt.**

It does two things:

- **Review.** A council called Curia examines the thing with five different methods and returns a verdict you can check, prioritized fixes, and an improved version.
- **Loop.** Fix, verify, release as agreed, have a fresh council review what was released, then stop so you can decide whether another round is worth it.

```
/sota review the rollout plan in docs/rollout.md
/sota review my cover letter in letter.md
/sota review deep: should we migrate to UUID primary keys this sprint?
/sota loop our signup page feels generic; goal: a first-time user finishes in under a minute
/sota loop the grant proposal in proposal.md, paper only
/sota continue signup-page
```

Plain language works too: "red team this", "what am I missing?", "convoca a cúria". Reports come back in your language.

## Install

You need [Claude Code](https://code.claude.com/docs) (terminal, desktop or IDE) and a Claude plan or API key. No coding is needed to review a document or a plan: open Claude Code in the file's folder and type the command.

**As a plugin:**

```
/plugin marketplace add phrbarbosa/sota
/plugin install sota@phrbarbosa-sota
```

The command is then `/sota:sota`. `claude plugin update` and `claude plugin uninstall` manage it.

**As a personal skill**, for plain `/sota` (needs git):

```bash
git clone https://github.com/phrbarbosa/sota
mkdir -p ~/.claude/skills
cp -r sota/skills/sota ~/.claude/skills/sota
```

To upgrade, from the folder holding the clone:

```bash
git -C sota pull && rm -rf ~/.claude/skills/sota && cp -r sota/skills/sota ~/.claude/skills/sota
```

**Other agents:** `skills/sota` follows the open [Agent Skills](https://agentskills.io/specification) format, so copy it into your agent's skills directory. It has only been tested on Claude Code. A Review needs subagents or a headless CLI for its fresh contexts, and without either it falls back to a weaker single-context mode and says so. The Loop does not run without them.

## Why not just five personas and a judge?

Research on LLM committees points away from that design:

- Same-model agents with different role prompts produced rationales with [0.888 mean cosine similarity](https://arxiv.org/abs/2604.03809) in one study. Personas do not [reliably improve accuracy](https://arxiv.org/abs/2311.10054).
- When agents read each other's full outputs, their proposals [converge within one round](https://arxiv.org/abs/2608.23541).
- Presenting the same error as coming from outside, rather than as the model's own thought, [raised explicit correction by 23–93 points](https://arxiv.org/abs/2606.05976).
- Two opposed debaters [raised judge accuracy](https://arxiv.org/abs/2402.06782), while a single persuasive one lowered it.

So seats differ by **what they do**. None of these studies tests that remedy, and it is this project's inference: different methods produce different kinds of evidence, and evidence can be opened and checked.

| Seat | Method |
|---|---|
| Verifier | Runs it, opens the sources, recomputes the numbers |
| Red Team | Pre-mortem and strongest case against |
| Steelman & Upside | The best version, and what must be protected |
| Outside View | Base rates, prior art, comparables |
| Pragmatist | Walks through it as each affected person; looks for a simpler way |

Every finding needs an evidence anchor, and the Chair opens the anchors of blockers and majors. Debate happens only on real disagreement and on blockers raised by one seat alone. A surviving blocker goes to a fresh verifier that has not seen the deliberation. The main rules are traced to research or field notes in [`evidence.md`](skills/sota/references/evidence.md). Others, such as the release contract and the numeric caps, are design choices.

## What a review gives you

A verdict with confidence and its reason · what must change, each with evidence and a concrete fix · what to keep · the **curated version**, with whether it was checked · unresolved disagreements · what would flip the verdict and the cheapest test for it · one pre-mortem line.

Real outputs, unedited except where noted:

- [A school bake-sale plan](examples/bake-sale-review.md): a `standard` review, with its input.
- [A club announcement](examples/club-announcement-loop.md): round 0 and the first pause of a paper-only loop.
- [This repository, before release](examples/self-review.md): the review that changed this version, including findings against itself and the mistakes in its own patches.

## How the loop works

```
Round 0   Write a checkable criterion and a release contract → you approve → first version
Round N   Council reviews the REAL thing (running build, rendered text, recomputed numbers)
Pause     Version → release as agreed → next council → show what changed, the proof,
          what was found, the trajectory → ask: continue / continue with notes / stop / roll back
Closing   Verdict, what is live, what stays pending, the checks left behind
```

Four rules do most of the work:

1. **Nothing happens outward without a contract.** Invoking the skill authorizes no send, deploy, publish or purchase. You approve a release contract at round 0 (the default is local files only), and irreversible steps are confirmed again when they come due. The run itself uses your model allowance, and it says how much it will start.
2. **You decide at every round.** Nothing found is fixed before you have seen it.
3. **Reality over description.** Reviewing the running thing finds what reviewing its description does not. For a text, that means simulated readers doing the task it is for, and sources actually opened.
4. **Regressions get guards that were seen to fail.** Otherwise each fix breaks something elsewhere and the loop oscillates.

State lives in `.sota/<slug>/LEDGER.md`, which quotes you verbatim, so keep it out of anything you publish. [`profiles.md`](skills/sota/references/profiles.md) maps the loop onto interfaces, APIs, writing, plans, decisions, data, prompts, concepts, personal plans and creative work.

## What to expect

**Cost.** A `standard` review starts 5 agents, up to 10 more when there is something to contest, and up to 2 checkers. Optional seats and `deep` add more. A loop that starts from nothing can run up to three reviews before your first decision about a real version, and one more each round. Measured at API prices on an Opus-class model: USD 7.24 for a review of a short plan, USD 7.25 for one loop round on a short message, and about USD 19 for a review of this repository. These are three runs and not an average, and on a subscription they draw on your plan's allowance. For a small low-stakes thing, ask for `lite`, or don't use this skill.

**It does not always converge.** Three earlier loops, run on this protocol's predecessor on one product, went `9 → 4 → 5 → 2`, `9 → 7 → 7 → 7` and `13 → 15 → 14` in major findings per round. None reached zero, and each stopped on judgment once the findings stopped being worth a round. The skill names those stop signals. That record comes from one owner's practice and is not a benchmark.

**It can be confidently wrong.** It is designed to reduce reviewer error, and that has not been measured against one careful reviewer. All seats normally run on one model, so their agreement is weaker evidence than it looks. The bundled evals check behavior, such as not sending and not touching the original. They do not measure review quality, and their no-send cases also pass without the skill, so they show that it does not break that behavior rather than that it causes it. For law, medicine, finance or safety, its output prepares you for a qualified professional and does not replace one.

**Don't use it for** quick factual questions, trivial edits, or anything where the cheapest real test can simply be run now.

## Layout

```
skills/sota/
├── SKILL.md                     modes and the loop
└── references/
    ├── council.md               the review protocol
    ├── seats.md                 seat briefs and contention prompts
    ├── chair.md                 triage, dimensions, verdict rules
    ├── report-template.md
    ├── lenses.md                checklists by kind of artifact
    ├── profiles.md              the loop per kind of subject
    ├── guards.md                checks that actually guard
    ├── ledger-template.md       the state that crosses rounds
    └── evidence.md              research and field notes behind the rules
examples/                        real outputs
evals/                           behavior cases for `claude plugin eval`
scripts/validate.py              repo conventions and links, run in CI with skills-ref
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Protocol changes should say why: a paper, a failed run, a measured effect.

## License

[MIT](LICENSE)
