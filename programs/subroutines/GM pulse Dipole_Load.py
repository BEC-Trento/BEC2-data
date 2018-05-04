prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-9020000, "Shutter Gray Molasses ON")
    prg.add(-9002000, "AOM GM Amp ch2 (-)", 1)
    prg.add(-9000000, "AOM GM Amp ch1 (+)", 1)
    prg.add(-8900000, "TTL GM Repumper ON")
    prg.add(-4980000, "AOM GM Detuning", 90.000)
    prg.add(-10000, "Shutter Gray Molasses OFF")
    prg.add(-500, "AOM GM Amp ch1 (+)", 500)
    prg.add(0, "AOM GM Amp ch2 (-)", 1000)
    prg.add(10000, "GM amp(+) ramp", start_t=0, stop_x=400, n_points=20, start_x=500, stop_t=2, enable=False)
    prg.add(10500, "GM Detuning ramp", start_t=0, stop_x=90, n_points=20, start_x=80, stop_t=2, enable=False)
    prg.add(28000, "TTL GM Repumper OFF")
    prg.add(31500, "AOM GM Amp ch1 (+)", 1)
    prg.add(32000, "AOM GM Amp ch2 (-)", 1)
    prg.add(20021500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(20021500, "AOM GM Amp ch2 (-)", 1000)
    return prg
