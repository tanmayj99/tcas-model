# tcas-model

A non-realtime Python model of the TCAS II Collision Avoidance System (CAS)
logic, per RTCA DO-185B Vol. II (2008).

Status: scaffold only. No TCAS logic is implemented yet. See
[docs/STATUS.md](docs/STATUS.md) for progress and [CLAUDE.md](CLAUDE.md) for
project conventions.

## Layout

- `tcas_model/` – the model package (`config`, `interfaces`, `functions`,
  `macros`, `cas`, `environment`, `sensor`, `analysis`)
- `tests/` – pytest suite
- `docs/design/` – per-item design docs (the source of truth for implementation)
- `docs/requirements/` – requirements notes
- `spec/` – local DO-185B excerpts (copyrighted, never committed)

## Running tests

Requires Python 3.11+.

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```
