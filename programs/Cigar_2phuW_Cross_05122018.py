prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompZfine OPEN")
    prg.add(50000, "Config field OFF")
    prg.add(100000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(115800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(165800, "Switch Off MOT")
    prg.add(5175800, "Set_BrightMOT", enable=False)
    prg.add(5175800, "Set_MOT")
    prg.add(35175800, "Switch Off MOT")
    prg.add(35178900, "DAC MT-MOT Current", 55.0000)
    prg.add(35179400, "DAC MT-MOT Voltage", 6.0000)
    prg.add(35182500, "GM_051018")
    prg.add(35232500, "wait")
    prg.add(35234500, "Config Field MT-MOT")
    prg.add(35236500, "DAC Horiz IR", 4.0000)
    prg.add(35237500, "AOM IR Horizontal freq", 80.00)
    prg.add(35238500, "AOM IR Horizontal Amp", 1000)
    prg.add(53238500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(57238500, "Horizontal Dipole Evaporation Ramp 10_2018", enable=False)
    prg.add(57238500, "Horizontal Dipole Evaporation Ramp_4V_12_2018")
    prg.add(89738500, "[VOID] End Evaporation")
    prg.add(92938500, "IGBT BCompZfine CLOSE")
    prg.add(95938500, "MT_to_Hor_Dipole_Cigar_Transfer_102018", enable=False)
    prg.add(95938500, "MT_to_Cross_Dipole_Transfer_122018")
    prg.add(106438500, "wait")
    prg.add(106439000, "Config field OFF")
    prg.add(116439000, "Synchronize.sub")
    prg.add(116740000, "Swich Off Dipole", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(116741500, "uW ON", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(116741500, "uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(116741500, "wait", enable=False)
    prg.add(116742000, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(116742500, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(116742500, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(116744100, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(116746209, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(116747209, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(116747209, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(116747209, "Picture Na_resonant_hamamatsu", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(116747209, "Picture Na_uW_Probe_hamamatsu", enable=False)
    prg.add(116747209, "Picture Na_2Gdet", enable=False)
    prg.add(116747209, "Picture Na_1Gdet", enable=False)
    prg.add(116747209, "Picture Na_0Gdet", enable=False)
    prg.add(117247209, "IGBT BCompZfine OPEN", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(122247209, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(122247209, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    x_arr, tpulse_arr = np.mgrid[0:1:1, 0.5:500:2.5, ]
    iters = list(zip(x_arr.ravel(), tpulse_arr.ravel()))
    j = 0
    while(cmd.running):
        x1, tpulse1 = iters[j]
        cmd.set_var('x', x1)
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nx = %g\ntpulse = %g\n'%(j+1, len(iters), x1, tpulse1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
