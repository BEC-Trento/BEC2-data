prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(170230000, "wait")
    prg.add(171229900, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0.04, stop_t=500, enable=False)
    prg.add(171230900, "IGBT BCompZfine CLOSE")
    prg.add(171231900, "DAC SRS", 0.0000, functions=dict(value=lambda x: cmd.get_var('SRS_voltage')))
    prg.add(171242900, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(176442900, "Config field OFF")
    prg.add(176444400, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(176544400, "uW_FeedForward", enable=False)
    prg.add(181444400, "wait")
    prg.add(181444400, "Synchronize.sub")
    prg.add(181540000, "Oscilloscope Trigger ON")
    prg.add(181548400, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181558400, "transfer_m1to0", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181588400, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse') + cmd.get_var('hold_time')))
    prg.add(181590400, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(181590400, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') + cmd.get_var('tof')))
    prg.add(181594520, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('hold_time') + cmd.get_var('tof')))
    prg.add(181595530, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(186595530, "fake_levitation", enable=False)
    prg.add(191595530, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(191596530, "AOM IR Horizontal Amp", 1000)
    prg.add(191596530, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.010000, 3.100000, 0.200000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse1 = iters[j]
        cmd.set_var('uW_pulse', uW_pulse1)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\n'%(j+1, len(iters), uW_pulse1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
