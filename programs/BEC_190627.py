prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(105500000, "Config field OFF", enable=False)
    prg.add(105600000, "DAC BCompX", 0.5000)
    prg.add(105600100, "IGBT BCompX CLOSE")
    prg.add(105700100, "BCompY current ramp", start_t=0, stop_x=0, n_points=100, start_x=0.15, stop_t=10)
    prg.add(105805100, "IGBT BcompY OPEN")
    prg.add(105806050, "Oscilloscope Trigger ON", enable=False)
    prg.add(105806100, "Switch Off Dipole")
    prg.add(105806150, "Config field MT-MOT to Levit", enable=False)
    prg.add(105806150, "Config field OFF")
    prg.add(105807150, "DAC MT-MOT Current", 40.0000, enable=False)
    prg.add(105807150, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(105807190, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')), enable=False)
    prg.add(105808940, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(110808940, "fake_levitation")
    prg.add(115808940, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(115809940, "AOM IR Horizontal Amp", 1000)
    prg.add(115809940, "Set_BrightMOT", enable=False)
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
