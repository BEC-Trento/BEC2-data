prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM Zeeman Slower Amp", 1000)
    prg.add(10000, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(20000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(30000, "AOM 2DMOT Amp ch1 (+)", 1000)
    prg.add(40000, "AOM 2DMOT Amp ch2 (-)", 1000)
    prg.add(50000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(60000, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(70000, "AOM Push Amp ch1 (+)", 1000)
    prg.add(80000, "AOM Push Amp ch2 (-)", 1000)
    prg.add(90000, "AOM Repumper Amp", 1000)
    prg.add(100000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(110000, "TTL Dark Spot ON")
    prg.add(120000, "TTL Repumper MOT  ON")
    return prg
