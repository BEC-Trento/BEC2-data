prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT", enable=False)
    prg.add(135060000, "Switch Off MOT_fast")
    prg.add(135061250, "GM_051018")
    prg.add(135063150, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135063650, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(135116750, "wait")
    prg.add(135117750, "Config Field MT-MOT")
    prg.add(135118750, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135119250, "AOM IR Horizontal Amp", 1000)
    prg.add(135119750, "AOM IR Horizontal freq", 80.00)
    prg.add(135120250, "Oscilloscope Trigger ON")
    prg.add(135620250, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135621250, "RF Evaporation", 0, enable=False)
    prg.add(137121250, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(142122250, "Evaporation Ramp.sub")
    prg.add(175622250, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(181622250, "Config field OFF", enable=False)
    prg.add(182622250, "Switch Off Dipole")
    prg.add(182622290, "Oscilloscope Trigger OFF")
    prg.add(182624040, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(182624040, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')), enable=False)
    prg.add(197624040, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(197625040, "AOM IR Horizontal Amp", 1000)
    prg.add(197625040, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 10, 1)
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
