prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 25.0000)
    prg.add(135079400, "DAC MT-MOT Voltage", 5.5000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133000, "IGBT BCompZfine CLOSE", enable=False)
    prg.add(135134000, "Config Field MT-MOT")
    prg.add(135136000, "DAC Horiz IR", 4.0000)
    prg.add(135137000, "DAC IR Horiz_Ellipt", 6.0000)
    prg.add(135137500, "DAC Vert IR", 2.0000)
    prg.add(135138500, "AOM IR Horizontal freq", 80.00)
    prg.add(135139500, "AOM IR Horiz_Ellipt freq", 110.00)
    prg.add(135140000, "AOM IR Vertical freq", 80.00)
    prg.add(135141000, "AOM IR Horizontal Amp", 1000)
    prg.add(235141000, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=25, stop_t=300)
    prg.add(239141000, "Horizontal Dipole Evaporation Ramp 10_2018", enable=False)
    prg.add(239141000, "Horizontal Dipole Evaporation Ramp_3.5V_11_2018", enable=False)
    prg.add(239141000, "Horizontal Dipole Evaporation Ramp_4V_12_2018")
    prg.add(271641000, "[VOID] End Evaporation")
    prg.add(272141000, "MTtoHorDipoleTransfer")
    prg.add(272641000, "DAC MT-MOT Voltage", 6.0000, enable=False)
    prg.add(283141000, "Config field OFF")
    prg.add(283141500, "DAC IR Horizontal Ellipt ramp", start_t=0, stop_x=0.5, n_points=100, start_x=3, stop_t=1000, enable=False)
    prg.add(283146500, "DAC IR Horizontal ramp", start_t=0, stop_x=0, n_points=50, start_x=0.1, stop_t=500)
    prg.add(288151500, "AOM IR Horizontal freq", 140.00)
    prg.add(298151500, "Config field OFF", enable=False)
    prg.add(298156500, "Picture HybridTrap to Levit at 0ms - Levit 30 ms 10_2018", enable=False)
    prg.add(298156500, "Picture HybridTrap to Levit at 0ms - Levit 50 ms 10_2018", enable=False)
    prg.add(298157880, "Swich Off Dipole")
    prg.add(298159349, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(298159349, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(298159349, "Picture_Mirror_Na_resonant_hamamatsu")
    prg.add(298159349, "Picture_Mirror_Na_uwrepump_hamamatsu", enable=False)
    prg.add(298159349, "Picture Na_2Gdet", enable=False)
    prg.add(298159349, "Picture Na_1Gdet", enable=False)
    prg.add(298159349, "Picture Na_0Gdet", enable=False)
    prg.add(303159349, "Set_MOT")
    prg.add(303259349, "IGBT BCompZfine OPEN")
    prg.add(303259349, "Set_BrightMOT", enable=False)
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
