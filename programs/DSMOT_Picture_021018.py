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
    hold_time_arr, x_arr = np.mgrid[0:200:10, 0:4:1, ]
    iters = list(zip(hold_time_arr.ravel(), x_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time1, x1 = iters[j]
        cmd.set_var('hold_time', hold_time1)
        cmd.set_var('x', x1)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\nx = %g\n'%(j+1, len(iters), hold_time1, x1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
