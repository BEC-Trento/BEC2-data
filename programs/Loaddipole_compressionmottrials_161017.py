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
    prg.add(135081000, "Bright_Compressed_MOT_fardetuned", enable=False)
    prg.add(135089000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135091500, "switch off MOT _ Depumper_short ")
    prg.add(135091500, "switch off MOT fast", enable=False)
    prg.add(135094349, "GM BrokenRamp_Short")
    prg.add(135104349, "DAC BCompZ", 0.1000, enable=False)
    prg.add(135154349, "Config Field MT")
    prg.add(135354349, "Evaporation Ramp.sub")
    prg.add(235354349, "[VOID] End Evaporation")
    prg.add(235355349, "DAC BCompZ", 0.2400, enable=False)
    prg.add(235355849, "IGBT BCompY field CLOSE", enable=False)
    prg.add(235356349, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(235356849, "MT_FastTransfer_to_Dipole10A")
    prg.add(239356849, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(239358849, "Swich Off Dipole")
    prg.add(239360349, "DAC BCompZ", 0.2400, functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(239440349, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(239440349, "Picture Na_2Gdet_offset", enable=False)
    prg.add(239440349, "Picture Na_1Gdet_offset", enable=False)
    prg.add(239440349, "Picture Na_offset")
    prg.add(239440349, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(239440349, "Picture Na_3Gdet_offset", enable=False)
    prg.add(239440349, "Picture Na_4Gdet_offset", enable=False)
    prg.add(244440349, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(244445349, "Set MOT", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
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
