prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT Magnetic Trap OPEN")
    prg.add(500, "IGBT AntiHelm OPEN")
    prg.add(1000, "IGBT Helm OPEN")
    return prg
