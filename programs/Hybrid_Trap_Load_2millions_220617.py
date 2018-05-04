prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5150000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5150500, "DAC Magnetic Trap Voltage", 5.0000)
    prg.add(5151000, "DAC Horiz IR", 1.2500)
    prg.add(5151500, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(125151500, "Compressed_MOT")
    prg.add(125413000, "switch off MOT _ Depumper ")
    prg.add(125413000, "switch off MOT ", enable=False)
    prg.add(125413850, "GM FullSequence")
    prg.add(125582850, "Config Field MT")
    prg.add(130581000, "AOM IR Horizontal freq", 80.00)
    prg.add(130582850, "MT_Compression")
    prg.add(133083350, "Evaporation Ramp.sub")
    prg.add(215093350, "MT_Transfer_to_Dipole")
    prg.add(245143350, "Config field OFF")
    prg.add(245343350, "AOM IR Horizontal freq", 120.00)
    prg.add(245383350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(245383350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(245383350, "Picture Na_05Gdet_offset", enable=False)
    prg.add(245383350, "Picture Na_offset")
    prg.add(255238000, "Set MOT")
    return prg
