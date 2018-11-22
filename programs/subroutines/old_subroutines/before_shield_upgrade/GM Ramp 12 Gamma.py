prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-100000, "Shutter Gray Molasses OFF")
    prg.add(-2500, "AOM GM Detuning", 120.000)
    prg.add(0, "GM amp(+) ramp", start_t=0, stop_x=450, n_points=50, start_x=1000, stop_t=15)
    prg.add(150000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=10, start_x=450, stop_t=1)
    prg.add(151000, "TTL GM Repumper OFF")
    prg.add(160500, "AOM GM Amp ch1 (+)", 1)
    prg.add(161000, "AOM GM Amp ch2 (-)", 1)
    prg.add(50000000, "AOM GM Amp ch1 (+)", 1000)
    prg.add(50010000, "AOM GM Amp ch2 (-)", 1000)
    prg.add(50020000, "TTL GM Repumper ON")
    return prg
