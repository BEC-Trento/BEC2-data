prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-180100, "Relay Helm CLOSE")
    prg.add(-50119, "Relay AntiHelm OPEN")
    prg.add(-40000, "IGBT AntiHelm OPEN")
    prg.add(50, "IGBT Magnetic Trap OPEN")
    prg.add(100, "IGBT MOT field CLOSE")
    prg.add(150, "IGBT Helm CLOSE")
    return prg
