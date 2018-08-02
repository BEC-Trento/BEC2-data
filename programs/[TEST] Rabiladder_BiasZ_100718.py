prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(150000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5170000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5170500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5171000, "DAC Horiz IR", 5.4000)
    prg.add(5171500, "DAC Vert IR", -0.1000)
    prg.add(5172000, "AOM IR Vertical freq", 120.00)
    prg.add(5172500, "AOM IR Horizontal freq", 80.00)
    prg.add(145172500, "wait")
    prg.add(145175004, "switch off MOT fast")
    prg.add(145177849, "GM BrokenRamp_Short")
    prg.add(145227849, "Config Field MT")
    prg.add(145427849, "Evaporation Ramp.sub")
    prg.add(245427849, "[VOID] End Evaporation")
    prg.add(245429349, "MT_FastTransfer_to_Dipole10A")
    prg.add(249429349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(249429349, "Horizontal Dipole Evaporation Ramp_smallBEC", enable=False)
    prg.add(249429349, "Horizontal Dipole Deep Evaporation", enable=False)
    prg.add(281929349, "[VOID] End Evaporation")
    prg.add(281934349, "MTtoHorDipoleTransfer", enable=False)
    prg.add(281934349, "MTtoCROSSDipoleTransfer")
    prg.add(302034349, "wait", enable=False)
    prg.add(302034849, "Synchronize.sub")
    prg.add(302134849, "DAC Magnetic Trap Voltage", 6.5000, enable=False)
    prg.add(302144849, "Landau_Zener_pure_020718")
    prg.add(302144849, "Landau_Zener", enable=False)
    prg.add(302144849, "Landau_Zener_NoBComp", enable=False)
    prg.add(304154849, "wait")
    prg.add(304164849, "DAC BComp1", 0.7500)
    prg.add(304165349, "DAC BComp2", 0.0000)
    prg.add(304215349, "DAC BCompZ", 0.0000)
    prg.add(304315349, "Relay BCompZ Normal")
    prg.add(304315349, "Relay BCompZ Invert", enable=False)
    prg.add(304365349, "IGBT Bcompz field OPEN", enable=False)
    prg.add(304515349, "IGBT BCompz field CLOSE", enable=False)
    prg.add(304516349, "DAC BCompZ", 0.9650, functions=dict(value=lambda x: cmd.get_var('bz'), funct_enable=False))
    prg.add(304716349, "DAC BComp1", 0.3900)
    prg.add(304717349, "DAC BComp2", 0.2250)
    prg.add(305717349, "IGBT Bcomp2 field OPEN", enable=False)
    prg.add(305718349, "IGBT Bcomp1 field OPEN", enable=False)
    prg.add(305723349, "uW ON", enable=False)
    prg.add(305724349, "Synchronize.sub")
    prg.add(305924349, "uW OFF", enable=False)
    prg.add(305934349, "RF Landau-Zener ON")
    prg.add(305934399, "RF Landau-Zener OFF", functions=dict(time=lambda x: x+cmd.get_var('t1'), funct_enable=False))
    prg.add(305937399, "uW OFF", enable=False)
    prg.add(305942399, "Picture_Levit_2018", functions=dict(time=lambda x: x+cmd.get_var('t1'), funct_enable=False))
    prg.add(305942399, "TESTBCompY_Picture_Levit_2018", enable=False)
    prg.add(305942399, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(305943599, "Swich Off Dipole", functions=dict(time=lambda x: x+cmd.get_var('t1'), funct_enable=False))
    prg.add(305945299, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(305946611, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(306026611, "Picture Na_uW_Repump", enable=False)
    prg.add(306026611, "Picture Na_2Gdet_offset", enable=False)
    prg.add(306026611, "Picture Na_1Gdet_offset", enable=False)
    prg.add(306029611, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(306029611, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(306029611, "Picture Na_3Gdet_offset", enable=False)
    prg.add(306029611, "Picture Na_4Gdet_offset", enable=False)
    prg.add(307029611, "Relay BCompZ Normal")
    prg.add(307039611, "IGBT BComp1 field CLOSE")
    prg.add(307049611, "IGBT BComp2 field CLOSE")
    prg.add(322049611, "Initialize_Dipole_Off")
    prg.add(322054611, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.01, 0.4, 0.01)
    j = 0
    while(cmd.running):
        t11 = iters[j]
        cmd.set_var('t1', t11)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt1 = %g\n'%(j+1, len(iters), t11))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd