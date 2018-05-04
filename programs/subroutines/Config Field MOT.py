prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-161230, "Relay AntiHelm CLOSE")
    prg.add(-40012, "Relay Helm OPEN")
    prg.add(0, "IGBT Magnetic Trap OPEN")
    prg.add(700, "IGBT MOT field CLOSE")
    prg.add(1000, "IGBT Helm OPEN")
    prg.add(1500, "IGBT AntiHelm CLOSE")
    return prg
