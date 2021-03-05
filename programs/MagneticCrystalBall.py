prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(210102000, "Synchronize.sub")
    prg.add(210103000, "ARP_linear", enable=False)
    prg.add(210104000, "+-1_mixture_preparation")
    prg.add(210504000, "wait", enable=False)
    prg.add(210505000, "+-1_mixture_preparation_Back", enable=False)
    prg.add(210506000, "ARP_linear", enable=False)
    prg.add(210515000, "wait", enable=False)
    prg.add(210518000, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_phase=lambda x: cmd.get_var('uW_phi'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(210519000, "DDS41_trigger")
    prg.add(210519005, "Oscilloscope Trigger ON")
    prg.add(210519010, "TTL uW 1 (100W) ON", enable=False)
    prg.add(210519025, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')), enable=False)
    prg.add(210519035, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(210519035, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time') + cmd.get_var('uW_pulse2') ))
    prg.add(210528035, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(210830035, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(210830135, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(210832145, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(210834130, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(210836004, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(212836004, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(212852664, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')+cmd.get_var('uW_pulse')))
    prg.add(212862664, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(215862664, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(10.000000, 20.000000, 21.000000)
    np.random.shuffle(iters)
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
