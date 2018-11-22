prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-9020000, "Shutter Gray Molasses ON")
    prg.add(-9002000, "AOM GM Amp ch2 (-)", 1)
    prg.add(-9000000, "AOM GM Amp ch1 (+)", 1)
    prg.add(-8900000, "TTL GM Repumper ON")
    prg.add(-4980000, "AOM GM Detuning", 120.000)
    prg.add(-400000, "Shutter Gray Molasses OFF", enable=False)
    prg.add(-500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(0, "AOM GM Amp ch2 (-)", 1000)
    prg.add(10000, "AOM GM Amp ch1 (+)", 1, enable=False)
    prg.add(10500, "AOM GM Amp ch2 (-)", 1, enable=False)
    prg.add(50039000, "AOM GM Amp ch1 (+)", 1000, enable=False)
    prg.add(50049000, "AOM GM Amp ch2 (-)", 1000, enable=False)
    return prg
