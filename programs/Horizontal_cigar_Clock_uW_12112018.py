prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompZfine OPEN", enable=False)
    prg.add(50000, "Config field OFF", enable=False)
    prg.add(100000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(115800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(165800, "Switch Off MOT")
    prg.add(5175800, "Set_BrightMOT", enable=False)
    prg.add(5175800, "Set_MOT")
    prg.add(35175800, "Switch Off MOT")
    prg.add(35178900, "DAC MT-MOT Current", 55.0000)
    prg.add(35179400, "DAC MT-MOT Voltage", 4.0000)
    prg.add(35182500, "GM_051018")
    prg.add(35232500, "wait")
    prg.add(35234500, "Config Field MT-MOT")
    prg.add(35236500, "DAC Horiz IR", 5.4000)
    prg.add(35237500, "AOM IR Horizontal freq", 80.00)
    prg.add(35238500, "AOM IR Horizontal Amp", 1000)
    prg.add(65238500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(69238500, "Horizontal Dipole Evaporation Ramp 10_2018")
    prg.add(101738500, "[VOID] End Evaporation")
    prg.add(101988500, "IGBT BCompZfine CLOSE")
    prg.add(102238500, "MT_to_Hor_Dipole_Cigar_Transfer_102018")
    prg.add(122238500, "Landau_Zener")
    prg.add(122238500, "Landau_Zener_to_finite_field", enable=False)
    prg.add(124238500, "Synchronize.sub")
    prg.add(124538500, "Swich Off Dipole", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(124540000, "uW ON", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(124540600, "uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(124541100, "IGBT Bcompz OPEN", enable=False)
    prg.add(124541600, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(124542100, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(124544209, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(124544209, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(124544209, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(124544209, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(124544209, "Picture Na_uW_Probe_hamamatsu", enable=False)
    prg.add(124544209, "Picture Na_2Gdet", enable=False)
    prg.add(124544209, "Picture Na_1Gdet", enable=False)
    prg.add(124544209, "Picture Na_0Gdet", enable=False)
    prg.add(125044209, "IGBT BCompZfine OPEN")
    prg.add(130044209, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(130044209, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.concatenate([np.concatenate([np.arange(7.03,7.72,0.03),np.arange(10.03,10.72,10.03)]),np.arange(12.03,12.72,0.03)])
    #iters = np.arange(6.12,6.72,0.03)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
