prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "3DMOT amp(+) ramp", start_t=0, stop_x=700, n_points=20, start_x=1000, stop_t=12, enable=False)
    prg.add(0, "TTL Repumper MOT  ON")
    prg.add(500, "TTL Dark spot OFF")
    prg.add(1000, "DAC 3DMOT Coils Current", 10.0000, enable=False)
    prg.add(1000, "3D MOT Coils ramp", start_t=0, stop_x=9, n_points=10, start_x=6, stop_t=0.5)
    prg.add(1500, "3DMOT Detuning ramp", start_t=0, stop_x=-10, n_points=10, start_x=-18, stop_t=0.5)
    prg.add(2000, "DS + RepMot amp ramp", start_t=0, stop_x=1000, n_points=10, start_x=500, stop_t=0.5)
    prg.add(42000, "DS + RepMot amp ramp", start_t=0, stop_x=1, n_points=4, start_x=200, stop_t=0.4, enable=False)
    return prg
