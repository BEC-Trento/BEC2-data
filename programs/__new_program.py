prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Oscilloscope Trigger ON")
    prg.add(101000, "DDS41_setfull", ch1_freq=0.000, ch0_amp=1000, ch0_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, enable=False)
    prg.add(101000, "DDS41_setnotrigger", ch1_freq=0.000, ch0_amp=1000, ch0_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0)
    prg.add(103000, "DDS41_trigger")
    prg.add(113000, "DDS41_setfull", ch1_freq=0.000, ch0_amp=1, ch0_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0)
    prg.add(123000, "Oscilloscope Trigger OFF")
    return prg
