prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(17000, "Initialize_Dipole_Off")
    prg.add(67000, "Switch Off MOT")
    prg.add(5077000, "Set_BrightMOT", enable=False)
    prg.add(5077000, "Set_MOT")
    prg.add(135077000, "Switch Off MOT", enable=False)
    prg.add(135077000, "Switch Off MOT_fast")
    prg.add(135078250, "GM_051018")
    prg.add(135080150, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135080650, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(135090000, "Oscilloscope Trigger ON", enable=False)
    prg.add(135133750, "wait")
    prg.add(135134750, "Config Field MT-MOT")
    prg.add(135135750, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135136250, "AOM IR Horizontal Amp", 1000)
    prg.add(135136750, "AOM IR Horizontal freq", 80.00)
    prg.add(135137250, "Oscilloscope Trigger ON", enable=False)
    prg.add(135637250, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135638250, "Evaporation Ramp.sub", enable=False)
    prg.add(137138250, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(175638250, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(180739250, "Horizontal Dipole Evaporation Ramp_5V_2019_03")
    prg.add(180740250, "DAC PiezoHorizEllipt", 0.0000, functions=dict(value=lambda x: cmd.get_var('PiezoElliptV')))
    prg.add(213241250, "wait")
    prg.add(213251250, "Oscilloscope Trigger ON")
    prg.add(213252250, "DAC IR Horiz_Ellipt", 0.0000, enable=False)
    prg.add(213252250, "CigarToPancakeTransfer_190523")
    prg.add(213257250, "IGBT BCompZfine CLOSE")
    prg.add(224807250, "wait", enable=False)
    prg.add(224817250, "DAC IR Horiz_Ellipt Exp ramp", start_t=0.0000, func_args="start_value=4.8, tau=0.4, offset=0.6", n_points=1000, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=1800.0000)
    prg.add(242818250, "wait")
    prg.add(242819250, "DAC IR Horiz_Ellipt Exp ramp", start_t=-1800.0000, func_args="start_value=5, tau=-0.4, offset=0.35", n_points=1000, func="(start_value-offset)*(exp(-t/tau))+offset", stop_t=0.0000, enable=False)
    prg.add(242820250, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(242821250, "Config field Levit", functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(242821250, "Config field OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')), enable=False)
    prg.add(242822229, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(242822250, "Switch Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('hold_time')))
    prg.add(242823490, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')+cmd.get_var('hold_time')))
    prg.add(242823490, "Picture_Mirror_Na_uWRepump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(242823490, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')+cmd.get_var('hold_time')), enable=False)
    prg.add(257823490, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(257824490, "AOM IR Horizontal Amp", 1000)
    prg.add(257824490, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    hold_time_arr, x_arr = np.mgrid[0:200:10, 0:4:1, ]
    iters = list(zip(hold_time_arr.ravel(), x_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time1, x1 = iters[j]
        cmd.set_var('hold_time', hold_time1)
        cmd.set_var('x', x1)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\nx = %g\n'%(j+1, len(iters), hold_time1, x1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
