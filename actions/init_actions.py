import libraries.action as lib_action

# save some useful strings

#HalfGaussRamp
# "a=-0.1, b={}, duration=0.2, width=0.1".format(1e-3*cmd.get_var('SRS_voltage'))
def action_list_init(act_lst):
    act_lst.add("AOM IR Horizontal freq", lib_action.DdsAction,
                board="DDS37",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="MHz")
    act_lst.add("AOM IR Horizontal Amp", lib_action.DdsAction,
                board="DDS37",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM IR Vertical freq", lib_action.DdsAction,
                board="DDS37",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="MHz")
                
    act_lst.add("AOM IR Vertical Amp", lib_action.DdsAction,
                board="DDS37",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
                
    act_lst.add("DDS37 LUT", lib_action.DdsAction,
                board="DDS37",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")

    act_lst.add("AOM IR Horiz_Ellipt freq", lib_action.DdsAction,
                board="DDS39",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="MHz")
                
    act_lst.add("AOM IR Horiz_Ellipt Amp", lib_action.DdsAction,
                board="DDS39",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM PhaseImprint freq", lib_action.DdsAction,
                board="DDS39",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="60 - 160 MHz")
                
    act_lst.add("AOM PhaseImprint Amp", lib_action.DdsAction,
                board="DDS39",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")           

    act_lst.add("AOM DS + RepumperMOT Amp ", lib_action.DdsAction,
                board="DDS36",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM DS + RepumperMOT Freq", lib_action.DdsAction,
                board="DDS36",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="240-636 (1) MHz")

    act_lst.add("DDS36 LUT", lib_action.DdsAction,
                board="DDS36",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    
    act_lst.add("uW mixin frequency", lib_action.DdsAction,
                board="DDS41",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("uW mixin amplitude", lib_action.DdsAction,
                board="DDS41",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    
    act_lst.add("uW2 mixin frequency", lib_action.DdsAction,
                board="DDS41",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("uW2 mixin amplitude", lib_action.DdsAction,
                board="DDS41",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
#    act_lst.add("DDS36 Ch2 Amp ", lib_action.DdsAction,
#                board="DDS36",
#                parameters=dict(channel=2),
#                variables=dict(amplitude=0),
#                var_formats=dict(amplitude="%d"),
#                categories=["actions", "DDS"],
#                comment="1,10,20,...1000")

#    act_lst.add("DDS36 Ch2 Freq", lib_action.DdsAction,
#                board="DDS36",
#                parameters=dict(channel=2),
#                variables=dict(frequency=0),
#                var_formats=dict(frequency="%.2f"),
#                categories=["actions", "DDS"],
#                comment="240-636 (1) MHz")


    act_lst.add("AOM Repumper freq", lib_action.DdsAction,
                board="DDS36",
                parameters=dict(channel=2),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="120-318 (0.5) MHz")
    act_lst.add("AOM Repumper Amp", lib_action.DdsAction,
                board="DDS36",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM Zeeman Slower freq", lib_action.DdsAction,
                board="DDS30",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.2f"),
                categories=["actions", "DDS"],
                comment="120-318 (0.5) MHz")
    act_lst.add("AOM Zeeman Slower Amp", lib_action.DdsAction,
                board="DDS30",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")
    act_lst.add("DDS30 LUT", lib_action.DdsAction,
                board="DDS30",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")
    

    act_lst.add("AOM Probe Detuning", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.3f"),
                categories=["actions", "DDS"],
                comment="-50 .. +50 MHz (0.125)")

    act_lst.add("AOM Probe Amp ch1 (+)", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM Probe Amp ch2 (-)", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("DDS35 LUT", lib_action.DdsAction,
                board="DDS35",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")


    act_lst.add("AOM 2DMOT Detuning", lib_action.DdsAction,
                board="DDS34",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.3f"),
                categories=["actions", "DDS"],
                comment="-50 .. +50 MHz (0.125)")

    act_lst.add("AOM 2DMOT Amp ch1 (+)", lib_action.DdsAction,
                board="DDS34",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM 2DMOT Amp ch2 (-)", lib_action.DdsAction,
                board="DDS34",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("DDS34 LUT", lib_action.DdsAction,
                board="DDS34",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")

    act_lst.add("AOM Push Detuning", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.3f"),
                categories=["actions", "DDS"],
                comment="-50 .. +50 MHz (0.125)")

    act_lst.add("AOM Push Amp ch1 (+)", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM Push Amp ch2 (-)", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("DDS33 LUT", lib_action.DdsAction,
                board="DDS33",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")


    act_lst.add("AOM GM Detuning", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.3f"),
                categories=["actions", "DDS"],
                comment="-100 .. +100 MHz (0.25)")


    act_lst.add("AOM GM Amp ch1 (+)", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM GM Amp ch2 (-)", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("DDS31 LUT", lib_action.DdsAction,
                board="DDS31",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")

    act_lst.add("AOM 3DMOT Detuning", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(channel=1),
                variables=dict(frequency=0),
                var_formats=dict(frequency="%.3f"),
                categories=["actions", "DDS"],
                comment="-50 .. +50 MHz (0.125)")

    act_lst.add("AOM 3DMOT Amp ch1 (+)", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("AOM 3DMOT Amp ch2 (-)", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(channel=2),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%d"),
                categories=["actions", "DDS"],
                comment="1,10,20,...1000")

    act_lst.add("DDS32 LUT", lib_action.DdsAction,
                board="DDS32",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")

# Remove when not needed
    act_lst.add("RF Evaporation", lib_action.DdsAction,
                board="DDS38",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")

# This copy is needed for compatibility with evaporation ramps widget
    act_lst.add("Evaporation", lib_action.DdsAction,
                board="DDS38",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="LUT")

    act_lst.add("RF Landau-Zener LUT", lib_action.DdsAction,
                board="DDS39",
                parameters=dict(),
                variables=dict(n_lut=0),
                var_formats=dict(n_lut="%d"),
                categories=["actions", "DDS"],
                comment="CH1 0 to 2MHz, CH1[399] = 14MHz, CH2 0 to 200MHz")

    act_lst.add("RF Landau-Zener Amp", lib_action.DdsAction,
                board="DDS39",
                parameters=dict(channel=1),
                variables=dict(amplitude=0),
                var_formats=dict(amplitude="%.3f"),
                categories=["actions", "DDS"],
                comment="CH1 0 to 1000, CH2 free")
    
### MAGICAL FULLDDSACTIONS
    act_lst.add("DDS41_setfull", lib_action.FullDdsAction,
                board="DDS41",
                parameters=dict(),
                variables=dict(ch0_freq=0, ch0_amp=0, ch0_phase=0, ch1_freq=0, ch1_amp=0, ch1_phase=0),
                var_formats=dict(ch0_freq="%.3f", ch0_amp="%d", ch0_phase="%.3f", ch1_freq="%.3f", ch1_amp="%d", ch1_phase="%.3f"),
                categories=["actions", "DDS"],
                comment="CH1 0 to 1000, CH2 free")
               

###TTL###


    act_lst.add("Initialize 1 TTL1", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]),
		categories=["actions", "TTL"])

    act_lst.add("Initialize 0 TTL1", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False]),
		categories=["actions", "TTL"])


    act_lst.add("Initialize 1 TTL2", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]),
		categories=["actions", "TTL"])

    act_lst.add("Initialize 0 TTL2", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False]),
		categories=["actions", "TTL"])

    act_lst.add("Breakpoint Main Table OFF", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[1], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Breakpoint Main Table ON", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[1], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT BCompZfine OPEN", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[2], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT BCompZfine CLOSE", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[2], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Relay AntiHelm CLOSE", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[3], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Relay AntiHelm OPEN", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[3], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT BGradX CLOSE", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[4], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT BGradX OPEN", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[4], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 4B CLOSE", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[5], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 4B OPEN", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[5], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT BGradZ CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[6], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BGradZ OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[6], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT MOT field CLOSE", lib_action.EmptyAction)

    act_lst.add("IGBT MOT field OPEN", lib_action.EmptyAction)

    act_lst.add("IGBT BCompX CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[7], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BcompX OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[7], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BComp1 field CLOSE", lib_action.EmptyAction)

    act_lst.add("IGBT Bcomp1 field OPEN", lib_action.EmptyAction)

    act_lst.add("IGBT BCompY CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[8], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BcompY OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[8], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BComp2 field CLOSE", lib_action.EmptyAction)

    act_lst.add("IGBT Bcomp2 field OPEN", lib_action.EmptyAction)


    act_lst.add("IGBT BCompz CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[9], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT Bcompz OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[9], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT 3A CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[10], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT 3A OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[10], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT 4A CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[11], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT 4A OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[11], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BGradY field OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[12], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BGradY field CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[12], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("TTL MirrorBottom MOT", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[13], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("TTL MirrorBottom Probe", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[13], status=[True]),
                categories=["actions", "TTL"])


    act_lst.add("RF Landau-Zener ON", lib_action.DigitalAction,
		        board="TTL1",
		        parameters=dict(channel=[14], status=[True]),
		        categories=["actions", "TTL"])

    act_lst.add("RF Landau-Zener OFF", lib_action.DigitalAction,
		        board="TTL1",
		        parameters=dict(channel=[14], status=[False]),
		        categories=["actions", "TTL"])
    
    act_lst.add("Oscilloscope Trigger ON", lib_action.DigitalAction,
		    board="TTL1",
		    parameters=dict(channel=[15], status=[True]),
		    categories=["actions", "TTL"])

    act_lst.add("Oscilloscope Trigger OFF", lib_action.DigitalAction,
		    board="TTL1",
		    parameters=dict(channel=[15], status=[False]),
		    categories=["actions", "TTL"])

    act_lst.add("Relay BCompZ Normal", lib_action.DigitalAction,
		    board="TTL1",
		    parameters=dict(channel=[16], status=[False]),
		    categories=["actions", "TTL"])

    act_lst.add("Relay BCompZ Invert", lib_action.DigitalAction,
		    board="TTL1",
		    parameters=dict(channel=[16], status=[True]),
		    categories=["actions", "TTL"])

    act_lst.add("TTL Dark Spot ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[1], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Dark spot OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[1], status=[False]),
		categories=["actions", "TTL"])


    act_lst.add("TTL Repumper MOT  ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[2], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Repumper MOT OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[2], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL GM Repumper ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[3], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL GM Repumper OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[3], status=[False]),
		categories=["actions", "TTL"])
		
    act_lst.add("TTL ProbeHor OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[4], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL ProbeHor ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[4], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Picture  ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[5], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Picture OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[5], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter Probe Vert ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[6], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter probe Vert OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[6], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Breakpoint Source Table ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[7], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Breakpoint Source Table OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[7], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL ProbeVert ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[8], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL ProbeVert OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[8], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL 2 Ch9 ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[9], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL 2 Ch9 OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[9], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter Push ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[11], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter Push OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[11], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter DS ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[14], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter DS OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[14], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter Gray Molasses OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[12], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter Gray Molasses ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[12], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter 2D MOT/ZS OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[9], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter 2D MOT/ZS ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[9], status=[False]),
		categories=["actions", "TTL"])


    act_lst.add("Shutter 3D MOT ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[15], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter 3D MOT OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[15], status=[False]),
		categories=["actions", "TTL"])

#act_lst.add("Shutter Probe OFF", lib_action.EmptyAction)
    act_lst.add("Shutter Probe ON", lib_action.EmptyAction)

    act_lst.add("Shutter Probe Hor ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[10], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter Probe Hor OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[10], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter RepumperMOT ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[13], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter RepumperMOT OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[13], status=[False]),
		categories=["actions", "TTL"])


    act_lst.add("Initialize 1 TTL3", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]),
		categories=["actions", "TTL"])

    act_lst.add("Initialize 0 TTL3", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], status=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Picture Hamamatsu  ON", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[1], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Picture Hamamatsu OFF", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[1], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 1A CLOSE", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[9], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 1A OPEN", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[9], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 2A CLOSE", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[10], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 2A OPEN", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[10], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 1B CLOSE", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[5], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 1B OPEN", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[5], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 2B CLOSE", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[6], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 2B OPEN", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[6], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 3B CLOSE", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[7], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT 3B OPEN", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[7], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 3 ON", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[3], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 3 OFF", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[3], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 2 ON", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[8], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 2 OFF", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[8], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 2 FSK HIGH", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[4], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 2 FSK LOW", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[4], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 4 ON", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[11], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 4 OFF", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[11], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL RF-arp ON", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[12], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL RF-arp OFF", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[12], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Relay Lower Coil CLOSE", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[13], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Relay Lower Coil OPEN", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[13], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Relay Upper Coil CLOSE", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[14], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Relay Upper Coil OPEN", lib_action.DigitalAction,
		board="TTL3",
		parameters=dict(channel=[14], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL uW 1 (100W) ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[15], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("TTL uW 1 (100W) OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[15], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("TTL uW coupling ON", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[4,15], status=[True,True]),
                categories=["actions", "TTL"])

    act_lst.add("TTL uW coupling OFF", lib_action.DigitalAction,
                board="TTL3",
                parameters=dict(channel=[4,15], status=[False,False]),
                categories=["actions", "TTL"])


###DAC####


    act_lst.add("DAC Vert IR", lib_action.AnalogAction,
                board="ANG11",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10 V")

    act_lst.add("DAC Horiz IR", lib_action.AnalogAction,
                board="ANG12",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC SRS", lib_action.AnalogAction,
                board="ANG13",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="-10 - 10V")

#    act_lst.add("DAC 3DMOT Coils Current", lib_action.EmptyAction)


    act_lst.add("DAC BGradX", lib_action.AnalogAction,
                board="ANG14",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC BComp1", lib_action.EmptyAction)

    act_lst.add("DAC BCompY", lib_action.AnalogAction,
                board="ANG15",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC BComp2", lib_action.EmptyAction)

    act_lst.add("DAC BCompX", lib_action.AnalogAction,
                board="ANG16",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC Magnetic Trap current", lib_action.EmptyAction)

    act_lst.add("DAC MT-MOT Current", lib_action.AnalogAction,
                board="ANG17",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC Magnetic Trap Voltage", lib_action.EmptyAction)

    act_lst.add("DAC MT-MOT Voltage", lib_action.AnalogAction,
                board="ANG18",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC IR Horiz_Ellipt", lib_action.AnalogAction,
                board="ANG19",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC PiezoHorizEllipt", lib_action.AnalogAction,
                board="ANG20",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="-10 - 10V")




    act_lst.add("ANG60", lib_action.AnalogAction,
                board="ANG60",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")
    act_lst.add("ANG61", lib_action.AnalogAction,
                board="ANG61",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

###OTHER###

    act_lst.add("wait", lib_action.EmptyAction)

#    act_lst.add("Set Marconi1", lib_action.MarconiScriptAction,
#                parameters=dict(script="data/devices/marconi_rpc.py"),
#                #parameters=dict(script="devices/fake_marconi.py"),
#                variables=dict(frequency=1769.0, amplitude=0),
#                var_formats=dict(frequency="%f", amplitude="%f"),
#                categories=["actions", "scripts"],
#                comment="Remote Marconi")  

    act_lst.add("Set MarconiS", lib_action.MarconiSScriptAction,
                parameters=dict(script="data/devices/set_marconis.py"),
#                parameters=dict(script="ls"),
                variables=dict(frequency1=1769.0, amplitude1=8., frequency2=1769.0, amplitude2=8.),
                var_formats=dict(frequency1="%f", amplitude1="%f", frequency2="%f", amplitude2="%f"),
                categories=["actions", "scripts"],
                comment="Remote Marconi") 
#                
#                
#    act_lst.add("Set Marconi2", lib_action.MarconiScriptAction2,
#                parameters=dict(script="data/devices/Marconi2-setFrequency.py"),
##                parameters=dict(script="ls"),
#                variables=dict(frequency=1769.0, amplitude=8.),
#                var_formats=dict(frequency="%f", amplitude="%f"),
#                categories=["actions", "scripts"],
#                comment="Remote Marconi")     
#    

