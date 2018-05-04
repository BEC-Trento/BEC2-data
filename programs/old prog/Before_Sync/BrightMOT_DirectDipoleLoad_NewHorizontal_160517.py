prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10900, "Initialize_Dipole_Off")
    prg.add(10000900, "Set Bright MOT")
    prg.add(10510900, "AOM IR Horizontal freq", 80.00)
    prg.add(10511250, "AOM IR Vertical freq", 80.00)
    prg.add(90001299, "DAC IR Horizontal ramp", start_t=0, stop_x=7.8, n_points=200, start_x=2, stop_t=100, enable=False)
    prg.add(90511250, "Compressed_MOT")
    prg.add(90761250, "switch off MOT ")
    prg.add(90761250, "switch off MOT _ Depumper ", enable=False)
    prg.add(90764000, "GM pulse 05ms")
    prg.add(90779000, "GM Ramp DipoleLoad", enable=False)
    prg.add(90779000, "GM Ramp 12 Gamma")
    prg.add(90952000, "IGBT MOT field ON", enable=False)
    prg.add(91952500, "Picture Na", enable=False)
    prg.add(91952500, "Picture Na Pushprobe", enable=False)
    prg.add(91952500, "AOM IR Horizontal freq", 130.00)
    prg.add(91953000, "AOM IR Vertical freq", 120.00)
    prg.add(91963000, "Picture Push Na", enable=False)
    prg.add(91963000, "Picture Na")
    prg.add(91963000, "Picture Na Pushprobe", enable=False)
    prg.add(98966040, "Set Bright MOT")
    prg.add(98973463, "Initialize_Dipole_Off")
    return prg