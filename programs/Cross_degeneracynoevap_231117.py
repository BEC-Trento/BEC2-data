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
    prg.add(5182500, "AOM IR Vertical freq", 81.50, enable=False)
    prg.add(135082000, "Bright_Compressed_MOT")
    prg.add(135090000, "switch off MOT _ Depumper ")
    prg.add(135092350, "GM BrokenRamp_Short")
    prg.add(135142350, "Config Field MT")
    prg.add(135348850, "Evaporation Ramp.sub")
    prg.add(235348850, "[VOID] End Evaporation")
    prg.add(235349350, "MT_FastTransfer_to_Dipole10A")
    prg.add(238854350, "Vertical_rampup")
    prg.add(238854350, "IGBT BCompY field OPEN", enable=False)
    prg.add(238854850, "BCompY current ramp", start_t=0, stop_x=10, n_points=50, start_x=0, stop_t=49.9, enable=False)
    prg.add(238855350, "MT Current Ramp", start_t=0, stop_x=0, n_points=50, start_x=3.5, stop_t=50, enable=False)
    prg.add(238905350, "Config field OFF")
    prg.add(238907350, "DAC Horiz IR", -0.1000, enable=False)
    prg.add(238907350, "DAC IR Horizontal ramp", start_t=0, stop_x=-0.1, n_points=30, start_x=5.4, stop_t=5)
    prg.add(238957850, "AOM IR Horizontal freq", 120.00)
    prg.add(239108350, "Swich Off Dipole")
    prg.add(239110350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(239118350, "Picture Na_Shortrepumper_offset")
    prg.add(239118350, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(239118350, "Picture Na_Shortrepumper_2G_offset", enable=False)
    prg.add(239118350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(239118350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(239118350, "Picture Na_offset", enable=False)
    prg.add(239118350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(239118350, "Picture Na_ProvaNew_150917", enable=False)
    prg.add(239118350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(239118350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(243222949, "Initialize_Dipole_Off")
    prg.add(243227949, "Set MOT")
    prg.add(2328569800, "AOM IR Vertical freq", 80.00, enable=False)
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
