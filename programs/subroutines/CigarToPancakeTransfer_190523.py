prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC IR Horiz_Ellipt", -1.0000)
    prg.add(500, "DAC Vert IR", -1.0000)
    prg.add(30500, "AOM IR Horiz_Ellipt Amp", 1000)
    prg.add(31000, "AOM IR Horiz_Ellipt freq", 110.00)
    prg.add(31500, "AOM IR Vertical Amp", 1000)
    prg.add(32000, "AOM IR Vertical freq", 80.00)
    prg.add(35500, "DAC IR Horizontal Ellipt ramp", start_t=0, stop_x=5, n_points=200, start_x=0, stop_t=100)
    prg.add(36500, "DAC IR Vertical ramp", start_t=0, stop_x=4, n_points=200, start_x=0, stop_t=100)
    prg.add(1036600, "wait")
    prg.add(1520500, "DAC IR Horizontal ramp", start_t=0, stop_x=-0.01, n_points=200, start_x=0.04, stop_t=500)
    prg.add(6530500, "AOM IR Horizontal freq", 110.00)
    prg.add(6531500, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=10, stop_t=500)
    prg.add(11532500, "Config field OFF")
    return prg
