prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 7.0000)
    prg.add(5181000, "DAC Vert IR", 5.0000)
    prg.add(5181500, "AOM IR Vertical freq", 80.00)
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135341350, "MT_Compression")
    prg.add(140541350, "Evaporation Ramp.sub")
    prg.add(360541350, "[VOID] End Evaporation")
    prg.add(360541850, "MT_Transfer_to_Dipole")
    prg.add(380542350, "Dipole Evaporation Ramp 5V", enable=False)
    prg.add(380542350, "Dipole Broken Evaporation Ramp 5V")
    prg.add(480543350, "Config field OFF")
    prg.add(480543350, "Picture Field off at 0ms - Levit 10 ms", enable=False)
    prg.add(480543350, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(480543350, "Picture Field off at 0ms - Levit 30 ms", enable=False)
    prg.add(480543350, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(480543350, "Picture Field off at 0ms - Levit 50 ms", enable=False)
    prg.add(480543350, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(480543350, "Picture MT to Levit at 0ms - Levit 75 ms", enable=False)
    prg.add(480543350, "Picture Field off at 0ms - Levit 100 ms", enable=False)
    prg.add(480543850, "Swich Off Dipole")
    prg.add(480548850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(480548850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(480548850, "Picture Na_offset", enable=False)
    prg.add(480848850, "Picture Na_Shortrepumper_offset")
    prg.add(480848850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(480848850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(484953449, "Initialize_Dipole_Off")
    prg.add(484958449, "Set MOT")
    return prg
