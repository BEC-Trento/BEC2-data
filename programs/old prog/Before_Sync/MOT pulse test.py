prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(2500000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(3750000, "Set Bright MOT", enable=False)
    prg.add(3750000, "Set MOT")
    prg.add(5000000, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(7500000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(10000000, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(12500000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(15000000, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(17500000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(20000000, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(22500000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(25000000, "AOM DS + RepumperMOT Amp ", 1)
    return prg
