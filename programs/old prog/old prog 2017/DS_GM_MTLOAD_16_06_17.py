prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5150000, "DAC Magnetic Trap current", 8.0000)
    prg.add(85650350, "Compressed_MOT")
    prg.add(85916850, "switch off MOT ", enable=False)
    prg.add(85916850, "switch off MOT _ Depumper ")
    prg.add(85919200, "GM FullSequence")
    prg.add(86099200, "Config Field MT")
    prg.add(91099200, "MT_Compression")
    prg.add(93599200, "Config field OFF")
    prg.add(93649200, "Picture Na_2Gdet_offset", enable=False)
    prg.add(93649200, "Picture Na_1Gdet_offset", enable=False)
    prg.add(93649200, "Picture Na_offset")
    prg.add(97754799, "Set MOT")
    return prg
