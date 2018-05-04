prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS OFF")
    prg.add(100, "Shutter 3D MOT OFF")
    prg.add(200, "Shutter DS OFF")
    prg.add(300, "Shutter Gray Molasses OFF")
    prg.add(400, "Shutter RepumperMOT OFF")
    prg.add(500, "Shutter Probe OFF")
    prg.add(600, "Shutter Push OFF")
    return prg
