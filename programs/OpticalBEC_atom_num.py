prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(150100000, "multi_images_Hamam", enable=False)
    prg.add(150110000, "+-1_mixture_preparation", enable=False)
    prg.add(152310000, "Switch Off Dipole", enable=False)
    prg.add(152321000, "Oscilloscope Trigger ON")
    prg.add(152331000, "two_photon_pulse_DDS", enable=False)
    prg.add(152333200, "three_pictures_hamamatsu", enable=False)
    prg.add(152824200, "TOF_Levitation", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False))
    prg.add(152825400, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False))
    prg.add(152829312, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(152831624, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+ cmd.get_var('tof')))
    prg.add(152860200, "TTL Picture Hamamatsu  ON", 'emptyprobe', enable=False)
    prg.add(152862200, "Probe_pulse_Hamam", enable=False)
    prg.add(157832624, "Oscilloscope Trigger OFF")
    prg.add(157833624, "fake_levitation", enable=False)
    prg.add(158833624, "Cigar_beam_check", enable=False)
    prg.add(158853624, "TTL uW 1 (100W) OFF")
    prg.add(198853624, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 1.000000, 5.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        x = iters[j]
        cmd.set_var('x', x)
        print('\n')
        print('Run #%d/%d, with variables:\nx = %g\n'%(j+1, len(iters), x))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
