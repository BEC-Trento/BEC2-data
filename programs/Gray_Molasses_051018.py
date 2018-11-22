prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135062100, "Oscilloscope Trigger ON")
    prg.add(135063200, "GM_051018")
    prg.add(135110700, "Oscilloscope Trigger OFF")
    prg.add(135160700, "wait")
    prg.add(135210700, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(135210700, "Picture Na_4Gdet_hamamatsu")
    prg.add(135210700, "Picture Na_2Gdet", enable=False)
    prg.add(135210700, "Picture Na_1Gdet", enable=False)
    prg.add(135210700, "Picture Na_0Gdet", enable=False)
    prg.add(140210700, "Set_MOT")
    prg.add(140210700, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 15, 2)
    j = 0
    while(cmd.running):
        TOF1 = iters[j]
        cmd.set_var('TOF', TOF1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nTOF = %g\n'%(j+1, len(iters), TOF1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
