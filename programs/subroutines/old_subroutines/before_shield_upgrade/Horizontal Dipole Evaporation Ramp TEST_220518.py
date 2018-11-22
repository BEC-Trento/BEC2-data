prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.04, n_points=2000, start_x=3, stop_t=10000, enable=False)
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=1, n_points=200, start_x=5.4, stop_t=1500)
    prg.add(15000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.33, n_points=100, start_x=1, stop_t=500)
    prg.add(20000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.11, n_points=200, start_x=0.33, stop_t=750)
    prg.add(27500000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.08, n_points=100, start_x=0.11, stop_t=500)
    return prg
