prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(180100000, "Synchronize.sub")
    prg.add(180200000, "+-1_mixture_preparation")
    prg.add(180205000, "TTL uW 2 ON")
    prg.add(182306200, "TTL uW 1 (100W) ON", enable=False)
    prg.add(182306200, "DDSpulse")
    prg.add(182306200, "DDSpulse_phaserot", enable=False)
    prg.add(182306200, "DDSpulse_phaserot_reducecoupling", enable=False)
    prg.add(182308209, "Oscilloscope Trigger ON")
    prg.add(182309209, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') +cmd.get_var('mixture_rest_time') + cmd.get_var('hold_time')), enable=False)
    prg.add(182311209, "Phase-Imprint", enable=False)
    prg.add(182313218, "beating", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(182324418, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') +cmd.get_var('mixture_rest_time') + cmd.get_var('hold_time')))
    prg.add(182324418, "X_images_Hamam", enable=False)
    prg.add(188325418, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(188325518, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(188328118, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(188330103, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(188331977, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(188351977, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(188368637, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(192351977, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(192361977, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(232361977, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(60.000000, 500.000000, 25.000000)
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
