prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.04, n_points=2000, start_x=3, stop_t=10000, enable=False)
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=1, n_points=200, start_x=5.4, stop_t=1500)
    prg.add(10000, "DAC Vert IR", -0.1000)
    prg.add(40000, "AOM IR Vertical freq", 80.00)
    prg.add(50000, "DAC IR Vertical ramp", start_t=0, stop_x=2, n_points=200, start_x=-0.1, stop_t=1500.5)
    prg.add(15000000, "DAC IR Horizontal ramp", start_t=0.05, stop_x=0.33, n_points=100, start_x=1, stop_t=500)
    prg.add(15010000, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=3.5, stop_t=1000)
    prg.add(25015000, "IGBT Magnetic Trap OPEN")
    prg.add(25016000, "IGBT AntiHelm OPEN")
    return prg
