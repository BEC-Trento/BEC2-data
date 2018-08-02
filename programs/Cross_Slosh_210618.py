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
    prg.add(302034349, "BComp1 current ramp", start_t=0, stop_x=10, n_points=100, start_x=0.26, stop_t=1000)
    prg.add(302084349, "Cross_Turnoff_and_Recapture", enable=False)
    prg.add(322084349, "DAC BComp1", 0.2600)
    prg.add(322184349, "DAC Magnetic Trap Voltage", 6.5000, enable=False)
    prg.add(322384349, "wait", functions=dict(time=lambda x: x +cmd.get_var('hold'), funct_enable=False))
    prg.add(322384363, "Picture_Levit_2018", functions=dict(time=lambda x: x + cmd.get_var('hold'), funct_enable=False), enable=False)
    prg.add(322384363, "TESTBCompY_Picture_Levit_2018", enable=False)
    prg.add(322384363, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(322385563, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold')))
    prg.add(322387263, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold')))
    prg.add(322388763, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(322388763, "Picture Na_2Gdet_offset", enable=False)
    prg.add(322388763, "Picture Na_1Gdet_offset", enable=False)
    prg.add(322391763, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(322791763, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x+ cmd.get_var('hold')))
    prg.add(322791763, "Picture Na_3Gdet_offset", enable=False)
    prg.add(322791763, "Picture Na_4Gdet_offset", enable=False)
    prg.add(332791763, "Relay BCompZ Normal")
    prg.add(332801763, "IGBT BComp1 field CLOSE")
    prg.add(332811763, "IGBT BComp2 field CLOSE")
    prg.add(347811763, "Initialize_Dipole_Off")
    prg.add(347816763, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    hold_arr, dummy_arr = np.mgrid[2.65:10:0.2, 0:3:1, ]
    iters = list(zip(hold_arr.ravel(), dummy_arr.ravel()))
    j = 0
    while(cmd.running):
        hold1, dummy1 = iters[j]
        cmd.set_var('hold', hold1)
        cmd.set_var('dummy', dummy1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nhold = %g\ndummy = %g\n'%(j+1, len(iters), hold1, dummy1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
