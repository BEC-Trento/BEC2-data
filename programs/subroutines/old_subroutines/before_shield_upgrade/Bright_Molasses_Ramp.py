prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2000, "TTL Repumper MOT  ON")
    prg.add(-1500, "AOM 3DMOT Detuning", -22.000)
    prg.add(-1000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(-500, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(0, "AOM DS + RepumperMOT Amp ", 500)
    prg.add(0, "3DMOT Detuning ramp", start_t=0, stop_x=-30, n_points=10, start_x=-22, stop_t=1)
    prg.add(500, "3DMOT amp(+) ramp", start_t=0, stop_x=800, n_points=10, start_x=1000, stop_t=1)
    prg.add(10000, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(11000, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(11500, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(12000, "TTL Repumper MOT OFF")
    return prg
