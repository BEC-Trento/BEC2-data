prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(15800, "Initialize_Dipole_Off")
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(85075800, "Switch Off MOT", enable=False)
    prg.add(85075800, "Switch Off MOT_fast")
    prg.add(85077050, "GM_051018")
    prg.add(85080170, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(85080670, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(85127100, "wait")
    prg.add(85128100, "Config Field MT-MOT")
    prg.add(85130100, "DAC Horiz IR", 5.0000, functions=dict(value=lambda x: cmd.get_var('CigarV'), funct_enable=False))
    prg.add(85130600, "AOM IR Horizontal Amp", 1000)
    prg.add(85131100, "AOM IR Horizontal freq", 80.00)
    prg.add(85131600, "DAC IR Horiz_Ellipt", 5.0000, enable=False)
    prg.add(85132100, "AOM IR Horiz_Ellipt Amp", 1000, enable=False)
    prg.add(85132600, "AOM IR Horiz_Ellipt freq", 110.00, enable=False)
    prg.add(85133100, "DAC Vert IR", 4.0000, enable=False)
    prg.add(85133600, "AOM IR Vertical Amp", 1000, enable=False)
    prg.add(85134100, "AOM IR Vertical freq", 80.00, enable=False)
    prg.add(85634100, "DAC MT-MOT Voltage", 8.5000)
    prg.add(85636600, "Evaporation Ramp.sub", enable=False)
    prg.add(87136600, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(125636600, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=50, stop_t=500, functions=dict(start_t=lambda x: cmd.get_var('MT_I_final')))
    prg.add(130636700, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(163136700, "Config field OFF", enable=False)
    prg.add(163146700, "Oscilloscope Trigger ON")
    prg.add(163147700, "DAC Vert IR", 4.0000)
    prg.add(163148200, "AOM IR Vertical Amp", 1000)
    prg.add(163148700, "AOM IR Vertical freq", 80.00)
    prg.add(163149200, "DAC IR Horiz_Ellipt", 3.0000, enable=False)
    prg.add(163149700, "AOM IR Horiz_Ellipt Amp", 1000, enable=False)
    prg.add(163150200, "AOM IR Horiz_Ellipt freq", 110.00, enable=False)
    prg.add(163151200, "AOM IR Horizontal freq", 120.00)
    prg.add(163151700, "AOM IR Horizontal Amp", 0)
    prg.add(163152200, "DAC Horiz IR", -1.0000)
    prg.add(165152200, "Switch Off Dipole")
    prg.add(165152300, "Oscilloscope Trigger OFF")
    prg.add(165153510, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(165154720, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(180154720, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(180164720, "Initialize_Dipole_Off")
    prg.add(180164720, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 200, 20)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        ODT_only1 = iters[j]
        cmd.set_var('ODT_only', ODT_only1)
        print('\n')
        print('Run #%d/%d, with variables:\nODT_only = %g\n'%(j+1, len(iters), ODT_only1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
