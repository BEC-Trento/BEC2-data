prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(170230000, "wait")
    prg.add(171230000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.01, n_points=100, start_x=0.04, stop_t=500)
    prg.add(171231000, "IGBT BCompZfine CLOSE")
    prg.add(171232000, "DAC SRS", -0.1000)
    prg.add(171243000, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(176443000, "Config field OFF")
    prg.add(176444000, "Oscilloscope Trigger ON")
    prg.add(176444500, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(176544500, "uW_FeedForward", enable=False)
    prg.add(179900000, "phase imprint ON", enable=False)
    prg.add(181444500, "wait")
    prg.add(181444500, "Synchronize.sub")
    prg.add(181544500, "wait")
    prg.add(181545500, "+-1_mixture_preparation")
    prg.add(183746500, "Phase-Imprint", functions=dict(time=lambda x: x - cmd.get_var('PI_time')))
    prg.add(183746500, "Phase-Imprint-beating", enable=False)
    prg.add(183752800, "beating")
    prg.add(183759800, "two_photon_pulse", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(183759800, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')+ cmd.get_var('hold_time')), enable=False)
    prg.add(183759800, "deloading", enable=False)
    prg.add(183760800, "All uW OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(183761500, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(183762300, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(183762300, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(183762300, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(183763310, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(183764560, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(183764560, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')  + cmd.get_var('hold_time')))
    prg.add(188824560, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(188825560, "AOM IR Horizontal Amp", 1000)
    prg.add(188825560, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.010000, 3.000000, 0.200000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        PI_time1 = iters[j]
        cmd.set_var('PI_time', PI_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nPI_time = %g\n'%(j+1, len(iters), PI_time1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
