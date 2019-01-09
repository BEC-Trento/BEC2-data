prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    return prg
def commands(cmd):
    import numpy as np
    #iters = np.concatenate([np.concatenate([np.arange(0.03,0.72,0.03),np.arange(4.03,4.72,0.03)]),np.arange(6.03,6.72,0.03)])
    iters = np.arange(1,50,2)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
