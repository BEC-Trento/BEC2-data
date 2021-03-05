prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(170102000, "Synchronize.sub")
    prg.add(170202000, "+-1_mixture_preparation")
    prg.add(171305500, "TTL uW 2 ON")
    prg.add(171305510, "DDS41_ramp", enable=False)
    prg.add(171507510, "DDS41_setfull", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(171510510, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_phase=lambda x: cmd.get_var('uW_phi'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(171511510, "DDS41_trigger")
    prg.add(171511515, "Oscilloscope Trigger ON")
    prg.add(171511525, "TTL uW 1 (100W) ON")
    prg.add(171511525, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(171511535, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')))
    prg.add(171513635, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(171513635, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')))
    prg.add(171522635, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(173522635, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(173522735, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(173524745, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(173526730, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(173528604, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(173548604, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(173565264, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')))
    prg.add(173575264, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(176575264, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 40.000000, 9.000000)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse = iters[j]
        cmd.set_var('uW_pulse', uW_pulse)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\n'%(j+1, len(iters), uW_pulse))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
