prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(195251000, "wait")
    prg.add(195252250, "Hybrid_to_Xigar_transfer")
    prg.add(205352250, "wait")
    prg.add(205353250, "Oscilloscope Trigger ON")
    prg.add(205354250, "DAC BGradX", 0.0000, enable=False)
    prg.add(205454250, "IGBT BGradX CLOSE", enable=False)
    prg.add(205455250, "DAC BGradX", 5.0000, enable=False)
    prg.add(205955250, "IGBT BGradX OPEN", enable=False)
    prg.add(205956250, "DAC Horiz IR", 0.0300)
    prg.add(205957750, "DAC Horiz IR", 0.0400)
    prg.add(205958750, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(205959750, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(205961290, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('hold_time') + cmd.get_var('tof')))
    prg.add(205961330, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(205961330, "multi_images_Hamam", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(211461330, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(211961330, "fake_levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(216961330, "Cigar_beam_check")
    prg.add(231961330, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') +cmd.get_var('hold_time')))
    prg.add(231962330, "AOM IR Horizontal Amp", 1000)
    prg.add(231962330, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(10.000000, 12.000000, 0.150000)
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
