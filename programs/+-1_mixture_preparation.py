prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-100000, "DAC 100W_amplitude", 1.0000, functions=dict(value=lambda x: cmd.get_var('uW_100WDAC')))
    prg.add(-10000, "DDS41_setfull", ch0_amp=1000, ch0_freq=10.000, ch1_freq=20.000, ch0_phase=1.000, ch1_phase=1.000, ch1_amp=1000, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(-1000, "Oscilloscope Trigger ON", enable=False)
    prg.add(0, "TTL uW 1 (100W) ON", enable=False)
    prg.add(10000, "SRS HalfGauss Current ramp", start_t=0.0000, func_args="a=-0.1, b=0.001, duration=0.2, width=0.1", n_points=400, func="(a - b * exp(-duration**2 / width**2)) / (1 - exp(-duration**2 / width**2)) + ((b - a) / (1 - exp(-duration**2 / width**2))) * exp(-(t - duration)**2 / width**2)", stop_t=200.0000, functions=dict(func_args=lambda x: "a={}, b={}, duration=0.2, width=0.1".format(cmd.get_var('SRS_V')-cmd.get_var('arp_amplitude'), cmd.get_var('SRS_V'))))
    prg.add(2001000, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(2001100, "wait")
    return prg
