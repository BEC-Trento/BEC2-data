prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1002500, "DAC SRS", -0.1000, functions=dict(value=lambda x: cmd.get_var('SRS_voltage'), funct_enable=False))
    prg.add(-10000, "uW mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3), enable=False)
    prg.add(-10000, "DDS41_setfull", ch1_freq=20.000, ch0_amp=1000, ch0_freq=10.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=700, functions=dict(ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3))
    prg.add(-9000, "uW2 mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3), enable=False)
    prg.add(-8000, "uW mixin amplitude", 1000, enable=False)
    prg.add(-7000, "uW2 mixin amplitude", 700, enable=False)
    prg.add(0, "TTL uW 1 (100W) ON")
    prg.add(10, "TTL uW 2 ON", enable=False)
    prg.add(10000, "DAC SRS ramp", start_t=0, stop_x=0, n_points=200, start_x=-0.1, stop_t=100, functions=dict(stop_x=lambda x: cmd.get_var('SRS_voltage')), enable=False)
    prg.add(10000, "SRS HalfGauss Current ramp", start_t=0.0000, func_args="a=-0.1, b=0.001, duration=0.2, width=0.1", n_points=400, func="(a - b * exp(-duration**2 / width**2)) / (1 - exp(-duration**2 / width**2)) + ((b - a) / (1 - exp(-duration**2 / width**2))) * exp(-(t - duration)**2 / width**2)", stop_t=200.0000, functions=dict(func_args=lambda x: "a=-0.1, b={}, duration=0.2, width=0.1".format(cmd.get_var('SRS_voltage'))))
    prg.add(2011000, "wait")
    prg.add(10000000, "All uW OFF")
    return prg
