prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(135050000, "switch off MOT ", enable=False)
    prg.add(135050000, "switch off MOT _ Depumper ")
    prg.add(135080000, "Picture Na_2Gdet_offset", enable=False)
    prg.add(135080000, "Picture Na_3Gdet_offset", enable=False)
    prg.add(135080000, "Picture Na_4Gdet_offset")
    prg.add(139185599, "Set MOT")
    return prg
