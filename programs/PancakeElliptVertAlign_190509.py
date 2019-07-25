prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(187724450, "DAC PiezoHorizEllipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('PiezoElliptV')))
    prg.add(220300000, "DAC IR Horiz_Ellipt", -0.1000, enable=False)
    prg.add(220310000, "AOM IR Horiz_Ellipt Amp", 1000, enable=False)
    prg.add(220310500, "AOM IR Horiz_Ellipt freq", 110.00, enable=False)
    prg.add(220311500, "DAC IR Horiz_Ellipt", 2.0000, functions=dict(value=lambda x: cmd.get_var('Ellipt_finalValue'), funct_enable=False), enable=False)
    prg.add(220312500, "DAC IR Horizontal Ellipt ramp", start_t=0, stop_x=5.5, n_points=100, start_x=0, stop_t=100, enable=False)
    prg.add(220312600, "Oscilloscope Trigger ON")
    prg.add(220330600, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(220332599, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(220334600, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(220335600, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(220335640, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(220537390, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x +cmd.get_var('hold_time')), enable=False)
    prg.add(220537390, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof'), funct_enable=False))
    prg.add(235537390, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(235537390, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.000000, 3.000000, 0.200000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time1 = iters[j]
        cmd.set_var('hold_time', hold_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\n'%(j+1, len(iters), hold_time1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
