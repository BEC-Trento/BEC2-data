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
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135141350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135141350, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(135341350, "Evaporation Ramp.sub")
    prg.add(235341350, "[VOID] End Evaporation")
    prg.add(235342350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(235347850, "MT_FastTransfer_to_Dipole10A")
    prg.add(235347850, "MT_Piecewise_Transfer_to_Dipole10A", enable=False)
    prg.add(239347850, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(239347850, "Horizontal Dipole Evaporation Ramp_smallBEC", enable=False)
    prg.add(276847850, "[VOID] End Evaporation")
    prg.add(276848350, "Config field OFF", enable=False)
    prg.add(276848350, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(276848350, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(276848350, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(276848350, "Picture MT to Levit at 0ms - Levit Variable Time new")
    prg.add(276851350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(276851850, "Swich Off Dipole")
    prg.add(276856850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(276856850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(276856850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(276856850, "Picture Na_offset", enable=False)
    prg.add(276856850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(276856850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(276856850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(286856850, "Initialize_Dipole_Off")
    prg.add(286861850, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    I_arr, dt_arr = np.mgrid[12:15:0.5, 0:35:5, ]
    iters = list(zip(I_arr.ravel(), dt_arr.ravel()))
    j = 0
    while(cmd.running):
        I1, dt1 = iters[j]
        cmd.set_var('I', I1)
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nI = %g\ndt = %g\n'%(j+1, len(iters), I1, dt1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
