prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5150000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5250500, "DAC Magnetic Trap Voltage", 7.1000)
    prg.add(125250500, "Compressed_MOT")
    prg.add(125510500, "switch off MOT ", enable=False)
    prg.add(125510500, "switch off MOT _ Depumper ")
    prg.add(125512850, "GM FullSequence")
    prg.add(125681850, "Config Field MT")
    prg.add(135681850, "Evaporation Ramp.sub")
    prg.add(285691850, "BComp1 current ramp", start_t=0, stop_x=2, n_points=50, start_x=0.31, stop_t=50)
    prg.add(286201850, "Config field OFF")
    prg.add(286211850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(286211850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(286211850, "Picture Na_Shortrepumper_offset")
    prg.add(286211850, "Picture Na_05Gdet_offset", enable=False)
    prg.add(286211850, "Picture Na_offset", enable=False)
    prg.add(290317449, "Set MOT")
    return prg
