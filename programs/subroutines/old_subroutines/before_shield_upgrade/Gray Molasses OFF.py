prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-100000, "Shutter Gray Molasses OFF")
    prg.add(0, "AOM GM Amp ch2 (-)", 1)
    prg.add(1000, "AOM GM Amp ch1 (+)", 1)
    prg.add(10000000, "AOM GM Amp ch2 (-)", 1000)
    prg.add(10001000, "AOM GM Amp ch1 (+)", 1000)
    return prg
