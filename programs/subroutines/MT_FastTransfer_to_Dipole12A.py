prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "MT Current Ramp", start_t=0, stop_x=3.0, n_points=50, start_x=12, stop_t=300)
    return prg
