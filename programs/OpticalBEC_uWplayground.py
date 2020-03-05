prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(180100000, "Synchronize.sub")
    prg.add(180200000, "+-1_mixture_preparation")
    prg.add(180205000, "TTL uW 2 ON")
    prg.add(182306200, "TTL uW 1 (100W) ON", enable=False)
    prg.add(182306200, "pulse_mixture")
    prg.add(182308209, "Oscilloscope Trigger ON")
    prg.add(182309209, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') +cmd.get_var('mixture_rest_time') + cmd.get_var('hold_time')))
    prg.add(182311209, "Phase-Imprint", enable=False)
    prg.add(182313218, "beating", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(182314418, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse') +cmd.get_var('mixture_rest_time') + cmd.get_var('hold_time')))
    prg.add(182314418, "X_images_Hamam", enable=False)
    prg.add(183315418, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(183315518, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(183318118, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(183320103, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(183321977, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(183341977, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(183358637, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(187341977, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(187351977, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(227351977, "wait")
    return prg
def commands(cmd):
    import numpy as np
    hold_time_arr, SRS_V_arr = np.meshgrid(np.linspace(0.000000, 6.000000, 12.000000), np.linspace(0.100000, 0.300000, 10.000000), )
    iters = list(zip(hold_time_arr.ravel(), SRS_V_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time, SRS_V = iters[j]
        cmd.set_var('hold_time', hold_time)
        cmd.set_var('SRS_V', SRS_V)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\nSRS_V = %g\n'%(j+1, len(iters), hold_time, SRS_V))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
