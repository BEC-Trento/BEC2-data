prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2500, "DAC 100W_amplitude", 10.0000, functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_00')))
    prg.add(-2000, "DDS41_setfull", ch0_amp=1000, ch0_freq=100626128.000, ch1_freq=100000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('freq00')*1e3, time=lambda x: x - cmd.get_var('uW_pulse_00')))
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_00')))
    prg.add(0, "TTL uW 1 (100W) OFF")
    return prg
