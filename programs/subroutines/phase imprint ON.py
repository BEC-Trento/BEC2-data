prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM PhaseImprint Amp", 1000)
    prg.add(500, "AOM PhaseImprint freq", 80.00)
    return prg
