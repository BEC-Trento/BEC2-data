prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-100000, "Shutter Gray Molasses OFF")
    prg.add(0, "GM ON")
    prg.add(5000, "AOM GM Detuning", 100.000, enable=False)
    prg.add(7500, "GM amp(+) ramp", start_t=0, stop_x=450, n_points=50, start_x=1000, stop_t=14.95, enable=False)
    prg.add(10000, "AOM GM Amp ch1 (+)", 1)
    prg.add(10500, "AOM GM Amp ch2 (-)", 1)
    prg.add(157500, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=10, start_x=450, stop_t=1, enable=False)
    prg.add(160000, "TTL GM Repumper OFF", enable=False)
    prg.add(164500, "AOM GM Detuning", 30.000, enable=False)
    prg.add(168500, "AOM GM Amp ch1 (+)", 1, enable=False)
    prg.add(169000, "AOM GM Amp ch2 (-)", 1, enable=False)
    prg.add(10169000, "AOM GM Amp ch1 (+)", 1000, enable=False)
    prg.add(10179000, "AOM GM Amp ch2 (-)", 1000, enable=False)
    prg.add(10189000, "TTL GM Repumper ON", enable=False)
    return prg
