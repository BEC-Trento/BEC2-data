prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(180100000, "+-1_mixture_preparation")
    prg.add(180101650, "TTL uW 2 ON")
    prg.add(182102650, "two_photon_pulse_DDS", enable=False)
    prg.add(182105620, "DAC BGradX", 1.0000, enable=False)
    prg.add(182205620, "IGBT BGradX CLOSE", enable=False)
    prg.add(184205620, "IGBT BGradX OPEN", enable=False)
    prg.add(184205620, "multi_images_Hamam", enable=False)
    prg.add(184256800, "Oscilloscope Trigger ON")
    prg.add(184257800, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(184257820, "X_images_Hamam")
    prg.add(194257820, "DAC Horiz IR", 0.0200, functions=dict(time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(194259820, "DAC Horiz IR", 0.0400, functions=dict(time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(194269820, "Switch Off Dipole")
    prg.add(194270970, "All uW OFF")
    prg.add(194271070, "TOF_Levitation")
    prg.add(194272170, "Oscilloscope Trigger OFF")
    prg.add(194274302, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(194275652, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(194305652, "TTL Picture Hamamatsu  ON", 'emptyprobe')
    prg.add(194308652, "Probe_pulse_Hamam")
    prg.add(194408652, "TTL Picture Hamamatsu  ON", 'background')
    prg.add(194413652, "TTL Picture Hamamatsu OFF")
    prg.add(202417862, "Cigar_beam_check")
    prg.add(202427862, "TTL uW 1 (100W) OFF")
    prg.add(242427862, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 3.000000, 15.000000)
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
