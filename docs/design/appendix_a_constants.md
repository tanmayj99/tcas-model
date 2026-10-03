# Design: Appendix A — Constant Definitions

| | |
|---|---|
| **DO-185B reference** | Vol. II, Appendix A, pp. A-1 to A-6 |
| **Status** | Ready |
| **Target module** | `tcas_model/config/constants.py` |
| **Test module** | `tests/test_constants.py` |
| **Depends on** | Nothing |

## Scope

Define all 175 Appendix A constants as module-level Python names, plus a registry recording each constant's value, units and source page for traceability and logging. No logic, no derived values, no unit conversions.

## Items

| Name | Kind | DO-185B ref | Target |
|---|---|---|---|
| 175 named constants | Constant | App. A, A-1 to A-6 | `config/constants.py` |
| `APPENDIX_A` registry | Data | App. A | `config/constants.py` |

## Implementation rules

1. **Names** are exactly as printed in Appendix A, including underscores and digits (`DZTHR_100`, `P_P_NOISE_FACTOR`).
2. **Order** follows Appendix A page order (alphabetical as printed), with a comment line `# --- Appendix A, p. A-n ---` at each page boundary. This keeps line-by-line review against the spec trivial. Do not regroup by category.
3. **Values** are exactly as in the table below. Do not convert units: ft/min stays ft/min, ft/s stays ft/s, nmi stays nmi. Conversions belong in the functions that use the constants, as the pseudocode specifies them.
4. **Types** follow one mechanical rule. A value printed with units or a decimal point is a `float`. A unitless integer as printed is an `int`. The table's Type column already applies this rule.
5. **Every line carries a trailing comment** with units and page, e.g. `ABOVNMC = 15500.0  # ft, A-1`. Dimensionless constants use `# dimensionless, A-n`.
6. **Registry.** At the end of the module, define `APPENDIX_A: dict[str, tuple[int | float, str, str]]` mapping each name to `(value, units, page)`, e.g. `"ABOVNMC": (ABOVNMC, "ft", "A-1")`. Reference the module-level names; never repeat the literal values. Use `""` for dimensionless.
7. **TRYMAX** is the only constant the standard doesn't fix. Define `TRYMAX = 9` with the comment `# manufacturer specific, 6..12 per App. A p. A-5; project value, see docs/decisions.md`. Its registry entry is `(TRYMAX, "", "A-5")`. Also define `MANUFACTURER_SPECIFIC: dict[str, tuple[int, int]] = {"TRYMAX": (6, 12)}`, holding the allowed range as stated in Appendix A. This dict is not part of `APPENDIX_A` and is not counted in the 175.
8. **Nothing else goes in this module.** No constants not printed in Appendix A, no aliases, and no derived quantities.

## Constant table

Units notation: `ft/s^2` = ft/s², `(ft/s^2)^2` = (ft/s²)², `—` = dimensionless.

