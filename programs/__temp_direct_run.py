prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(135050000, "Bright_Compressed_MOT", enable=False)
    prg.add(135058000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135058000, "switch off MOT ")
    prg.add(135058000, "switch off MOT fast", enable=False)
    prg.add(135060849, "GM FullSequence", enable=False)
    prg.add(135060849, "GM FullSequence_Short", enable=False)
    prg.add(135060849, "GM BrokenRamp_Short", enable=False)
    prg.add(135070849, "Picture Na_2Gdet_offset", enable=False)
    prg.add(135070849, "Picture Na_3Gdet_offset", enable=False)
    prg.add(135080849, "Picture Na_4Gdet_offset")
    prg.add(135080849, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(139186448, "Set MOT")
    return prg
