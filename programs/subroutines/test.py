prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "uW mixin amplitude", 123, enable=False)
    prg.add(10000, "uW mixin frequency", 234.00, enable=False)
    prg.add(20000, "uW2 mixin amplitude", 345, enable=False)
    prg.add(30000, "uW2 mixin frequency", 456.00, enable=False)
    prg.add(50030000, "DDS41_setfull", ch1_freq=20000000.000, ch0_amp=1000, ch0_freq=1000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3))
    prg.add(50040000, "TTL uW 1 (100W) ON")
    prg.add(150040000, "TTL uW 1 (100W) OFF")
    prg.add(150059000, "Oscilloscope Trigger ON")
    prg.add(150060000, "DDS41_setfull", ch0_amp=200, ch0_freq=2000000.000, ch1_freq=10.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(150070000, "Oscilloscope Trigger OFF")
    prg.add(150080000, "three-pictures_VarProbeDet_190625")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.010000, 3.000000, 0.200000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        PI_time1 = iters[j]
        cmd.set_var('PI_time', PI_time1)
        print('\n')
        print('Run #%d/%d, with variables:\nPI_time = %g\n'%(j+1, len(iters), PI_time1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
