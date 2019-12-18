prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(178650000, "Synchronize.sub")
    prg.add(178750000, "+-1_mixture_preparation")
    prg.add(179352000, "TTL uW 2 ON")
    prg.add(179454560, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(179455560, "F1_imaging")
    prg.add(179611560, "Phase-Imprint")
    prg.add(179611660, "Oscilloscope Trigger ON")
    prg.add(179616560, "beating", functions=dict(time=lambda x: x + cmd.get_var('PI_time')), enable=False)
    prg.add(179671120, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(179671120, "X_images_Hamam", enable=False)
    prg.add(181671120, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181673120, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(181674120, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(181675470, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(181695470, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181698470, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181715130, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(185698470, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(185708470, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(225708470, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(120, 400, 10)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time = iters[j]
        cmd.set_var('hold_time', hold_time)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\n'%(j+1, len(iters), hold_time))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
