prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "BCompZ current ramp", start_t=0, stop_x=0, n_points=5, start_x=0.24, stop_t=1)
    prg.add(10500, "BComp2 current ramp", start_t=0, stop_x=0.5, n_points=5, start_x=0.21, stop_t=1)
    prg.add(11000, "BCompZ current ramp", start_t=0, stop_x=2, n_points=20, start_x=0, stop_t=5)
    prg.add(61500, "BComp2 current ramp", start_t=0, stop_x=0.21, n_points=5, start_x=5, stop_t=5)
    return prg
