prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5510000, "AOM GM Amp ch2 (-)", 1)
    prg.add(-5500000, "AOM GM Amp ch1 (+)", 1)
    prg.add(-5000000, "Shutter Gray Molasses ON")
    prg.add(-1000, "AOM GM Amp ch1 (+)", 1000)
    prg.add(1000, "AOM GM Amp ch2 (-)", 1000)
    return prg
