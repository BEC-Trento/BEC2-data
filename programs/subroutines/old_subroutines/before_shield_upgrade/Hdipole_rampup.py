prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 80.00)
    prg.add(500, "DAC IR Vertical ramp", start_t=0, stop_x=1, n_points=500, start_x=0, stop_t=500)
    return prg
