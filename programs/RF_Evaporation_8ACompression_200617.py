prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5150000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5250500, "DAC Magnetic Trap Voltage", 5.0000)
    prg.add(125250500, "Compressed_MOT")
    prg.add(125510500, "switch off MOT ", enable=False)
    prg.add(125510500, "switch off MOT _ Depumper ")
    prg.add(125512850, "GM FullSequence")
    prg.add(125681850, "Config Field MT")
    prg.add(130681850, "MT_Compression", enable=False)
    prg.add(133181850, "Evaporation Ramp.sub")
    prg.add(183181850, "Config field OFF")
    prg.add(183231850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(183231850, "Picture Na_1Gdet_offset")
    prg.add(183231850, "Picture Na_05Gdet_offset", enable=False)
    prg.add(183231850, "Picture Na_offset", enable=False)
    prg.add(187337449, "Set MOT")
    return prg
