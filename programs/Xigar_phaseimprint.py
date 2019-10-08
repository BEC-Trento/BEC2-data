prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(135250000, "Hybrid_to_Xigar_transfer")
    prg.add(145350000, "wait")
    prg.add(145450000, "+-1_mixture_preparation")
    prg.add(147470000, "wait")
    prg.add(147471000, "DDS41_setfull", ch0_amp=300, ch0_freq=100646128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(147480900, "Probe_pulse_1ms", enable=False)
    prg.add(147480900, "Oscilloscope Trigger ON", enable=False)
    prg.add(147481000, "Phase-Imprint")
    prg.add(147486000, "beating", enable=False)
    prg.add(147502300, "two_states_imaging", functions=dict(time=lambda x: x +cmd.get_var('hold_time')))
    prg.add(147652300, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(147655300, "All uW OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(147656300, "15ms_Levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(147657300, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(147813280, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(147813320, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(155813310, "fake_levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time') ), enable=False)
    prg.add(156113310, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time') ))
    prg.add(157113310, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(157113310, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.000000, 400.000000, 10.000000)
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
