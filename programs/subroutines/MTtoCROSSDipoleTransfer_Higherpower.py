prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 80.00)
    prg.add(500, "DAC IR Vertical ramp", start_t=0, stop_x=0.6, n_points=400, start_x=-0.1, stop_t=1000)
    prg.add(10010500, "DAC BCompZ", 0.0000)
    prg.add(10010511, "DAC IR Horizontal ramp", start_t=0, stop_x=0.03, n_points=100, start_x=0.04, stop_t=1000, enable=False)
    prg.add(10010516, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=3.5, stop_t=1000)
    prg.add(10020512, "IGBT BCompY field CLOSE", enable=False)
    prg.add(20010600, "Compensate_external_Mag_Field", enable=False)
    prg.add(20011500, "IGBT Magnetic Trap OPEN")
    prg.add(20011600, "IGBT AntiHelm OPEN")
    prg.add(20011700, "Relay Helm OPEN", enable=False)
    return prg
