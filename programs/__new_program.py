prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DDS39_setfull", ch1_freq=0.000, ch0_amp=1000, ch0_freq=10000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0)
    prg.add(50000000, "DDS39_setfull", ch1_freq=0.000, ch0_amp=250, ch0_freq=100000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0)
    return prg
