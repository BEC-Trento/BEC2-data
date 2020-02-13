prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS ON")
    prg.add(100, "Shutter 3D MOT ON")
    prg.add(300, "Shutter Gray Molasses OFF")
    prg.add(700, "Shutter Push ON")
    prg.add(800, "Shutter Probe Hor OFF")
    prg.add(900, "Shutter probe Vert OFF")
    prg.add(1200, "Shutter DS-Repumper ON")
    return prg
