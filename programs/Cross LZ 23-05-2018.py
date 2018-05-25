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
    prg.add(249429349, "Horizontal Dipole Deep Evaporation", enable=False)
    prg.add(281929349, "[VOID] End Evaporation")
    prg.add(281934349, "MTtoHorDipoleTransfer", enable=False)
    prg.add(281934349, "MTtoCROSSDipoleTransfer")
    prg.add(301954349, "wait")
    prg.add(301964349, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(301979349, "Landau_Zener_NoBComp", enable=False)
    prg.add(301979349, "Landau_Zener_-1to+1", enable=False)
    prg.add(301979349, "Landau_Zener_Double")
    prg.add(305069349, "wait")
    prg.add(305069363, "Picture_Levit_2018", enable=False)
    prg.add(305119363, "TESTBCompY_Picture_Levit_2018")
    prg.add(305119363, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(305120563, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(305122263, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(305123575, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(305123575, "Picture Na_2Gdet_offset", enable=False)
    prg.add(305123575, "Picture Na_1Gdet_offset", enable=False)
    prg.add(305124575, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(305124575, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(305124575, "Picture Na_3Gdet_offset", enable=False)
    prg.add(305124575, "Picture Na_4Gdet_offset", enable=False)
    prg.add(306124575, "Relay BCompZ Normal")
    prg.add(321124575, "Initialize_Dipole_Off")
    prg.add(321129575, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    pulse_arr, dummy_arr = np.mgrid[0.0025:0.2:0.0075, 0:3:1, ]
    iters = list(zip(pulse_arr.ravel(), dummy_arr.ravel()))
    j = 0
    while(cmd.running):
        pulse1, dummy1 = iters[j]
        cmd.set_var('pulse', pulse1)
        cmd.set_var('dummy', dummy1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\npulse = %g\ndummy = %g\n'%(j+1, len(iters), pulse1, dummy1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
