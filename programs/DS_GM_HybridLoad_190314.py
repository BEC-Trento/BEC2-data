prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 36.0000, functions=dict(value=lambda x: cmd.get_var('MT_I'), funct_enable=False))
    prg.add(135079400, "DAC MT-MOT Voltage", 8.0000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133500, "Config Field MT-MOT")
    prg.add(135133710, "Oscilloscope Trigger ON")
    prg.add(135134710, "AOM IR Horizontal freq", 80.00)
    prg.add(135135210, "AOM IR Horizontal Amp", 1000)
    prg.add(135135710, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135136210, "AOM IR Horiz_Ellipt freq", 110.00, enable=False)
    prg.add(135136710, "AOM IR Horiz_Ellipt Amp", 1000, enable=False)
    prg.add(135137210, "DAC IR Horiz_Ellipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('ElliptV')), enable=False)
    prg.add(135138710, "Evaporation Ramp.sub", enable=False)
    prg.add(135138710, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=400, functions=dict(time=lambda x: x+cmd.get_var('tload')), enable=False)
    prg.add(135148710, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('tload')))
    prg.add(136148710, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('tload')))
    prg.add(136149920, "Picture_Mirror_Na_resonant_hamamatsu", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(136149920, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('tload')))
    prg.add(136151130, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('tload')))
    prg.add(136151130, "Picture Na_2Gdet", enable=False)
    prg.add(136151130, "Picture Na_1Gdet", enable=False)
    prg.add(136151130, "Picture Na_0Gdet", enable=False)
    prg.add(151151130, "Set_MOT")
    prg.add(151151130, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1000, 10000, 1000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tload1 = iters[j]
        cmd.set_var('tload', tload1)
        print('\n')
        print('Run #%d/%d, with variables:\ntload = %g\n'%(j+1, len(iters), tload1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
