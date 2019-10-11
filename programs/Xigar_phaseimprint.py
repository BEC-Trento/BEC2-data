prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(195250000, "Hybrid_to_Xigar_transfer")
    prg.add(205350000, "wait")
    prg.add(205450000, "+-1_mixture_preparation")
    prg.add(207470000, "wait")
    prg.add(210470000, "DDS41_setfull", ch0_amp=300, ch0_freq=100646128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(210471000, "Oscilloscope Trigger ON")
    prg.add(210471200, "Phase-Imprint")
    prg.add(210481740, "multi_images_Hamam", functions=dict(time=lambda x: x +cmd.get_var('hold_time')))
    prg.add(213482740, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(213485740, "All uW OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(213486740, "15ms_Levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(213487740, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(213493720, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(213493760, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(221493750, "fake_levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time') ), enable=False)
    prg.add(221793750, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time') ))
    prg.add(222793750, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(222793750, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(600.000000, 1000.000000, 10.000000)
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
