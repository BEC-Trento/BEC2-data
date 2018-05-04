prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Oscilloscope Trigger ON")
    prg.add(100004, "RF Landau-Zener Amp", 1000.000)
    prg.add(100008, "RF Landau-Zener Freq", 60.000)
    prg.add(200008, "Oscilloscope Trigger OFF")
    prg.add(200012, "RF Landau-Zener Amp", 0.000)
    prg.add(200016, "RF Landau-Zener Freq", 0.000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(40, 60, 1)
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
