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
    prg.add(135079400, "DAC MT-MOT Voltage", 4.0000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133500, "Config Field MT-MOT")
    prg.add(135135500, "DAC Horiz IR", 5.4000)
    prg.add(135136500, "AOM IR Horizontal freq", 80.00)
    prg.add(135137500, "AOM IR Horizontal Amp", 1000)
    prg.add(235137500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(239137500, "Horizontal Dipole Evaporation Ramp 10_2018")
    prg.add(271637500, "[VOID] End Evaporation")
    prg.add(271737500, "Synchronize.sub")
    prg.add(271837500, "Relay BCompZ Invert", enable=False)
    prg.add(272037500, "IGBT BCompz CLOSE", enable=False)
    prg.add(272047500, "DAC BCompZ", 0.5000, enable=False)
    prg.add(277047500, "Config field OFF")
    prg.add(277147500, "uW ON", enable=False)
    prg.add(277148500, "uW OFF", enable=False)
    prg.add(277149000, "Picture HybridTrap to Levit at 0ms - Levit 30 ms 10_2018", enable=False)
    prg.add(277149000, "Picture HybridTrap to Levit at 0ms - Levit 10 ms 10_2018")
    prg.add(277149000, "Picture HybridTrap to Levit at 0ms - Levit 50 ms 10_2018", enable=False)
    prg.add(277150600, "Swich Off Dipole")
    prg.add(277160600, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(277160600, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(277160600, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(277160600, "Picture Na_2Gdet", enable=False)
    prg.add(277160600, "Picture Na_1Gdet", enable=False)
    prg.add(277160600, "Picture Na_0Gdet", enable=False)
    prg.add(282160600, "Set_MOT")
    prg.add(282160600, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 15, 2)
    j = 0
    while(cmd.running):
        TOF1 = iters[j]
        cmd.set_var('TOF', TOF1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nTOF = %g\n'%(j+1, len(iters), TOF1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
