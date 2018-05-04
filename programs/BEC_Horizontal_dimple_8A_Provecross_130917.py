prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 5.4000)
    prg.add(5181500, "DAC Vert IR", 3.0000)
    prg.add(5182000, "AOM IR Horizontal freq", 80.00)
    prg.add(5182500, "AOM IR Vertical freq", 80.00)
    prg.add(135082000, "Bright_Compressed_MOT")
    prg.add(135090000, "switch off MOT _ Depumper ")
    prg.add(135090000, "switch off MOT ", enable=False)
    prg.add(135092350, "GM BrokenRamp_Short")
    prg.add(135142350, "Config Field MT")
    prg.add(135347350, "MT_Compression", enable=False)
    prg.add(135354350, "DAC BCompZ", 0.2400)
    prg.add(135354350, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(140554350, "Evaporation Ramp.sub", enable=False)
    prg.add(240554350, "[VOID] End Evaporation")
    prg.add(240554850, "MT_Transfer_to_Dipole", enable=False)
    prg.add(240559850, "MT_FastTransfer_to_Dipole8A")
    prg.add(244560350, "Horizontal Dipole Evaporation Ramp CMT20A_5.4V")
    prg.add(279560350, "[VOID] End Evaporation")
    prg.add(279560850, "Config field OFF", enable=False)
    prg.add(279560850, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(279560850, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(279560850, "Picture MT to Levit at 0ms - Levit 50 ms")
    prg.add(279560850, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(279563850, "DAC BCompZ", 0.2400)
    prg.add(279564350, "Swich Off Dipole")
    prg.add(279624350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(279624350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(279624350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(279624350, "Picture Na_offset", enable=False)
    prg.add(279624350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(279624350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(279624350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(299624350, "Initialize_Dipole_Off")
    prg.add(299629350, "Set MOT")
    return prg
