prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS ON")
    prg.add(100, "Shutter 3D MOT ON")
    prg.add(300, "Shutter Gray Molasses OFF", enable=False)
    prg.add(500, "Shutter Probe OFF")
    prg.add(700, "Shutter Push ON")
    prg.add(1000, "Shutter DS OFF")
    prg.add(1200, "Shutter RepumperMOT ON")
    return prg
