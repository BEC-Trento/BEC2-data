prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(130250000, "Hybrid_to_Xigar_transfer")
    prg.add(140330000, "wait")
    prg.add(140340000, "DAC MT-MOT Current", 40.0000)
    prg.add(141340000, "+-1_mixture_preparation")
    prg.add(143360000, "wait")
    prg.add(143361000, "DDS41_setfull", ch0_amp=500, ch0_freq=100646128.000, ch1_freq=100000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(143362000, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(143362000, "Phase-Imprint")
    prg.add(143367000, "beating", enable=False)
    prg.add(143368000, "Oscilloscope Trigger ON", enable=False)
    prg.add(143369300, "All uW OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(143379300, "two_states_imaging", functions=dict(time=lambda x: x +cmd.get_var('hold_time')))
    prg.add(143480800, "15ms_Levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(143481800, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(143482200, "horizontal_SG", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(143483760, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('hold_time') + cmd.get_var('tof')), enable=False)
    prg.add(143483800, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(148483790, "fake_levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time') ))
    prg.add(149483790, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(149483790, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.000000, 50.000000, 4.000000)
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
