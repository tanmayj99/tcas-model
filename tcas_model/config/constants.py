"""Constant definitions.

DO-185B Vol. II, Appendix A, pp. A-1 to A-6.

Implemented from docs/design/appendix_a_constants.md. Names, values, and
units are as printed in Appendix A, in Appendix A page order. No unit
conversions and no derived values.
"""

# --- Appendix A, p. A-1 ---
AB_COEFF = 3  # dimensionless, A-1
ABOVNMC = 15500.0  # ft, A-1
ADEQSEP = 100.0  # ft, A-1
ALERTER_TMAX = 300.0  # s, A-1
ALERTER_TMIN = 5.0  # s, A-1
ALFAO = 0.58  # dimensionless, A-1
AVEVALT = 200.0  # ft, A-1
BACKDELAY = -2.5  # s, A-1
BBCC_DISABLE_VAL = 100.0  # nmi, A-1
BETAO = 0.25  # dimensionless, A-1
CLMRT = 1500.0  # ft/min, A-1
COAST_ACCEL = 32.2  # ft/s^2, A-1
CREDACCDIV = 20.0  # ft/s^2, A-1
CREDINIT = 200.0  # ft/s, A-1
CREDMINDT = 5.5  # s, A-1
CREDZADC = 65.0  # ft, A-1
CREDZDERR = 30.0  # ft/s, A-1
CROSSTHR = 100.0  # ft, A-1
DELZDT = 4.0  # s, A-1
DELZTHR = 20.0  # ft, A-1
DESRT = -1500.0  # ft/min, A-1
DMOD_MDF = 18000.0  # ft, A-1
DT = 1.0  # s, A-1
DTCOAST = 2.5  # s, A-1
DTLONG = 6.5  # s, A-1
DTSTART = 2.5  # s, A-1
DZTHR_100 = 60.0  # ft, A-1
DZTHR_25 = 22.5  # ft, A-1
EARLYLATE = 1.5  # s, A-1

# --- Appendix A, p. A-2 ---
GAMMAZ = 0.5  # dimensionless, A-2
GUESDU1 = 4.5  # s, A-2
GUESDU2 = 9.5  # s, A-2
GUESDU3 = 14.5  # s, A-2
GUESRATE = 480.0  # ft/min, A-2
HI1 = 2.0  # dimensionless, A-2
HI2 = 1.5  # dimensionless, A-2
HI3 = 1.25  # dimensionless, A-2
HISCORE = 1200  # dimensionless, A-2
HMD_DISABLE_VAL = -1.0  # ft, A-2
HMD_RB_TAU_THRESHOLD = 100.0  # s, A-2
HMDMULT = 1.05  # dimensionless, A-2
HUGE = 100000.0  # ft/min, A-2
HUGEDZ = 75.0  # ft, A-2
HYSTERCOR = 300.0  # ft/min, A-2
ILEV = 1000.0  # ft/min, A-2
INC_ADD_SEP = 50.0  # ft, A-2
INC_CLMRATE = 2500.0  # ft/min, A-2
INC_DESRATE = -2500.0  # ft/min, A-2
INC_TAU_THR = 6.0  # s, A-2
INITCOUNT = 5  # dimensionless, A-2
LARGEDZ = 22.5  # ft, A-2
LATELEVEL = 4.5  # s, A-2
LATESLACK = 0.5  # s, A-2
LEVOFFACCX2 = 8.0  # ft/s^2, A-2
LO1 = 0.0  # dimensionless, A-2
LO2 = 0.667  # dimensionless, A-2
LO3 = 0.8  # dimensionless, A-2
LONGCOAST = 3.5  # s, A-2
LOSCORE = 100  # dimensionless, A-2
LOWFIRMRZ = 150.0  # ft, A-2

