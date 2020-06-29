prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(180100000, "Synchronize.sub")
    prg.add(180200000, "+-1_mixture_preparation")
    prg.add(181203500, "TTL uW 2 ON", enable=False)
    prg.add(181203500, "TTL uW 1 (100W) ON", enable=False)
    prg.add(181203500, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(181204500, "DDS41_ramp", enable=False)
    prg.add(181304600, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=12288.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, time=lambda x: x + cmd.get_var('cc_ramplength') + cmd.get_var('hold_time'), ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(181309500, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('cc_ramplength') + cmd.get_var('hold_time')))
    prg.add(181310500, "DDS41_trigger", functions=dict(time=lambda x: x + cmd.get_var('cc_ramplength')+ cmd.get_var('hold_time')), enable=False)
    prg.add(181310500, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')), enable=False)
    prg.add(181310500, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') +cmd.get_var('mixture_rest_time') + cmd.get_var('hold_time')), enable=False)
    prg.add(181310500, "Phase-Imprint", enable=False)
    prg.add(181310500, "beating", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(181310500, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(181310500, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(181311790, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')))
    prg.add(181311790, "X_images_Hamam", enable=False)
    prg.add(183311790, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')))
    prg.add(183311890, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')))
    prg.add(183314490, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')))
    prg.add(183316475, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')), enable=False)
    prg.add(183318349, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')), enable=False)
    prg.add(183338349, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(183355009, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')))
    prg.add(197338349, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(197348349, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(237348349, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.120000, 0.150000, 5.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse_p10 = iters[j]
        cmd.set_var('uW_pulse_p10', uW_pulse_p10)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse_p10 = %g\n'%(j+1, len(iters), uW_pulse_p10))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
