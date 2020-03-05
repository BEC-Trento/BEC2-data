prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1600, "ttl_phase_imprint OFF")
    prg.add(-1500, "AOM PhaseImprint Amp", 1000)
    prg.add(-1000, "AOM PhaseImprint freq", 80.00)
    prg.add(0, "ttl_phase_imprint ON")
    return prg
