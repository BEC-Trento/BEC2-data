prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "MT Current Ramp", start_t=0, stop_x=5, n_points=100, start_x=8, stop_t=300)
    prg.add(21000500, "MT Current Ramp", start_t=0, stop_x=3.5, n_points=100, start_x=5, stop_t=1000)
    return prg
