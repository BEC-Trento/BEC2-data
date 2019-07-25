prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC SRS ramp", start_t=0, stop_x=-0.1, n_points=200, start_x=0, stop_t=100, enable=False)
    prg.add(0, "SRS HalfGauss Current ramp", start_t=0.0000, func_args="a=0, b=-0.1, duration=0.2, width=0.1", n_points=400, func="(a - b * exp(-duration**2 / width**2)) / (1 - exp(-duration**2 / width**2)) + ((b - a) / (1 - exp(-duration**2 / width**2))) * exp(-(t - duration)**2 / width**2)", stop_t=200.0000, functions=dict(func_args=lambda x: 'a={}, b=-0.1, duration=0.2, width=0.1'.format(cmd.get_var('SRS_voltage'))))
    return prg
