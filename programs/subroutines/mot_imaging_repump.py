prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-40000, "Shutter DS-Repumper ON")
    prg.add(-3000, "AOM Repumper freq", 225.00)
    prg.add(-2500, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(-2000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-1000, "TTL Repumper MOT  ON")
    prg.add(0, "TTL Repumper MOT OFF")
    return prg
