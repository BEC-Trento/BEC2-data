prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DDS41_setfull", ch1_freq=100000000.000, ch0_amp=1000, ch0_freq=100808400.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(800, "TTL uW 1 (100W) ON")
    prg.add(1500, "TTL uW 1 (100W) OFF")
    return prg
