prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(1000000, "uW mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3))
    prg.add(1000500, "uW2 mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3))
    prg.add(171230500, "wait")
    prg.add(172230400, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0.04, stop_t=500, enable=False)
    prg.add(172231400, "IGBT BCompZfine CLOSE", enable=False)
    prg.add(172232400, "DAC SRS", 0.0000)
    prg.add(172243400, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(177443400, "Config field OFF")
    prg.add(177444400, "Oscilloscope Trigger ON")
    prg.add(177444900, "Relay AntiHelm OPEN", enable=False)
    prg.add(177445400, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(177545400, "uW_FeedForward", enable=False)
    prg.add(182445400, "wait")
    prg.add(182445400, "Synchronize.sub")
    prg.add(182546400, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(182548400, "uW mixin amplitude", 1000, enable=False)
    prg.add(182548900, "uW2 mixin amplitude", 1, enable=False)
    prg.add(182558900, "TTL uW 1 (100W) ON", enable=False)
    prg.add(182559960, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(182580960, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(182580960, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse') + cmd.get_var('hold_time')))
    prg.add(182581060, "TTL uW 2 ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(182581060, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x  + cmd.get_var('hold_time')), enable=False)
    prg.add(182581160, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(182583160, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(182583160, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(182583160, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(182584170, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(182585420, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(182585420, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')  + cmd.get_var('hold_time')))
    prg.add(187585420, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(187586420, "AOM IR Horizontal Amp", 1000)
    prg.add(187586420, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(427.000000, 466.000000, 3.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_freq11 = iters[j]
        cmd.set_var('uW_freq1', uW_freq11)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_freq1 = %g\n'%(j+1, len(iters), uW_freq11))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
