prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DDS41_setfull", ch1_freq=100808289.000, ch0_amp=100, ch0_freq=100443853.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=102, functions=dict(ch1_amp=lambda x: cmd.get_var('uW_amp2'), funct_enable=False))
    prg.add(1000, "TTL uW 1 (100W) ON")
    prg.add(1000, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(6000, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False), enable=False)
    prg.add(7000, "Hamam_picture", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False), enable=False)
    return prg
