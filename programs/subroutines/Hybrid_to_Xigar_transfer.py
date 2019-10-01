prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC Vert IR", 0.0000)
    prg.add(50000, "AOM IR Vertical Amp", 1000)
    prg.add(50500, "AOM IR Vertical freq", 80.00)
    prg.add(51500, "DAC IR Vertical ramp", start_t=0, stop_x=1, n_points=100, start_x=0, stop_t=500)
    prg.add(52500, "DAC SRS ramp", start_t=0, stop_x=-0.1, n_points=100, start_x=-9, stop_t=500)
    prg.add(53500, "IGBT BCompZfine CLOSE")
    prg.add(54500, "Oscilloscope Trigger ON")
    prg.add(5055500, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(5065500, "BCompY current ramp", start_t=0, stop_x=0, n_points=100, start_x=0.15, stop_t=500)
    prg.add(10075000, "Config field OFF")
    prg.add(10076000, "IGBT BcompY OPEN")
    return prg
