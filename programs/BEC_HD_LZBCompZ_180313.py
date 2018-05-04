prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5170000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5170500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5171000, "DAC Horiz IR", 5.4000)
    prg.add(5171500, "AOM IR Horizontal freq", 80.00)
    prg.add(135071000, "wait")
    prg.add(135071004, "switch off MOT fast")
    prg.add(135073849, "GM BrokenRamp_Short")
    prg.add(135123849, "Config Field MT")
    prg.add(135323849, "Evaporation Ramp.sub")
    prg.add(235323849, "[VOID] End Evaporation")
    prg.add(235325349, "MT_FastTransfer_to_Dipole10A")
    prg.add(239325349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(271825349, "[VOID] End Evaporation")
    prg.add(271825353, "MTtoHorDipoleTransfer")
    prg.add(281825463, "wait")
    prg.add(281825473, "DAC BCompY", 0.4000, enable=False)
    prg.add(281825483, "BCompZ current ramp", start_t=0, stop_x=8.9, n_points=100, start_x=0, stop_t=250)
    prg.add(284375495, "wait")
    prg.add(284375506, "Oscilloscope Trigger ON")
    prg.add(284375521, "RF Landau-Zener Freq", 6.750, functions=dict(frequency=lambda x: cmd.get_var('f1'), funct_enable=False))
    prg.add(284375535, "RF Landau-Zener Amp", 1000.000)
    prg.add(284375549, "BCompZ current ramp", start_t=0, stop_x=9.2, n_points=100, start_x=8.9, stop_t=500)
    prg.add(289425563, "RF Landau-Zener Amp", 0.000)
    prg.add(289525573, "BCompZ current ramp", start_t=0, stop_x=0.28, n_points=100, start_x=9.2, stop_t=250)
    prg.add(292025593, "wait")
    prg.add(292025604, "BComp2 current ramp", start_t=0, stop_x=0.25, n_points=10, start_x=00.5, stop_t=10)
    prg.add(292026704, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(292026704, "Picture MT to Levit at 0ms - Levit 20 ms")
    prg.add(292026704, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(292026704, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(292026704, "Picture MT to Levit at 0ms - Levit 50 ms", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(292026704, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(292029704, "DAC BCompZ", 0.2800, functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(292030904, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(292032604, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(292033916, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(292033916, "Picture Na_2Gdet_offset", enable=False)
    prg.add(292033916, "Picture Na_1Gdet_offset", enable=False)
    prg.add(292033916, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(292033916, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(292033916, "Picture Na_3Gdet_offset", enable=False)
    prg.add(292033916, "Picture Na_4Gdet_offset", enable=False)
    prg.add(307033916, "Initialize_Dipole_Off")
    prg.add(307038916, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(25, 35, 1)
    j = 0
    while(cmd.running):
        f11 = iters[j]
        cmd.set_var('f1', f11)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nf1 = %g\n'%(j+1, len(iters), f11))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
