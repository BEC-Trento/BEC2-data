prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(178651000, "+-1_mixture_preparation")
    prg.add(179261000, "two_photon_pulse_DDS", enable=False)
    prg.add(179263870, "Oscilloscope Trigger ON")
    prg.add(179264870, "DAC Vert IR", 1.5000, enable=False)
    prg.add(179464870, "DAC Vert IR", 2.0000, enable=False)
    prg.add(179464870, "multi_images_Hamam", enable=False)
    prg.add(179464870, "X_images_Hamam")
    prg.add(182464870, "DAC Horiz IR", 0.0200, functions=dict(time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(182466870, "DAC Horiz IR", 0.0400, functions=dict(time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(182476870, "Switch Off Dipole")
    prg.add(182478770, "TTL uW 1 (100W) OFF")
    prg.add(182478870, "TOF_Levitation")
    prg.add(182479870, "Oscilloscope Trigger OFF")
    prg.add(182482002, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(182483352, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(182513352, "TTL Picture Hamamatsu  ON", 'emptyprobe')
    prg.add(182516352, "Probe_pulse_Hamam")
    prg.add(182616352, "TTL Picture Hamamatsu  ON", 'background')
    prg.add(182621352, "TTL Picture Hamamatsu OFF")
    prg.add(190625562, "Cigar_beam_check")
    prg.add(190635562, "TTL uW 1 (100W) OFF")
    prg.add(230635562, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 4, 0.2)
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
