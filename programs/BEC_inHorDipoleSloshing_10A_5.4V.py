prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 5.4000)
    prg.add(5181500, "AOM IR Horizontal freq", 80.00)
    prg.add(135081000, "wait")
    prg.add(135089000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135089000, "switch off MOT fast")
    prg.add(135091849, "GM BrokenRamp_Short")
    prg.add(135141849, "Config Field MT")
    prg.add(135141849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135141849, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(135341849, "Evaporation Ramp.sub", enable=False)
    prg.add(235341849, "[VOID] End Evaporation")
    prg.add(235342849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(235344349, "MT_FastTransfer_to_Dipole10A")
    prg.add(235344349, "MT_Piecewise_Transfer_to_Dipole10A", enable=False)
    prg.add(239344349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(239344349, "Horizontal Dipole Evaporation Ramp variable", enable=False)
    prg.add(271844349, "[VOID] End Evaporation")
    prg.add(272844349, "DAC IR Horizontal ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0.04, stop_t=100)
    prg.add(273844359, "DAC Magnetic Trap current", 0.0000)
    prg.add(273854359, "wait")
    prg.add(273855366, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(273855367, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(273855367, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(273855367, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(273855367, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(273855367, "Picture MT to Levit at 0ms - Levit 50 ms", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(273855367, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(273858367, "DAC BCompZ", 0.2800, functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(273859567, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(273862567, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(273862567, "Picture Na_2Gdet_offset", enable=False)
    prg.add(273862567, "Picture Na_1Gdet_offset", enable=False)
    prg.add(273872567, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(273872567, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(273872567, "Picture Na_3Gdet_offset", enable=False)
    prg.add(273872567, "Picture Na_4Gdet_offset", enable=False)
    prg.add(288872567, "Initialize_Dipole_Off")
    prg.add(288877567, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(420, 610, 20)
    j = 0
    while(cmd.running):
        t11 = iters[j]
        cmd.set_var('t1', t11)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt1 = %g\n'%(j+1, len(iters), t11))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
