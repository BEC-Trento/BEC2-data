prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(170230000, "wait")
    prg.add(171230000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.01, n_points=100, start_x=0.04, stop_t=500)
    prg.add(171231000, "IGBT BCompZfine CLOSE")
    prg.add(171232000, "DAC SRS", -0.0010)
    prg.add(171243000, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(176443000, "Config field OFF")
    prg.add(176444500, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(177989000, "wait")
    prg.add(177989000, "Synchronize.sub")
    prg.add(178089000, "wait")
    prg.add(178090000, "+-1_mixture_preparation", enable=False)
    prg.add(180291000, "Phase-Imprint", functions=dict(time=lambda x: x - cmd.get_var('PI_time')), enable=False)
    prg.add(180291000, "Phase-Imprint-beating", enable=False)
    prg.add(180297300, "beating", enable=False)
    prg.add(180300000, "Oscilloscope Trigger ON")
    prg.add(180304300, "two_photon_pulse", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(180304300, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')+ cmd.get_var('hold_time')))
    prg.add(180304300, "deloading", enable=False)
    prg.add(180305300, "All uW OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180306000, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180306800, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180308800, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(180308800, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') + cmd.get_var('tof')))
    prg.add(180309810, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180311060, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(180311060, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')  + cmd.get_var('hold_time')), enable=False)
    prg.add(180311060, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+cmd.get_var('tof')  + cmd.get_var('hold_time')))
    prg.add(185371060, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(185372060, "AOM IR Horizontal Amp", 1000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-11.000000, 11.000000, 2.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        SRS_voltage1 = iters[j]
        cmd.set_var('SRS_voltage', SRS_voltage1)
        print('\n')
        print('Run #%d/%d, with variables:\nSRS_voltage = %g\n'%(j+1, len(iters), SRS_voltage1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
