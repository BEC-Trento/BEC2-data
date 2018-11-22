prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT Magnetic Trap OPEN")
    prg.add(500, "IGBT MOT field CLOSE")
    prg.add(1000, "IGBT Upper Coil OPEN")
    prg.add(1500, "IGBT Bypass Upper Coil CLOSE")
    return prg
