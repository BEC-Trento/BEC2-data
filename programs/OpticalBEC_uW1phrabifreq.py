prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(178650000, "Synchronize.sub")
    prg.add(178750000, "+-1_mixture_preparation")
    prg.add(180752000, "TTL uW 2 ON", enable=False)
    prg.add(180762000, "two_photon_pulse_DDS", enable=False)
    prg.add(180767000, "DDS41_setfull", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_phase=lambda x: cmd.get_var('beat_phase'), ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(180769000, "TTL uW 1 (100W) ON", enable=False)
    prg.add(180775000, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(180775200, "Oscilloscope Trigger ON", enable=False)
    prg.add(180776400, "soliton_imaging", enable=False)
    prg.add(180776400, "transfer_m1to0", enable=False)
    prg.add(180786400, "Switch Off Dipole")
    prg.add(180806400, "Oscilloscope Trigger ON")
    prg.add(180806500, "transfer_m1m2", enable=False)
    prg.add(180806500, "transfer_m1to0")
    prg.add(180806500, "transfer_p1p2", enable=False)
    prg.add(180826500, "transfer_p1to0", enable=False)
    prg.add(180826500, "transfer_0to0", enable=False)
    prg.add(180826500, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(180826500, "interferometer", enable=False)
    prg.add(180826500, "TTL uW 2 ON")
    prg.add(180826500, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(180826510, "Oscilloscope Trigger ON", enable=False)
    prg.add(180836510, "TOF_Levitation")
    prg.add(180842090, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(180846410, "Oscilloscope Trigger OFF")
    prg.add(180865310, "All uW OFF")
    prg.add(184842090, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(184852090, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(224852090, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.3, 2, 0.1)
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
