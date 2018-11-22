prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "MT Current Ramp", start_t=0, stop_x=20.5, n_points=100, start_x=35, stop_t=500)
    prg.add(10000000, "MT Current Ramp", start_t=0, stop_x=35, n_points=100, start_x=20.5, stop_t=500)
    return prg
