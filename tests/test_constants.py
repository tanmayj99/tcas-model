"""Tests for tcas_model.config.constants.

DO-185B Vol. II, Appendix A, pp. A-1 to A-6.
Test vectors TC-A-01 to TC-A-10 from docs/design/appendix_a_constants.md.

EXPECTED is an independent copy of the design doc table. It must not be
imported from constants.py.
"""

import math

import pytest

from tcas_model.config import constants

# (name, value, units, page, type)
EXPECTED = [
    ("AB_COEFF", 3, "", "A-1", int),
    ("ABOVNMC", 15500.0, "ft", "A-1", float),
    ("ADEQSEP", 100.0, "ft", "A-1", float),
    ("ALERTER_TMAX", 300.0, "s", "A-1", float),
    ("ALERTER_TMIN", 5.0, "s", "A-1", float),
    ("ALFAO", 0.58, "", "A-1", float),
    ("AVEVALT", 200.0, "ft", "A-1", float),
    ("BACKDELAY", -2.5, "s", "A-1", float),
    ("BBCC_DISABLE_VAL", 100.0, "nmi", "A-1", float),
    ("BETAO", 0.25, "", "A-1", float),
    ("CLMRT", 1500.0, "ft/min", "A-1", float),
    ("COAST_ACCEL", 32.2, "ft/s^2", "A-1", float),
    ("CREDACCDIV", 20.0, "ft/s^2", "A-1", float),
    ("CREDINIT", 200.0, "ft/s", "A-1", float),
    ("CREDMINDT", 5.5, "s", "A-1", float),
    ("CREDZADC", 65.0, "ft", "A-1", float),
    ("CREDZDERR", 30.0, "ft/s", "A-1", float),
    ("CROSSTHR", 100.0, "ft", "A-1", float),
    ("DELZDT", 4.0, "s", "A-1", float),
    ("DELZTHR", 20.0, "ft", "A-1", float),
    ("DESRT", -1500.0, "ft/min", "A-1", float),
    ("DMOD_MDF", 18000.0, "ft", "A-1", float),
    ("DT", 1.0, "s", "A-1", float),
    ("DTCOAST", 2.5, "s", "A-1", float),
    ("DTLONG", 6.5, "s", "A-1", float),
    ("DTSTART", 2.5, "s", "A-1", float),
    ("DZTHR_100", 60.0, "ft", "A-1", float),
    ("DZTHR_25", 22.5, "ft", "A-1", float),
    ("EARLYLATE", 1.5, "s", "A-1", float),
    ("GAMMAZ", 0.5, "", "A-2", float),
    ("GUESDU1", 4.5, "s", "A-2", float),
    ("GUESDU2", 9.5, "s", "A-2", float),
    ("GUESDU3", 14.5, "s", "A-2", float),
    ("GUESRATE", 480.0, "ft/min", "A-2", float),
    ("HI1", 2.0, "", "A-2", float),
    ("HI2", 1.5, "", "A-2", float),
    ("HI3", 1.25, "", "A-2", float),
    ("HISCORE", 1200, "", "A-2", int),
    ("HMD_DISABLE_VAL", -1.0, "ft", "A-2", float),
    ("HMD_RB_TAU_THRESHOLD", 100.0, "s", "A-2", float),
    ("HMDMULT", 1.05, "", "A-2", float),
    ("HUGE", 100000.0, "ft/min", "A-2", float),
    ("HUGEDZ", 75.0, "ft", "A-2", float),
    ("HYSTERCOR", 300.0, "ft/min", "A-2", float),
    ("ILEV", 1000.0, "ft/min", "A-2", float),
    ("INC_ADD_SEP", 50.0, "ft", "A-2", float),
    ("INC_CLMRATE", 2500.0, "ft/min", "A-2", float),
    ("INC_DESRATE", -2500.0, "ft/min", "A-2", float),
    ("INC_TAU_THR", 6.0, "s", "A-2", float),
    ("INITCOUNT", 5, "", "A-2", int),
    ("LARGEDZ", 22.5, "ft", "A-2", float),
    ("LATELEVEL", 4.5, "s", "A-2", float),
    ("LATESLACK", 0.5, "s", "A-2", float),
    ("LEVOFFACCX2", 8.0, "ft/s^2", "A-2", float),
    ("LO1", 0.0, "", "A-2", float),
    ("LO2", 0.667, "", "A-2", float),
    ("LO3", 0.8, "", "A-2", float),
    ("LONGCOAST", 3.5, "s", "A-2", float),
    ("LOSCORE", 100, "", "A-2", int),
    ("LOWFIRMRZ", 150.0, "ft", "A-2", float),
    ("MAXALTDIFF", 600.0, "ft", "A-3", float),
    ("MAXALTDIFF2", 850.0, "ft", "A-3", float),
    ("MAXBINS", 8, "", "A-3", int),
    ("MAXDRATE", 4400.0, "ft/min", "A-3", float),
    ("MAXSOFT", 5, "", "A-3", int),
    ("MAXZDINT", 10000.0, "ft/min", "A-3", float),
    ("MAXZDTIME", 17.0, "s", "A-3", float),
    ("MEDHISCORE", 500, "", "A-3", int),
    ("MEDLOSCORE", 300, "", "A-3", int),
    ("MEDSCORE", 400, "", "A-3", int),
    ("MINBINS", 3, "", "A-3", int),
    ("MINDRATE", -4400.0, "ft/min", "A-3", float),
    ("MINFIRM", 2, "", "A-3", int),
    ("MINRITIME", 4.0, "s", "A-3", float),
    ("MINRVSTIME", 10.0, "s", "A-3", float),
    ("MINTATIME", 8.0, "s", "A-3", float),
    ("MINTAU", 0.0, "s", "A-3", float),
    ("MODEL_T", 9.0, "s", "A-3", float),
    ("MODEL_ZD", 2500.0, "ft/min", "A-3", float),
    ("NAFRANGE", 1.7, "nmi", "A-3", float),
    ("NBINSNL", 5, "", "A-3", int),
    ("NEWVSL", 75.0, "ft", "A-3", float),
    ("NODESHI", 1200.0, "ft", "A-3", float),
    ("NODESLO", 1000.0, "ft", "A-3", float),
    ("NOWEAK", 10.0, "s", "A-3", float),
    ("NOZCROSS", 100.0, "ft", "A-3", float),
    ("NSGNCT", 0.1, "", "A-3", float),
    ("OLEV", 600.0, "ft/min", "A-3", float),
    ("OUT2", 1.1, "s", "A-3", float),
    ("OUT3", 0.55, "s", "A-3", float),
    ("OVERDUE", 3.5, "s", "A-3", float),
    ("P_ACCTHR", 1.5, "ft/s^2", "A-4", float),
    ("P_ALPHA3D", 0.1, "", "A-4", float),
    ("P_ALPHARESSQ", 0.1, "", "A-4", float),
    ("P_INITRHODDTHR", 9999, "", "A-4", int),
    ("P_MAXRANGERESID", 150.0, "ft", "A-4", float),
    ("P_MAXSIGDPX", 3, "", "A-4", int),
    ("P_MINSIGDPX", 0.7, "", "A-4", float),
    ("P_P_NOISE_FACTOR", 100.0, "", "A-4", float),
    ("P_PROCNOIVAR", 2.56, "(ft/s^2)^2", "A-4", float),
    ("P_RESDL_SIGMAS", -3, "", "A-4", int),
    ("P_RESSD_C_EXP_FACT", 1.2, "", "A-4", float),
    ("P_RESSD_N", 35.0, "ft", "A-4", float),
    ("P_VAR_BRNG", 7.569e-3, "", "A-4", float),
    ("PROXA", 1200.0, "ft", "A-4", float),
    ("PROXR", 6.0, "nmi", "A-4", float),
    ("Q100", 100.0, "ft", "A-4", float),
    ("Q25", 25.0, "ft", "A-4", float),
    ("Q50", 50.0, "ft", "A-4", float),
    ("QUIKREAC", 2.5, "s", "A-4", float),
    ("RACCEL", 11.2, "ft/s^2", "A-4", float),
    ("RADARLOST", 10, "", "A-4", int),
    ("RDTHR", 10.0, "ft/s", "A-4", float),
    ("RDTHRTA", 10.0, "ft/s", "A-4", float),
    ("RESIDECAY", 0.5, "", "A-4", float),
    ("RESIDIMIN", 0.8, "", "A-4", float),
    ("RMAX", 12.0, "nmi", "A-4", float),
    ("RRD_THR", 10, "", "A-4", int),
    ("SLACKEN1", 3.5, "s", "A-4", float),
    ("SLACKEN2", 6.5, "s", "A-4", float),
    ("SLITEOFF", 1.35, "s", "A-4", float),
    ("SMALLZD", 5.0, "ft/s", "A-4", float),
    ("STIMOUT", 240.0, "s", "A-5", float),
    ("STROFIR", 20.0, "s", "A-5", float),
    ("TARHYST", 0.20, "nmi", "A-5", float),
    ("TBINHI", 1.1, "s", "A-5", float),
    ("TBINLO", 0.9, "s", "A-5", float),
    ("TBINMIN", 2.0, "s", "A-5", float),
    ("TCATRES", 6.0, "s", "A-5", float),
    ("TGOLEV", 20.5, "s", "A-5", float),
    ("TIETHR", 3.0, "s", "A-5", float),
    ("TINITZD", 5.5, "s", "A-5", float),
    ("TINYSCORE", 40, "", "A-5", int),
    ("TINYZD", 2.5, "ft/s", "A-5", float),
    ("TTLORATE", 1000.0, "ft/min", "A-5", float),
    ("TTLOSEP", 800.0, "ft", "A-5", float),
    ("TTLOZD", 600.0, "ft/min", "A-5", float),
    ("TMIN", 4.5, "s", "A-5", float),
    ("TRVSNOWEAK", 5.0, "s", "A-5", float),
    ("TRYMAX", 9, "", "A-5", int),
    ("TTRENDMIN", 2.5, "s", "A-5", float),
    ("TV1", 5.0, "s", "A-5", float),
    ("V0", 0.0, "ft/min", "A-5", float),
    ("V1000", 1000.0, "ft/min", "A-5", float),
    ("V2000", 2000.0, "ft/min", "A-5", float),
    ("V500", 500.0, "ft/min", "A-5", float),
    ("VACCEL", 8.0, "ft/s^2", "A-5", float),
    ("VELOCITY_THRESHOLD", -10.0, "ft/s", "A-5", float),
    ("ZDABTHR", 7.0, "ft/s", "A-5", float),
    ("ZDDABTHR", 2.0, "ft/s^2", "A-5", float),
    ("ZDDECAY", 0.9, "", "A-5", float),
    ("ZDESBOT", 900.0, "ft", "A-5", float),
    ("ZDFRACC", 1.3, "", "A-5", float),
    ("ZDLARGE", 12000.0, "ft/min", "A-6", float),
    ("ZDLIKELY", 3000.0, "ft/min", "A-6", float),
    ("ZDTHR", -1.0, "ft/s", "A-6", float),
    ("ZDTHRTA", -1.0, "ft/s", "A-6", float),
    ("ZLARGE", 100000.0, "ft", "A-6", float),
    ("ZLIMITL", 50.0, "ft", "A-6", float),
    ("ZLIMITU", 60.0, "ft", "A-6", float),
    ("ZNO_AURALHI", 600.0, "ft", "A-6", float),
    ("ZNO_AURALLO", 400.0, "ft", "A-6", float),
    ("ZNOINCDESHI", 1650.0, "ft", "A-6", float),
    ("ZNOINCDESLO", 1450.0, "ft", "A-6", float),
    ("ZRJIT", 0.24, "", "A-6", float),
    ("ZSL2TO3", 1100.0, "ft", "A-6", float),
    ("ZSL3TO2", 900.0, "ft", "A-6", float),
    ("ZSL3TO4", 2550.0, "ft", "A-6", float),
    ("ZSL4TO3", 2150.0, "ft", "A-6", float),
    ("ZSL4TO5", 5500.0, "ft", "A-6", float),
    ("ZSL5TO4", 4500.0, "ft", "A-6", float),
    ("ZSL5TO6", 10500.0, "ft", "A-6", float),
    ("ZSL6TO5", 9500.0, "ft", "A-6", float),
    ("ZSL6TO7", 20500.0, "ft", "A-6", float),
    ("ZSL7TO6", 19500.0, "ft", "A-6", float),
]

