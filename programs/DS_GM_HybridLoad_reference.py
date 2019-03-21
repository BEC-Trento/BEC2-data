prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(165075800, "Switch Off MOT")
    prg.add(165078900, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(165079400, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(165082500, "GM_051018")
    prg.add(165132500, "wait")
    prg.add(165133500, "Config Field MT-MOT")
    prg.add(165133710, "Oscilloscope Trigger ON")
    prg.add(165138710, "DAC MT-MOT Voltage", 6.0000)
    prg.add(165139710, "Evaporation Ramp.sub", enable=False)
    prg.add(165139710, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=400, enable=False)
    prg.add(165140940, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('MT_load_time')))
    prg.add(165142150, "Picture_Mirror_Na_resonant_hamamatsu", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('MT_load_time')+cmd.get_var('tof')), enable=False)
    prg.add(165142150, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(165143360, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(165143360, "Picture Na_2Gdet", enable=False)
    prg.add(165143360, "Picture Na_1Gdet", enable=False)
    prg.add(165143360, "Picture Na_0Gdet", enable=False)
    prg.add(180143360, "Set_MOT", functions=dict(time=lambda x: x + cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(180143360, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    tof_arr, MT_I_arr = np.mgrid[1:15:1, 25:29:1, ]
    iters = list(zip(tof_arr.ravel(), MT_I_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof1, MT_I1 = iters[j]
        cmd.set_var('tof', tof1)
        cmd.set_var('MT_I', MT_I1)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\nMT_I = %g\n'%(j+1, len(iters), tof1, MT_I1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
