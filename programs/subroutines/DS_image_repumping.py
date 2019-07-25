prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4000000, "Shutter DS ON")
    prg.add(-2000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-1000, "AOM DS + RepumperMOT Freq", 406.00)
    prg.add(0, "TTL Dark Spot ON")
    prg.add(3000, "TTL Dark spot OFF")
    prg.add(10000, "Shutter DS OFF")
    return prg
