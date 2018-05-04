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
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135341350, "Evaporation Ramp.sub")
    prg.add(185341350, "[VOID] End Evaporation")
    prg.add(185342350, "DAC BCompZ", 0.2400, enable=False)
    prg.add(185342350, "MT_FastTransfer_to_Dipole10A", enable=False)
    prg.add(185342350, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V", enable=False)
    prg.add(185342350, "[VOID] End Evaporation")
    prg.add(185342850, "MT Current Ramp", start_t=0, stop_x=0, n_points=50, start_x=10, stop_t=10)
    prg.add(185343350, "IGBT BCompY field CLOSE")
    prg.add(185343850, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15)
    prg.add(185494350, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    prg.add(185994350, "Picture MT to Levit at 0ms - Levit 50 ms", functions=dict(time=lambda x: x + cmd.get_var('dt')), enable=False)
    prg.add(185997350, "DAC BCompZ", 0.2400, functions=dict(time=lambda x: x + cmd.get_var('dt')), enable=False)
    prg.add(185997850, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    prg.add(186077850, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    prg.add(186077850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(186077850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(186077850, "Picture Na_offset", enable=False)
    prg.add(186077850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(186077850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(186077850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(191077850, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    prg.add(191082850, "Set MOT", functions=dict(time=lambda x: x + cmd.get_var('dt')))
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
