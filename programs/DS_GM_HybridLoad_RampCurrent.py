prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 30.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135079400, "DAC MT-MOT Voltage", 7.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133500, "Config Field MT-MOT")
    prg.add(135133710, "Oscilloscope Trigger ON")
    prg.add(135134710, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135135210, "AOM IR Horizontal Amp", 1000)
    prg.add(135135710, "AOM IR Horizontal freq", 80.00)
    prg.add(135635710, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135636710, "Evaporation Ramp.sub", enable=False)
    prg.add(137136710, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=500, functions=dict(stop_x=lambda x: cmd.get_var('MT_I_final'), start_x=lambda x: cmd.get_var('MT_I')))
    prg.add(137137940, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('MT_load_time')))
    prg.add(138137940, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('MT_load_time')))
    prg.add(138139150, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('MT_load_time')))
    prg.add(138140360, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(153140360, "Set_MOT", functions=dict(time=lambda x: x + cmd.get_var('MT_load_time')+cmd.get_var('tof')))
    prg.add(153140360, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1500, 6000, 500)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        MT_load_time1 = iters[j]
        cmd.set_var('MT_load_time', MT_load_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nMT_load_time = %g\n'%(j+1, len(iters), MT_load_time1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
