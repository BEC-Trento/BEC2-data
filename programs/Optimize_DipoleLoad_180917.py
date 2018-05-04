prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 5.4000)
    prg.add(5181500, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135089000, "switch off MOT ", enable=False)
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135346350, "MT_Compression", enable=False)
    prg.add(135346350, "MT_Compression_10A")
    prg.add(135346350, "MT_Compression_12A", enable=False)
    prg.add(135346350, "MT_Compression_20A", enable=False)
    prg.add(135353350, "DAC BCompZ", 0.2400)
    prg.add(135353350, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(140553350, "Evaporation Ramp.sub")
    prg.add(155553350, "[VOID] End Evaporation")
    prg.add(155553850, "DAC Horiz IR", 0.0000)
    prg.add(155554350, "AOM IR Horizontal freq", 80.00)
    prg.add(155554850, "DAC IR Horizontal ramp", start_t=0, stop_x=5.4, n_points=100, start_x=0, stop_t=1000)
    prg.add(255554850, "MT_Transfer_to_Dipole", enable=False)
    prg.add(255554850, "MT20A_Transfer_to_Dipole", enable=False)
    prg.add(255554850, "MT_Transfer_to_Dipole10A", enable=False)
    prg.add(255554850, "MT_FastTransfer_to_Dipole10A")
    prg.add(255554850, "MT_Transfer_to_Dipole8A", enable=False)
    prg.add(255554850, "MT_FastTransfer_to_Dipole8A", enable=False)
    prg.add(255554850, "MT_FastTransfer_to_Dipole12A", enable=False)
    prg.add(255554850, "MT_StepTransfer_to_Dipole8A", enable=False)
    prg.add(259555350, "Horizontal Dipole Evaporation Ramp trials", enable=False)
    prg.add(259555350, "Horizontal Dipole Evaporation Ramp Dimple3V", enable=False)
    prg.add(259555350, "Horizontal Dipole Evaporation Ramp 5.4V", enable=False)
    prg.add(259555350, "Horizontal Dipole Evaporation Ramp CMT20A_5.4V")
    prg.add(259555350, "Horizontal Dipole Evaporation Ramp CMT8A_5V", enable=False)
    prg.add(259555350, "Horizontal Dimple Evaporation BEC 24_08_17", enable=False)
    prg.add(292055350, "[VOID] End Evaporation")
    prg.add(292055850, "Config field OFF", enable=False)
    prg.add(292055850, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(292055850, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(292055850, "Picture MT to Levit at 0ms - Levit 50 ms")
    prg.add(292055850, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(292058850, "DAC BCompZ", 0.2400, enable=False)
    prg.add(292059350, "Swich Off Dipole")
    prg.add(292109350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(292109350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(292109350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(292109350, "Picture Na_offset", enable=False)
    prg.add(292109350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(292109350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(292109350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(312109350, "Initialize_Dipole_Off")
    prg.add(312114350, "Set MOT")
    return prg
