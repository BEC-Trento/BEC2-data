prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Vertical ramp", start_t=0, stop_x=0.25, n_points=2000, start_x=5, stop_t=10000)
    return prg
