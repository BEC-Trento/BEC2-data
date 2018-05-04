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
    prg.add(140541350, "Evaporation Ramp.sub")
    prg.add(240541350, "[VOID] End Evaporation")
    prg.add(240546850, "MT_Transfer_to_Dipole10A", enable=False)
    prg.add(240546850, "MT_FastTransfer_to_Dipole10A")
    prg.add(240546850, "MT_FastTransfer_to_Dipole8A", enable=False)
    prg.add(241556850, "Horizontal Dipole Evaporation Ramp trials", enable=False)
    prg.add(241556850, "Horizontal Dipole Evaporation Ramp Dimple3V", enable=False)
    prg.add(241556850, "Horizontal Dipole Evaporation Ramp 5.4V", enable=False)
    prg.add(241556850, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(274056850, "[VOID] End Evaporation")
    prg.add(274057850, "BComp1 current ramp", start_t=0, stop_x=0, n_points=50, start_x=0.31, stop_t=200, functions=dict(stop_x=lambda x: x + cmd.get_var('b1'), funct_enable=False), enable=False)
    prg.add(274058850, "BCompZ current ramp", start_t=0, stop_x=0, n_points=50, start_x=0.24, stop_t=1000, functions=dict(stop_x=lambda x: x + cmd.get_var('bz')), enable=False)
    prg.add(304058850, "BComp Axial Oscillation Ramp", enable=False)
    prg.add(304058850, "BCompY Axial Oscillation Ramp")
    prg.add(334060350, "Config field OFF", functions=dict(time=lambda x: x + 500*cmd.get_var('a') + cmd.get_var('dt')))
    prg.add(334065350, "Swich Off Dipole", functions=dict(time=lambda x: x + 500*cmd.get_var('a') + cmd.get_var('dt')))
    prg.add(334075350, "DAC BCompZ", 0.2400, functions=dict(time=lambda x: x + 500*cmd.get_var('a') + cmd.get_var('dt')))
    prg.add(334075850, "DAC BComp1", 0.3100, functions=dict(time=lambda x: x + 500*cmd.get_var('a') + cmd.get_var('dt')))
    prg.add(334325850, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x + 500*cmd.get_var('a') + cmd.get_var('dt')))
    prg.add(334325850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(334325850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(334325850, "Picture Na_offset", enable=False)
    prg.add(334325850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(334325850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(334325850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(338430449, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + 500*cmd.get_var('a') + cmd.get_var('dt')))
    prg.add(338435449, "Set MOT", functions=dict(time=lambda x: x + 500*cmd.get_var('a') + cmd.get_var('dt')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(500, 755, 25)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
