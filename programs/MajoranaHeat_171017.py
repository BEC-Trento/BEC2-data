prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 5.4000)
    prg.add(5181500, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135341350, "Evaporation Ramp.sub", enable=False)
    prg.add(135341350, "[VOID] End Evaporation", functions=dict(time=lambda x: x + cmd.get_var('ht')))
    prg.add(135342350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135342850, "IGBT BCompY field CLOSE", enable=False)
    prg.add(135343350, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(135493850, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('ht')))
    prg.add(135496850, "DAC BCompZ", 0.2400, functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(135596850, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht') ), enable=False)
    prg.add(135596850, "Picture Na_2Gdet_offset", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')))
    prg.add(135596850, "Picture Na_1Gdet_offset", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')), enable=False)
    prg.add(135596850, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')), enable=False)
    prg.add(135596850, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')), enable=False)
    prg.add(135596850, "Picture Na_3Gdet_offset", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')), enable=False)
    prg.add(135596850, "Picture Na_4Gdet_offset", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')), enable=False)
    prg.add(140596850, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')))
    prg.add(140601850, "Set MOT", functions=dict(time=lambda x: x + cmd.get_var('dt') +  cmd.get_var('ht')))
    return prg
def commands(cmd):
    import numpy as np
    ht_arr, dt_arr, x_arr = np.mgrid[22000:22100:100, 2:8:2, 0:3:1, ]
    iters = list(zip(ht_arr.ravel(), dt_arr.ravel(), x_arr.ravel()))
    j = 0
    while(cmd.running):
        ht1, dt1, x1 = iters[j]
        cmd.set_var('ht', ht1)
        cmd.set_var('dt', dt1)
        cmd.set_var('x', x1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nht = %g\ndt = %g\nx = %g\n'%(j+1, len(iters), ht1, dt1, x1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
