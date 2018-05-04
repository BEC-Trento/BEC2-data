prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(10, "IGBT Helm CLOSE", enable=False)
    prg.add(20, "IGBT MOT field CLOSE", enable=False)
    prg.add(1000020, "Oscilloscope Trigger ON")
    prg.add(1000030, "Relay Helm CLOSE")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(420, 610, 20)
    j = 0
    while(cmd.running):
        t11 = iters[j]
        cmd.set_var('t1', t11)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt1 = %g\n'%(j+1, len(iters), t11))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
