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
    prg.add(135210700, "wait")
    prg.add(135211900, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(135211900, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(135211900, "Picture Na_3Gdet_hamamatsu")
    prg.add(135211900, "Picture Na_2Gdet", enable=False)
    prg.add(135211900, "Picture Na_1Gdet", enable=False)
    prg.add(135211900, "Picture Na_0Gdet", enable=False)
    prg.add(140211900, "Set_MOT")
    prg.add(140211900, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    #iters = np.concatenate([np.concatenate([np.arange(0.03,0.72,0.03),np.arange(4.03,4.72,0.03)]),np.arange(6.03,6.72,0.03)])
    iters = np.arange(1,50,2)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
