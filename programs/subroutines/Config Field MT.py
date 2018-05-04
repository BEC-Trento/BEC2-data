prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT MOT field OPEN")
    prg.add(10, "Relay AntiHelm CLOSE", enable=False)
    prg.add(20, "Relay Helm OPEN", enable=False)
    prg.add(500, "IGBT Magnetic Trap CLOSE")
    prg.add(1000, "IGBT Helm OPEN")
    prg.add(1500, "IGBT AntiHelm CLOSE")
    return prg
