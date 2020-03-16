prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM Zeeman Slower Amp", 1000)
    prg.add(500, "AOM Zeeman Slower freq", 170.00)
    prg.add(1000, "AOM 2DMOT Amp ch1 (+)", 1000)
    prg.add(1500, "AOM 2DMOT Amp ch2 (-)", 1000)
    prg.add(2000, "AOM 2DMOT Detuning", -13.000)
    prg.add(2500, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(3000, "AOM 3DMOT Amp ch2 (-)", 650)
    prg.add(3500, "AOM 3DMOT Detuning", -18.000)
    prg.add(4000, "AOM Repumper Amp", 1000)
    prg.add(4500, "AOM DS + RepumperMOT Amp ", 600)
    prg.add(5000, "AOM Repumper freq", 225.00)
    prg.add(5500, "AOM DS + RepumperMOT Freq", 406.00)
    prg.add(5600, "TTL Dark Spot ON")
    prg.add(5699, "TTL Repumper MOT  ON", enable=False)
    prg.add(5750, "TTL Repumper MOT OFF")
    return prg
