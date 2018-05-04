prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=5.5, n_points=50, start_x=3, stop_t=50)
    prg.add(500500, "DAC Horiz IR", 0.0000)
    return prg
