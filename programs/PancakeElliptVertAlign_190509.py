prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(150000000, "DAC PiezoHorizEllipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('PiezoElliptV')))
    prg.add(170230000, "DAC IR Horiz_Ellipt", -0.1000, enable=False)
    prg.add(170240000, "AOM IR Horiz_Ellipt Amp", 1000, enable=False)
    prg.add(170240500, "AOM IR Horiz_Ellipt freq", 110.00, enable=False)
    prg.add(170241500, "DAC IR Horiz_Ellipt", 2.0000, functions=dict(value=lambda x: cmd.get_var('Ellipt_finalValue'), funct_enable=False), enable=False)
    prg.add(170241600, "Oscilloscope Trigger ON")
    prg.add(170259600, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(170261200, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(170263199, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(170265200, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(170266200, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(170266240, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(170467990, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x +cmd.get_var('hold_time')), enable=False)
    prg.add(170467990, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x +cmd.get_var('hold_time')))
    prg.add(170467990, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(175467990, "fake_levitation")
    prg.add(180467990, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(180467990, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-10.000000, 11.000000, 5.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        PiezoElliptV1 = iters[j]
        cmd.set_var('PiezoElliptV', PiezoElliptV1)
        print('\n')
        print('Run #%d/%d, with variables:\nPiezoElliptV = %g\n'%(j+1, len(iters), PiezoElliptV1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
