prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set Bright MOT")
    prg.add(85550350, "Compressed_MOT")
    prg.add(85800350, "switch off MOT ", enable=False)
    prg.add(85800350, "switch off MOT _ Depumper ")
    prg.add(85815350, "Picture Na_2Gdet_offset")
    prg.add(89920949, "Set Bright MOT")
    return prg
