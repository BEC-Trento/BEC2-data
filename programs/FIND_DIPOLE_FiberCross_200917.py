prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 4.0000)
    prg.add(5181500, "DAC Vert IR", 6.0000)
    prg.add(5182000, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(5182500, "AOM IR Vertical freq", 81.50)
    prg.add(135082000, "Bright_Compressed_MOT")
    prg.add(135090000, "switch off MOT _ Depumper ")
    prg.add(135092350, "GM BrokenRamp_Short")
    prg.add(135142350, "Config Field MT")
    prg.add(135147350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135147850, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(135148350, "AOM IR Vertical freq", 80.00, enable=False)
    prg.add(135148850, "BCompZ current ramp", start_t=0, stop_x=0.05, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(135348850, "Evaporation Ramp.sub")
    prg.add(235348850, "[VOID] End Evaporation")
    prg.add(235349350, "MT_FastTransfer_to_Dipole10A")
    prg.add(239349350, "Config field OFF")
    prg.add(239352350, "Swich Off Dipole")
    prg.add(239354350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(239357350, "Picture Na_Shortrepumper_offset")
    prg.add(239357350, "Picture Na_Shortrepumper_2G_offset", enable=False)
    prg.add(239357350, "Picture Na_2Gdet_offset", enable=False)
    prg.add(239357350, "Picture Na_1Gdet_offset", enable=False)
    prg.add(239357350, "Picture Na_offset", enable=False)
    prg.add(239357350, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(239357350, "Picture Na_ProvaNew_150917", enable=False)
    prg.add(239357350, "Picture Na_3Gdet_offset", enable=False)
    prg.add(239357350, "Picture Na_4Gdet_offset", enable=False)
    prg.add(243461949, "Initialize_Dipole_Off")
    prg.add(243466949, "Set MOT")
    prg.add(2328808800, "AOM IR Vertical freq", 80.00, enable=False)
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
