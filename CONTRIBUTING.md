# Contributing

Issues and pull requests are welcome.

- **Protocol changes must say why**: a paper, a failed run, a measured effect. Add it to `skills/sota/references/evidence.md`. The rules here are meant to be traceable.
- **A new kind of subject** goes in `references/profiles.md`, with a checklist in `references/lenses.md` if one is needed. If it needs a new step in `SKILL.md`, the design may be wrong, so open an issue first.
- **A behavior bug** should come with an eval case under `evals/` that fails before the change.
- **Keep `SKILL.md` short.** Detail belongs in `references/`, one level deep.
- **The main README is in Portuguese, with `README.en.md` alongside it.** A change to either goes in both, in the same commit, above all a change to cost or limits. `scripts/validate.py` checks that they carry the same arXiv sources, numbers, heading count and table rows, not that their words match.

Before opening a pull request:

```bash
python3 scripts/validate.py
claude plugin validate .                 # if you use Claude Code
claude plugin eval . --scaffold --allow-tools Bash Write Edit --runs 3 --no-publish --max-cost-usd 20
```

The eval run costs tokens and starts agents. Granting Bash on Linux needs bubblewrap and socat. The default run also includes a baseline arm without the plugin.

Running the skill on your own change is encouraged, and the report makes a good PR description.