# --- Appendix A, p. A-3 ---
MAXALTDIFF = 600.0  # ft, A-3
MAXALTDIFF2 = 850.0  # ft, A-3
MAXBINS = 8  # dimensionless, A-3
MAXDRATE = 4400.0  # ft/min, A-3
MAXSOFT = 5  # dimensionless, A-3
MAXZDINT = 10000.0  # ft/min, A-3
MAXZDTIME = 17.0  # s, A-3
MEDHISCORE = 500  # dimensionless, A-3
MEDLOSCORE = 300  # dimensionless, A-3
MEDSCORE = 400  # dimensionless, A-3
MINBINS = 3  # dimensionless, A-3
MINDRATE = -4400.0  # ft/min, A-3
MINFIRM = 2  # dimensionless, A-3
MINRITIME = 4.0  # s, A-3
MINRVSTIME = 10.0  # s, A-3
MINTATIME = 8.0  # s, A-3
MINTAU = 0.0  # s, A-3
MODEL_T = 9.0  # s, A-3
MODEL_ZD = 2500.0  # ft/min, A-3
NAFRANGE = 1.7  # nmi, A-3
NBINSNL = 5  # dimensionless, A-3
NEWVSL = 75.0  # ft, A-3
NODESHI = 1200.0  # ft, A-3
NODESLO = 1000.0  # ft, A-3
NOWEAK = 10.0  # s, A-3
NOZCROSS = 100.0  # ft, A-3
NSGNCT = 0.1  # dimensionless, A-3
OLEV = 600.0  # ft/min, A-3
OUT2 = 1.1  # s, A-3
OUT3 = 0.55  # s, A-3
OVERDUE = 3.5  # s, A-3

# --- Appendix A, p. A-4 ---
P_ACCTHR = 1.5  # ft/s^2, A-4
P_ALPHA3D = 0.1  # dimensionless, A-4
P_ALPHARESSQ = 0.1  # dimensionless, A-4
P_INITRHODDTHR = 9999  # dimensionless, A-4
P_MAXRANGERESID = 150.0  # ft, A-4
P_MAXSIGDPX = 3  # dimensionless, A-4
P_MINSIGDPX = 0.7  # dimensionless, A-4
P_P_NOISE_FACTOR = 100.0  # dimensionless, A-4
P_PROCNOIVAR = 2.56  # (ft/s^2)^2, A-4
P_RESDL_SIGMAS = -3  # dimensionless, A-4
P_RESSD_C_EXP_FACT = 1.2  # dimensionless, A-4
P_RESSD_N = 35.0  # ft, A-4
P_VAR_BRNG = 7.569e-3  # dimensionless, A-4
PROXA = 1200.0  # ft, A-4
PROXR = 6.0  # nmi, A-4
Q100 = 100.0  # ft, A-4
Q25 = 25.0  # ft, A-4
Q50 = 50.0  # ft, A-4
QUIKREAC = 2.5  # s, A-4
RACCEL = 11.2  # ft/s^2, A-4
RADARLOST = 10  # dimensionless, A-4
RDTHR = 10.0  # ft/s, A-4
RDTHRTA = 10.0  # ft/s, A-4
RESIDECAY = 0.5  # dimensionless, A-4
RESIDIMIN = 0.8  # dimensionless, A-4
RMAX = 12.0  # nmi, A-4
RRD_THR = 10  # dimensionless, A-4
SLACKEN1 = 3.5  # s, A-4
SLACKEN2 = 6.5  # s, A-4
SLITEOFF = 1.35  # s, A-4
SMALLZD = 5.0  # ft/s, A-4

