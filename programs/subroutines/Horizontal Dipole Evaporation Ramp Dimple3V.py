prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=1, n_points=200, start_x=3, stop_t=2500)
    prg.add(25000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.33, n_points=100, start_x=1, stop_t=1000)
    prg.add(35000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.11, n_points=200, start_x=0.33, stop_t=1250)
    prg.add(47500000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.02, n_points=100, start_x=0.11, stop_t=1750)
    return prg
