prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(51200, "Switch Off MOT")
    prg.add(61200, "[test] Degauss_1012")
    prg.add(17035800, "Set_BrightMOT", enable=False)
    prg.add(17035800, "Set_MOT")
    prg.add(147035800, "Switch Off MOT", enable=False)
    prg.add(147035800, "Switch Off MOT_fast")
    prg.add(147037050, "GM_051018")
    prg.add(147038950, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(147039450, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(147092550, "wait")
    prg.add(147093550, "Config Field MT-MOT")
    prg.add(147094550, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(147095050, "AOM IR Horizontal Amp", 1000)
    prg.add(147095550, "AOM IR Horizontal freq", 80.00)
    prg.add(147096050, "Oscilloscope Trigger ON")
    prg.add(147596050, "DAC MT-MOT Voltage", 8.5000)
    prg.add(147597050, "Evaporation Ramp.sub", enable=False)
    prg.add(149097050, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(187597050, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(192698050, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(192698050, "DAC Horiz IR Exp ramp", start_t=0.0000, func_args="start_value=5, tau=1, offset=0.00", n_points=1000, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=3250.0000, enable=False)
    prg.add(225199050, "wait")
    prg.add(226199050, "Config field OFF", enable=False)
    prg.add(226200000, "Oscilloscope Trigger ON", enable=False)
    prg.add(226200050, "Switch Off Dipole")
    prg.add(226200100, "Config field MT-MOT to Levit")
    prg.add(226201100, "DAC MT-MOT Current", 40.0000)
    prg.add(226201100, "Config field OFF", enable=False)
    prg.add(226201140, "Oscilloscope Trigger OFF")
    prg.add(226202890, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(226202890, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(241202890, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(241203890, "AOM IR Horizontal Amp", 1000)
    prg.add(241203890, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.200000, 1.800000, 0.100000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tau1 = iters[j]
        cmd.set_var('tau', tau1)
        print('\n')
        print('Run #%d/%d, with variables:\ntau = %g\n'%(j+1, len(iters), tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
