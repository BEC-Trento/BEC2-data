prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BcompX OPEN")
    prg.add(100, "IGBT BcompY OPEN")
    prg.add(200, "IGBT Bcompz OPEN")
    prg.add(300, "IGBT BGradX OPEN")
    prg.add(400, "IGBT BGradY field OPEN")
    prg.add(500, "IGBT BGradZ OPEN")
    return prg
