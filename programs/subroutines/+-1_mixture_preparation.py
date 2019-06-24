prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1002500, "DAC SRS", -0.1000, functions=dict(value=lambda x: cmd.get_var('SRS_voltage'), funct_enable=False))
    prg.add(0, "TTL uW 1 (100W) ON")
    prg.add(10, "TTL uW 2 ON")
    prg.add(10000, "DAC SRS ramp", start_t=0, stop_x=0, n_points=200, start_x=-0.1, stop_t=100, functions=dict(stop_x=lambda x: cmd.get_var('SRS_voltage')), enable=False)
    prg.add(10000, "SRS HalfGauss Current ramp", start_t=0.0000, func_args="a=-0.1, b=0, duration=0.1, width=0.02", n_points=200, func="(a - b * exp(-duration**2 / width**2)) / (1 - exp(-duration**2 / width**2)) + ((b - a) / (1 - exp(-duration**2 / width**2))) * exp(-(t - duration)**2 / width**2)", stop_t=100.0000)
    prg.add(1011000, "wait")
    return prg
