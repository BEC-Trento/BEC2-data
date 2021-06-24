prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(250102000, "Synchronize.sub")
    prg.add(250103000, "ARP_linear", enable=False)
    prg.add(250104000, "+-1_mixture_preparation", enable=False)
    prg.add(250504000, "wait", enable=False)
    prg.add(250505000, "+-1_mixture_preparation_Back", enable=False)
    prg.add(250506000, "ARP_linear", enable=False)
    prg.add(250515000, "wait", enable=False)
    prg.add(250518000, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_phase=lambda x: cmd.get_var('uW_phi'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(250519000, "DDS41_trigger", enable=False)
    prg.add(250519005, "Oscilloscope Trigger ON")
    prg.add(250519010, "TTL uW 1 (100W) ON", enable=False)
    prg.add(250519025, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')), enable=False)
    prg.add(250519035, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(250519035, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time') + cmd.get_var('uW_pulse2') ))
    prg.add(250528035, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(250830035, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(250830135, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(250832145, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(250834130, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(250836004, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(252836004, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(252852664, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')+cmd.get_var('uW_pulse')))
    prg.add(252862664, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(255862664, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")))
    return prg
def commands(cmd):
    import numpy as np
    uW_pulse_arr, uW_phi_arr = np.meshgrid(np.linspace(0.000000, 30.000000, 13.000000), np.linspace(8192.000000, 9830.000000, 3.000000), )
    iters = list(zip(uW_pulse_arr.ravel(), uW_phi_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse, uW_phi = iters[j]
        cmd.set_var('uW_pulse', uW_pulse)
        cmd.set_var('uW_phi', uW_phi)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\nuW_phi = %g\n'%(j+1, len(iters), uW_pulse, uW_phi))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
