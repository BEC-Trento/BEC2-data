prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135079400, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133500, "Config Field MT-MOT")
    prg.add(135134500, "DAC Horiz IR", 4.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')), enable=False)
    prg.add(135135500, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(135136000, "AOM IR Horizontal Amp", 1000, enable=False)
    prg.add(135136210, "Oscilloscope Trigger ON")
    prg.add(135141210, "DAC MT-MOT Voltage", 6.0000, enable=False)
    prg.add(135142210, "Evaporation Ramp.sub", enable=False)
    prg.add(137142210, "DAC MT-MOT Voltage", 9.0000, enable=False)
    prg.add(137143210, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=400, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')), enable=False)
    prg.add(187143210, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('MT_load_time'), funct_enable=False))
    prg.add(187144210, "Switch Off Dipole", enable=False)
    prg.add(187145420, "Picture_Mirror_Na_resonant_hamamatsu", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('MT_load_time')+cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(187145420, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(187146630, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('MT_load_time')+cmd.get_var('tof')), enable=False)
    prg.add(187146630, "Picture Na_2Gdet", enable=False)
    prg.add(187146630, "Picture Na_1Gdet", enable=False)
    prg.add(187146630, "Picture Na_0Gdet", enable=False)
    prg.add(202146630, "Set_MOT", functions=dict(time=lambda x: x + cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(202146630, "Set_BrightMOT", enable=False)
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
