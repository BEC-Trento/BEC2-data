prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(119969000, "Config Field OFF.sub")
    prg.add(119970000, "MOT lights Off.sub")
    prg.add(119972010, "GrayMolasses_ON.sub")
    prg.add(119976010, "Rampa GM per test", start_t=0.0000, stop_x=200.000, n_points=25, start_x=1000.000, stop_t=2.0000)
    prg.add(119996010, "Repumper D1 OFF")
    prg.add(119998000, "GrayMolasses_OFF.sub")
    prg.add(120002000, "Grav Comp", 8.0000)
    prg.add(120003020, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=50, start_x=50.000, stop_t=1700.0000)
    prg.add(120003040, "Config MT not compr.sub")
    prg.add(120013020, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=50, start_x=0.000, stop_t=1700.0000)
    prg.add(122007040, "All Shutter Close.sub")
    prg.add(125009040, "Mirrors Imaging")
    prg.add(125509040, "IGBT B comp x ON")
    prg.add(126009040, "All AOM On.sub")
    prg.add(127506050, "IGBT 2 pinch+comp", 10.0000)
    prg.add(127507000, "IGBT 1 ramp", start_t=0.0000, stop_x=-10.000, n_points=500, start_x=10.000, stop_t=2000.0000)
    prg.add(130008020, "Grav Comp", 0.0000)
    prg.add(139998020, "B comp x", 100.0)
    prg.add(145000020, "Evaporation Ramp.sub")
    prg.add(672010000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(672020000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(680010000, "Config Field OFF.sub", enable=False)
    prg.add(680210000, "Picture NaK.sub", enable=False)
    prg.add(681800020, "Decompress Current MT.sub", enable=False)
    prg.add(681810020, "Decompress Voltage MT.sub", enable=False)
    prg.add(747410000, "Picture - Field off at 0ms - Levit 20ms.sub")
    prg.add(757410000, "Set MOT NaK.sub")
    prg.add(757910000, "Config MOT.sub")
    prg.add(758010000, "Dark Spot MOT load.sub")
    prg.add(995917018, "Picture - Field off at 0ms - Levit 5ms.sub", enable=False)
    return prg