| # | Name | Value | Units | Page | Type |
|---|---|---|---|---|---|
| 1 | `AB_COEFF` | 3 | — | A-1 | int |
| 2 | `ABOVNMC` | 15500.0 | ft | A-1 | float |
| 3 | `ADEQSEP` | 100.0 | ft | A-1 | float |
| 4 | `ALERTER_TMAX` | 300.0 | s | A-1 | float |
| 5 | `ALERTER_TMIN` | 5.0 | s | A-1 | float |
| 6 | `ALFAO` | 0.58 | — | A-1 | float |
| 7 | `AVEVALT` | 200.0 | ft | A-1 | float |
| 8 | `BACKDELAY` | -2.5 | s | A-1 | float |
| 9 | `BBCC_DISABLE_VAL` | 100.0 | nmi | A-1 | float |
| 10 | `BETAO` | 0.25 | — | A-1 | float |
| 11 | `CLMRT` | 1500.0 | ft/min | A-1 | float |
| 12 | `COAST_ACCEL` | 32.2 | ft/s^2 | A-1 | float |
| 13 | `CREDACCDIV` | 20.0 | ft/s^2 | A-1 | float |
| 14 | `CREDINIT` | 200.0 | ft/s | A-1 | float |
| 15 | `CREDMINDT` | 5.5 | s | A-1 | float |
| 16 | `CREDZADC` | 65.0 | ft | A-1 | float |
| 17 | `CREDZDERR` | 30.0 | ft/s | A-1 | float |
| 18 | `CROSSTHR` | 100.0 | ft | A-1 | float |
| 19 | `DELZDT` | 4.0 | s | A-1 | float |
| 20 | `DELZTHR` | 20.0 | ft | A-1 | float |
| 21 | `DESRT` | -1500.0 | ft/min | A-1 | float |
| 22 | `DMOD_MDF` | 18000.0 | ft | A-1 | float |
| 23 | `DT` | 1.0 | s | A-1 | float |
| 24 | `DTCOAST` | 2.5 | s | A-1 | float |
| 25 | `DTLONG` | 6.5 | s | A-1 | float |
| 26 | `DTSTART` | 2.5 | s | A-1 | float |
| 27 | `DZTHR_100` | 60.0 | ft | A-1 | float |
| 28 | `DZTHR_25` | 22.5 | ft | A-1 | float |
| 29 | `EARLYLATE` | 1.5 | s | A-1 | float |
| 30 | `GAMMAZ` | 0.5 | — | A-2 | float |
| 31 | `GUESDU1` | 4.5 | s | A-2 | float |
| 32 | `GUESDU2` | 9.5 | s | A-2 | float |
| 33 | `GUESDU3` | 14.5 | s | A-2 | float |
| 34 | `GUESRATE` | 480.0 | ft/min | A-2 | float |
| 35 | `HI1` | 2.0 | — | A-2 | float |
| 36 | `HI2` | 1.5 | — | A-2 | float |
| 37 | `HI3` | 1.25 | — | A-2 | float |
| 38 | `HISCORE` | 1200 | — | A-2 | int |
| 39 | `HMD_DISABLE_VAL` | -1.0 | ft | A-2 | float |
| 40 | `HMD_RB_TAU_THRESHOLD` | 100.0 | s | A-2 | float |
| 41 | `HMDMULT` | 1.05 | — | A-2 | float |
| 42 | `HUGE` | 100000.0 | ft/min | A-2 | float |
| 43 | `HUGEDZ` | 75.0 | ft | A-2 | float |
| 44 | `HYSTERCOR` | 300.0 | ft/min | A-2 | float |
| 45 | `ILEV` | 1000.0 | ft/min | A-2 | float |
| 46 | `INC_ADD_SEP` | 50.0 | ft | A-2 | float |
| 47 | `INC_CLMRATE` | 2500.0 | ft/min | A-2 | float |
| 48 | `INC_DESRATE` | -2500.0 | ft/min | A-2 | float |
| 49 | `INC_TAU_THR` | 6.0 | s | A-2 | float |
| 50 | `INITCOUNT` | 5 | — | A-2 | int |
| 51 | `LARGEDZ` | 22.5 | ft | A-2 | float |
| 52 | `LATELEVEL` | 4.5 | s | A-2 | float |
| 53 | `LATESLACK` | 0.5 | s | A-2 | float |
| 54 | `LEVOFFACCX2` | 8.0 | ft/s^2 | A-2 | float |
| 55 | `LO1` | 0.0 | — | A-2 | float |
| 56 | `LO2` | 0.667 | — | A-2 | float |
| 57 | `LO3` | 0.8 | — | A-2 | float |
| 58 | `LONGCOAST` | 3.5 | s | A-2 | float |
| 59 | `LOSCORE` | 100 | — | A-2 | int |
| 60 | `LOWFIRMRZ` | 150.0 | ft | A-2 | float |
| 61 | `MAXALTDIFF` | 600.0 | ft | A-3 | float |
| 62 | `MAXALTDIFF2` | 850.0 | ft | A-3 | float |
| 63 | `MAXBINS` | 8 | — | A-3 | int |
| 64 | `MAXDRATE` | 4400.0 | ft/min | A-3 | float |
| 65 | `MAXSOFT` | 5 | — | A-3 | int |
| 66 | `MAXZDINT` | 10000.0 | ft/min | A-3 | float |
| 67 | `MAXZDTIME` | 17.0 | s | A-3 | float |
| 68 | `MEDHISCORE` | 500 | — | A-3 | int |
| 69 | `MEDLOSCORE` | 300 | — | A-3 | int |
| 70 | `MEDSCORE` | 400 | — | A-3 | int |
| 71 | `MINBINS` | 3 | — | A-3 | int |
| 72 | `MINDRATE` | -4400.0 | ft/min | A-3 | float |
| 73 | `MINFIRM` | 2 | — | A-3 | int |
| 74 | `MINRITIME` | 4.0 | s | A-3 | float |
| 75 | `MINRVSTIME` | 10.0 | s | A-3 | float |
| 76 | `MINTATIME` | 8.0 | s | A-3 | float |
| 77 | `MINTAU` | 0.0 | s | A-3 | float |
| 78 | `MODEL_T` | 9.0 | s | A-3 | float |
| 79 | `MODEL_ZD` | 2500.0 | ft/min | A-3 | float |
| 80 | `NAFRANGE` | 1.7 | nmi | A-3 | float |
| 81 | `NBINSNL` | 5 | — | A-3 | int |
| 82 | `NEWVSL` | 75.0 | ft | A-3 | float |
| 83 | `NODESHI` | 1200.0 | ft | A-3 | float |
| 84 | `NODESLO` | 1000.0 | ft | A-3 | float |
| 85 | `NOWEAK` | 10.0 | s | A-3 | float |
| 86 | `NOZCROSS` | 100.0 | ft | A-3 | float |
| 87 | `NSGNCT` | 0.1 | — | A-3 | float |
| 88 | `OLEV` | 600.0 | ft/min | A-3 | float |
| 89 | `OUT2` | 1.1 | s | A-3 | float |
| 90 | `OUT3` | 0.55 | s | A-3 | float |
| 91 | `OVERDUE` | 3.5 | s | A-3 | float |
| 92 | `P_ACCTHR` | 1.5 | ft/s^2 | A-4 | float |
| 93 | `P_ALPHA3D` | 0.1 | — | A-4 | float |
| 94 | `P_ALPHARESSQ` | 0.1 | — | A-4 | float |
| 95 | `P_INITRHODDTHR` | 9999 | — | A-4 | int |
| 96 | `P_MAXRANGERESID` | 150.0 | ft | A-4 | float |
| 97 | `P_MAXSIGDPX` | 3 | — | A-4 | int |
| 98 | `P_MINSIGDPX` | 0.7 | — | A-4 | float |
| 99 | `P_P_NOISE_FACTOR` | 100.0 | — | A-4 | float |
| 100 | `P_PROCNOIVAR` | 2.56 | (ft/s^2)^2 | A-4 | float |
| 101 | `P_RESDL_SIGMAS` | -3 | — | A-4 | int |
| 102 | `P_RESSD_C_EXP_FACT` | 1.2 | — | A-4 | float |
| 103 | `P_RESSD_N` | 35.0 | ft | A-4 | float |
| 104 | `P_VAR_BRNG` | 7.569e-3 | — | A-4 | float |
| 105 | `PROXA` | 1200.0 | ft | A-4 | float |
| 106 | `PROXR` | 6.0 | nmi | A-4 | float |
| 107 | `Q100` | 100.0 | ft | A-4 | float |
| 108 | `Q25` | 25.0 | ft | A-4 | float |
| 109 | `Q50` | 50.0 | ft | A-4 | float |
| 110 | `QUIKREAC` | 2.5 | s | A-4 | float |
| 111 | `RACCEL` | 11.2 | ft/s^2 | A-4 | float |
| 112 | `RADARLOST` | 10 | — | A-4 | int |
| 113 | `RDTHR` | 10.0 | ft/s | A-4 | float |
| 114 | `RDTHRTA` | 10.0 | ft/s | A-4 | float |
| 115 | `RESIDECAY` | 0.5 | — | A-4 | float |
| 116 | `RESIDIMIN` | 0.8 | — | A-4 | float |
| 117 | `RMAX` | 12.0 | nmi | A-4 | float |
| 118 | `RRD_THR` | 10 | — | A-4 | int |
| 119 | `SLACKEN1` | 3.5 | s | A-4 | float |
| 120 | `SLACKEN2` | 6.5 | s | A-4 | float |
| 121 | `SLITEOFF` | 1.35 | s | A-4 | float |
| 122 | `SMALLZD` | 5.0 | ft/s | A-4 | float |
| 123 | `STIMOUT` | 240.0 | s | A-5 | float |
| 124 | `STROFIR` | 20.0 | s | A-5 | float |
| 125 | `TARHYST` | 0.20 | nmi | A-5 | float |
| 126 | `TBINHI` | 1.1 | s | A-5 | float |
| 127 | `TBINLO` | 0.9 | s | A-5 | float |
| 128 | `TBINMIN` | 2.0 | s | A-5 | float |
| 129 | `TCATRES` | 6.0 | s | A-5 | float |
| 130 | `TGOLEV` | 20.5 | s | A-5 | float |
| 131 | `TIETHR` | 3.0 | s | A-5 | float |
| 132 | `TINITZD` | 5.5 | s | A-5 | float |
| 133 | `TINYSCORE` | 40 | — | A-5 | int |
| 134 | `TINYZD` | 2.5 | ft/s | A-5 | float |
| 135 | `TTLORATE` | 1000.0 | ft/min | A-5 | float |
| 136 | `TTLOSEP` | 800.0 | ft | A-5 | float |
| 137 | `TTLOZD` | 600.0 | ft/min | A-5 | float |
| 138 | `TMIN` | 4.5 | s | A-5 | float |
| 139 | `TRVSNOWEAK` | 5.0 | s | A-5 | float |
| 140 | `TRYMAX` | 9 | — | A-5 | int |
| 141 | `TTRENDMIN` | 2.5 | s | A-5 | float |
| 142 | `TV1` | 5.0 | s | A-5 | float |
| 143 | `V0` | 0.0 | ft/min | A-5 | float |
| 144 | `V1000` | 1000.0 | ft/min | A-5 | float |
| 145 | `V2000` | 2000.0 | ft/min | A-5 | float |
| 146 | `V500` | 500.0 | ft/min | A-5 | float |
| 147 | `VACCEL` | 8.0 | ft/s^2 | A-5 | float |
| 148 | `VELOCITY_THRESHOLD` | -10.0 | ft/s | A-5 | float |
| 149 | `ZDABTHR` | 7.0 | ft/s | A-5 | float |
| 150 | `ZDDABTHR` | 2.0 | ft/s^2 | A-5 | float |
| 151 | `ZDDECAY` | 0.9 | — | A-5 | float |
| 152 | `ZDESBOT` | 900.0 | ft | A-5 | float |
| 153 | `ZDFRACC` | 1.3 | — | A-5 | float |
| 154 | `ZDLARGE` | 12000.0 | ft/min | A-6 | float |
| 155 | `ZDLIKELY` | 3000.0 | ft/min | A-6 | float |
| 156 | `ZDTHR` | -1.0 | ft/s | A-6 | float |
| 157 | `ZDTHRTA` | -1.0 | ft/s | A-6 | float |
| 158 | `ZLARGE` | 100000.0 | ft | A-6 | float |
| 159 | `ZLIMITL` | 50.0 | ft | A-6 | float |
| 160 | `ZLIMITU` | 60.0 | ft | A-6 | float |
| 161 | `ZNO_AURALHI` | 600.0 | ft | A-6 | float |
| 162 | `ZNO_AURALLO` | 400.0 | ft | A-6 | float |
| 163 | `ZNOINCDESHI` | 1650.0 | ft | A-6 | float |
| 164 | `ZNOINCDESLO` | 1450.0 | ft | A-6 | float |
| 165 | `ZRJIT` | 0.24 | — | A-6 | float |
| 166 | `ZSL2TO3` | 1100.0 | ft | A-6 | float |
| 167 | `ZSL3TO2` | 900.0 | ft | A-6 | float |
| 168 | `ZSL3TO4` | 2550.0 | ft | A-6 | float |
| 169 | `ZSL4TO3` | 2150.0 | ft | A-6 | float |
| 170 | `ZSL4TO5` | 5500.0 | ft | A-6 | float |
| 171 | `ZSL5TO4` | 4500.0 | ft | A-6 | float |
| 172 | `ZSL5TO6` | 10500.0 | ft | A-6 | float |
| 173 | `ZSL6TO5` | 9500.0 | ft | A-6 | float |
| 174 | `ZSL6TO7` | 20500.0 | ft | A-6 | float |
| 175 | `ZSL7TO6` | 19500.0 | ft | A-6 | float |
**Count check:** A-1: 29, A-2: 31, A-3: 31, A-4: 31, A-5: 31, A-6: 22. Total 175.

