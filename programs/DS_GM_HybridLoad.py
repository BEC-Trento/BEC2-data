prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 24.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135079400, "DAC MT-MOT Voltage", 8.0000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133500, "Config Field MT-MOT")
    prg.add(135135500, "DAC Horiz IR", 4.5000, functions=dict(value=lambda x: cmd.get_var('CigarV')), enable=False)
    prg.add(135136500, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(135137500, "AOM IR Horizontal Amp", 1000, enable=False)
    prg.add(135138500, "AOM IR Vertical freq", 80.00, enable=False)
    prg.add(135139500, "DAC Vert IR", 3.5000, enable=False)
    prg.add(135139600, "Oscilloscope Trigger ON")
    prg.add(135140600, "Evaporation Ramp.sub")
    prg.add(235140600, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=400, enable=False)
    prg.add(240140600, "Config field OFF")
    prg.add(240141600, "DAC Horiz IR", 1.0000, enable=False)
    prg.add(240142600, "Switch Off Dipole", enable=False)
    prg.add(240144380, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(240144380, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(240144380, "Picture Na_2Gdet_hamamatsu", enable=False)
    prg.add(240144380, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(240149480, "Picture_Mirror_Na_resonant_hamamatsu")
    prg.add(240149580, "Oscilloscope Trigger OFF")
    prg.add(240149580, "Picture Na_2Gdet", enable=False)
    prg.add(240149580, "Picture Na_1Gdet", enable=False)
    prg.add(240149580, "Picture Na_0Gdet", enable=False)
    prg.add(255149580, "Set_MOT")
    prg.add(255149580, "Set_BrightMOT", enable=False)
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
