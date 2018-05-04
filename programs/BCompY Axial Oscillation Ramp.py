prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT BCompY field CLOSE")
    prg.add(500, "BCompY current ramp", start_t=0, stop_x=0.45, n_points=250, start_x=0, stop_t=195)
    prg.add(22000500, "IGBT BCompY field OPEN")
    return prg
