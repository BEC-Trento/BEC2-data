prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-9002000, "Shutter Gray Molasses ON")
    prg.add(-9001000, "AOM GM Amp ch2 (-)", 1)
    prg.add(-9000000, "AOM GM Amp ch1 (+)", 1)
    prg.add(-8900000, "TTL GM Repumper ON")
    prg.add(-8890000, "TTL GM Repumper OFF", enable=False)
    prg.add(-4980000, "AOM GM Detuning", 40.000)
    prg.add(-1000, "TTL GM Repumper ON")
    prg.add(-500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(0, "AOM GM Amp ch2 (-)", 1000)
    return prg
