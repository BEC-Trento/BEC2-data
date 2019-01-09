prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135063100, "GM_051018")
    prg.add(135063600, "DAC MT-MOT Current", 40.0000)
    prg.add(135064100, "DAC MT-MOT Voltage", 6.0000)
    prg.add(135114100, "wait")
    prg.add(135114600, "Config Field MT-MOT")
    prg.add(135114600, "MT_spill_out", enable=False)
    prg.add(150114600, "wait")
    prg.add(150115100, "Config field OFF")
    prg.add(150265100, "Picture Na_VariableDet_hamamatsu")
    prg.add(155265100, "Set_MOT")
    prg.add(155265100, "Set_BrightMOT", enable=False)
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
