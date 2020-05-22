prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "Shutter Probe Vert ON")
    prg.add(5990000, "TTL Picture Hamamatsu  ON", 'image0', enable=False)
    prg.add(6000000, "hamam_twofastpictures", enable=False)
    prg.add(6000000, "hamam_magnetiz_imaging", enable=False)
    prg.add(6000000, "magnetization_imaging")
    prg.add(6000000, "soliton_imaging", enable=False)
    prg.add(6000100, "Oscilloscope Trigger ON")
    prg.add(6005000, "TTL Picture Hamamatsu  ON", 'image1', enable=False)
    prg.add(6305000, "Oscilloscope Trigger OFF")
    prg.add(6306000, "All uW OFF")
    prg.add(56306000, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 250.000000, 20.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        amp = iters[j]
        cmd.set_var('amp', amp)
        print('\n')
        print('Run #%d/%d, with variables:\namp = %g\n'%(j+1, len(iters), amp))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
