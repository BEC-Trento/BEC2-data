import libraries.ramp as lib_ramp

# 2017-04-10 brand newer FunctionRamps
# FunctionRamp Example
#    action_list.add("Dipole y Func", lib_ramp.FunctionRamp,
#                    categories=["func"],
#                    parameters=dict(act_name="Dipole Trap y DAC V", act_var_name="value", act_parameters={}),
#                    variables=dict(start_t=0, stop_t=100, n_points=100,
#                                   func="amp*sin(2*pi*freq*t)**2", func_args="amp=5, freq=100"),
#                    var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
#                    comment="time")

def action_list_init(action_list):

    action_list.add(
        "SRS HalfGauss Current ramp", lib_ramp.FunctionRamp,
        categories=["func"], 
        parameters=dict(act_name="DAC SRS", act_var_name="value", act_parameters={}),
        variables=dict(
            start_t=0, stop_t=100, n_points=100,
            func="(a - b * exp(-duration**2 / width**2)) / (1 - exp(-duration**2 / width**2)) + ((b - a) / (1 - exp(-duration**2 / width**2))) * exp(-(t - duration)**2 / width**2)", func_args="a=0, b=1, duration=1, width=0.5"),
            var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
            comment="time")
                    
#                    action_list.add("DAC SRS ramp", lib_ramp.LinearRamp,
#                    categories=["ramps"],
#                    parameters=dict(act_name="DAC SRS", act_var_name="value"),
#                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
#                    comment="")

    action_list.add("3D MOT Coils ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC 3DMOT Coils Current", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("MT Current Ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC MT-MOT Current", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("3DMOT amp(+) ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM 3DMOT Amp ch1 (+)", act_var_name="amplitude"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("3DMOT Detuning ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM 3DMOT Detuning", act_var_name="frequency"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")


    
    action_list.add("GM amp(+) ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM GM Amp ch1 (+)", act_var_name="amplitude"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")
    
    action_list.add("GM Detuning ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM GM Detuning", act_var_name="frequency"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("DAC IR Horizontal ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC Horiz IR", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("DAC IR Horizontal Ellipt ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC IR Horiz_Ellipt", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("DAC IR Vertical ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC Vert IR", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("DS + RepMot amp ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM DS + RepumperMOT Amp ", act_var_name="amplitude"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("DS + RepMot freq ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="AOM DS + RepumperMOT Freq", act_var_name="frequency"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("BComp2 current ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC BComp2", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")
                    
    action_list.add("DAC SRS ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC SRS", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")
                    
    action_list.add("BCompZ current ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC BCompZ", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("BComp1 current ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC BComp1", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("BCompY current ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="DAC BCompY", act_var_name="value"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")
    
    action_list.add("Landau-Zener Freq ramp", lib_ramp.LinearRamp,
                    categories=["ramps"],
                    parameters=dict(act_name="RF Landau-Zener LUT", act_var_name="n_lut"),
                    variables=dict(start_x=0, stop_x=0, start_t=0, stop_t=0, n_points=1),
                    comment="")

    action_list.add("DAC Horiz IR Exp ramp",
                    lib_ramp.FunctionRamp,
                    categories = ["func"],
                    parameters=dict(act_name="DAC Horiz IR", act_var_name="value", act_parameters={}),
                    variables=dict( start_t=0,
                                    stop_t=0,
#                                    start_value=0,
#                                    offset=0,
#                                    tau=0,
                                    n_points=1,
                                    func="(start_value-offset)*exp(-t/tau)+offset",
                                    func_args='start_value=1, tau=1, offset=0'),
                    var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
                    comment="time")  
    action_list.add("DAC IR Horiz_Ellipt Exp ramp",
                    lib_ramp.FunctionRamp,
                    categories = ["func"],
                    parameters=dict(act_name="DAC IR Horiz_Ellipt", act_var_name="value", act_parameters={}),
                    variables=dict( start_t=0,
                                    stop_t=0,
#                                    start_value=0,
#                                    offset=0,
#                                    tau=0,
                                    n_points=1,
                                    func="(start_value-offset)*exp(-t/tau)+offset",
                                    func_args='start_value=1, tau=1, offset=0'),
                    var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
                    comment="time")

    action_list.add("DAC Vert IR Exp ramp",
                    lib_ramp.FunctionRamp,
                    categories = ["func"],
                    parameters=dict(act_name="DAC Vert IR", act_var_name="value", act_parameters={}),
                    variables=dict( start_t=0,
                                    stop_t=0,
#                                    start_value=0,
#                                    offset=0,
#                                    tau=0,
                                    n_points=1,
                                    func="(start_value-offset)*exp(-t/tau)+offset",
                                    func_args='start_value=1, tau=1, offset=0'),
                    var_formats=dict(start_t="%.4f", stop_t="%.4f", n_points="%d", func="%s", func_args="%s"),
                    comment="time")


