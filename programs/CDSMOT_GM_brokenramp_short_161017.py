prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5180000, "DAC Horiz IR", 0.0000, enable=False)
    prg.add(5181000, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(135050000, "Bright_Compressed_MOT", enable=False)
    prg.add(135058000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135058000, "switch off MOT fast")
    prg.add(135060849, "GM BrokenRamp_Short")
    prg.add(135060849, "GM FullSequence_Short", enable=False)
    prg.add(135111849, "Probe_Flash", enable=False)
    prg.add(135111849, "Picture Na_2Gdet_offset", enable=False)
    prg.add(135111849, "Picture Na_offset", enable=False)
    prg.add(135111849, "Picture Na_3Gdet_offset", enable=False)
    prg.add(135311849, "Picture Na_4Gdet_offset", functions=dict(time=lambda x: x + cmd.get_var('time'), funct_enable=False))
    prg.add(139417448, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 18, 3)
    j = 0
    while(cmd.running):
        time1 = iters[j]
        cmd.set_var('time', time1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntime = %g\n'%(j+1, len(iters), time1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
