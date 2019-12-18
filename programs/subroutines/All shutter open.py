prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS ON")
    prg.add(100, "Shutter 3D MOT ON")
    prg.add(200, "Shutter DS-Repumper ON")
    prg.add(300, "Shutter Gray Molasses ON")
    prg.add(400, "Shutter Probe Hor ON")
    prg.add(500, "Shutter Push ON")
    prg.add(600, "Shutter Probe Vert ON")
    return prg
