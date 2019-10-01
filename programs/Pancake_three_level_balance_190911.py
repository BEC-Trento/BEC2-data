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
    prg.add(212034000, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse'), funct_enable=False))
    prg.add(212136000, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse'), funct_enable=False), enable=False)
    prg.add(212137000, "transfer_m1to0", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(212140300, "beating", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')))
    prg.add(212141100, "All uW OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(212141600, "15ms_Levitation", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(212142900, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(212142900, "horizontal_SG", enable=False)
    prg.add(212144130, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(212162869, "Oscilloscope Trigger OFF")
    prg.add(218244129, "15ms_Levitation", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(223245329, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(223345329, "All uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(223345329, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.010000, 2.100000, 0.100000)
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
