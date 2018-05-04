prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "switch off MOT ")
    prg.add(10000, "Initialize_Dipole_Off")
    prg.add(10010000, "Set MOT")
    prg.add(90420350, "DS + RepMot amp ramp", start_t=0, stop_x=1000, n_points=100, start_x=450, stop_t=2.5, enable=False)
    prg.add(90420350, "Compressed_MOT")
    prg.add(90428000, "switchToBrightMot", enable=False)
    prg.add(90670350, "switch off MOT ", enable=False)
    prg.add(90670350, "switch off MOT _ Depumper ")
    prg.add(90720350, "Picture Na")
    prg.add(90720350, "Picture Na_offset", enable=False)
    prg.add(90720350, "Picture Na Pushprobe", enable=False)
    prg.add(90720350, "Picture Push Na", enable=False)
    prg.add(94825949, "Set MOT")
    return prg
