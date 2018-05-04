prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Vertical ramp", start_t=0, stop_x=0.19, n_points=500, start_x=3, stop_t=10000)
    return prg
