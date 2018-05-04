prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 5.0000)
    prg.add(135080000, "Bright_Compressed_MOT")
    prg.add(135088000, "switch off MOT _ Depumper ")
    prg.add(135090350, "GM BrokenRamp_Short")
    prg.add(135140350, "Config Field MT")
    prg.add(135340350, "MT_Compression", enable=False)
    prg.add(140540350, "Evaporation Ramp.sub", enable=False)
    prg.add(140540350, "[VOID] End Evaporation")
    prg.add(140740350, "Config field OFF")
    prg.add(140790350, "Picture Na_2Gdet_offset")
    prg.add(140790350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(140790350, "Picture Na_offset", enable=False)
    prg.add(140790350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(140790350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(144895949, "Set MOT")
    return prg
