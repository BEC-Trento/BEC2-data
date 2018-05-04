prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5170000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5170500, "DAC Magnetic Trap Voltage", 7.0000)
    prg.add(135070000, "Bright_Compressed_MOT")
    prg.add(135078000, "switch off MOT _ Depumper ")
    prg.add(135080350, "GM BrokenRamp_Short")
    prg.add(135130350, "Config Field MT")
    prg.add(135330350, "MT_Compression", enable=False)
    prg.add(135530350, "Config field OFF", enable=False)
    prg.add(135530350, "BComp1 current ramp", start_t=0, stop_x=1, n_points=50, start_x=0.31, stop_t=10, enable=False)
    prg.add(135530350, "BComp2 current ramp", start_t=0, stop_x=1, n_points=50, start_x=0.21, stop_t=10)
    prg.add(135530350, "BCompZ current ramp", start_t=0, stop_x=2, n_points=100, start_x=0.24, stop_t=10, enable=False)
    prg.add(140030350, "Config field OFF")
    prg.add(140035350, "Picture Na_2Gdet_offset")
    prg.add(140035350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(140035350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(144140949, "Set MOT")
    return prg
