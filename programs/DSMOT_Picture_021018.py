prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135062340, "Picture Na_4Gdet", enable=False)
    prg.add(135062340, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(135063340, "Picture_Na_VarProbeDet")
    prg.add(135063340, "Picture_Mirror_Na_VarProbeDet", enable=False)
    prg.add(135063340, "Picture Na_3Gdet_hamamatsu", enable=False)
    prg.add(135063340, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(140063340, "Set_MOT")
    prg.add(140063340, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(400.000000, 800.000000, 50.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        amp1 = iters[j]
        cmd.set_var('amp', amp1)
        print('\n')
        print('Run #%d/%d, with variables:\namp = %g\n'%(j+1, len(iters), amp1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
