prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(178650000, "Synchronize.sub")
    prg.add(178750000, "+-1_mixture_preparation")
    prg.add(178751000, "TTL uW 2 ON")
    prg.add(180753000, "TTL uW 1 (100W) ON", enable=False)
    prg.add(180753000, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(180753000, "Phase-Imprint", enable=False)
    prg.add(180753000, "beating", functions=dict(time=lambda x: x + cmd.get_var('PI_time') + cmd.get_var('hold_time')), enable=False)
    prg.add(180753100, "Oscilloscope Trigger ON")
    prg.add(180753100, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(180753100, "X_images_Hamam", enable=False)
    prg.add(180763100, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180765100, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(180765700, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(180767051, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(180787051, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(180803711, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(184787051, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(184797051, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(224797051, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(-182.900000, -183.100000, 10.000000)
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
