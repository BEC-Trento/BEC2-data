prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2100, "TTL uW 1 (100W) OFF")
    prg.add(-2000, "DDS41_setfull", ch0_amp=1000, ch0_freq=101171128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(0, "TTL uW 1 (100W) ON")
    prg.add(90, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False))
    prg.add(3000, "DDS41_setfull", ch0_amp=500, ch0_freq=100646128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, enable=False)
    prg.add(5000, "TTL uW 1 (100W) ON", enable=False)
    return prg
