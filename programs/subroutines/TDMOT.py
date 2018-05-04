prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM DS + RepumperMOT Amp ", 380)
    prg.add(500, "AOM 3DMOT Detuning", -18.000)
    prg.add(1000000, "AOM 3DMOT Detuning", -36.000)
    prg.add(1000500, "3D MOT Coils ramp", start_t=0, stop_x=0, n_points=25, start_x=9, stop_t=20)
    return prg
