prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT Bcompz OPEN")
    prg.add(1000, "IGBT BCompX CLOSE")
    prg.add(2000, "DAC BCompX", 0.1000)
    prg.add(101000, "Relay BCompZ Invert")
    prg.add(101000, "Relay BCompZ Normal", enable=False)
    prg.add(301000, "IGBT BCompz CLOSE")
    prg.add(311000, "BCompZ current ramp", start_t=0, stop_x=9, n_points=10, start_x=0, stop_t=50)
    prg.add(1001000, "BCompZ current ramp", start_t=0, stop_x=0, n_points=10, start_x=9, stop_t=50)
    prg.add(1601000, "DAC BCompX", 0.0000)
    prg.add(1801000, "IGBT BcompX OPEN")
    prg.add(1801100, "IGBT Bcompz OPEN")
    return prg
