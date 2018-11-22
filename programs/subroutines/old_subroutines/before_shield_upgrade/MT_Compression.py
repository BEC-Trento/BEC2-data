prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC Magnetic Trap Voltage", 11.0000)
    prg.add(500, "MT Current Ramp", start_t=0, stop_x=15, n_points=1000, start_x=10, stop_t=500)
    return prg
