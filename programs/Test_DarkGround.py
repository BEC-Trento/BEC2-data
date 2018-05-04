prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(10000000, "Picture DarkGround")
    return prg
def commands(cmd):
    import numpy as np
    I_arr, dt_arr = np.mgrid[12:15:0.5, 0:35:5, ]
    iters = list(zip(I_arr.ravel(), dt_arr.ravel()))
    j = 0
    while(cmd.running):
        I1, dt1 = iters[j]
        cmd.set_var('I', I1)
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nI = %g\ndt = %g\n'%(j+1, len(iters), I1, dt1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
