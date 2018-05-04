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
    prg.add(5181500, "DAC Vert IR", -0.1000)
    prg.add(5182000, "AOM IR Horizontal freq", 80.00)
    prg.add(135081500, "Bright_Compressed_MOT")
    prg.add(135089500, "switch off MOT _ Depumper ")
    prg.add(135091850, "GM BrokenRamp_Short")
    prg.add(135141850, "Config Field MT")
    prg.add(135141850, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135141850, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(135341850, "Evaporation Ramp.sub")
    prg.add(235341850, "[VOID] End Evaporation")
    prg.add(235342850, "DAC BCompZ", 0.2400)
    prg.add(235348350, "MT_FastTransfer_to_Dipole10A")
    prg.add(235348350, "MT_Piecewise_Transfer_to_Dipole10A", enable=False)
    prg.add(239349350, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(271849350, "[VOID] End Evaporation")
    prg.add(271849850, "AOM IR Vertical freq", 80.00)
    prg.add(271850350, "DAC IR Vertical ramp", start_t=0, stop_x=0.1, n_points=100, start_x=0, stop_t=1000)
    prg.add(271850850, "MT Current Ramp", start_t=0, stop_x=0.05, n_points=100, start_x=3.5, stop_t=2000)
    prg.add(291851350, "BCompZ current ramp", start_t=0, stop_x=1, n_points=20, start_x=0.24, stop_t=10)
    prg.add(316851350, "Config field OFF")
    prg.add(316851350, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(316851350, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(316851350, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(316851350, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(316854350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(321854350, "Swich Off Dipole")
    prg.add(322054350, "Picture Na_Shortrepumper_offset")
    prg.add(322054350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(322054350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(322054350, "Picture Na_offset", enable=False)
    prg.add(322054350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(322054350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(322054350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(327054350, "Initialize_Dipole_Off")
    prg.add(327059350, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 18000, 1000)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=750)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
