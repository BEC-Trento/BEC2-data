prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(135050000, "Bright_Compressed_MOT", enable=False)
    prg.add(135058000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135061000, "switch off MOT fast")
    prg.add(135063849, "GM BrokenRamp_Short")
    prg.add(135063849, "GM FullSequence_Short", enable=False)
    prg.add(135114849, "Probe_Flash", enable=False)
    prg.add(135214849, "Picture Na_2Gdet_offset", enable=False)
    prg.add(135214849, "Picture Na_offset", enable=False)
    prg.add(135214849, "Picture Na_3Gdet_offset", enable=False)
    prg.add(135214849, "Picture Na_4Gdet_offset")
    prg.add(139320448, "Set MOT")
    return prg
