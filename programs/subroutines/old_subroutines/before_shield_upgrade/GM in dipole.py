prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-100000, "Shutter Gray Molasses OFF", enable=False)
    prg.add(-90000, "TTL GM Repumper ON")
    prg.add(-2500, "AOM GM Detuning", 120.000)
    prg.add(0, "AOM GM Amp ch1 (+)", 1000)
    prg.add(500, "AOM GM Amp ch2 (-)", 200)
    prg.add(1000, "GM amp(+) ramp", start_t=0, stop_x=1, n_points=50, start_x=400, stop_t=5, enable=False)
    prg.add(101000, "AOM GM Amp ch2 (-)", 1)
    prg.add(101500, "AOM GM Amp ch1 (+)", 1)
    return prg
