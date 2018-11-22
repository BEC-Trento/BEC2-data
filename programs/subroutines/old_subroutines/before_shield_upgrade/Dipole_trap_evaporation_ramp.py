prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-58000, "DAC Horiz IR", 6.0000)
    prg.add(-30000, "DAC Vert IR", 6.0000)
    prg.add(-14000, "AOM IR Horizontal freq", 80.00)
    prg.add(-4000, "AOM IR Vertical freq", 80.00)
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=3, n_points=50, start_x=6, stop_t=5)
    prg.add(500, "DAC IR Vertical ramp", start_t=0, stop_x=3, n_points=50, start_x=6, stop_t=5)
    prg.add(50000, "DAC IR Horizontal ramp", start_t=0, stop_x=1, n_points=100, start_x=3, stop_t=50)
    prg.add(50500, "DAC IR Vertical ramp", start_t=0, stop_x=1, n_points=100, start_x=3, stop_t=50)
    prg.add(550000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.2, n_points=100, start_x=1, stop_t=150)
    prg.add(550500, "DAC IR Vertical ramp", start_t=0, stop_x=0.2, n_points=100, start_x=1, stop_t=150)
    prg.add(2051000, "Initialize_Dipole_Off")
    return prg
