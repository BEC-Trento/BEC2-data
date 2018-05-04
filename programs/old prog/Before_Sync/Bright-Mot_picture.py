prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10000, "Initialize_Dipole_Off")
    prg.add(10010000, "Set Bright MOT")
    prg.add(90520000, "Compressed_MOT", enable=False)
    prg.add(90770000, "switch off MOT ")
    prg.add(90780000, "Picture Na")
    prg.add(100780000, "Set Bright MOT")
    return prg
