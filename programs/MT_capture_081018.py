prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135063100, "GM_051018")
    prg.add(135063600, "DAC MT-MOT Current", 24.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135064100, "DAC MT-MOT Voltage", 8.0000)
    prg.add(135114100, "wait")
    prg.add(135114600, "Config Field MT-MOT")
    prg.add(135115700, "Oscilloscope Trigger ON")
    prg.add(135116700, "AOM IR Horizontal Amp", 1000)
    prg.add(135117700, "AOM IR Horizontal freq", 80.00)
    prg.add(135118700, "DAC Horiz IR", 5.0000)
    prg.add(135118700, "MT_spill_out", enable=False)
    prg.add(140118700, "wait")
    prg.add(140120700, "MT Current Ramp", start_t=0, stop_x=20, n_points=100, start_x=55, stop_t=2500, enable=False)
    prg.add(145121700, "Oscilloscope Trigger OFF")
    prg.add(145122700, "Config field OFF")
    prg.add(146122700, "Switch Off Dipole")
    prg.add(146173930, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(146173930, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(146173930, "Picture_Mirror_Na_resonant_hamamatsu", enable=False)
    prg.add(146173930, "Picture_Mirror_Na_3Gamma_hamamatsu", functions=dict(time=lambda x: x +cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(146173930, "Picture_Mirror_Na_2Gamma_hamamatsu", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(146173930, "Picture Na_2Gdet_hamamatsu", enable=False)
    prg.add(146173930, "Picture Na_2Gdet", enable=False)
    prg.add(146173930, "Picture Na_1Gdet", enable=False)
    prg.add(146173930, "Picture Na_0Gdet", enable=False)
    prg.add(156173930, "Set_MOT")
    prg.add(156173930, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(24, 55, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        MT_I1 = iters[j]
        cmd.set_var('MT_I', MT_I1)
        print('\n')
        print('Run #%d/%d, with variables:\nMT_I = %g\n'%(j+1, len(iters), MT_I1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
