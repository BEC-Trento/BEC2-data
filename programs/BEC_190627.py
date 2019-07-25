prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(220500000, "Config field OFF", enable=False)
    prg.add(220500950, "Oscilloscope Trigger ON", enable=False)
    prg.add(220501000, "Switch Off Dipole")
    prg.add(220501050, "Config field MT-MOT to Levit", enable=False)
    prg.add(220502050, "DAC MT-MOT Current", 40.0000, enable=False)
    prg.add(220502050, "Config field OFF")
    prg.add(220502090, "Oscilloscope Trigger OFF")
    prg.add(220503840, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(220503840, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')), enable=False)
    prg.add(220503840, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(235503840, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(235504840, "AOM IR Horizontal Amp", 1000)
    prg.add(235504840, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.200000, 1.800000, 0.100000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tau1 = iters[j]
        cmd.set_var('tau', tau1)
        print('\n')
        print('Run #%d/%d, with variables:\ntau = %g\n'%(j+1, len(iters), tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
