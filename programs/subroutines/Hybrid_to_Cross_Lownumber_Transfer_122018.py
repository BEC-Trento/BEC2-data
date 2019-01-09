prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC Vert IR", -0.1000)
    prg.add(1011, "DAC IR Horizontal ramp", start_t=0, stop_x=0.0005, n_points=100, start_x=0.04, stop_t=500)
    prg.add(1511, "DAC IR Vertical ramp", start_t=0, stop_x=0.005, n_points=100, start_x=-0.1, stop_t=500)
    prg.add(1516, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(201300, "AOM IR Vertical freq", 80.00)
    return prg
