prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=1.25, n_points=200, start_x=5, stop_t=1500, functions=dict(start_x=lambda x: cmd.get_var('CigarV')))
    prg.add(15000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.4, n_points=100, start_x=1.25, stop_t=500)
    prg.add(20000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.14, n_points=200, start_x=0.4, stop_t=750)
    prg.add(27500000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.04, n_points=100, start_x=0.14, stop_t=500)
    return prg
