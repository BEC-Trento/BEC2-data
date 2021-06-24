prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(230102000, "Synchronize.sub")
    prg.add(230103000, "+-1_mixture_preparation", enable=False)
    prg.add(230605100, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(230605100, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(230607110, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(230609095, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(230610969, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(232610969, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(232627629, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')+cmd.get_var('uW_pulse')))
    prg.add(232637629, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(235637629, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(2500.000000, 6000.000000, 21.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        siglent1_freq = iters[j]
        cmd.set_var('siglent1_freq', siglent1_freq)
        print('\n')
        print('Run #%d/%d, with variables:\nsiglent1_freq = %g\n'%(j+1, len(iters), siglent1_freq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
