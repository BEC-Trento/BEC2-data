prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-50000, "Relay BCompZ Invert")
    prg.add(0, "IGBT Bcompz field OPEN")
    prg.add(100000, "IGBT BCompz field CLOSE")
    prg.add(100100, "BCompZ current ramp", start_t=0, stop_x=10, n_points=20, start_x=0, stop_t=10)
    prg.add(101000, "Oscilloscope Trigger ON")
    prg.add(380000, "RF Landau-Zener LUT", 14)
    prg.add(380500, "RF Landau-Zener LUT", 500)
    prg.add(400000, "BCompZ current ramp", start_t=0, stop_x=9, n_points=100, start_x=10, stop_t=100)
    prg.add(1420000, "RF Landau-Zener LUT", 0)
    prg.add(1450000, "BCompZ current ramp", start_t=0, stop_x=0.230, n_points=10, start_x=9, stop_t=10)
    prg.add(1551000, "Oscilloscope Trigger OFF")
    prg.add(1798000, "RF Landau-Zener LUT", 1000)
    prg.add(1799000, "RF Landau-Zener LUT", 541)
    prg.add(1800000, "RF Landau-Zener ON")
    prg.add(1800180, "RF Landau-Zener OFF")
    prg.add(1801000, "RF Landau-Zener LUT", 0)
    return prg
