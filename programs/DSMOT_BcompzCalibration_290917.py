prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT", enable=False)
    prg.add(5050000, "Set MOT_smallload")
    prg.add(10050000, "Bright_Compressed_MOT")
    prg.add(10058000, "switch off MOT _ Depumper ")
    prg.add(10060350, "GM FullSequence", enable=False)
    prg.add(10060350, "GM FullSequence_Short", enable=False)
    prg.add(10060350, "GM BrokenRamp_Short", enable=False)
    prg.add(10060850, "DAC BCompZ", 0.2400)
    prg.add(10080850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(10080850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(10080850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(10080850, "Picture Na_offset")
    prg.add(14186449, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    bz_arr, a_arr, dt_arr = np.mgrid[0.4:0.6:0.05, 1:2:1, 10:200:10, ]
    iters = list(zip(bz_arr.ravel(), a_arr.ravel(), dt_arr.ravel()))
    j = 0
    while(cmd.running):
        bz1, a1, dt1 = iters[j]
        cmd.set_var('bz', bz1)
        cmd.set_var('a', a1)
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nbz = %g\na = %g\ndt = %g\n'%(j+1, len(iters), bz1, a1, dt1))
        cmd.run(wait_end=True, add_time=750)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
