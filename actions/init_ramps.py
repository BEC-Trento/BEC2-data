import libraries.ramp as lib_ramp

def action_list_init(action_list):

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

