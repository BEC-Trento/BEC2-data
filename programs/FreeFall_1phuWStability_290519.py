prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Set_BrightMOT", enable=False)
    prg.add(50000, "Switch Off MOT")
    prg.add(60000, "[test] Degauss_1012")
    prg.add(12060000, "Set_MOT")
    prg.add(142060000, "Switch Off MOT", enable=False)
    prg.add(142060000, "Switch Off MOT_fast")
    prg.add(142061250, "GM_051018")
    prg.add(142063150, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(142063650, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(142116750, "wait")
    prg.add(142117750, "Config Field MT-MOT")
    prg.add(142118750, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(142119250, "AOM IR Horizontal Amp", 1000)
    prg.add(142119750, "AOM IR Horizontal freq", 80.00)
    prg.add(142120250, "Oscilloscope Trigger ON", enable=False)
    prg.add(142620250, "DAC MT-MOT Voltage", 8.5000)
    prg.add(142621250, "Evaporation Ramp.sub", enable=False)
    prg.add(144121250, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(182621250, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(187722250, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(220223250, "wait")
    prg.add(221223250, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0.04, stop_t=500)
    prg.add(221224250, "IGBT BCompZfine CLOSE")
    prg.add(221235250, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(226435250, "Config field OFF")
    prg.add(226436250, "Oscilloscope Trigger ON")
    prg.add(226436750, "Relay AntiHelm OPEN", enable=False)
    prg.add(226437250, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False))
    prg.add(226537250, "uW_FeedForward", enable=False)
    prg.add(231437250, "wait")
    prg.add(231437250, "Synchronize.sub")
    prg.add(231538250, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231548250, "TTL uW 1 (100W) ON")
    prg.add(231549500, "TTL uW 1 (100W) OFF")
    prg.add(231600500, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse') + cmd.get_var('hold_time')))
    prg.add(231600600, "TTL uW 2 ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse') + cmd.get_var('hold_time')))
    prg.add(231600600, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x  + cmd.get_var('hold_time')))
    prg.add(231600700, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231600800, "Config field Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231600800, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(231600800, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time'), funct_enable=False), enable=False)
    prg.add(231601810, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(231603060, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(231603060, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')  + cmd.get_var('hold_time')))
    prg.add(236603060, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(236604060, "AOM IR Horizontal Amp", 1000)
    prg.add(236604060, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.010000, 0.500000, 0.020000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse1 = iters[j]
        cmd.set_var('uW_pulse', uW_pulse1)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\n'%(j+1, len(iters), uW_pulse1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
