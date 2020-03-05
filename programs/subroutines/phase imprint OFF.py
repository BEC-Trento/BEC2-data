prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "ttl_phase_imprint OFF")
    prg.add(100, "AOM PhaseImprint freq", 120.00)
    prg.add(500, "AOM PhaseImprint Amp", 0)
    return prg
