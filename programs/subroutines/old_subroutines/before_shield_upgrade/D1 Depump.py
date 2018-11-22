prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM GM Detuning", -120.000)
    prg.add(500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(1000, "AOM GM Amp ch2 (-)", 1000)
    prg.add(3000, "AOM GM Amp ch2 (-)", 400, enable=False)
    prg.add(3500, "AOM GM Amp ch1 (+)", 400, enable=False)
    prg.add(4000, "AOM GM Detuning", 140.000, enable=False)
    return prg
