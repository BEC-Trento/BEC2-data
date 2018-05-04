prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Vertical ramp", start_t=0, stop_x=2, n_points=150, start_x=5, stop_t=3000)
    prg.add(30000500, "DAC IR Vertical ramp", start_t=0, stop_x=1, n_points=150, start_x=2, stop_t=3000)
    prg.add(60001000, "DAC IR Vertical ramp", start_t=0, stop_x=0.8, n_points=100, start_x=1, stop_t=10000)
    return prg
