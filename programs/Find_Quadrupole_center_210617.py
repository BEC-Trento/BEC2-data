prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(1050000, "Set MOT")
    prg.add(1150000, "DAC Magnetic Trap current", 8.0000)
    prg.add(1250500, "DAC Magnetic Trap Voltage", 5.0000)
    prg.add(3750500, "Compressed_MOT")
    prg.add(4010500, "switch off MOT ", enable=False)
    prg.add(4010500, "switch off MOT _ Depumper ")
    prg.add(4012850, "GM FullSequence")
    prg.add(4182350, "Config Field MT")
    prg.add(9182350, "MT_Compression")
    prg.add(19182350, "MOT_Light_Flash")
    prg.add(19333350, "Config field OFF")
    prg.add(19334350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(19334350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(19334350, "Picture Na_05Gdet_offset", enable=False)
    prg.add(19334350, "Picture Na_offset")
    prg.add(23439949, "Set MOT")
    return prg