EXPECTED_NEGATIVE = {
    "BACKDELAY",
    "DESRT",
    "HMD_DISABLE_VAL",
    "INC_DESRATE",
    "MINDRATE",
    "P_RESDL_SIGMAS",
    "VELOCITY_THRESHOLD",
    "ZDTHR",
    "ZDTHRTA",
}

NON_CONSTANT_NAMES = {"APPENDIX_A", "MANUFACTURER_SPECIFIC"}

ids = [row[0] for row in EXPECTED]


def test_expected_table_is_well_formed():
    assert len(EXPECTED) == 175
    assert len(set(ids)) == 175


def test_tc_a_01_registry_size():
    assert len(constants.APPENDIX_A) == 175


@pytest.mark.parametrize("name", ids)
def test_tc_a_02_name_exists(name):
    assert hasattr(constants, name)


def test_tc_a_03_no_extra_names():
    module_caps = {n for n in vars(constants) if n.isupper() and not n.startswith("_")}
    extras = module_caps - NON_CONSTANT_NAMES - set(constants.APPENDIX_A)
    assert extras == set()
    assert set(constants.APPENDIX_A) == set(ids)


@pytest.mark.parametrize("name, value, units, page, typ", EXPECTED, ids=ids)
def test_tc_a_04_value(name, value, units, page, typ):
    actual = getattr(constants, name)
    if typ is float:
        assert math.isclose(actual, value, rel_tol=0, abs_tol=1e-12)
    else:
        assert actual == value


