prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(90000, "DDS41_setnotrigger", ch1_freq=1000000.000, ch0_amp=1000, ch0_freq=80000000.000, ch0_phase=1.000, ch1_phase=0.000, ch1_amp=0)
    prg.add(100000, "DAC 100W_amplitude", 10.0000)
    prg.add(200000, "DDS41_setfull", ch0_amp=1000, ch0_freq=80000000.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, enable=False)
    prg.add(200000, "DDS41_trigger")
    prg.add(200004, "DDS41_setnotrigger", ch1_freq=0.000, ch0_amp=200, ch0_freq=100000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0)
    prg.add(200008, "Oscilloscope Trigger ON")
    prg.add(200300, "DDS41_trigger")
    prg.add(201000, "DDS41_setfull", ch1_freq=0.000, ch0_amp=100, ch0_freq=120000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, enable=False)
    prg.add(250000, "DDS41_setfull", ch0_amp=1, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0)
    prg.add(250100, "Oscilloscope Trigger OFF")
    return prg
