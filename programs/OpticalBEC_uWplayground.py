prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(178650000, "Synchronize.sub")
    prg.add(178750000, "+-1_mixture_preparation")
    prg.add(179352000, "TTL uW 2 ON")
    prg.add(179454560, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(179610560, "Phase-Imprint", enable=False)
    prg.add(179615560, "beating", functions=dict(time=lambda x: x + cmd.get_var('PI_time') + cmd.get_var('hold_time')), enable=False)
    prg.add(179620120, "Oscilloscope Trigger ON")
    prg.add(179670120, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(179670120, "X_images_Hamam", enable=False)
    prg.add(181670120, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181672120, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(181673120, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(181674470, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(181694470, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181697470, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181714130, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(185697470, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(185707470, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(225707470, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 16384, 1024)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        beat_phase = iters[j]
        cmd.set_var('beat_phase', beat_phase)
        print('\n')
        print('Run #%d/%d, with variables:\nbeat_phase = %g\n'%(j+1, len(iters), beat_phase))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
