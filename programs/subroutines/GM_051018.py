prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-101199, "Shutter Gray Molasses OFF")
    prg.add(0, "GM ON")
    prg.add(5000, "AOM GM Detuning", 100.000)
    prg.add(5010, "Oscilloscope Trigger ON", enable=False)
    prg.add(7500, "GM amp(+) ramp", start_t=0, stop_x=750, n_points=15, start_x=1000, stop_t=1)
    prg.add(18000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=30, start_x=750, stop_t=3)
    prg.add(38000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=10, start_x=350, stop_t=1, enable=False)
    prg.add(44000, "TTL GM Repumper OFF")
    prg.add(44500, "AOM GM Detuning", 40.000)
    prg.add(49000, "AOM GM Amp ch1 (+)", 1)
    prg.add(49500, "AOM GM Amp ch2 (-)", 1)
    prg.add(49550, "Oscilloscope Trigger OFF", enable=False)
    prg.add(10049500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(10059500, "AOM GM Amp ch2 (-)", 1000)
    prg.add(10069500, "TTL GM Repumper ON", enable=False)
    prg.add(10069500, "TTL GM Repumper OFF", enable=False)
    return prg
