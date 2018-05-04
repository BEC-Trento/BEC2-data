prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Vertical ramp", start_t=0, stop_x=0.8, n_points=200, start_x=6, stop_t=2000, enable=False)
    prg.add(15000000, "DAC IR Vertical ramp", start_t=0.05, stop_x=0.4, n_points=100, start_x=1, stop_t=500)
    prg.add(20000000, "DAC IR Vertical ramp", start_t=0.05, stop_x=0.15, n_points=200, start_x=0.33, stop_t=750)
    prg.add(27500000, "DAC IR Vertical ramp", start_t=0.05, stop_x=0.06, n_points=100, start_x=0.11, stop_t=500)
    return prg
