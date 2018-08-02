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
    prg.add(105181500, "Bright_Compressed_MOT", enable=False)
    prg.add(105189500, "switch off MOT _ Depumper ", enable=False)
    prg.add(105189500, "switch off MOT fast")
    prg.add(105192349, "GM BrokenRamp_Short")
    prg.add(105242349, "Config Field MT")
    prg.add(105242359, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(105442359, "Evaporation Ramp.sub")
    prg.add(205442359, "[VOID] End Evaporation")
    prg.add(205443359, "DAC BCompZ", 0.2400, enable=False)
    prg.add(205444859, "MT_FastTransfer_to_Dipole10A")
    prg.add(209444859, "TransferToCross_HighPower")
    prg.add(234544859, "[VOID] End Evaporation", enable=False)
    prg.add(234554859, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(234554859, "Synchronize.sub")
    prg.add(234654859, "Landau_Zener_NoBComp")
    prg.add(234655510, "IGBT BCompY field CLOSE", enable=False)
    prg.add(234656010, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(236666010, "wait", functions=dict(time=lambda x: x+cmd.get_var('pulse')), enable=False)
    prg.add(236666010, "wait", functions=dict(time=lambda x: x + cmd.get_var('hold')), enable=False)
    prg.add(236676010, "Picture_Levit_2018", enable=False)
    prg.add(236676010, "Picture_Levit_ShortTime220618", functions=dict(time=lambda x: x  + cmd.get_var('pulse')))
    prg.add(236676510, "Config field OFF", enable=False)
    prg.add(236676510, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(236676510, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(236676510, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(236676510, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(236676510, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(236676510, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(236679510, "DAC BCompZ", 0.2400, enable=False)
    prg.add(236680010, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('pulse')))
    prg.add(236760010, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(236760010, "Picture Na_2Gdet_offset", enable=False)
    prg.add(236760010, "Picture Na_1Gdet_offset", enable=False)
    prg.add(236765010, "Picture Na_offset", enable=False)
    prg.add(236765050, "Oscilloscope Trigger ON", enable=False)
    prg.add(236765050, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(236765050, "Picture Na_3Gdet_offset", enable=False)
    prg.add(236765050, "Picture Na_4Gdet_offset", enable=False)
    prg.add(246765050, "Initialize_Dipole_Off")
    prg.add(246770050, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    pulse_arr, dummy_arr = np.mgrid[0.025:2:0.025, 0:2:1, ]
    iters = list(zip(pulse_arr.ravel(), dummy_arr.ravel()))
    j = 0
    while(cmd.running):
        pulse1, dummy1 = iters[j]
        cmd.set_var('pulse', pulse1)
        cmd.set_var('dummy', dummy1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\npulse = %g\ndummy = %g\n'%(j+1, len(iters), pulse1, dummy1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
