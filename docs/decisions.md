# Decision log

Format: `## YYYY-MM-DD: title`, then **Decision** and **Reason**.

## 2026-10-01: Start fresh

**Decision**: Start the model from a clean scaffold. Prior code is not reused.
The conventions from earlier work are retained in `CLAUDE.md`.

**Reason**: A clean start keeps every implemented item traceable to a design
doc in `docs/design/`, while keeping the conventions that worked.

## 2026-10-03: TRYMAX project value

Spec: DO-185B Vol. II App. A p. A-5 defines TRYMAX as "between 6 and 12
(manufacturer specific)". It is not a fixed standard value.
Decision: TRYMAX = 9.
Reason: Midpoint of the allowed range; no manufacturer data available.
Constraint: Any change must stay within 6..12 (enforced by TC-A-09).
Revisit: When coordination retry behavior is verified, or if a target
manufacturer value becomes known.
