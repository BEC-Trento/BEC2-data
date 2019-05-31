prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT", enable=False)
    prg.add(135075800, "Switch Off MOT_fast")
    prg.add(135077050, "GM_051018")
    prg.add(135078950, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135079450, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(135132550, "wait")
    prg.add(135133550, "Config Field MT-MOT")
    prg.add(135134550, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135135050, "AOM IR Horizontal Amp", 1000)
    prg.add(135135550, "AOM IR Horizontal freq", 80.00)
    prg.add(135636050, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135637050, "Evaporation Ramp.sub", enable=False)
    prg.add(137137050, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(175637050, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(180006050, "Oscilloscope Trigger ON")
    prg.add(180738050, "Horizontal Dipole Evaporation Ramp_5V_2019_03", enable=False)
    prg.add(180738050, "DAC Horiz IR Exp ramp", start_t=0.0000, func_args="start_value=5, tau=cmd.get_var('tau'), offset=0.03", n_points=2000, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=4000.0000)
    prg.add(220739050, "wait")
    prg.add(221739050, "Config field OFF", enable=False)
    prg.add(221740000, "Oscilloscope Trigger ON", enable=False)
    prg.add(221740050, "Switch Off Dipole")
    prg.add(221740100, "Config field MT-MOT to Levit")
    prg.add(221741100, "DAC MT-MOT Current", 40.0000)
    prg.add(221741100, "Config field OFF", enable=False)
    prg.add(221741140, "Oscilloscope Trigger OFF")
    prg.add(221742890, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(221742890, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(236742890, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(236743890, "AOM IR Horizontal Amp", 1000)
    prg.add(236743890, "Set_BrightMOT", enable=False)
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
