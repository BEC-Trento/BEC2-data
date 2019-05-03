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
    prg.add(135133710, "Oscilloscope Trigger ON")
    prg.add(135138710, "DAC MT-MOT Voltage", 6.0000, enable=False)
    prg.add(135139710, "Evaporation Ramp.sub", enable=False)
    prg.add(135139710, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=400, enable=False)
    prg.add(135140940, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('MT_load_time')))
    prg.add(135140940, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('MT_load_time')))
    prg.add(135142150, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(135142150, "Picture Na_2Gdet", enable=False)
    prg.add(135142150, "Picture Na_1Gdet", enable=False)
    prg.add(135142150, "Picture Na_0Gdet", enable=False)
    prg.add(150142150, "Set_MOT", functions=dict(time=lambda x: x + cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(150142150, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 10, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
