prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "BComp1 current ramp", start_t=0, stop_x=0.33, n_points=50, start_x=0.31, stop_t=199)
    prg.add(500, "BComp2 current ramp", start_t=0, stop_x=0.24, n_points=50, start_x=0.21, stop_t=199)
    prg.add(2000500, "DAC BComp1", 0.3100)
    prg.add(2001000, "DAC BComp2", 0.2100)
    return prg
