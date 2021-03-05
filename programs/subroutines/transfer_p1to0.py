prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2000, "DAC 100W_amplitude", 10.0000, functions=dict(time=lambda x: x-  cmd.get_var('uW_pulse_p10')))
    prg.add(-1000, "DDS41_setfull", ch0_amp=1, ch0_freq=80000000.000, ch1_freq=100808400.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=340, functions=dict(time=lambda x: x-  cmd.get_var('uW_pulse_p10'), ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3))
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x-  cmd.get_var('uW_pulse_p10')))
    prg.add(0, "TTL uW 1 (100W) OFF")
    prg.add(1040, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False), enable=False)
    return prg
