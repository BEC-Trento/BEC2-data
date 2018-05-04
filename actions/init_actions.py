import libraries.action as lib_action
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

    act_lst.add("RF Evaporation", lib_action.DdsAction,
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

    act_lst.add("TTL 1 ch2 OFF", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[2], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL 1 ch2 ON", lib_action.DigitalAction,
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

    act_lst.add("Relay Helm CLOSE", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[4], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Relay Helm OPEN", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[4], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT Magnetic Trap CLOSE", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[5], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT Magnetic Trap OPEN", lib_action.DigitalAction,
		board="TTL1",
		parameters=dict(channel=[5], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("IGBT MOT field CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[6], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT MOT field OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[6], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BComp1 field CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[7], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT Bcomp1 field OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[7], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BComp2 field CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[8], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT Bcomp2 field OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[8], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BCompz field CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[9], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT Bcompz field OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[9], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT Helm CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[10], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT Helm OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[10], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT AntiHelm CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[11], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT AntiHelm OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[11], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BCompY field OPEN", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[12], status=[False]),
                categories=["actions", "TTL"])

    act_lst.add("IGBT BCompY field CLOSE", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[12], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("uW ON", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[13], status=[True]),
                categories=["actions", "TTL"])

    act_lst.add("uW OFF", lib_action.DigitalAction,
                board="TTL1",
                parameters=dict(channel=[13], status=[False]),
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


    act_lst.add("TTL Picture  ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[5], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Picture OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[5], status=[False]),
		categories=["actions", "TTL"])



    act_lst.add("TTL GM Repumper ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[3], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL GM Repumper OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[3], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Test Trigger ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[4], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL Test Trigger OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[4], status=[False]),
		categories=["actions", "TTL"])





    act_lst.add("Breakpoint Source Table ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[7], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Breakpoint Source Table OFF", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[7], status=[False]),
		categories=["actions", "TTL"])

    act_lst.add("TTL 2 Ch8 ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[8], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("TTL 2 Ch8 OFF", lib_action.DigitalAction,
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

    act_lst.add("Shutter 2D MOT/ZS ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[9], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter 2D MOT/ZS OFF", lib_action.DigitalAction,
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




    act_lst.add("Shutter Probe ON", lib_action.DigitalAction,
		board="TTL2",
		parameters=dict(channel=[10], status=[True]),
		categories=["actions", "TTL"])

    act_lst.add("Shutter Probe OFF", lib_action.DigitalAction,
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

    act_lst.add("DAC 3DMOT Coils Current", lib_action.AnalogAction,
                board="ANG13",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10 A")

    act_lst.add("DAC BComp1", lib_action.AnalogAction,
                board="ANG14",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC BComp2", lib_action.AnalogAction,
                board="ANG15",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC BCompZ", lib_action.AnalogAction,
                board="ANG16",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")


    act_lst.add("DAC Magnetic Trap current", lib_action.AnalogAction,
                board="ANG17",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC Magnetic Trap Voltage", lib_action.AnalogAction,
                board="ANG18",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC BCompY", lib_action.AnalogAction,
                board="ANG19",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="0 - 10V")

    act_lst.add("DAC CC_AB", lib_action.AnalogAction,
                board="ANG20",
                parameters=dict(),
                variables=dict(value=0),
                var_formats=dict(value="%.4f"),
                categories=["actions", "analog"],
                comment="-6 - 6V")




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