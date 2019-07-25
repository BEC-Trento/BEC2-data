prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(220223300, "wait")
    prg.add(221223300, "DAC IR Horizontal ramp", start_t=0, stop_x=0.08, n_points=100, start_x=0.04, stop_t=500)
    prg.add(221228300, "DAC SRS", 0.0000)
    prg.add(221239300, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(226439300, "Config field OFF")
    prg.add(226440300, "Oscilloscope Trigger ON")
    prg.add(226440800, "Relay AntiHelm OPEN", enable=False)
    prg.add(226441300, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(226541300, "uW_FeedForward", enable=False)
    prg.add(231441300, "wait")
    prg.add(231441300, "Synchronize.sub")
    prg.add(231491300, "uW mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3))
    prg.add(231491800, "uW2 mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3))
    prg.add(231492300, "uW mixin amplitude", 1000)
    prg.add(231492800, "uW2 mixin amplitude", 1)
    prg.add(231542800, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231552800, "TTL uW 1 (100W) ON")
    prg.add(231553817, "TTL uW 1 (100W) OFF")
    prg.add(231554317, "uW mixin amplitude", 1)
    prg.add(231554817, "uW2 mixin amplitude", 766, functions=dict(amplitude=lambda x: cmd.get_var('uW2_amp')))
    prg.add(231574817, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x + cmd.get_var('hold_time') - cmd.get_var('uW_pulse')))
    prg.add(231574817, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231574916, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231574916, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(231574916, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(231575926, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231577176, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(231577176, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')  + cmd.get_var('hold_time')))
    prg.add(236577176, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(237577176, "All uW OFF")
    prg.add(237578176, "AOM IR Horizontal Amp", 1000)
    prg.add(237578176, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.010000, 0.800000, 0.040000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse1 = iters[j]
        cmd.set_var('uW_pulse', uW_pulse1)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\n'%(j+1, len(iters), uW_pulse1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
