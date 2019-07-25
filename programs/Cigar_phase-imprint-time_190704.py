prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(100000, "uW mixin frequency", 100000000, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3))
    prg.add(220330000, "wait")
    prg.add(221330000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.01, n_points=100, start_x=0.04, stop_t=500)
    prg.add(221331000, "IGBT BCompZfine CLOSE")
    prg.add(221332000, "DAC SRS", 0.0000)
    prg.add(221343000, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(226543000, "Config field OFF")
    prg.add(226544000, "Oscilloscope Trigger ON")
    prg.add(226544500, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(226644500, "uW_FeedForward", enable=False)
    prg.add(231544500, "wait")
    prg.add(231544500, "Synchronize.sub")
    prg.add(231644500, "wait")
    prg.add(231645500, "+-1_mixture_preparation", enable=False)
    prg.add(233646500, "two_photon_pulse", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(233746500, "Phase-Imprint", enable=False)
    prg.add(233846500, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(233846510, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(233846520, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(233847320, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(233847320, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(233847320, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(233848330, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(233849580, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(233849580, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')  + cmd.get_var('hold_time')))
    prg.add(238849580, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(238850580, "AOM IR Horizontal Amp", 1000)
    prg.add(238850580, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.100000, 1.000000, 0.100000)
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
