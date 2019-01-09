prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(11, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0.04, stop_t=1000)
    prg.add(16, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=1000)
    prg.add(10000100, "Compensate_external_Mag_Field", enable=False)
    return prg
