prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10900, "Initialize_Dipole_Off")
    prg.add(10000900, "Set Bright MOT", enable=False)
    prg.add(10200900, "Set MOT")
    prg.add(10510900, "AOM IR Horizontal freq", 80.00)
    prg.add(10511250, "AOM IR Vertical freq", 80.00)
    prg.add(90511250, "DS + RepMot amp ramp", start_t=0, stop_x=1000, n_points=100, start_x=450, stop_t=2.5, enable=False)
    prg.add(90536750, "switch off MOT ")
    prg.add(90539500, "GM pulse 05ms")
    prg.add(90554500, "GM Ramp DipoleLoad")
    prg.add(90759500, "IGBT MOT field ON", enable=False)
    prg.add(90900500, "Picture Na")
    prg.add(90959500, "AOM IR Horizontal freq", 120.00)
    prg.add(90960500, "AOM IR Vertical freq", 120.00)
    prg.add(93078037, "Set MOT")
    prg.add(93081077, "Set Bright MOT", enable=False)
    prg.add(93088500, "Initialize_Dipole_Off")
    return prg
