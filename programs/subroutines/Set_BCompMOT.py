prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BcompX OPEN")
    prg.add(10, "IGBT BcompY OPEN")
    prg.add(20, "IGBT Bcompz OPEN")
    prg.add(30, "IGBT BCompZfine OPEN")
    prg.add(40, "IGBT BGradX OPEN")
    prg.add(50, "IGBT BGradY OPEN")
    prg.add(60, "IGBT BGradZ OPEN")
    prg.add(70, "DAC BCompX", 0.0000)
    prg.add(80, "DAC BCompY", 0.0000)
    prg.add(90, "DAC BGradX", 0.0000)
    return prg
