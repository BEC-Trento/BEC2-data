prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC BCompZ", 0.0000)
    prg.add(11, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0.04, stop_t=1000)
    prg.add(16, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=3.5, stop_t=1000)
    prg.add(10012, "IGBT BCompY field CLOSE", enable=False)
    prg.add(10000100, "Compensate_external_Mag_Field", enable=False)
    prg.add(10001000, "IGBT Magnetic Trap OPEN", enable=False)
    prg.add(10001100, "IGBT AntiHelm OPEN")
    prg.add(10001200, "Relay Helm OPEN")
    return prg
