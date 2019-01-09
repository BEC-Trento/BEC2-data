prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC Vert IR", -0.1000)
    prg.add(100, "AOM IR Vertical freq", 80.00, enable=False)
    prg.add(1000100, "DAC IR Horizontal ramp", start_t=0, stop_x=0.01, n_points=100, start_x=0.04, stop_t=500)
    prg.add(1000600, "DAC IR Vertical ramp", start_t=0, stop_x=0.4, n_points=100, start_x=-0.1, stop_t=750)
    prg.add(1000605, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(1200605, "AOM IR Vertical freq", 80.00)
    return prg
