prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "MT Current Ramp", start_t=0, stop_x=4.25, n_points=500, start_x=35, stop_t=250)
    prg.add(5000000, "MT Current Ramp", start_t=0, stop_x=35, n_points=500, start_x=4.25, stop_t=500)
    return prg
