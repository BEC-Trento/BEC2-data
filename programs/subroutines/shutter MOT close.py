prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Shutter 2D MOT/ZS OFF")
    prg.add(10, "Shutter DS-Repumper OFF")
    prg.add(20, "Shutter Push OFF")
    prg.add(30, "Shutter 3D MOT OFF")
    return prg
