prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2500, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(-2000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-100, "TTL Repumper MOT  ON")
    prg.add(0, "TTL Repumper MOT OFF")
    prg.add(1300, "AOM DS + RepumperMOT Amp ", 0)
    return prg
