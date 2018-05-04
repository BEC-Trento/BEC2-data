prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 7.0000)
    prg.add(5181000, "DAC Horiz IR", 3.0000)
    prg.add(5181500, "AOM IR Horizontal freq", 80.00)
    prg.add(135081000, "Bright_Compressed_MOT", enable=False)
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135341350, "MT_Compression", enable=False)
    prg.add(135341350, "MT_Compression_20A", enable=False)
    prg.add(140541350, "Evaporation Ramp.sub")
    prg.add(290541350, "[VOID] End Evaporation")
    prg.add(290541850, "MT_Transfer_to_Dipole", enable=False)
    prg.add(290541850, "MT20A_Transfer_to_Dipole", enable=False)
    prg.add(290546850, "MT_Transfer_to_Dipole10A", enable=False)
    prg.add(290546850, "MT_FastTransfer_to_Dipole10A")
    prg.add(291556850, "Config field OFF")
    prg.add(291561850, "Horizontal Dipole Evaporation Ramp trials")
    prg.add(391571850, "Config field OFF", enable=False)
    prg.add(391576850, "Swich Off Dipole")
    prg.add(391676850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(391676850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(391676850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(391676850, "Picture Na_offset")
    prg.add(391676850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(391676850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(391676850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(395781449, "Initialize_Dipole_Off")
    prg.add(395786449, "Set MOT")
    return prg
