prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=4000, start_x=1.6, stop_t=6000)
    return prg
