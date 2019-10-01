prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(170220000, "Oscilloscope Trigger ON", enable=False)
    prg.add(170230000, "wait")
    prg.add(170231000, "DAC PiezoHorizEllipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('PiezoElliptV')))
    prg.add(170233000, "CigarToPancakeTransfer_190523")
    prg.add(181784000, "DAC MT-MOT Current", 40.0000)
    prg.add(209784000, "wait")
    prg.add(209804000, "Synchronize.sub")
    prg.add(209834000, "+-1_mixture_preparation")
    prg.add(212133900, "Oscilloscope Trigger ON")
    prg.add(212134000, "Phase-Imprint", functions=dict(time=lambda x: x - cmd.get_var('PI_time')))
    prg.add(212135000, "transfer_m1to0", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(212135000, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(212137000, "beating", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(212147000, "All uW OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(212247000, "deloading", enable=False)
    prg.add(212247000, "Config field Levit", functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(212297119, "horizontal_SG", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(212297119, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(212297919, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(212299919, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(212301149, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(212301149, "Picture_Mirror_Na_uWRepump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(212301149, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(212301149, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(212319888, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(218401148, "fake_levitation", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(223402348, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(223502348, "All uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(223502348, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.000000, 50.000000, 5.000000)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time1 = iters[j]
        cmd.set_var('hold_time', hold_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\n'%(j+1, len(iters), hold_time1))
        cmd.run(wait_end=True, add_time=5000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
