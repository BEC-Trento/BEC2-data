prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.04, n_points=2000, start_x=3, stop_t=10000, enable=False)
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=1, n_points=200, start_x=3, stop_t=3000)
    prg.add(30000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.2, n_points=200, start_x=1, stop_t=3000)
    prg.add(60000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.06, n_points=200, start_x=0.2, stop_t=4000)
    return prg
