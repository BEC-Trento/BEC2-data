prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "LoadDipole_2020-10-13")
    prg.add(148500000, "+-1_mixture_preparation")
    prg.add(149702000, "TTL uW 2 ON")
    prg.add(149712000, "DAC IR Horizontal ramp", start_t=0, stop_x=0.3, n_points=500, start_x=0.6, stop_t=500)
    prg.add(154713000, "Oscilloscope Trigger ON")
    prg.add(156713000, "XYplane_pulse")
    prg.add(156763000, "Oscilloscope Trigger ON", enable=False)
    prg.add(156763100, "wait", functions=dict(time=lambda x: x+cmd.get_var('T_Ramsey')), enable=False)
    prg.add(156763100, "XYplane_pulse2", functions=dict(time=lambda x: x+cmd.get_var('T_Ramsey')))
    prg.add(156763100, "XYplane_pulse", functions=dict(time=lambda x: x+cmd.get_var('T_Ramsey')), enable=False)
    prg.add(156763100, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')), enable=False)
    prg.add(156764100, "Switch Off Dipole", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')), enable=False)
    prg.add(156764121, "TTL uW 2 OFF", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')), enable=False)
    prg.add(156765131, "hamam_magnetiz_imaging", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')), enable=False)
    prg.add(156766131, "TTL uW 1 (100W) ON", enable=False)
    prg.add(156776231, "All uW OFF", functions=dict(time=lambda x: x+cmd.get_var('T_Ramsey')))
    prg.add(156776331, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')))
    prg.add(156778363, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')))
    prg.add(156780348, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')))
    prg.add(156782222, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')))
    prg.add(156798882, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')+cmd.get_var('T_Ramsey')))
    prg.add(156808882, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')))
    prg.add(159808882, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('T_Ramsey')))
    return prg
def commands(cmd):
    import numpy as np
    T_Ramsey_arr, uW_phi_arr = np.meshgrid(np.linspace(20.000000, 500.000000, 12.000000), np.linspace(0.000000, 16384.000000, 10.000000), )
    iters = list(zip(T_Ramsey_arr.ravel(), uW_phi_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        T_Ramsey, uW_phi = iters[j]
        cmd.set_var('T_Ramsey', T_Ramsey)
        cmd.set_var('uW_phi', uW_phi)
        print('\n')
        print('Run #%d/%d, with variables:\nT_Ramsey = %g\nuW_phi = %g\n'%(j+1, len(iters), T_Ramsey, uW_phi))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
