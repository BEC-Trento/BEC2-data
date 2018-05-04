prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5150000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5250500, "DAC Magnetic Trap Voltage", 6.0000)
    prg.add(125251500, "Compressed_MOT", enable=False)
    prg.add(125251500, "Compressed_MOT_New_290617", enable=False)
    prg.add(125311500, "switch off MOT ", enable=False)
    prg.add(125311500, "switch off MOT _ Depumper ")
    prg.add(125313850, "GM FullSequence")
    prg.add(125483350, "Config Field MT")
    prg.add(125683350, "MT_Compression")
    prg.add(135683350, "Config field OFF")
    prg.add(135783350, "Picture Na_2Gdet_offset")
    prg.add(135783350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(135783350, "Picture Na_05Gdet_offset", enable=False)
    prg.add(135783350, "Picture Na_offset", enable=False)
    prg.add(139888949, "Set MOT")
    return prg