@pytest.mark.parametrize("name, value, units, page, typ", EXPECTED, ids=ids)
def test_tc_a_05_type(name, value, units, page, typ):
    assert type(getattr(constants, name)) is typ


@pytest.mark.parametrize("name", ids)
def test_tc_a_06_registry_value_is_module_attribute(name):
    assert constants.APPENDIX_A[name][0] is getattr(constants, name)


@pytest.mark.parametrize("name, value, units, page, typ", EXPECTED, ids=ids)
def test_tc_a_07_registry_units_and_page(name, value, units, page, typ):
    _, reg_units, reg_page = constants.APPENDIX_A[name]
    assert reg_units == units
    assert reg_page == page


def test_tc_a_08_negative_constants():
    negative = {n for n, (v, _, _) in constants.APPENDIX_A.items() if v < 0}
    assert negative == EXPECTED_NEGATIVE


def test_tc_a_09_trymax_manufacturer_specific():
    assert constants.MANUFACTURER_SPECIFIC == {"TRYMAX": (6, 12)}
    assert isinstance(constants.TRYMAX, int)
    lo, hi = 6, 12
    assert lo <= constants.TRYMAX <= hi


def test_tc_a_10_spot_checks():
    assert constants.MINDRATE == -constants.MAXDRATE
    assert constants.DMOD_MDF == 18000.0
    assert constants.P_VAR_BRNG == 7.569e-3
    assert constants.DT == 1.0
