prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC BCompY", 0.0000)
    prg.add(500, "DAC BCompX", 0.0000)
    prg.add(1000, "DAC BGradX", 0.0000)
    prg.add(1100, "IGBT Bcompz OPEN")
    prg.add(1200, "IGBT BcompY OPEN")
    prg.add(1300, "IGBT BGradX OPEN")
    prg.add(1400, "IGBT BGradZ OPEN")
    prg.add(1500, "IGBT BGradY OPEN")
    prg.add(1600, "IGBT BcompX OPEN")
    return prg
