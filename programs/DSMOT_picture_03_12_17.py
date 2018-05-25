prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(135050000, "Bright_Compressed_MOT", enable=False)
    prg.add(135058000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135058000, "switch off MOT ")
    prg.add(135058000, "switch off MOT fast", enable=False)
    prg.add(135060849, "GM FullSequence", enable=False)
    prg.add(135060849, "GM FullSequence_Short", enable=False)
    prg.add(135060849, "GM BrokenRamp_Short", enable=False)
    prg.add(135070849, "Picture Na_2Gdet_offset", enable=False)
    prg.add(135070849, "Picture Na_3Gdet_offset", enable=False)
    prg.add(135080849, "Picture Na_4Gdet_offset")
    prg.add(135080849, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(139186448, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    pulse_arr, dummy_arr = np.mgrid[0.0025:0.2:0.0075, 0:3:1, ]
    iters = list(zip(pulse_arr.ravel(), dummy_arr.ravel()))
    j = 0
    while(cmd.running):
        pulse1, dummy1 = iters[j]
        cmd.set_var('pulse', pulse1)
        cmd.set_var('dummy', dummy1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\npulse = %g\ndummy = %g\n'%(j+1, len(iters), pulse1, dummy1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
