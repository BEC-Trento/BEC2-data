prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5051100, "DAC Magnetic Trap current", 10.0000)
    prg.add(5052100, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(135052100, "wait")
    prg.add(135060100, "switch off MOT _ Depumper ", enable=False)
    prg.add(135060100, "switch off MOT fast")
    prg.add(135062949, "GM BrokenRamp_Short")
    prg.add(135062949, "GM FullSequence_Short", enable=False)
    prg.add(135112949, "wait")
    prg.add(135113949, "Config Field MT")
    prg.add(135115949, "DAC BCompZ", 0.2400, enable=False)
    prg.add(142615949, "Config field OFF")
    prg.add(142625949, "Oscilloscope Trigger ON", enable=False)
    prg.add(142625949, "Picture Na_2Gdet_offset", enable=False)
    prg.add(142625949, "Picture Na_offset", enable=False)
    prg.add(142625949, "Picture Na_3Gdet_offset", enable=False)
    prg.add(142650949, "Picture Na_4Gdet_offset")
    prg.add(142850949, "Oscilloscope Trigger OFF", enable=False)
    prg.add(146956508, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(591, 621, 1)
    j = 0
    while(cmd.running):
        LUT1 = iters[j]
        cmd.set_var('LUT', LUT1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nLUT = %g\n'%(j+1, len(iters), LUT1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
