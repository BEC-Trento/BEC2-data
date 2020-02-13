prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(177781000, "multi_images_Hamam", enable=False)
    prg.add(177791000, "+-1_mixture_preparation")
    prg.add(179991000, "Switch Off Dipole", enable=False)
    prg.add(180002000, "Oscilloscope Trigger ON", enable=False)
    prg.add(180012000, "two_photon_pulse_DDS", enable=False)
    prg.add(180512000, "TOF_Levitation", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False))
    prg.add(180513000, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False))
    prg.add(180515120, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(180518240, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+ cmd.get_var('tof')))
    prg.add(185519240, "Oscilloscope Trigger OFF")
    prg.add(185520240, "fake_levitation", enable=False)
    prg.add(186520240, "Cigar_beam_check")
    prg.add(186530240, "TTL uW 1 (100W) OFF")
    prg.add(226530240, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(260, 275, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_lockfreq = iters[j]
        cmd.set_var('uW_lockfreq', uW_lockfreq)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_lockfreq = %g\n'%(j+1, len(iters), uW_lockfreq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
