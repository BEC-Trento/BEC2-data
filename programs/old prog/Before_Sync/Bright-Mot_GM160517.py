prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10000, "Initialize_Dipole_Off")
    prg.add(10010000, "Set Bright MOT")
    prg.add(90520000, "Compressed_MOT")
    prg.add(90770000, "switch off MOT ")
    prg.add(90772350, "GM pulse 05ms")
    prg.add(90783000, "GM Ramp 12 Gamma")
    prg.add(91046000, "Picture Na")
    prg.add(101046000, "Set Bright MOT")
    return prg
