prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.04, n_points=2000, start_x=3, stop_t=10000, enable=False)
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=3.2, n_points=100, start_x=5.4, stop_t=1250)
    prg.add(25000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.66, n_points=50, start_x=1, stop_t=500, enable=False)
    prg.add(35000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.22, n_points=100, start_x=0.33, stop_t=625, enable=False)
    prg.add(47500000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.066, n_points=50, start_x=0.11, stop_t=866.2, enable=False)
    return prg
