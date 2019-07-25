prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(220000000, "DAC PiezoHorizEllipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('PiezoElliptV')))
    prg.add(220501000, "wait")
    prg.add(220511000, "Oscilloscope Trigger ON")
    prg.add(220512000, "DAC IR Horiz_Ellipt", 0.0000, enable=False)
    prg.add(220512000, "CigarToPancakeTransfer_190523")
    prg.add(220517000, "IGBT BCompZfine CLOSE")
    prg.add(232067000, "wait", enable=False)
    prg.add(232077000, "DAC IR Horiz_Ellipt Exp ramp", start_t=0.0000, func_args="start_value=4.8, tau=0.4, offset=0.6", n_points=1000, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=1800.0000)
    prg.add(240000000, "phase imprint ON")
    prg.add(250078000, "wait")
    prg.add(250079000, "DAC IR Horiz_Ellipt Exp ramp", start_t=-1800.0000, func_args="start_value=5, tau=-0.4, offset=0.35", n_points=1000, func="(start_value-offset)*(exp(-t/tau))+offset", stop_t=0.0000, enable=False)
    prg.add(250080000, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(250081000, "Config field Levit", functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(250081000, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(250081979, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(250082000, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(250083240, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(250083240, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(250083240, "Picture_Mirror_Na_uWRepump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(250083240, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(265083240, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(265084240, "AOM IR Horizontal Amp", 1000)
    prg.add(265084240, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    hold_time_arr, x_arr = np.mgrid[0:200:10, 0:4:1, ]
    iters = list(zip(hold_time_arr.ravel(), x_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time1, x1 = iters[j]
        cmd.set_var('hold_time', hold_time1)
        cmd.set_var('x', x1)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\nx = %g\n'%(j+1, len(iters), hold_time1, x1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
