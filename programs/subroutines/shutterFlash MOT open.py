prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS ON")
    prg.add(400, "Shutter 3D MOT ON")
    prg.add(800, "Shutter DS ON")
    prg.add(1200, "Shutter Push ON")
    prg.add(1600, "Shutter RepumperMOT ON")
    prg.add(1800, "Shutter Probe ON")
    return prg
