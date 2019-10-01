prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(170250000, "DAC Vert IR", 0.0000, enable=False)
    prg.add(170250000, "Hybrid_to_Xigar_transfer")
    prg.add(180330000, "wait")
    prg.add(180340000, "DAC Horiz IR", 0.0200, enable=False)
    prg.add(180342000, "DAC Horiz IR", 0.0400, enable=False)
    prg.add(180343000, "Oscilloscope Trigger ON")
    prg.add(180344000, "IGBT BCompY CLOSE")
    prg.add(180349000, "BCompY current ramp", start_t=0, stop_x=0.1, n_points=20, start_x=0, stop_t=5)
    prg.add(180409000, "DAC SRS ramp", start_t=0, stop_x=-10, n_points=100, start_x=0, stop_t=10)
    prg.add(180561000, "IGBT BCompZfine OPEN")
    prg.add(180571000, "DAC BGradX", 0.0000)
    prg.add(180581000, "IGBT BGradX CLOSE")
    prg.add(180582000, "BGradX current ramp", start_t=0, stop_x=10, n_points=100, start_x=0, stop_t=5)
    prg.add(180633000, "IGBT BGradX OPEN")
    prg.add(180634000, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180639100, "Config field MT-MOT to Levit", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(180640100, "DAC MT-MOT Current", 40.0000, functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(180640100, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180640140, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(180640260, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('hold_time') + cmd.get_var('tof')))
    prg.add(185640260, "fake_levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time') ))
    prg.add(190640260, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(190640260, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.100000, 300.000000, 10.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time1 = iters[j]
        cmd.set_var('hold_time', hold_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\n'%(j+1, len(iters), hold_time1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
