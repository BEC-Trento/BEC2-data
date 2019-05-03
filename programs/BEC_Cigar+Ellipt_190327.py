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
    prg.add(135134500, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135135000, "AOM IR Horizontal Amp", 1000)
    prg.add(135135500, "AOM IR Horizontal freq", 80.00)
    prg.add(135635500, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135638000, "Evaporation Ramp.sub", enable=False)
    prg.add(137138000, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(175638000, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=50, stop_t=500)
    prg.add(180739000, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(215709000, "Oscilloscope Trigger ON")
    prg.add(215710000, "DAC IR Horizontal ramp", start_t=0, stop_x=-0.1, n_points=100, start_x=0.04, stop_t=200)
    prg.add(215710500, "DAC IR Horiz_Ellipt", 3.0000, enable=False)
    prg.add(215711000, "AOM IR Horiz_Ellipt Amp", 1000, enable=False)
    prg.add(215711500, "AOM IR Horiz_Ellipt freq", 110.00, enable=False)
    prg.add(219711500, "Config field OFF")
    prg.add(219712500, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('MT_load_time'), funct_enable=False))
    prg.add(219713710, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(219714920, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(234714920, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(234715920, "AOM IR Horizontal Amp", 1000)
    prg.add(234715920, "Set_BrightMOT", enable=False)
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
