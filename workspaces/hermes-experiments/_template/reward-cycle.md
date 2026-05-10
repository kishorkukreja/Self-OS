# Reward Cycle

## Cadence

Checkpoint after each meaningful run, or after a scheduled delay if this is a long-running goal experiment.

## Reward/eval signals

Use concrete signals instead of vibes:

- Did the agent produce the artifact named in `mission.md`?
- Did it preserve enough evidence for another agent to verify the result?
- Did it avoid scattering runtime files into wiki raw folders?
- Did review find a blocking flaw?
- Did the next step become clearer?

## Checkpoint prompt template

```text
Review this experiment workspace:
<workspace-path>

Read README.md, mission.md, reward-cycle.md, latest runs/, latest artifacts/, and latest reviews/.
Score whether the mission should continue, revise, or stop.
Write your review to reviews/YYYY-MM-DD-<reviewer>-checkpoint.md and update the current next step in mission.md if needed.
```

## Continue / revise / stop rules

- Continue when the latest run produced useful evidence and the next step is clear.
- Revise when the objective is still useful but the method or eval criteria are weak.
- Stop when the mission is complete, duplicated elsewhere, or no longer worth running.
