prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(16300, "Magnetization_test_subroutine")
    prg.add(16800, "Degaussing_test_subroutine")
    prg.add(66800, "Switch Off MOT")
    prg.add(5076800, "Set_BrightMOT", enable=False)
    prg.add(5076800, "Set_MOT")
    prg.add(135076800, "Switch Off MOT")
    prg.add(135079900, "DAC MT-MOT Current", 55.0000)
    prg.add(135080400, "DAC MT-MOT Voltage", 6.0000)
    prg.add(135083500, "GM_051018")
    prg.add(135133500, "wait")
    prg.add(135134000, "IGBT BCompZfine CLOSE", enable=False)
    prg.add(135135000, "Config Field MT-MOT")
    prg.add(135137000, "DAC Horiz IR", 4.0000)
    prg.add(135138000, "AOM IR Horizontal freq", 80.00)
    prg.add(135139000, "AOM IR Horizontal Amp", 1000)
    prg.add(175139000, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(179139000, "Horizontal Dipole Evaporation Ramp 10_2018", enable=False)
    prg.add(179139000, "Horizontal Dipole Evaporation Ramp_3.5V_11_2018", enable=False)
    prg.add(179139000, "Horizontal Dipole Evaporation Ramp_4V_12_2018")
    prg.add(211639000, "[VOID] End Evaporation")
    prg.add(211639500, "IGBT BCompz CLOSE")
    prg.add(211640000, "DAC BCompZ", 0.1000)
    prg.add(212140000, "MT_to_Hor_Dipole_Cigar_Transfer_102018")
    prg.add(222150000, "wait", enable=False)
    prg.add(223150000, "Config field OFF")
    prg.add(223350000, "Synchronize.sub")
    prg.add(223650000, "uW ON", enable=False)
    prg.add(223650500, "uW OFF", enable=False)
    prg.add(228650500, "wait")
    prg.add(228651500, "Picture HybridTrap to Levit at 0ms - Levit 30 ms 10_2018", enable=False)
    prg.add(228651500, "Picture Levit at 0ms - Levit 50 ms 11_2018")
    prg.add(228651500, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", enable=False)
    prg.add(228651500, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018", enable=False)
    prg.add(228653100, "Swich Off Dipole")
    prg.add(228803100, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(228803100, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(228803100, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(228803100, "Picture Na_2Gdet", enable=False)
    prg.add(228803100, "Picture Na_1Gdet", enable=False)
    prg.add(228803100, "Picture Na_0Gdet", enable=False)
    prg.add(233803100, "Set_MOT")
    prg.add(233903100, "IGBT BCompZfine OPEN")
    prg.add(233903100, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    #iters = np.concatenate([np.concatenate([np.arange(0.03,0.72,0.03),np.arange(4.03,4.72,0.03)]),np.arange(6.03,6.72,0.03)])
    iters = np.arange(1,50,2)
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
