prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-50000, "Relay BCompZ Invert")
    prg.add(0, "IGBT Bcompz field OPEN")
    prg.add(100000, "IGBT BCompz field CLOSE")
    prg.add(100500, "BCompZ current ramp", start_t=0, stop_x=10, n_points=20, start_x=0, stop_t=10)
    prg.add(400000, "BCompZ current ramp", start_t=0, stop_x=7.8, n_points=100, start_x=10, stop_t=100)
    prg.add(680000, "RF Landau-Zener LUT", 75)
    prg.add(680500, "RF Landau-Zener LUT", 500)
    prg.add(690000, "Oscilloscope Trigger ON")
    prg.add(1210000, "Oscilloscope Trigger OFF")
    prg.add(1220000, "RF Landau-Zener LUT", 0)
    prg.add(1450000, "BCompZ current ramp", start_t=0, stop_x=0.2, n_points=10, start_x=7.8, stop_t=10, functions=dict(stop_x=lambda x: cmd.get_var('bfin'), funct_enable=False))
    prg.add(1898000, "RF Landau-Zener LUT", 1000, enable=False)
    prg.add(1899000, "RF Landau-Zener LUT", 541, enable=False)
    prg.add(1905047, "RF Landau-Zener LUT", 0)
    return prg
