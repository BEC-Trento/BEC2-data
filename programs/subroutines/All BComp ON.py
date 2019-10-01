prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompX CLOSE")
    prg.add(500, "IGBT BCompY CLOSE")
    prg.add(1000, "IGBT BCompz CLOSE")
    return prg
