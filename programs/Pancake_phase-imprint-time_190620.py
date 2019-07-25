prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(170230000, "wait")
    prg.add(170231000, "DAC PiezoHorizEllipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('PiezoElliptV')))
    prg.add(170232000, "Oscilloscope Trigger ON")
    prg.add(170233000, "CigarToPancakeTransfer_190523")
    prg.add(181783000, "wait", enable=False)
    prg.add(181784000, "DAC MT-MOT Current", 40.0000)
    prg.add(181794000, "DAC IR Horiz_Ellipt Exp ramp", start_t=0.0000, func_args="start_value=4.8, tau=0.4, offset=0.6", n_points=1000, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=1800.0000)
    prg.add(199795000, "wait")
    prg.add(199815000, "Synchronize.sub")
    prg.add(199845000, "+-1_mixture_preparation", enable=False)
    prg.add(202045000, "Phase-Imprint", enable=False)
    prg.add(202045000, "Phase-Imprint-beating", functions=dict(time=lambda x: x - cmd.get_var('PI_time') - cmd.get_var('uW_pulse')), enable=False)
    prg.add(202045000, "transfer_m1to0")
    prg.add(202098099, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(202098099, "beating", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')))
    prg.add(202098099, "deloading", enable=False)
    prg.add(202098599, "All uW OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(202099099, "Config field Levit", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(202099099, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(202099899, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(202099899, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(202101129, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(202101129, "Picture_Mirror_Na_uWRepump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(202101129, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(202101129, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(202119868, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(206201129, "fake_levitation", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(211201129, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(211301129, "All uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(211302129, "AOM IR Horizontal Amp", 1000)
    prg.add(211302129, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.000000, 1.000000, 0.100000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse1 = iters[j]
        cmd.set_var('uW_pulse', uW_pulse1)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\n'%(j+1, len(iters), uW_pulse1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
