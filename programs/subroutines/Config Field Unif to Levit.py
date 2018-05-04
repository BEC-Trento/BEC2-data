prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-201234, "Relay AntiHelm CLOSE")
    prg.add(-50000, "Relay Helm OPEN")
    prg.add(0, "IGBT Helm CLOSE")
    prg.add(200, "IGBT AntiHelm OPEN")
    prg.add(250, "IGBT Magnetic Trap CLOSE")
    prg.add(300, "IGBT MOT field OPEN")
    return prg
