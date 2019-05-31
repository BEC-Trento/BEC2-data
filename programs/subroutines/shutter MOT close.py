prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS OFF")
    prg.add(400, "Shutter DS OFF")
    prg.add(800, "Shutter RepumperMOT OFF", enable=False)
    prg.add(1200, "Shutter Push OFF")
    prg.add(1600, "Shutter 3D MOT OFF")
    return prg
