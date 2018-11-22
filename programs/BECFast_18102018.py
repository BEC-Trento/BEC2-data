prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(30075800, "Switch Off MOT")
    prg.add(30078900, "DAC MT-MOT Current", 55.0000)
    prg.add(30079400, "DAC MT-MOT Voltage", 4.0000)
    prg.add(30082500, "GM_051018")
    prg.add(30132500, "wait")
    prg.add(30133500, "Config Field MT-MOT")
    prg.add(30135500, "DAC Horiz IR", 5.4000)
    prg.add(30136500, "AOM IR Horizontal freq", 80.00)
    prg.add(30137500, "AOM IR Horizontal Amp", 1000)
    prg.add(55137500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(59137500, "Horizontal Dipole Evaporation Ramp 10_2018")
    prg.add(91637500, "[VOID] End Evaporation")
    prg.add(96637500, "Config field OFF", enable=False)
    prg.add(96637500, "Picture HybridTrap to Levit at 0ms - Levit 50 ms 10_2018")
    prg.add(96639100, "Swich Off Dipole")
    prg.add(96789100, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(96789100, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(96789100, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(96789100, "Picture Na_2Gdet", enable=False)
    prg.add(96789100, "Picture Na_1Gdet", enable=False)
    prg.add(96789100, "Picture Na_0Gdet", enable=False)
    prg.add(101789100, "Set_MOT")
    prg.add(101789100, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.1, 10, 1)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
