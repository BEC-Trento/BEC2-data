prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2800000, "Shutter Gray Molasses ON")
    prg.add(-2790299, "AOM GM Amp ch1 (+)", 1)
    prg.add(-2780299, "AOM GM Amp ch2 (-)", 1)
    prg.add(-2770299, "TTL GM Repumper ON")
    prg.add(-2760299, "AOM GM Detuning", 40.000)
    prg.add(-100000, "Shutter Gray Molasses OFF")
    prg.add(-1500, "TTL Repumper MOT  ON")
    prg.add(-1000, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(-500, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(0, "AOM GM Amp ch1 (+)", 1000)
    prg.add(500, "AOM GM Amp ch2 (-)", 1000)
    prg.add(20500, "AOM GM Amp ch1 (+)", 1)
    prg.add(20500, "AOM GM Amp ch2 (-)", 1)
    prg.add(2020500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(2020500, "AOM GM Amp ch2 (-)", 1000)
    return prg
