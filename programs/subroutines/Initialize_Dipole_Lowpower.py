prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 80.00)
    prg.add(500, "AOM IR Vertical Amp", 1000)
    prg.add(1000, "DAC Vert IR", 0.5000)
    prg.add(1500, "AOM IR Horizontal freq", 80.00)
    prg.add(2000, "AOM IR Horizontal Amp", 200)
    prg.add(2500, "DAC Horiz IR", 8.0000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(591, 621, 1)
    j = 0
    while(cmd.running):
        LUT1 = iters[j]
        cmd.set_var('LUT', LUT1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nLUT = %g\n'%(j+1, len(iters), LUT1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
