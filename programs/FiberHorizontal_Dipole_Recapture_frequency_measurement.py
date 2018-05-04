prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 7.0000)
    prg.add(5181000, "DAC Horiz IR", 3.0000)
    prg.add(5181500, "AOM IR Horizontal freq", 80.00)
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(140541350, "Evaporation Ramp.sub")
    prg.add(290541350, "[VOID] End Evaporation")
    prg.add(290546850, "MT_FastTransfer_to_Dipole10A")
    prg.add(292546850, "Dipole_Turnoff_and_Recapture")
    prg.add(292946850, "Config field OFF")
    prg.add(292951850, "Swich Off Dipole")
    prg.add(292971850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(292971850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(292971850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(292971850, "Picture Na_offset", enable=False)
    prg.add(292971850, "Picture Na_Shortrepumper_offset")
    prg.add(292971850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(292971850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(297076449, "Initialize_Dipole_Off")
    prg.add(297081449, "Set MOT")
    return prg