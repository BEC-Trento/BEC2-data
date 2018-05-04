prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 8.0000)
    prg.add(5181000, "DAC Vert IR", 6.0000)
    prg.add(5181500, "AOM IR Vertical freq", 80.00)
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135341350, "MT_Compression")
    prg.add(140541350, "MT_Transfer_to_Dipole10A")
    prg.add(160541350, "Config field OFF")
    prg.add(160941350, "Swich Off Dipole", enable=False)
    prg.add(160946350, "Picture Na_Shortrepumper_offset")
    prg.add(160946350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(160946350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(160946350, "Picture Na_offset", enable=False)
    prg.add(160946350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(160946350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(160946350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(165050949, "Initialize_Dipole_Off")
    prg.add(165055949, "Set MOT")
    return prg
