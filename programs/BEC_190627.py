prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(195251000, "Hybrid_to_Xigar_transfer")
    prg.add(205351000, "Config field OFF", enable=False)
    prg.add(205451950, "Oscilloscope Trigger ON", enable=False)
    prg.add(210551950, "two_states_imaging")
    prg.add(211001950, "Switch Off Dipole")
    prg.add(211002000, "Config field MT-MOT to Levit", enable=False)
    prg.add(211002000, "Config field OFF")
    prg.add(211003000, "DAC MT-MOT Current", 40.0000, enable=False)
    prg.add(211003000, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(211003040, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')), enable=False)
    prg.add(211004790, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(216004790, "fake_levitation")
    prg.add(221004790, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(221005790, "AOM IR Horizontal Amp", 1000)
    prg.add(221005790, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.000000, 200.000000, 5.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        amp1 = iters[j]
        cmd.set_var('amp', amp1)
        print('\n')
        print('Run #%d/%d, with variables:\namp = %g\n'%(j+1, len(iters), amp1))
        cmd.run(wait_end=True, add_time=5000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
