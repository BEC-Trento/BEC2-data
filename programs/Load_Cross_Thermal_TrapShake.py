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
    prg.add(135192359, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(135392359, "Evaporation Ramp.sub")
    prg.add(235392359, "[VOID] End Evaporation")
    prg.add(235393359, "DAC BCompZ", 0.2400, enable=False)
    prg.add(235394859, "MT_FastTransfer_to_Dipole10A")
    prg.add(239394859, "TransferToCross_HighPower")
    prg.add(264494859, "[VOID] End Evaporation", enable=False)
    prg.add(264495359, "TTL Dipole Shaking ON", enable=False)
    prg.add(284495359, "TTL Dipole Shaking OFF", enable=False)
    prg.add(284496010, "IGBT BCompY field CLOSE", enable=False)
    prg.add(284496510, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(284596510, "Config field OFF")
    prg.add(284596510, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(284596510, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(284596510, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(284596510, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(284596510, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(284596510, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(284599510, "DAC BCompZ", 0.2400, enable=False)
    prg.add(284600010, "Swich Off Dipole")
    prg.add(284640010, "Picture Na_Shortrepumper_offset")
    prg.add(284640010, "Picture Na_2Gdet_offset", enable=False)
    prg.add(284640010, "Picture Na_1Gdet_offset", enable=False)
    prg.add(284645010, "Picture Na_offset", enable=False)
    prg.add(284645050, "Oscilloscope Trigger ON", enable=False)
    prg.add(284645050, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(284645050, "Picture Na_3Gdet_offset", enable=False)
    prg.add(284645050, "Picture Na_4Gdet_offset", enable=False)
    prg.add(289645050, "Initialize_Dipole_Off")
    prg.add(289650050, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    hold_arr, dummy_arr = np.mgrid[2.65:10:0.2, 0:3:1, ]
    iters = list(zip(hold_arr.ravel(), dummy_arr.ravel()))
    j = 0
    while(cmd.running):
        hold1, dummy1 = iters[j]
        cmd.set_var('hold', hold1)
        cmd.set_var('dummy', dummy1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nhold = %g\ndummy = %g\n'%(j+1, len(iters), hold1, dummy1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
