prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 5.4000)
    prg.add(5181500, "AOM IR Horizontal freq", 80.00)
    prg.add(135131500, "Bright_Compressed_MOT", enable=False)
    prg.add(135139500, "switch off MOT _ Depumper ", enable=False)
    prg.add(135139500, "switch off MOT fast")
    prg.add(135142349, "GM BrokenRamp_Short")
    prg.add(135192349, "Config Field MT")
    prg.add(135192359, "DAC Magnetic Trap Voltage", 6.0000)
    prg.add(135192359, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135192359, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(135392359, "Evaporation Ramp.sub")
    prg.add(235392359, "[VOID] End Evaporation")
    prg.add(235393359, "DAC BCompZ", 0.2400, enable=False)
    prg.add(235394859, "MT_FastTransfer_to_Dipole10A")
    prg.add(235394859, "MT_Piecewise_Transfer_to_Dipole10A", enable=False)
    prg.add(239394859, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(239394859, "Horizontal Dipole Evaporation Ramp variable", enable=False)
    prg.add(271894859, "[VOID] End Evaporation")
    prg.add(271895510, "IGBT BCompY field CLOSE", enable=False)
    prg.add(271896010, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(272896010, "Config field OFF", enable=False)
    prg.add(272896010, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(272896010, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(272896010, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(272896010, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(272896010, "Picture MT to Levit at 0ms - Levit 50 ms")
    prg.add(272896010, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(272899010, "DAC BCompZ", 0.2400, enable=False)
    prg.add(272899510, "Swich Off Dipole")
    prg.add(272902510, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(272902510, "Picture Na_2Gdet_offset", enable=False)
    prg.add(272902510, "Picture Na_1Gdet_offset", enable=False)
    prg.add(272912510, "Picture Na_offset", enable=False)
    prg.add(272912550, "Oscilloscope Trigger ON")
    prg.add(272912550, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(272912550, "Picture Na_3Gdet_offset", enable=False)
    prg.add(272912550, "Picture Na_4Gdet_offset", enable=False)
    prg.add(277912550, "Initialize_Dipole_Off")
    prg.add(277917550, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(591, 621, 1)
    j = 0
    while(cmd.running):
        LUT1 = iters[j]
        cmd.set_var('LUT', LUT1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nLUT = %g\n'%(j+1, len(iters), LUT1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
