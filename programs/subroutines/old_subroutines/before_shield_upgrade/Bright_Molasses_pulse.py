prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1500, "AOM 3DMOT Detuning", -30.000)
    prg.add(-1000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(-500, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(0, "AOM DS + RepumperMOT Amp ", 200)
    prg.add(10000, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(10500, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(11000, "AOM 3DMOT Amp ch2 (-)", 1)
    return prg
