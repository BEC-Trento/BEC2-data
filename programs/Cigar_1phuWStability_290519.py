prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT", enable=False)
    prg.add(135075800, "Switch Off MOT_fast")
    prg.add(135077050, "GM_051018")
    prg.add(135078950, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135079450, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(135132550, "wait")
    prg.add(135133550, "Config Field MT-MOT")
    prg.add(135134550, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135135050, "AOM IR Horizontal Amp", 1000)
    prg.add(135135550, "AOM IR Horizontal freq", 80.00)
    prg.add(135136050, "Oscilloscope Trigger ON", enable=False)
    prg.add(135636050, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135637050, "Evaporation Ramp.sub", enable=False)
    prg.add(137137050, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(175637050, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(180738050, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(213239050, "wait")
    prg.add(214239050, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0.04, stop_t=500)
    prg.add(214240050, "IGBT BCompZfine CLOSE")
    prg.add(214241050, "DAC uW 1", 0.0000)
    prg.add(214251050, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(219451050, "Config field OFF")
    prg.add(219452050, "Oscilloscope Trigger ON")
    prg.add(219453050, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(224453050, "wait")
    prg.add(224454050, "DAC uW 1", 1.2000)
    prg.add(224455050, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(224475050, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')))
    prg.add(224475050, "TTL uW 1 (100W) OFF")
    prg.add(224475150, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(224475150, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(224475150, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(224476160, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(224477410, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(224477410, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(229474150, "DAC uW 1", 0.0000)
    prg.add(229477410, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(229478410, "AOM IR Horizontal Amp", 1000)
    prg.add(229478410, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    x_arr, uW2_freq_arr = np.mgrid[0:40:1, 1771.4172:1771.4185:0.0011, ]
    iters = list(zip(x_arr.ravel(), uW2_freq_arr.ravel()))
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        x1, uW2_freq1 = iters[j]
        cmd.set_var('x', x1)
        cmd.set_var('uW2_freq', uW2_freq1)
        print('\n')
        print('Run #%d/%d, with variables:\nx = %g\nuW2_freq = %g\n'%(j+1, len(iters), x1, uW2_freq1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
