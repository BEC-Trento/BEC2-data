prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-100000, "Shutter DS-Repumper ON")
    prg.add(-99750, "TTL Repumper MOT OFF")
    prg.add(-99500, "TTL Dark spot OFF")
    prg.add(-99000, "AOM DS + RepumperMOT Amp ", 0)
    prg.add(-3000, "AOM Repumper freq", 225.00)
    prg.add(-2500, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(-2000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-50, "TTL Repumper MOT  ON")
    prg.add(0, "TTL Repumper MOT OFF")
    prg.add(1300, "AOM DS + RepumperMOT Amp ", 0)
    prg.add(2000, "Shutter DS-Repumper OFF")
    prg.add(100000, "TTL Dark Spot ON")
    prg.add(100500, "AOM DS + RepumperMOT Amp ", 1000)
    return prg