# --- Appendix A, p. A-5 ---
STIMOUT = 240.0  # s, A-5
STROFIR = 20.0  # s, A-5
TARHYST = 0.20  # nmi, A-5
TBINHI = 1.1  # s, A-5
TBINLO = 0.9  # s, A-5
TBINMIN = 2.0  # s, A-5
TCATRES = 6.0  # s, A-5
TGOLEV = 20.5  # s, A-5
TIETHR = 3.0  # s, A-5
TINITZD = 5.5  # s, A-5
TINYSCORE = 40  # dimensionless, A-5
TINYZD = 2.5  # ft/s, A-5
TTLORATE = 1000.0  # ft/min, A-5
TTLOSEP = 800.0  # ft, A-5
TTLOZD = 600.0  # ft/min, A-5
TMIN = 4.5  # s, A-5
TRVSNOWEAK = 5.0  # s, A-5
TRYMAX = 9  # manufacturer specific, 6..12 per App. A p. A-5; project value, see docs/decisions.md
TTRENDMIN = 2.5  # s, A-5
TV1 = 5.0  # s, A-5
V0 = 0.0  # ft/min, A-5
V1000 = 1000.0  # ft/min, A-5
V2000 = 2000.0  # ft/min, A-5
V500 = 500.0  # ft/min, A-5
VACCEL = 8.0  # ft/s^2, A-5
VELOCITY_THRESHOLD = -10.0  # ft/s, A-5
ZDABTHR = 7.0  # ft/s, A-5
ZDDABTHR = 2.0  # ft/s^2, A-5
ZDDECAY = 0.9  # dimensionless, A-5
ZDESBOT = 900.0  # ft, A-5
ZDFRACC = 1.3  # dimensionless, A-5

# --- Appendix A, p. A-6 ---
ZDLARGE = 12000.0  # ft/min, A-6
ZDLIKELY = 3000.0  # ft/min, A-6
ZDTHR = -1.0  # ft/s, A-6
ZDTHRTA = -1.0  # ft/s, A-6
ZLARGE = 100000.0  # ft, A-6
ZLIMITL = 50.0  # ft, A-6
ZLIMITU = 60.0  # ft, A-6
ZNO_AURALHI = 600.0  # ft, A-6
ZNO_AURALLO = 400.0  # ft, A-6
ZNOINCDESHI = 1650.0  # ft, A-6
ZNOINCDESLO = 1450.0  # ft, A-6
ZRJIT = 0.24  # dimensionless, A-6
ZSL2TO3 = 1100.0  # ft, A-6
ZSL3TO2 = 900.0  # ft, A-6
ZSL3TO4 = 2550.0  # ft, A-6
ZSL4TO3 = 2150.0  # ft, A-6
ZSL4TO5 = 5500.0  # ft, A-6
ZSL5TO4 = 4500.0  # ft, A-6
ZSL5TO6 = 10500.0  # ft, A-6
ZSL6TO5 = 9500.0  # ft, A-6
ZSL6TO7 = 20500.0  # ft, A-6
ZSL7TO6 = 19500.0  # ft, A-6


# Allowed ranges for the constants Appendix A leaves manufacturer specific.
# Not part of APPENDIX_A.
MANUFACTURER_SPECIFIC: dict[str, tuple[int, int]] = {"TRYMAX": (6, 12)}


