# CLAUDE.md

## Project

- Non-realtime model of the TCAS II Collision Avoidance System (CAS) logic,
  written in Python, per RTCA DO-185B Vol. II (2008).
- Fixed 1 s timestep (`DT`).
- Mode S messages are exchanged as decoded data; there is no pulse-level
  simulation.
- No Stateflow. State machines are implemented as Python classes.

## Source of truth

- Implement ONLY from `docs/design/*.md`.
- If a design doc has an open question, or anything is ambiguous, STOP and
  report it. Do not guess.
- Never invent constants, table values, or thresholds.
- Never reinterpret the standard.

## Naming

- Use DO-185B names exactly. Constants are ALL_CAPS (e.g. `RDTHRTA`,
  `ZSL2TO3`).
- State names are strings that match the spec exactly.
- Every numeric constant carries its units in a comment.
- Docstrings cite the DO-185B section and page.

## Conventions

- **State machine**: a class with state constants, a default `self.state`, a
  `state_entry_time` dict, and `update(inputs, t)` which calls
  `_transition()` then `_compute_outputs()`. `_enter_state()` records the
  entry time.
- **PREV(x)**: an instance attribute, updated at the end of `update()`.
- **Timeouts**: `t - state_entry_time[state] >= limit`.
- **AND/OR tables**: columns are OR'd; rows within a column are AND'd; a dot
  means the row is omitted for that column. Use one local bool per column,
  named `col_1`, `col_2`, ...
- **Statechart arrays**: a list of instances; `THIS` is `self.index`.
- **Parallel states**: every sub-machine is updated every cycle.
- **Macro** = module-level function returning `bool`.
  **Function** = module-level function returning a value.
  **Abbreviation** = local ALL_CAPS variable.
- **Events**: string constants with the exact DO-185B names (some lack the
  `_Event` suffix). A synchronous `EventBus`: `publish()` queues;
  `dispatch_all()` runs once per timestep (synchrony hypothesis, App. D).
- **Identity transitions** still emit their output events.
- **Interfaces**: plain dataclasses with `Literal` types; not stored.

## Workflow

- One design doc per PR.
- Write tests from the design doc's test vectors.
- Run `pytest` before opening the PR.
- Update `docs/STATUS.md` in every PR.
