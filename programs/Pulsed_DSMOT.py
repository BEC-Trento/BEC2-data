prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "AOM 3DMOT Amp ch1 (+)", 0)
    prg.add(11000, "AOM 3DMOT Amp ch2 (-)", 0)
    prg.add(5000000, "Set_MOT")
    prg.add(10000000, "wait")
    return prg
