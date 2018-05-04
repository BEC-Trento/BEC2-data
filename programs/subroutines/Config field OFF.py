prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT Magnetic Trap OPEN")
    prg.add(500, "IGBT MOT field OPEN")
    prg.add(1000, "IGBT AntiHelm OPEN")
    prg.add(1509, "IGBT Helm OPEN")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(25, 35, 1)
    j = 0
    while(cmd.running):
        f11 = iters[j]
        cmd.set_var('f1', f11)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nf1 = %g\n'%(j+1, len(iters), f11))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
