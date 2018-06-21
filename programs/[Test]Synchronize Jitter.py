prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(99900000, "wait")
    prg.add(99900500, "Synchronize.sub")
    prg.add(100000500, "Oscilloscope Trigger ON")
    prg.add(100000550, "TTL Test Trigger ON")
    prg.add(100200550, "Oscilloscope Trigger OFF")
    prg.add(100200650, "TTL Test Trigger OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.025, 5, 0.025)
    j = 0
    while(cmd.running):
        pulse1 = iters[j]
        cmd.set_var('pulse', pulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\npulse = %g\n'%(j+1, len(iters), pulse1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
