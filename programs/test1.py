prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Oscilloscope Trigger ON")
    prg.add(5000, "Oscilloscope Trigger OFF")
    prg.add(10000, "Synchronize_MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 20.000000, 20.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse = iters[j]
        cmd.set_var('uW_pulse', uW_pulse)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\n'%(j+1, len(iters), uW_pulse))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
