prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompY CLOSE")
    prg.add(2000, "DAC BCompY", 2.0000)
    prg.add(100000, "DAC MT-MOT Current", 0.0000)
    prg.add(200000, "Config field Levit", enable=False)
    prg.add(200000, "Config field Bottom_coil_Bup", enable=False)
    prg.add(200000, "Config Field MT_helmDown", enable=False)
    prg.add(200000, "Config Field_HelmUp", enable=False)
    prg.add(200000, "Config Field MT-MOT")
    prg.add(200000, "Config field AntiHelm inverted", enable=False)
    prg.add(210000, "MT Current Ramp", start_t=0, stop_x=50, n_points=100, start_x=0, stop_t=50)
    prg.add(1000000, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=50, stop_t=50)
    prg.add(2000000, "Config field OFF")
    prg.add(2010000, "DAC BCompY", 0.0000)
    prg.add(2200000, "IGBT BcompY OPEN")
    return prg
