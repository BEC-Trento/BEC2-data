prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-700000, "shutterFlash MOT open")
    prg.add(-90000, "AOM 3DMOT Detuning", -20.000)
    prg.add(-20000, "shutter MOT close")
    prg.add(-2500, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-1500, "TTL Repumper MOT  ON")
    prg.add(-1000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(-500, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(149500, "TTL Repumper MOT OFF")
    prg.add(150000, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(150500, "AOM 3DMOT Amp ch2 (-)", 1)
    return prg
