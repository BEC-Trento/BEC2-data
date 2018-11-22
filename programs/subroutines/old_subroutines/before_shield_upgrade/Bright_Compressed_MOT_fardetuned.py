prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "TTL Repumper MOT  ON", enable=False)
    prg.add(500, "TTL Dark spot OFF", enable=False)
    prg.add(1000, "3D MOT Coils ramp", start_t=0, stop_x=10, n_points=10, start_x=6, stop_t=0.5)
    prg.add(1500, "3DMOT Detuning ramp", start_t=0, stop_x=-58, n_points=10, start_x=-18, stop_t=0.5, enable=False)
    prg.add(2000, "DS + RepMot amp ramp", start_t=0, stop_x=350, n_points=10, start_x=500, stop_t=0.5, enable=False)
    return prg
