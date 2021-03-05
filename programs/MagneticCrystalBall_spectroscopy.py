prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(210102000, "Synchronize.sub")
    prg.add(210103000, "ARP_linear", enable=False)
    prg.add(210104000, "+-1_mixture_preparation", enable=False)
    prg.add(210105000, "ARP_field")
    prg.add(210505000, "wait", enable=False)
    prg.add(210505500, "DDS41_setfull", ch1_freq=0.000, ch0_amp=0, ch0_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(210506000, "+-1_mixture_preparation_Back", enable=False)
    prg.add(210507000, "ARP_linear", enable=False)
    prg.add(210516000, "wait", enable=False)
    prg.add(210516005, "Oscilloscope Trigger ON")
    prg.add(210516010, "TTL uW 1 (100W) ON")
    prg.add(210516025, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(210516035, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(210516035, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time') + cmd.get_var('uW_pulse2') ), enable=False)
    prg.add(210525035, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') + cmd.get_var('hold_time')+cmd.get_var('uW_pulse2')), enable=False)
    prg.add(210827035, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(210827135, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(210829145, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(210831130, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(210833004, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(212833004, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(212849664, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')+cmd.get_var('uW_pulse')))
    prg.add(212859664, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(215859664, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.100000, 0.350000, 11.000000)
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
