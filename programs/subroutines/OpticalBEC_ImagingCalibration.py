prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(60000, "[test] Degauss_1012")
    prg.add(12060000, "Set_MOT")
    prg.add(92060000, "Switch Off MOT_fast")
    prg.add(92061250, "GM_051018")
    prg.add(92063150, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(92063649, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(92116750, "wait")
    prg.add(92117750, "Config Field MT-MOT")
    prg.add(92118750, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(92119250, "AOM IR Horizontal Amp", 1000)
    prg.add(92119750, "AOM IR Horizontal freq", 80.00)
    prg.add(92120250, "DAC Vert IR", 2.0000)
    prg.add(92120750, "AOM IR Vertical Amp", 1000)
    prg.add(92121250, "AOM IR Vertical freq", 80.00)
    prg.add(92122500, "IGBT BCompY CLOSE")
    prg.add(92123250, "DAC BCompY", 0.4160, functions=dict(value=lambda x: cmd.get_var('BCompY_value')*30.0/18.))
    prg.add(92622500, "DAC MT-MOT Voltage", 8.5000)
    prg.add(94122500, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(94123250, "BCompY current ramp", start_t=0, stop_x=0.15, n_points=100, start_x=0.416, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('BCompY_value')*30.0/18., stop_x=lambda x: cmd.get_var('BCompY_value')*50.0/18.))
    prg.add(132622500, "MT Current Ramp", start_t=0, stop_x=18, n_points=500, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(132623500, "BCompY current ramp", start_t=0, stop_x=0, n_points=500, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('BCompY_value')*50.0/18., stop_x=lambda x: cmd.get_var('BCompY_value')))
    prg.add(132623500, "MT Current HalfGauss ramp", start_t=0.0000, func_args="a=50, b=18, duration=3, width=2", n_points=500, func="(a - b * exp(-duration**2 / width**2)) / (1 - exp(-duration**2 / width**2)) + ((b - a) / (1 - exp(-duration**2 / width**2))) * exp(-(t - duration)**2 / width**2)", stop_t=3000.0000, functions=dict(func_args=lambda x: "a={}, b=18, duration=3000, width=1".format(cmd.get_var('MT_I_final')), funct_enable=False), enable=False)
    prg.add(137633500, "Horizontal Dipole Evaporation Ramp_Truncated")
    prg.add(157634500, "MT Current Ramp", start_t=0, stop_x=-0.5, n_points=200, start_x=18, stop_t=1000)
    prg.add(157635500, "BCompY current ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=1000, functions=dict(start_x=lambda x: cmd.get_var('BCompY_value')))
    prg.add(157636500, "DAC SRS ramp", start_t=0, stop_x=0, n_points=200, start_x=-9, stop_t=500)
    prg.add(167736500, "Config field OFF")
    prg.add(167737500, "IGBT BcompY OPEN")
    prg.add(168237500, "Switch Off Dipole")
    prg.add(168240830, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(168240830, "transfer_m1m2_2", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(168242180, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(174500000, "TOF_Levitation")
    prg.add(176246390, "Cigar_beam_check")
    prg.add(176256390, "TTL uW 1 (100W) OFF")
    prg.add(216256390, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.000000, 1001.000000, 50.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probvert_amp1 = iters[j]
        cmd.set_var('probvert_amp', probvert_amp1)
        print('\n')
        print('Run #%d/%d, with variables:\nprobvert_amp = %g\n'%(j+1, len(iters), probvert_amp1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
