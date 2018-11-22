prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.02, n_points=200, start_x=0.03, stop_t=100)
    prg.add(500, "DAC IR Vertical ramp", start_t=0, stop_x=0.02, n_points=200, start_x=0.05, stop_t=100)
    return prg
