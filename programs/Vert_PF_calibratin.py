prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Shutter Probe Vert ON")
    prg.add(101000, "Shutter Probe Hor ON")
    prg.add(20101000, "Oscilloscope Trigger ON")
    prg.add(20101100, "Probe_pulse")
    prg.add(25106100, "Oscilloscope Trigger OFF")
    prg.add(25218600, "test_pictures")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.000000, 1000.000000, 50.000000)
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
