prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10900, "Initialize_Dipole_Off")
    prg.add(10000900, "Set Bright MOT")
    prg.add(10500000, "DAC Horiz IR", 7.0000)
    prg.add(10510900, "AOM IR Horizontal freq", 80.00)
    prg.add(10511250, "AOM IR Vertical freq", 80.00, enable=False)
    prg.add(90750000, "CMOT_DipoleLoad")
    prg.add(91559250, "switch off MOT ")
    prg.add(91559250, "switch off MOT _ Depumper ", enable=False)
    prg.add(91562000, "GM pulse Dipole_Load")
    prg.add(92162000, "Picture Na", enable=False)
    prg.add(92162000, "Picture Na_offset", enable=False)
    prg.add(92162000, "Picture Na Pushprobe", enable=False)
    prg.add(92162500, "DAC IR Horizontal ramp", start_t=0, stop_x=5, n_points=50, start_x=7, stop_t=10)
    prg.add(92267500, "DAC IR Horizontal ramp", start_t=0, stop_x=1.5, n_points=750, start_x=5, stop_t=75)
    prg.add(93018000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.5, n_points=500, start_x=1.5, stop_t=150)
    prg.add(94518500, "DAC IR Horizontal ramp", start_t=0, stop_x=0.4, n_points=1000, start_x=0.5, stop_t=300)
    prg.add(97618500, "AOM IR Horizontal freq", 120.00)
    prg.add(97619000, "AOM IR Vertical freq", 120.00)
    prg.add(97619500, "Picture Push Na", enable=False)
    prg.add(97619500, "Picture Na", enable=False)
    prg.add(97619500, "Picture Na_offset")
    prg.add(97619500, "Picture Na Pushprobe", enable=False)
    prg.add(104622540, "Set Bright MOT")
    prg.add(104629963, "Initialize_Dipole_Off")
    return prg