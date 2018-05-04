prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(135050000, "Compressed_MOT", enable=False)
    prg.add(135306500, "switch off MOT ", enable=False)
    prg.add(135306500, "switch off MOT _ Depumper ", enable=False)
    prg.add(135306500, "switch off MOT _ Depumper_short ")
    prg.add(135308850, "GM FullSequence", enable=False)
    prg.add(135308850, "GMPulse", enable=False)
    prg.add(135309850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(135309850, "Picture Na_3Gdet_offset")
    prg.add(135309850, "Picture Na_offset", enable=False)
    prg.add(139415449, "Set MOT")
    return prg
