prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10900, "Initialize_Dipole_Off")
    prg.add(10000900, "Set Bright MOT")
    prg.add(10500000, "DAC Horiz IR", 7.0000)
    prg.add(10510900, "AOM IR Horizontal freq", 80.00)
    prg.add(10511250, "AOM IR Vertical freq", 80.00)
    prg.add(90750000, "CMOT_DipoleLoad")
    prg.add(91560000, "Bright_Molasses_Quadrupoleramp", enable=False)
    prg.add(91560000, "switch off MOT ")
    prg.add(91560500, "DAC 3DMOT Coils Current", 10.0000)
    prg.add(91560500, "switch off MOT _ Depumper ", enable=False)
    prg.add(91563250, "GM pulse 05ms")
    prg.add(91573250, "GM Ramp 12 Gamma")
    prg.add(91743250, "IGBT MOT field ON")
    prg.add(91743750, "3D MOT Coils ramp", start_t=0, stop_x=0, n_points=500, start_x=10, stop_t=50)
    prg.add(91753750, "GM pulse Dipole_Load")
    prg.add(92253750, "Picture Na_offset", enable=False)
    prg.add(92254250, "IGBT MOT field OFF")
    prg.add(92254250, "DAC 3DMOT Coils Current", 10.0000, enable=False)
    prg.add(93254250, "Picture Na", enable=False)
    prg.add(93254250, "Picture Na_offset", enable=False)
    prg.add(93254250, "Picture Na Pushprobe", enable=False)
    prg.add(93254250, "AOM IR Horizontal freq", 120.00)
    prg.add(93254750, "AOM IR Vertical freq", 120.00)
    prg.add(93264750, "Picture Push Na", enable=False)
    prg.add(93264750, "Picture Na", enable=False)
    prg.add(93264750, "Picture Na_offset")
    prg.add(93264750, "Picture Na Pushprobe", enable=False)
    prg.add(100267790, "Set Bright MOT")
    prg.add(100275213, "Initialize_Dipole_Off")
    return prg
