prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(210102000, "Synchronize.sub")
    prg.add(210102000, "Oscilloscope Trigger ON")
    prg.add(210112000, "Oscilloscope Trigger OFF")
    prg.add(210113000, "TTL siglent1 ON")
    prg.add(210113500, "TTL siglent1 OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(212114100, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(212116110, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(212118095, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(212119969, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(214119969, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(214136629, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')+cmd.get_var('uW_pulse')))
    prg.add(214146629, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(217146629, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(100.000000, 3000.000000, 15.000000)
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