## Edge cases and transcription notes

- **MINDRATE sign.** The PDF text layer reads `4,400 ft/min`, but the rendered page shows `–4,400 ft/min`. Tabled as **−4400.0**, consistent with MAXDRATE = +4400 forming a symmetric pair. See OQ-1.
- **NOWEAK** is printed as `10s` (missing space). Value 10.0 s.
- **RADARLOST** is printed without units. Treated as dimensionless; don't attach units the spec doesn't state.
- **P_VAR_BRNG** is printed as `7.569x10-3`, i.e. 7.569 × 10⁻³, without units. Write it as `7.569e-3`.
- **P_PROCNOIVAR** has units (ft/s²)², a variance.
- **DMOD_MDF** is in **ft** (18,000 ft), not nmi, even though most range-like constants are in nmi. Keep it in ft.
- **HMD_DISABLE_VAL** (−1 ft) is a sentinel value. Keep it as-is; callers compare against it.
- **Mixed rate units.** The spec deliberately uses both ft/min (e.g. CLMRT, ILEV) and ft/s (e.g. RDTHR, SMALLZD). The units comment on every line is the guard against mixing them.
- **Negative constants** (9 total): BACKDELAY, DESRT, HMD_DISABLE_VAL, INC_DESRATE, MINDRATE, P_RESDL_SIGMAS, VELOCITY_THRESHOLD, ZDTHR, ZDTHRTA.

