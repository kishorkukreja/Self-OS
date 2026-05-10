# Mission

## Objective

State the concrete experiment objective in one paragraph.

## Definition of done

- [ ] A real artifact exists, not just a plan.
- [ ] Evidence is saved under `artifacts/`, `runs/`, or `reviews/`.
- [ ] A reviewer can decide continue/revise/stop from the evidence.
- [ ] The Kanban card is completed or blocked with a clear handoff.

## Constraints

- Do not commit secrets or raw credentials.
- Do not put temporary run logs in wiki raw folders.
- Keep the experiment minimal until there is evidence it needs more structure.
- Prefer the existing `default` Hermes profile unless profile separation is justified.

## Evaluation criteria

| Criterion | Pass condition | Evidence path |
| --- | --- | --- |
| Usability | Future agent can resume from `README.md` and this mission. | `README.md`, `mission.md` |
| Artifact quality | Outputs are specific, inspectable, and not only prose claims. | `artifacts/` |
| Reviewability | Independent review checks work against mission criteria. | `reviews/` |
| Routing discipline | Durable knowledge/backlog/execution artifacts went to the right stores. | completion metadata |

## Current next step

Replace this with the next action and update after each checkpoint.
