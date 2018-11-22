prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-100000, "Shutter Gray Molasses OFF")
    prg.add(-2500, "GM Detuning ramp", start_t=5, stop_x=140, n_points=140, start_x=120, stop_t=0.25, enable=False)
    prg.add(-2500, "AOM GM Detuning", 140.000)
    prg.add(0, "GM amp(+) ramp", start_t=0, stop_x=400, n_points=150, start_x=1000, stop_t=15)
    prg.add(150000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=10, start_x=450, stop_t=1, enable=False)
    prg.add(190000, "TTL GM Repumper OFF")
    prg.add(198000, "D1 Depump")
    prg.add(201000, "AOM GM Amp ch1 (+)", 1)
    prg.add(201500, "AOM GM Amp ch2 (-)", 1)
    prg.add(202000, "AOM 3DMOT Detuning", -58.000)
    prg.add(202500, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(203000, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(204000, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(204500, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(50033500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(50043500, "AOM GM Amp ch2 (-)", 1000)
    return prg
