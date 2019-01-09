prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 55.0000)
    prg.add(135079400, "DAC MT-MOT Voltage", 6.0000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133000, "IGBT BCompZfine CLOSE", enable=False)
    prg.add(135134000, "Config Field MT-MOT")
    prg.add(135136000, "DAC Horiz IR", 4.5000)
    prg.add(135137000, "AOM IR Horizontal freq", 80.00)
    prg.add(135138000, "AOM IR Horizontal Amp", 1000)
    prg.add(185138000, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(189138000, "Horizontal Dipole Evaporation Ramp 10_2018", enable=False)
    prg.add(189138000, "Horizontal Dipole Evaporation Ramp_3.5V_11_2018")
    prg.add(221638000, "[VOID] End Evaporation")
    prg.add(221638500, "IGBT BCompz CLOSE")
    prg.add(221639000, "DAC BCompZ", 0.1000)
    prg.add(222139000, "MT_to_Hor_Dipole_Cigar_Transfer_102018")
    prg.add(232149000, "wait", enable=False)
    prg.add(232149000, "Config field OFF")
    prg.add(232159000, "Config Field MT_helmDown")
    prg.add(232169000, "DAC MT-MOT Current", 2.0000)
    prg.add(432169000, "DAC MT-MOT Current", 0.0000)
    prg.add(432179000, "Config field OFF")
    prg.add(432180000, "Picture HybridTrap to Levit at 0ms - Levit 30 ms 10_2018", enable=False)
    prg.add(432180000, "Picture HybridTrap to Levit at 0ms - Levit 50 ms 10_2018")
    prg.add(432181600, "Swich Off Dipole")
    prg.add(432331600, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(432331600, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(432331600, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(432331600, "Picture Na_2Gdet", enable=False)
    prg.add(432331600, "Picture Na_1Gdet", enable=False)
    prg.add(432331600, "Picture Na_0Gdet", enable=False)
    prg.add(437331600, "Set_MOT")
    prg.add(437431600, "IGBT BCompZfine OPEN")
    prg.add(437431600, "Set_BrightMOT", enable=False)
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
