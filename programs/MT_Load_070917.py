prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5150000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5250500, "DAC Magnetic Trap Voltage", 6.0000)
    prg.add(135251500, "Compressed_MOT", enable=False)
    prg.add(135251500, "Compressed_MOT_New_290617", enable=False)
    prg.add(135311500, "switch off MOT ", enable=False)
    prg.add(135311500, "switch off MOT _ Depumper ")
    prg.add(135313850, "GM FullSequence", enable=False)
    prg.add(135313850, "GM BrokenRamp_Short")
    prg.add(135363850, "Config Field MT")
    prg.add(135563850, "MT_Compression", enable=False)
    prg.add(140563850, "Config field OFF")
    prg.add(140613850, "Picture Na_2Gdet_offset")
    prg.add(140613850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(140613850, "Picture Na_05Gdet_offset", enable=False)
    prg.add(140613850, "Picture Na_offset", enable=False)
    prg.add(144719449, "Set MOT")
    return prg