## Test vectors (`tests/test_constants.py`)

| ID | Test | Expected |
|---|---|---|
| TC-A-01 | `len(APPENDIX_A)` | 175 |
| TC-A-02 | Every table name exists as a module attribute | True for all 175 |
| TC-A-03 | Every module-level ALL_CAPS name is in `APPENDIX_A`, except `APPENDIX_A` and `MANUFACTURER_SPECIFIC` (no extras) | No extras |
| TC-A-04 | Each constant's value equals the table value (parametrized over the full table; floats compared with `math.isclose(rel_tol=0, abs_tol=1e-12)`) | All equal |
| TC-A-05 | Each constant's type matches the table's Type column | All match |
| TC-A-06 | Registry value is the same object as the module attribute | All identical |
| TC-A-07 | Registry units and page match the table | All match |
| TC-A-08 | The set of negative-valued constants equals the 9 listed above | Exact set match |
| TC-A-09 | `MANUFACTURER_SPECIFIC == {"TRYMAX": (6, 12)}`; `isinstance(TRYMAX, int)`; `lo <= TRYMAX <= hi`; the test asserts the range literal (6, 12) independently rather than reading it from the module | True |
| TC-A-10 | Spot checks: `MINDRATE == -MAXDRATE`, `DMOD_MDF == 18000.0`, `P_VAR_BRNG == 7.569e-3`, `DT == 1.0` | True |

