prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT Magnetic Trap OPEN")
    prg.add(500, "IGBT MOT field OPEN")
    prg.add(1000, "IGBT AntiHelm OPEN")
    prg.add(1509, "IGBT Helm OPEN")
    return prg
