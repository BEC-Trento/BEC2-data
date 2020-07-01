prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(190100000, "+-1_mixture_preparation")
    prg.add(190101650, "TTL uW 2 ON", enable=False)
    prg.add(192102650, "two_photon_pulse_DDS", enable=False)
    prg.add(192105620, "DAC BGradX", 1.0000, enable=False)
    prg.add(192205620, "IGBT BGradX CLOSE", enable=False)
    prg.add(194205620, "IGBT BGradX OPEN", enable=False)
    prg.add(194205620, "multi_images_Hamam", enable=False)
    prg.add(194257800, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(194257820, "X_images_Hamam")
    prg.add(194257820, "TTL uW 1 (100W) ON", enable=False)
    prg.add(194258820, "TTL uW 2 ON", enable=False)
    prg.add(197268720, "Oscilloscope Trigger ON")
    prg.add(197268820, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: 0.8*cmd.get_var('Cigar_compressed'), time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(197270820, "DAC Horiz IR", 0.0400, functions=dict(value=lambda x: cmd.get_var('Cigar_compressed'), time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(197280820, "Switch Off Dipole")
    prg.add(197281970, "All uW OFF")
    prg.add(197282070, "TOF_Levitation")
    prg.add(197283170, "Oscilloscope Trigger OFF")
    prg.add(197285302, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(197286652, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(197316652, "TTL Picture Hamamatsu  ON", 'emptyprobe')
    prg.add(197319652, "Probe_pulse_Hamam")
    prg.add(197419652, "TTL Picture Hamamatsu  ON", 'background')
    prg.add(197424652, "TTL Picture Hamamatsu OFF")
    prg.add(205428862, "Cigar_beam_check")
    prg.add(205438862, "TTL uW 1 (100W) OFF")
    prg.add(245438862, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 1.000000, 15.000000)
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
