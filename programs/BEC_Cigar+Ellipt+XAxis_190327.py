prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(85075800, "Switch Off MOT", enable=False)
    prg.add(85075800, "Switch Off MOT_fast")
    prg.add(85077050, "GM_051018")
    prg.add(85082150, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(85082650, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(85127150, "wait")
    prg.add(85127250, "Config Field MT-MOT")
    prg.add(85128250, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(85128750, "AOM IR Horizontal Amp", 1000)
    prg.add(85129250, "AOM IR Horizontal freq", 80.00)
    prg.add(85629250, "DAC MT-MOT Voltage", 8.5000)
    prg.add(85631750, "Evaporation Ramp.sub", enable=False)
    prg.add(87131750, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(125631750, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=50, stop_t=500)
    prg.add(130732750, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(161000000, "DAC Vert IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('XaxisV')))
    prg.add(161000500, "AOM IR Vertical Amp", 1000)
    prg.add(161001000, "AOM IR Vertical freq", 80.00)
    prg.add(165702750, "Oscilloscope Trigger ON")
    prg.add(165703750, "DAC IR Horizontal ramp", start_t=0, stop_x=0.01, n_points=100, start_x=0.04, stop_t=200)
    prg.add(165704250, "DAC IR Horiz_Ellipt", 3.0000, enable=False)
    prg.add(165704750, "AOM IR Horiz_Ellipt Amp", 1000, enable=False)
    prg.add(165705250, "AOM IR Horiz_Ellipt freq", 110.00, enable=False)
    prg.add(169706750, "Config field OFF")
    prg.add(169707750, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('MT_load_time'), funct_enable=False))
    prg.add(169708960, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(169710170, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(179710170, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(179711170, "AOM IR Horizontal Amp", 1000)
    prg.add(179711170, "Set_BrightMOT", enable=False)
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
