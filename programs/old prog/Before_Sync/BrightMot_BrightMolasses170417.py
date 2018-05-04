prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10000, "Initialize_Dipole_Off")
    prg.add(10010000, "Set Bright MOT")
    prg.add(90520000, "Compressed_MOT")
    prg.add(90770000, "switch off MOT ")
    prg.add(90780000, "Bright_Molasses_Ramp")
    prg.add(90780000, "Bright_Molasses_pulse", enable=False)
    prg.add(90802000, "Picture Na", enable=False)
    prg.add(90802000, "Picture Na_offset")
    prg.add(100802000, "Set Bright MOT")
    return prg
