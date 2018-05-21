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
    prg.add(140212359, "DAC BCompZ", 0.2400, enable=False)
    prg.add(140212359, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(140412359, "Evaporation Ramp.sub")
    prg.add(160412359, "Config field OFF")
    prg.add(160432359, "Picture Na_4Gdet_offset")
    prg.add(200824718, "[VOID] End Evaporation")
    prg.add(200825718, "DAC BCompZ", 0.2400, enable=False)
    prg.add(200827218, "MT_FastTransfer_to_Dipole10A")
    prg.add(200827218, "MT_Piecewise_Transfer_to_Dipole10A", enable=False)
    prg.add(204827218, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(204827218, "Horizontal Dipole Evaporation Ramp variable", enable=False)
    prg.add(237327218, "[VOID] End Evaporation")
    prg.add(237327869, "IGBT BCompY field CLOSE", enable=False)
    prg.add(237328369, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(238328369, "Config field OFF")
    prg.add(238328369, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(238328369, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(238328369, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(238328369, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(238328369, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(238328369, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(238331369, "DAC BCompZ", 0.2400, enable=False)
    prg.add(238331869, "Swich Off Dipole")
    prg.add(238334869, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(238334869, "Picture Na_2Gdet_offset", enable=False)
    prg.add(238334869, "Picture Na_1Gdet_offset", enable=False)
    prg.add(238344869, "Picture Na_offset")
    prg.add(238344909, "Oscilloscope Trigger ON", enable=False)
    prg.add(238344909, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(238344909, "Picture Na_3Gdet_offset", enable=False)
    prg.add(238344909, "Picture Na_4Gdet_offset", enable=False)
    prg.add(243344909, "Initialize_Dipole_Off")
    prg.add(243349909, "Set MOT")
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
