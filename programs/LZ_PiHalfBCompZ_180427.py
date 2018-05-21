prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(150000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5170000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5170500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5171000, "DAC Horiz IR", 5.4000)
    prg.add(5171500, "AOM IR Horizontal freq", 80.00)
    prg.add(145171500, "wait")
    prg.add(145174004, "switch off MOT fast")
    prg.add(145176849, "GM BrokenRamp_Short")
    prg.add(145226849, "Config Field MT")
    prg.add(145426849, "Evaporation Ramp.sub")
    prg.add(245426849, "[VOID] End Evaporation")
    prg.add(245428349, "MT_FastTransfer_to_Dipole10A")
    prg.add(249428349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(281928349, "[VOID] End Evaporation")
    prg.add(281928353, "MTtoHorDipoleTransfer")
    prg.add(291928463, "wait")
    prg.add(291938000, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(291938463, "Config field OFF", enable=False)
    prg.add(291948463, "Compensate_external_Mag_Field", enable=False)
    prg.add(291948463, "Landau_Zener", enable=False)
    prg.add(291948463, "Landau_Zener_1swait_pihalf", enable=False)
    prg.add(291948463, "Landau_Zener_NoHorcomp", enable=False)
    prg.add(291948463, "Landau_Zener_Prova_G")
    prg.add(291948463, "Landau_Zener_wideRF_8Afin", enable=False)
    prg.add(291948463, "Landau_Zener_SLOW_nohorcomp", enable=False)
    prg.add(293868463, "wait")
    prg.add(293868463, "wait", enable=False)
    prg.add(293868477, "Picture_Levit_2018", enable=False)
    prg.add(293868477, "TESTBCompY_Picture_Levit_2018")
    prg.add(293869677, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(293871377, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(293872689, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(293872689, "Picture Na_2Gdet_offset", enable=False)
    prg.add(293872689, "Picture Na_1Gdet_offset", enable=False)
    prg.add(293873689, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(293873689, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(293873689, "Picture Na_3Gdet_offset", enable=False)
    prg.add(293873689, "Picture Na_4Gdet_offset", enable=False)
    prg.add(294873689, "Relay BCompZ Normal")
    prg.add(309873689, "Initialize_Dipole_Off")
    prg.add(309878689, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    pulse_arr, dummy_arr = np.mgrid[0.0025:0.2:0.0075, 0:3:1, ]
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