The test file holds its own copy of the table as expected data. It must not import the expected values from `constants.py`, or the tests would be checking the module against itself.

## Resolved questions

- **OQ-1: MINDRATE sign.** Confirmed −4400.0 on p. A-3. (The PDF text layer omits the minus sign. The rendered page and the user's copy show it.)
- **OQ-2: TRYMAX value.** 9, chosen as the project value within Appendix A's manufacturer-specific range of 6–12. Recorded in `docs/decisions.md`, in the code comment, and in `MANUFACTURER_SPECIFIC`, and enforced by TC-A-09.

## Decision log entry (add to `docs/decisions.md` in the same PR)

```
## YYYY-MM-DD: TRYMAX project value
Spec: DO-185B Vol. II App. A p. A-5 defines TRYMAX as "between 6 and 12
(manufacturer specific)". It is not a fixed standard value.
Decision: TRYMAX = 9.
Reason: Midpoint of the allowed range; no manufacturer data available.
Constraint: Any change must stay within 6..12 (enforced by TC-A-09).
Revisit: When coordination retry behavior is verified, or if a target
manufacturer value becomes known.
```

## Handoff prompt for Claude Code

```
Implement docs/design/appendix_a_constants.md exactly, following CLAUDE.md.
Create tcas_model/config/constants.py and tests/test_constants.py.
Add the TRYMAX entry from the design doc to docs/decisions.md.
Run pytest. Update docs/STATUS.md. Open a PR.
If anything in the design doc is ambiguous, stop and report instead of guessing.
```
