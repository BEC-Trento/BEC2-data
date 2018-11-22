prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135080000, "Picture Na_4Gdet", enable=False)
    prg.add(135080000, "Picture Na_4Gdet_hamamatsu")
    prg.add(135080000, "Picture Na_2Gdet", enable=False)
    prg.add(135080000, "Picture Na_1Gdet", enable=False)
    prg.add(135080000, "Picture Na_0Gdet", enable=False)
    prg.add(140080000, "Set_MOT")
    prg.add(140080000, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.1, 10, 1)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
