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
    prg.add(135635550, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135636550, "Evaporation Ramp.sub", enable=False)
    prg.add(137136550, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(175636550, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(180737550, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(183239550, "DAC PiezoHorizEllipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('PiezoElliptV')))
    prg.add(213238550, "wait")
    prg.add(214239550, "wait")
    prg.add(214240550, "DAC IR Horiz_Ellipt", -0.1000)
    prg.add(214250550, "AOM IR Horiz_Ellipt Amp", 1000)
    prg.add(214251050, "AOM IR Horiz_Ellipt freq", 110.00)
    prg.add(214252050, "DAC IR Horiz_Ellipt", 1.0000, functions=dict(value=lambda x: cmd.get_var('Ellipt_finalValue'), funct_enable=False))
    prg.add(214253050, "DAC IR Horizontal Ellipt ramp", start_t=0, stop_x=5.5, n_points=100, start_x=0, stop_t=100, enable=False)
    prg.add(214253150, "Oscilloscope Trigger ON")
    prg.add(214253200, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(214255200, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(214256200, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(214256200, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(214256240, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(214257990, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(214257990, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')), enable=False)
    prg.add(229257990, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(229257990, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-10, 11, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        PiezoElliptV1 = iters[j]
        cmd.set_var('PiezoElliptV', PiezoElliptV1)
        print('\n')
        print('Run #%d/%d, with variables:\nPiezoElliptV = %g\n'%(j+1, len(iters), PiezoElliptV1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
