prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.04, n_points=200, start_x=1.25, stop_t=2000)
    prg.add(10000500, "DAC IR Vertical ramp", start_t=0, stop_x=0.75, n_points=500, start_x=4, stop_t=1000, enable=False)
    return prg
