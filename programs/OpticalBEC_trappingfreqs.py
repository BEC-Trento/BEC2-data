prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(178651000, "+-1_mixture_preparation")
    prg.add(178652650, "TTL uW 2 ON")
    prg.add(180653650, "two_photon_pulse_DDS", enable=False)
    prg.add(180656620, "DAC BGradX", 1.0000)
    prg.add(180756620, "IGBT BGradX CLOSE")
    prg.add(182756620, "IGBT BGradX OPEN")
    prg.add(182756620, "multi_images_Hamam", enable=False)
    prg.add(182807800, "Oscilloscope Trigger ON")
    prg.add(182808800, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(182808820, "X_images_Hamam", enable=False)
    prg.add(192808820, "DAC Horiz IR", 0.0200, functions=dict(time=lambda x: x - cmd.get_var('hold_time')), enable=False)
    prg.add(192810820, "DAC Horiz IR", 0.0400, functions=dict(time=lambda x: x - cmd.get_var('hold_time')), enable=False)
    prg.add(192820820, "Switch Off Dipole")
    prg.add(192821970, "All uW OFF")
    prg.add(192822070, "TOF_Levitation")
    prg.add(192823070, "Oscilloscope Trigger OFF")
    prg.add(192825202, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(192826552, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(192856552, "TTL Picture Hamamatsu  ON", 'emptyprobe')
    prg.add(192859552, "Probe_pulse_Hamam")
    prg.add(192959552, "TTL Picture Hamamatsu  ON", 'background')
    prg.add(192964552, "TTL Picture Hamamatsu OFF")
    prg.add(200968762, "Cigar_beam_check")
    prg.add(200978762, "TTL uW 1 (100W) OFF")
    prg.add(240978762, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 1000.000000, 20.000000)
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
