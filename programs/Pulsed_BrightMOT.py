prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(50000, "Switch Off MOT", enable=False)
    prg.add(100000, "AOM 3DMOT Amp ch1 (+)", 0)
    prg.add(101000, "AOM 3DMOT Amp ch2 (-)", 0)
    prg.add(5111000, "Set_BrightMOT")
    prg.add(10051000, "wait")
    return prg
