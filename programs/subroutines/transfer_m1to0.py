prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2000, "DDS41_setfull", ch0_amp=1000, ch0_freq=100443853.000, ch1_freq=100000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_m10')))
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_m10')))
    prg.add(0, "TTL uW 1 (100W) OFF")
    prg.add(580, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False), enable=False)
    return prg
