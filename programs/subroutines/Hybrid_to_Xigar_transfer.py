prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000000, "DAC Vert IR", 0.0010, enable=False)
    prg.add(0, "MT Current Ramp", start_t=0, stop_x=0, n_points=200, start_x=18, stop_t=1000)
    prg.add(10000, "BCompY current ramp", start_t=0, stop_x=0, n_points=200, start_x=0.15, stop_t=1000)
    prg.add(20000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.03, n_points=500, start_x=0.04, stop_t=1000)
    prg.add(50000, "AOM IR Vertical Amp", 1000, enable=False)
    prg.add(50500, "AOM IR Vertical freq", 80.00, enable=False)
    prg.add(51500, "DAC IR Vertical ramp", start_t=0, stop_x=1, n_points=100, start_x=-0.1, stop_t=500, enable=False)
    prg.add(52500, "DAC SRS ramp", start_t=0, stop_x=-0.1, n_points=100, start_x=-9, stop_t=500)
    prg.add(53500, "IGBT BCompZfine CLOSE", enable=False)
    prg.add(54500, "Oscilloscope Trigger ON", enable=False)
    prg.add(10075000, "Config field OFF")
    prg.add(10076000, "IGBT BcompY OPEN")
    return prg
