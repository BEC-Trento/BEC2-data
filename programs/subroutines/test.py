prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Synchronize.sub")
    prg.add(100000, "multi_images_Hamam")
    prg.add(150000, "Oscilloscope 3 Trigger ON")
    prg.add(160000, "Oscilloscope 3 Trigger OFF")
    prg.add(2000000, "All uW OFF")
    prg.add(5000000, "three-pictures_VarProbeDet_190625")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.010000, 3.000000, 0.200000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        PI_time1 = iters[j]
        cmd.set_var('PI_time', PI_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nPI_time = %g\n'%(j+1, len(iters), PI_time1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
