prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-800, "AOM 3DMOT Detuning", -92.000)
    prg.add(-400, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(0, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(1000, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(1400, "AOM 3DMOT Amp ch1 (+)", 1)
    return prg
