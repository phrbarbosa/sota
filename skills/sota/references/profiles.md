# Profiles

The loop is the same for every subject. What changes is what each of its words means. Pick the closest row at round 0 and write the result into the ledger. Mixed subjects compose rows. A subject that fits none gets its own answers to the same five questions.

| Question | Meaning |
|---|---|
| **Reality surface** | What does the council read, so that it meets the thing the way its audience does? |
| **Matrix** | Across which conditions must a fix be re-measured? |
| **Gate** | What must pass before anything is released? |
| **Guard** | What check survives the round and goes red if the defect returns? |
| **Release** | What does "release" mean here? (The level is the owner's call, in the contract.) |

## Software with an interface

- **Reality surface:** a running build of this exact version, on its own port or preview, with data shaped like production. Mock data often lacks the very fields that expose the defect.
- **Matrix:** widths (for instance 320 · 390 · 768 · 1024 · 1280 · 1440) × roles × data states (empty, one, many, very long, failed) × themes × keyboard and screen reader.
- **Gate:** the project's tests, types, lint and build; an end-to-end check of the changed flow.
- **Guard:** an automated browser or interaction test. A pixel comparison is blind to behavior, so anything shared gets an interaction check on both narrow and wide layouts.
- **Release:** preview → production through the project's own deploy, with rollback noted.
- **Lens:** "Product / feature / UX" plus "Code".

## Backend, API, library, CLI

- **Reality surface:** the service running, or the package built and installed, and exercised from outside as a client would.
- **Matrix:** input classes (empty, huge, concurrent, malformed) × versions × environments × failure of each dependency.
- **Gate:** the test suite, contract tests, static checks. Read results from a structured report rather than scrolling output.
- **Guard:** a regression test, proven red against the unfixed code.
- **Release:** merge → tagged release or deploy. Data migrations always need their own consent.
- **Lens:** "Code".

## Writing: a message, report, essay, documentation

- **Reality surface:** the final rendered text as the reader receives it. Seats simulate each recipient doing the task the text is for, with no outside context.
- **Matrix:** audiences × tasks ("after reading, can this person do X?") × reading conditions (skim, phone, forwarded without context).
- **Gate:** a fact table in which every checkable claim has a source; every number and name checked against it.
- **Guard:** a line in that fact table, or a checklist item with the failing passage quoted as its evidence. Summaries of time, scope and quantity ("most of", "the last fix") are where simplification turns false, so check each one.
- **Release:** a new version file by default. Sending or publishing remains the owner's act.
- **Lens:** "Document / argument". State per audience what it must not receive. Requests for more detail are not majors by themselves.

## Plan, strategy, business idea

- **Reality surface:** the plan with its numbers recomputed from inputs, and any contact with the world you can get: a customer quote, a price page, a filed comparable, a small test.
- **Matrix:** scenarios (base, bad, very bad) × stakeholders × time horizons.
- **Gate:** an assumptions ledger in which every load-bearing assumption is labeled measured or hypothesis. No hypothesis is presented as a promise.
- **Guard:** a recomputation that fails if an input changes and the conclusion does not; an entry stating what would falsify each assumption.
- **Release:** a new version for the people who decide. Commitments remain the owner's.
- **Lens:** "Plan / strategy / business idea".

## Decision between options

- **Reality surface:** the cheapest real evidence that separates the top options. Open the sources and run the small experiment.
- **Matrix:** options × criteria, each scored separately × reversibility.
- **Gate:** criteria written before scoring; the conditions under which the losing option would win are stated.
- **Guard:** the falsifiers, recorded in the ledger with a date to check.
- **Release:** a written recommendation. The decision is the owner's.
- **Lens:** "Decision between options". Most decisions need one review and not a loop.

## Data, analysis, research claim

- **Reality surface:** the result re-derived from raw inputs in a clean environment.
- **Matrix:** segments × time windows × reasonable alternative specifications.
- **Gate:** reproducible from what is given; headline numbers recomputed; effect size and uncertainty reported.
- **Guard:** an assertion on the recomputed number, and a planted-error check on the pipeline.
- **Release:** a versioned report with data provenance.
- **Lens:** "Research claim / analysis / data result".

## Prompt, skill, agent

- **Reality surface:** the prompt run on realistic inputs in a fresh session. Reading it is not running it.
- **Matrix:** input classes (typical, adversarial, off-topic) × models × with and without tools.
- **Gate:** an eval suite, each case run more than once because outputs vary.
- **Guard:** an eval case that fails on the previous version.
- **Release:** a tagged version.
- **Lens:** "Prompt / skill / agent instructions".

## Product concept, service, process (no build yet)

- **Reality surface:** a walkthrough for each stakeholder, then the cheapest real probe: a mock shown to one person, a manual run of the process.
- **Matrix:** stakeholders × first use and repeated use × failure and recovery paths.
- **Gate:** a stated job to be done, a measure of success, and a guardrail metric.
- **Guard:** a recorded observation from the probe, not an opinion about it.
- **Release:** a revised concept document.
- **Lens:** "Product / feature / UX".

## Personal plan: study, routine, finances, career

- **Reality surface:** the plan tried for a real short period, or checked against the person's actual calendar and numbers.
- **Matrix:** a normal week × a bad week × missing a step.
- **Gate:** the steps add up to the objective, and the hours exist.
- **Guard:** a weekly checkpoint that says whether the plan is on or off track.
- **Release:** the owner adopts a version.
- **Lens:** "Personal plan".

## Creative work: design, copy, naming, visual identity

- **Reality surface:** the work in context, at real size, seen by people from the audience where possible.
- **Matrix:** contexts of use × audiences × first and repeated exposure.
- **Gate:** the brief's constraints are met, and factual claims and rights are checked.
- **Guard:** the brief's criteria as an explicit checklist. Taste remains the owner's: the council can find defects and name options, and the owner chooses.
- **Release:** a new version for the owner.
- **Lens:** "Creative work".

## High-stakes professional domains: law, medicine, finance, safety

High stakes means a wrong answer could cause harm the person could not absorb. A household budget is a personal plan; a loan, a medication change or a settlement is high stakes. Use the row that fits the artifact and add these rules:

- **Add a domain source-check seat**, and open primary sources (statutes, guidelines, standards, filings) in the jurisdiction and version that apply.
- **The council's output is preparation for a qualified professional, not a replacement for one.** Say so in every report, and list what the professional must decide.
- **Release is always `local`** until that professional has signed off, whatever the contract says.
