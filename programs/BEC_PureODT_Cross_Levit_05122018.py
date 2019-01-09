prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 45.0000)
    prg.add(135079400, "DAC MT-MOT Voltage", 8.0000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133000, "IGBT BCompZfine CLOSE")
    prg.add(135134000, "Config Field MT-MOT")
    prg.add(135136000, "DAC Horiz IR", 4.0000)
    prg.add(135137000, "AOM IR Horizontal freq", 80.00)
    prg.add(135138000, "AOM IR Horizontal Amp", 1000)
    prg.add(175138000, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=45, stop_t=300)
    prg.add(179138000, "Horizontal Dipole Evaporation Ramp 10_2018", enable=False)
    prg.add(179138000, "Horizontal Dipole Evaporation Ramp_3.5V_11_2018", enable=False)
    prg.add(179138000, "Horizontal Dipole Evaporation Ramp_4V_12_2018")
    prg.add(211638000, "[VOID] End Evaporation")
    prg.add(211638500, "IGBT BCompz CLOSE", enable=False)
    prg.add(211639000, "DAC BCompZ", 0.1000, enable=False)
    prg.add(212139000, "MT_to_Hor_Dipole_Cigar_Transfer_102018", enable=False)
    prg.add(212139000, "MT_to_Cross_Dipole_Transfer_122018")
    prg.add(222169000, "wait", enable=False)
    prg.add(223169000, "Config field OFF")
    prg.add(225169000, "DAC MT-MOT Voltage", 6.0000)
    prg.add(228169000, "wait", enable=False)
    prg.add(228170000, "Picture HybridTrap to Levit at 0ms - Levit 30 ms 10_2018", enable=False)
    prg.add(228170000, "Picture HybridTrap to Levit at 0ms - Levit 50 ms 10_2018", enable=False)
    prg.add(228170000, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", enable=False)
    prg.add(228170000, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018")
    prg.add(228171600, "Swich Off Dipole")
    prg.add(228173100, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(228173100, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(228173100, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(228173100, "Picture Na_2Gdet", enable=False)
    prg.add(228173100, "Picture Na_1Gdet", enable=False)
    prg.add(228173100, "Picture Na_0Gdet", enable=False)
    prg.add(233173100, "Set_MOT")
    prg.add(233273100, "IGBT BCompZfine OPEN")
    prg.add(233273100, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    x_arr, tpulse_arr = np.mgrid[0:1:1, 4.5:4.6:1.5, ]
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
