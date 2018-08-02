prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC BCompZ", 0.0000)
    prg.add(500, "DAC IR Horizontal ramp", start_t=0, stop_x=0.04, n_points=200, start_x=5.4, stop_t=1000)
    prg.add(10500, "DAC Vert IR", -0.1000)
    prg.add(40500, "AOM IR Vertical freq", 80.00)
    prg.add(50700, "DAC IR Vertical ramp", start_t=0, stop_x=0.1, n_points=200, start_x=-0.1, stop_t=1500.5)
    prg.add(15010500, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=3.5, stop_t=1000)
    prg.add(25015500, "DAC IR Horizontal ramp", start_t=0, stop_x=1.5, n_points=100, start_x=0.5, stop_t=100, enable=False)
    prg.add(25016000, "IGBT Magnetic Trap OPEN")
    prg.add(25017000, "IGBT AntiHelm OPEN")
    return prg