# name -> (value, units, page). Units are "" for dimensionless.
APPENDIX_A: dict[str, tuple[int | float, str, str]] = {
    "AB_COEFF": (AB_COEFF, "", "A-1"),
    "ABOVNMC": (ABOVNMC, "ft", "A-1"),
    "ADEQSEP": (ADEQSEP, "ft", "A-1"),
    "ALERTER_TMAX": (ALERTER_TMAX, "s", "A-1"),
    "ALERTER_TMIN": (ALERTER_TMIN, "s", "A-1"),
    "ALFAO": (ALFAO, "", "A-1"),
    "AVEVALT": (AVEVALT, "ft", "A-1"),
    "BACKDELAY": (BACKDELAY, "s", "A-1"),
    "BBCC_DISABLE_VAL": (BBCC_DISABLE_VAL, "nmi", "A-1"),
    "BETAO": (BETAO, "", "A-1"),
    "CLMRT": (CLMRT, "ft/min", "A-1"),
    "COAST_ACCEL": (COAST_ACCEL, "ft/s^2", "A-1"),
    "CREDACCDIV": (CREDACCDIV, "ft/s^2", "A-1"),
    "CREDINIT": (CREDINIT, "ft/s", "A-1"),
    "CREDMINDT": (CREDMINDT, "s", "A-1"),
    "CREDZADC": (CREDZADC, "ft", "A-1"),
    "CREDZDERR": (CREDZDERR, "ft/s", "A-1"),
    "CROSSTHR": (CROSSTHR, "ft", "A-1"),
    "DELZDT": (DELZDT, "s", "A-1"),
    "DELZTHR": (DELZTHR, "ft", "A-1"),
    "DESRT": (DESRT, "ft/min", "A-1"),
    "DMOD_MDF": (DMOD_MDF, "ft", "A-1"),
    "DT": (DT, "s", "A-1"),
    "DTCOAST": (DTCOAST, "s", "A-1"),
    "DTLONG": (DTLONG, "s", "A-1"),
    "DTSTART": (DTSTART, "s", "A-1"),
    "DZTHR_100": (DZTHR_100, "ft", "A-1"),
    "DZTHR_25": (DZTHR_25, "ft", "A-1"),
    "EARLYLATE": (EARLYLATE, "s", "A-1"),
    "GAMMAZ": (GAMMAZ, "", "A-2"),
    "GUESDU1": (GUESDU1, "s", "A-2"),
    "GUESDU2": (GUESDU2, "s", "A-2"),
    "GUESDU3": (GUESDU3, "s", "A-2"),
    "GUESRATE": (GUESRATE, "ft/min", "A-2"),
    "HI1": (HI1, "", "A-2"),
    "HI2": (HI2, "", "A-2"),
    "HI3": (HI3, "", "A-2"),
    "HISCORE": (HISCORE, "", "A-2"),
    "HMD_DISABLE_VAL": (HMD_DISABLE_VAL, "ft", "A-2"),
    "HMD_RB_TAU_THRESHOLD": (HMD_RB_TAU_THRESHOLD, "s", "A-2"),
    "HMDMULT": (HMDMULT, "", "A-2"),
    "HUGE": (HUGE, "ft/min", "A-2"),
    "HUGEDZ": (HUGEDZ, "ft", "A-2"),
    "HYSTERCOR": (HYSTERCOR, "ft/min", "A-2"),
    "ILEV": (ILEV, "ft/min", "A-2"),
    "INC_ADD_SEP": (INC_ADD_SEP, "ft", "A-2"),
    "INC_CLMRATE": (INC_CLMRATE, "ft/min", "A-2"),
    "INC_DESRATE": (INC_DESRATE, "ft/min", "A-2"),
    "INC_TAU_THR": (INC_TAU_THR, "s", "A-2"),
    "INITCOUNT": (INITCOUNT, "", "A-2"),
    "LARGEDZ": (LARGEDZ, "ft", "A-2"),
    "LATELEVEL": (LATELEVEL, "s", "A-2"),
    "LATESLACK": (LATESLACK, "s", "A-2"),
    "LEVOFFACCX2": (LEVOFFACCX2, "ft/s^2", "A-2"),
    "LO1": (LO1, "", "A-2"),
    "LO2": (LO2, "", "A-2"),
    "LO3": (LO3, "", "A-2"),
    "LONGCOAST": (LONGCOAST, "s", "A-2"),
    "LOSCORE": (LOSCORE, "", "A-2"),
    "LOWFIRMRZ": (LOWFIRMRZ, "ft", "A-2"),
    "MAXALTDIFF": (MAXALTDIFF, "ft", "A-3"),
    "MAXALTDIFF2": (MAXALTDIFF2, "ft", "A-3"),
    "MAXBINS": (MAXBINS, "", "A-3"),
    "MAXDRATE": (MAXDRATE, "ft/min", "A-3"),
    "MAXSOFT": (MAXSOFT, "", "A-3"),
    "MAXZDINT": (MAXZDINT, "ft/min", "A-3"),
    "MAXZDTIME": (MAXZDTIME, "s", "A-3"),
    "MEDHISCORE": (MEDHISCORE, "", "A-3"),
    "MEDLOSCORE": (MEDLOSCORE, "", "A-3"),
    "MEDSCORE": (MEDSCORE, "", "A-3"),
    "MINBINS": (MINBINS, "", "A-3"),
    "MINDRATE": (MINDRATE, "ft/min", "A-3"),
    "MINFIRM": (MINFIRM, "", "A-3"),
    "MINRITIME": (MINRITIME, "s", "A-3"),
    "MINRVSTIME": (MINRVSTIME, "s", "A-3"),
    "MINTATIME": (MINTATIME, "s", "A-3"),
    "MINTAU": (MINTAU, "s", "A-3"),
    "MODEL_T": (MODEL_T, "s", "A-3"),
    "MODEL_ZD": (MODEL_ZD, "ft/min", "A-3"),
    "NAFRANGE": (NAFRANGE, "nmi", "A-3"),
    "NBINSNL": (NBINSNL, "", "A-3"),
    "NEWVSL": (NEWVSL, "ft", "A-3"),
    "NODESHI": (NODESHI, "ft", "A-3"),
    "NODESLO": (NODESLO, "ft", "A-3"),
    "NOWEAK": (NOWEAK, "s", "A-3"),
    "NOZCROSS": (NOZCROSS, "ft", "A-3"),
    "NSGNCT": (NSGNCT, "", "A-3"),
    "OLEV": (OLEV, "ft/min", "A-3"),
    "OUT2": (OUT2, "s", "A-3"),
    "OUT3": (OUT3, "s", "A-3"),
    "OVERDUE": (OVERDUE, "s", "A-3"),
    "P_ACCTHR": (P_ACCTHR, "ft/s^2", "A-4"),
    "P_ALPHA3D": (P_ALPHA3D, "", "A-4"),
    "P_ALPHARESSQ": (P_ALPHARESSQ, "", "A-4"),
    "P_INITRHODDTHR": (P_INITRHODDTHR, "", "A-4"),
    "P_MAXRANGERESID": (P_MAXRANGERESID, "ft", "A-4"),
    "P_MAXSIGDPX": (P_MAXSIGDPX, "", "A-4"),
    "P_MINSIGDPX": (P_MINSIGDPX, "", "A-4"),
    "P_P_NOISE_FACTOR": (P_P_NOISE_FACTOR, "", "A-4"),
    "P_PROCNOIVAR": (P_PROCNOIVAR, "(ft/s^2)^2", "A-4"),
    "P_RESDL_SIGMAS": (P_RESDL_SIGMAS, "", "A-4"),
    "P_RESSD_C_EXP_FACT": (P_RESSD_C_EXP_FACT, "", "A-4"),
    "P_RESSD_N": (P_RESSD_N, "ft", "A-4"),
    "P_VAR_BRNG": (P_VAR_BRNG, "", "A-4"),
    "PROXA": (PROXA, "ft", "A-4"),
    "PROXR": (PROXR, "nmi", "A-4"),
    "Q100": (Q100, "ft", "A-4"),
    "Q25": (Q25, "ft", "A-4"),
    "Q50": (Q50, "ft", "A-4"),
    "QUIKREAC": (QUIKREAC, "s", "A-4"),
    "RACCEL": (RACCEL, "ft/s^2", "A-4"),
    "RADARLOST": (RADARLOST, "", "A-4"),
    "RDTHR": (RDTHR, "ft/s", "A-4"),
    "RDTHRTA": (RDTHRTA, "ft/s", "A-4"),
    "RESIDECAY": (RESIDECAY, "", "A-4"),
    "RESIDIMIN": (RESIDIMIN, "", "A-4"),
    "RMAX": (RMAX, "nmi", "A-4"),
    "RRD_THR": (RRD_THR, "", "A-4"),
    "SLACKEN1": (SLACKEN1, "s", "A-4"),
    "SLACKEN2": (SLACKEN2, "s", "A-4"),
    "SLITEOFF": (SLITEOFF, "s", "A-4"),
    "SMALLZD": (SMALLZD, "ft/s", "A-4"),
    "STIMOUT": (STIMOUT, "s", "A-5"),
    "STROFIR": (STROFIR, "s", "A-5"),
    "TARHYST": (TARHYST, "nmi", "A-5"),
    "TBINHI": (TBINHI, "s", "A-5"),
    "TBINLO": (TBINLO, "s", "A-5"),
    "TBINMIN": (TBINMIN, "s", "A-5"),
    "TCATRES": (TCATRES, "s", "A-5"),
    "TGOLEV": (TGOLEV, "s", "A-5"),
    "TIETHR": (TIETHR, "s", "A-5"),
    "TINITZD": (TINITZD, "s", "A-5"),
    "TINYSCORE": (TINYSCORE, "", "A-5"),
    "TINYZD": (TINYZD, "ft/s", "A-5"),
    "TTLORATE": (TTLORATE, "ft/min", "A-5"),
    "TTLOSEP": (TTLOSEP, "ft", "A-5"),
    "TTLOZD": (TTLOZD, "ft/min", "A-5"),
    "TMIN": (TMIN, "s", "A-5"),
    "TRVSNOWEAK": (TRVSNOWEAK, "s", "A-5"),
    "TRYMAX": (TRYMAX, "", "A-5"),
    "TTRENDMIN": (TTRENDMIN, "s", "A-5"),
    "TV1": (TV1, "s", "A-5"),
    "V0": (V0, "ft/min", "A-5"),
    "V1000": (V1000, "ft/min", "A-5"),
    "V2000": (V2000, "ft/min", "A-5"),
    "V500": (V500, "ft/min", "A-5"),
    "VACCEL": (VACCEL, "ft/s^2", "A-5"),
    "VELOCITY_THRESHOLD": (VELOCITY_THRESHOLD, "ft/s", "A-5"),
    "ZDABTHR": (ZDABTHR, "ft/s", "A-5"),
    "ZDDABTHR": (ZDDABTHR, "ft/s^2", "A-5"),
    "ZDDECAY": (ZDDECAY, "", "A-5"),
    "ZDESBOT": (ZDESBOT, "ft", "A-5"),
    "ZDFRACC": (ZDFRACC, "", "A-5"),
    "ZDLARGE": (ZDLARGE, "ft/min", "A-6"),
    "ZDLIKELY": (ZDLIKELY, "ft/min", "A-6"),
    "ZDTHR": (ZDTHR, "ft/s", "A-6"),
    "ZDTHRTA": (ZDTHRTA, "ft/s", "A-6"),
    "ZLARGE": (ZLARGE, "ft", "A-6"),
    "ZLIMITL": (ZLIMITL, "ft", "A-6"),
    "ZLIMITU": (ZLIMITU, "ft", "A-6"),
    "ZNO_AURALHI": (ZNO_AURALHI, "ft", "A-6"),
    "ZNO_AURALLO": (ZNO_AURALLO, "ft", "A-6"),
    "ZNOINCDESHI": (ZNOINCDESHI, "ft", "A-6"),
    "ZNOINCDESLO": (ZNOINCDESLO, "ft", "A-6"),
    "ZRJIT": (ZRJIT, "", "A-6"),
    "ZSL2TO3": (ZSL2TO3, "ft", "A-6"),
    "ZSL3TO2": (ZSL3TO2, "ft", "A-6"),
    "ZSL3TO4": (ZSL3TO4, "ft", "A-6"),
    "ZSL4TO3": (ZSL4TO3, "ft", "A-6"),
    "ZSL4TO5": (ZSL4TO5, "ft", "A-6"),
    "ZSL5TO4": (ZSL5TO4, "ft", "A-6"),
    "ZSL5TO6": (ZSL5TO6, "ft", "A-6"),
    "ZSL6TO5": (ZSL6TO5, "ft", "A-6"),
    "ZSL6TO7": (ZSL6TO7, "ft", "A-6"),
    "ZSL7TO6": (ZSL7TO6, "ft", "A-6"),
}
