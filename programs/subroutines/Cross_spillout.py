prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(500, "DAC IR Horizontal ramp", start_t=0, stop_x=0.001, n_points=100, start_x=0.01, stop_t=205)
    prg.add(1200, "DAC IR Vertical ramp", start_t=0, stop_x=0.005, n_points=100, start_x=0.4, stop_t=200)
    prg.add(8000000, "DAC IR Vertical ramp", start_t=0, stop_x=0.05, n_points=100, start_x=0.05, stop_t=200, enable=False)
    return prg
