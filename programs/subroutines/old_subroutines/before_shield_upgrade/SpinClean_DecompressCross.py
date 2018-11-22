prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC IR Horizontal ramp", start_t=0, stop_x=0.02, n_points=200, start_x=0.03, stop_t=100)
    prg.add(0, "DAC Magnetic Trap Voltage", 15.0000)
    prg.add(500, "DAC IR Vertical ramp", start_t=0, stop_x=0.02, n_points=200, start_x=0.07, stop_t=100)
    prg.add(1300, "DAC Magnetic Trap current", 25.0000)
    prg.add(1100000, "Config field gradient to levit")
    prg.add(1300000, "IGBT Magnetic Trap OPEN")
    prg.add(1310000, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(1320000, "DAC Magnetic Trap current", 0.0000)
    return prg
