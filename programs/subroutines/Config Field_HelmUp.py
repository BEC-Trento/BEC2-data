prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT 1A OPEN")
    prg.add(100, "IGBT 1B CLOSE")
    prg.add(200, "IGBT 2A CLOSE")
    prg.add(300, "IGBT 2B OPEN")
    prg.add(400, "IGBT 3A OPEN")
    prg.add(500, "IGBT 3B CLOSE")
    prg.add(600, "IGBT 4A CLOSE")
    prg.add(700, "IGBT 4B OPEN")
    return prg
