prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "3D MOT Coils", 0.0000)
    prg.add(300, "shutter MOT close")
    prg.add(600, "AOM Push Amp ch1 (+)", 1)
    prg.add(900, "AOM Push Amp ch2 (-)", 1)
    prg.add(1200, "AOM Zeeman Slower Amp", 1)
    prg.add(1500, "AOM 2DMOT Amp ch1 (+)", 1)
    prg.add(1800, "AOM 2DMOT Amp ch2 (-)", 1)
    prg.add(2100, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(2400, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(2700, "AOM DS + RepumperMOT Amp ", 1)
    return prg
