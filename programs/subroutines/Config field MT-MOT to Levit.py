prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT Helm CLOSE")
    prg.add(200, "IGBT AntiHelm OPEN")
    return prg
