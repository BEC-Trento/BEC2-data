prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(180100000, "Synchronize.sub")
    prg.add(180200000, "+-1_mixture_preparation")
    prg.add(180205000, "TTL uW 2 ON")
    prg.add(182205000, "Oscilloscope Trigger ON", enable=False)
    prg.add(182206200, "two_photon_pulse_DDS", enable=False)
    prg.add(182217200, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(182313200, "F1_imaging", enable=False)
    prg.add(182469200, "Phase-Imprint", enable=False)
    prg.add(182474200, "beating", functions=dict(time=lambda x: x + cmd.get_var('PI_time')), enable=False)
    prg.add(182475200, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(182741860, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(182743860, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(182744860, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')))
    prg.add(182744960, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(182746310, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(182766310, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(182769310, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(182785970, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(186769310, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(186779310, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(226779310, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 20.000000, 10.000000)
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
