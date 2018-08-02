prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(500, "DAC IR Vertical ramp", start_t=0, stop_x=0.2, n_points=10, start_x=0.08, stop_t=10)
    prg.add(1000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=10, start_x=0.03, stop_t=10)
    return prg
