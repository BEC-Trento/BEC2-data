prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 81.50)
    prg.add(500, "DAC IR Vertical ramp", start_t=0, stop_x=3, n_points=20, start_x=-0.1, stop_t=1)
    return prg
