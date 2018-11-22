prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "3DMOT amp(+) ramp", start_t=0, stop_x=700, n_points=20, start_x=1000, stop_t=12, enable=False)
    prg.add(500, "DAC 3DMOT Coils Current", 9.0000, enable=False)
    prg.add(500, "3D MOT Coils ramp", start_t=0, stop_x=10, n_points=75, start_x=5, stop_t=75)
    prg.add(1000, "3DMOT Detuning ramp", start_t=0, stop_x=-23, n_points=75, start_x=-17, stop_t=75)
    prg.add(1500, "DS + RepMot amp ramp", start_t=0, stop_x=600, n_points=75, start_x=900, stop_t=75)
    prg.add(796000, "DS + RepMot amp ramp", start_t=0, stop_x=1, n_points=4, start_x=600, stop_t=0.4)
    return prg
