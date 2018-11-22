prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(500, "IGBT Magnetic Trap CLOSE")
    prg.add(1000, "IGBT Helm OPEN")
    prg.add(1500, "IGBT AntiHelm CLOSE")
    return prg
