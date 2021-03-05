prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(210102000, "Synchronize.sub")
    prg.add(210202000, "+-1_mixture_preparation")
    prg.add(211305500, "TTL uW 2 ON", enable=False)
    prg.add(211305510, "DDS41_ramp", enable=False)
    prg.add(211507510, "DDS41_setfull", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(211510510, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_phase=lambda x: cmd.get_var('uW_phi'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(211511510, "DDS41_trigger", enable=False)
    prg.add(211511520, "Oscilloscope Trigger ON")
    prg.add(211511530, "TTL uW 1 (100W) ON", enable=False)
    prg.add(211511530, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(211511540, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(211513640, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(211513640, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(211522640, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(213522640, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(213522740, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(213524750, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(213526735, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(213528609, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(213548609, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(213565269, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')))
    prg.add(213575269, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(216575269, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.400000, 1.200000, 10.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        SRS_V = iters[j]
        cmd.set_var('SRS_V', SRS_V)
        print('\n')
        print('Run #%d/%d, with variables:\nSRS_V = %g\n'%(j+1, len(iters), SRS_V))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
