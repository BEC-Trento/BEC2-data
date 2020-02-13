prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT_fast")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135050150, "Oscilloscope Trigger ON")
    prg.add(135060000, "Switch Off MOT", enable=False)
    prg.add(135060000, "Switch Off MOT_fast")
    prg.add(135061250, "GM_051018")
    prg.add(135111250, "Oscilloscope Trigger OFF")
    prg.add(135112450, "MOT_pictures_090120", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(140112450, "Set_MOT")
    prg.add(140112450, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 30, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof = iters[j]
        cmd.set_var('tof', tof)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
