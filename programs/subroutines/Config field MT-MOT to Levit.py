prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT 4A OPEN")
    prg.add(100, "IGBT 4B CLOSE")
    return prg
