prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(110102000, "Synchronize.sub")
    prg.add(110103000, "+-1_mixture_preparation", enable=False)
    prg.add(110104000, "ARP_field")
    prg.add(110504000, "wait", enable=False)
    prg.add(110513000, "wait", enable=False)
    prg.add(110516000, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_phase=lambda x: cmd.get_var('uW_phi'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(110517000, "DDS41_trigger", enable=False)
    prg.add(110518000, "TTL siglent1 ON")
    prg.add(110519000, "TTL siglent1 OFF", functions=dict(time=lambda x: x+cmd.get_var('uW_pulse2')))
    prg.add(110519005, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(110520005, "+-1_mixture_preparation", functions=dict(time=lambda x: x-cmd.get_var('hold_time')+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(110521005, "Katana_pulse", functions=dict(time=lambda x: x+cmd.get_var('uW_pulse2') - cmd.get_var('kat_time')), enable=False)
    prg.add(110526105, "wait", functions=dict(time=lambda x: x+cmd.get_var('uW_pulse2')))
    prg.add(110526105, "PPP_images_Hamam", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('uW_pulse2') + cmd.get_var('kat_time') ), enable=False)
    prg.add(110537114, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('uW_pulse2') + cmd.get_var('kat_time') ), enable=False)
    prg.add(110545114, "multi_images_Hamam", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('kat_time') ))
    prg.add(110546114, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('uW_pulse2') + cmd.get_var('kat_time') ), enable=False)
    prg.add(112517214, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2') + cmd.get_var('kat_time') ))
    prg.add(112546114, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(112848114, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2') + cmd.get_var('kat_time') ))
    prg.add(112848214, "Switch Off Dipole", functions=dict(time=lambda x: x +cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(112850224, "TOF_Levitation", functions=dict(time=lambda x: x+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(112852209, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(112854083, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') +cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(114854083, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x +cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(114870743, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x +  cmd.get_var('cc_ramplength')+cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(114880743, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x +cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(117880743, "Cigar_beam_check", functions=dict(time=lambda x: x +cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(118380743, "Initialize_Dipole_Off", functions=dict(time=lambda x: x +cmd.get_var("uW_pulse")+cmd.get_var('uW_pulse2')))
    prg.add(118380743, "DAC 100W_amplitude", 0.0500, enable=False)
    prg.add(118380743, "hamam_twofastpictures", enable=False)
    prg.add(118380743, "hamam_twofast2furious", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(2.000000, 6.000000, 6.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        time_delay_hamam = iters[j]
        cmd.set_var('time_delay_hamam', time_delay_hamam)
        print('\n')
        print('Run #%d/%d, with variables:\ntime_delay_hamam = %g\n'%(j+1, len(iters), time_delay_hamam))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
