prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-100000, "shutter MOT close")
    prg.add(-5000, "Shutter Gray Molasses OFF", enable=False)
    prg.add(-4000, "TTL Dark spot OFF")
    prg.add(-3500, "TTL Repumper MOT OFF")
    prg.add(-3000, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(-2500, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(-2000, "AOM Push Amp ch1 (+)", 1)
    prg.add(-1500, "AOM Zeeman Slower Amp", 1)
    prg.add(-1000, "AOM Push Amp ch2 (-)", 1)
    prg.add(-500, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(0, "Config field OFF")
    prg.add(2000, "AOM 2DMOT Amp ch2 (-)", 1)
    prg.add(2500, "AOM 2DMOT Amp ch1 (+)", 1)
    prg.add(3000, "AOM GM Amp ch1 (+)", 1, enable=False)
    prg.add(3500, "AOM GM Amp ch2 (-)", 1, enable=False)
    return prg
