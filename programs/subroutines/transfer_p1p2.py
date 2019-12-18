prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5100, "TTL uW 1 (100W) OFF")
    prg.add(-5000, "DDS41_setfull", ch0_amp=0, ch0_freq=80000000.000, ch1_freq=101172700.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1000)
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_p1p2')))
    prg.add(0, "TTL uW 1 (100W) OFF")
    prg.add(3000, "DDS41_setfull", ch0_amp=300, ch0_freq=100646128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, enable=False)
    return prg
