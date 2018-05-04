prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2000, "TTL Repumper MOT  ON")
    prg.add(-1500, "AOM 3DMOT Detuning", -23.000)
    prg.add(-1000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(-500, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(0, "AOM DS + RepumperMOT Amp ", 500)
    prg.add(500, "3DMOT Detuning ramp", start_t=0, stop_x=-38, n_points=100, start_x=-22, stop_t=20)
    prg.add(1000, "3DMOT amp(+) ramp", start_t=0, stop_x=800, n_points=100, start_x=1000, stop_t=20, enable=False)
    prg.add(1500, "3D MOT Coils ramp", start_t=0, stop_x=0, n_points=40, start_x=9, stop_t=20, enable=False)
    prg.add(201500, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(202500, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(203000, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(203500, "TTL Repumper MOT OFF")
    return prg
