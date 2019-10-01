prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC IR Horiz_Ellipt", -1.0000)
    prg.add(500, "DAC Vert IR", -1.0000)
    prg.add(10000, "IGBT BCompZfine CLOSE")
    prg.add(11000, "DAC SRS", 0.0000, functions=dict(value=lambda x: 1e-3*cmd.get_var('SRS_voltage')))
    prg.add(12000, "All BComp OFF")
    prg.add(30500, "AOM IR Horiz_Ellipt Amp", 1000)
    prg.add(31000, "AOM IR Horiz_Ellipt freq", 110.00)
    prg.add(31500, "AOM IR Vertical Amp", 1000)
    prg.add(32000, "AOM IR Vertical freq", 80.00)
    prg.add(35500, "DAC IR Horizontal Ellipt ramp", start_t=0, stop_x=4.8, n_points=200, start_x=0, stop_t=100)
    prg.add(36500, "DAC IR Vertical ramp", start_t=0, stop_x=4, n_points=200, start_x=0, stop_t=100)
    prg.add(1036600, "wait")
    prg.add(1520500, "DAC IR Horizontal ramp", start_t=0, stop_x=-0.01, n_points=200, start_x=0.04, stop_t=700)
    prg.add(6530500, "AOM IR Horizontal freq", 110.00)
    prg.add(6531500, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500)
    prg.add(11532500, "Config field OFF")
    prg.add(11542500, "DAC IR Horiz_Ellipt Exp ramp", start_t=0.0000, func_args="start_value=4.8, tau=0.4, offset=0.6", n_points=1000, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=1800.0000)
    prg.add(29552500, "IRHorizEllipt HalfGauss ramp", start_t=0.0000, func_args="a=0.6467, b=1, duration=1, width=0.5", n_points=500, func="(a - b * exp(-duration**2 / width**2)) / (1 - exp(-duration**2 / width**2)) + ((b - a) / (1 - exp(-duration**2 / width**2))) * exp(-(t - duration)**2 / width**2)", stop_t=1000.0000)
    return prg
