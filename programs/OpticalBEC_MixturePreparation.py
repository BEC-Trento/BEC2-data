prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(178650000, "Synchronize.sub")
    prg.add(178750000, "+-1_mixture_preparation")
    prg.add(178751000, "TTL uW 2 ON")
    prg.add(179352500, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(179362500, "Probe_pulse")
    prg.add(179412000, "Oscilloscope Trigger ON")
    prg.add(179412500, "Phase-Imprint")
    prg.add(179422500, "beating", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(179542500, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(179692500, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(179694500, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(179695500, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(179700130, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(179700140, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(179700260, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(179730260, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(179780260, "TTL Picture Hamamatsu  ON", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(179782260, "TTL Picture Hamamatsu OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(179798920, "Oscilloscope Trigger OFF")
    prg.add(183782260, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(183792260, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(223792260, "wait")
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
