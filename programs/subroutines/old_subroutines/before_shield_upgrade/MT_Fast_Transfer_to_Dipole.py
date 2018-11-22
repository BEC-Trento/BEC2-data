prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "MT Current Ramp", start_t=0, stop_x=3.5, n_points=150, start_x=15, stop_t=400)
    return prg
