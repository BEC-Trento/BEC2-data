prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS ON")
    prg.add(100, "Shutter 3D MOT ON")
    prg.add(200, "Shutter DS ON")
    prg.add(300, "Shutter RepumperMOT OFF")
    prg.add(500, "Shutter Probe OFF")
    prg.add(700, "Shutter Push ON")
    return prg