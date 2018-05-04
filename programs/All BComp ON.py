prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT BComp1 field CLOSE")
    prg.add(500, "IGBT BComp2 field CLOSE")
    prg.add(1000, "IGBT BCompz field CLOSE")
    return prg
