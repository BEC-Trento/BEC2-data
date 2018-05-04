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
    prg.add(5181500, "AOM IR Horizontal freq", 80.00, enable=False)
    prg.add(135081000, "Bright_Compressed_MOT", enable=False)
    prg.add(135089000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135089000, "switch off MOT fast")
    prg.add(135091849, "GM BrokenRamp_Short")
    prg.add(135101849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135201849, "Config Field MT")
    prg.add(135203849, "BCompZ current ramp", start_t=0, stop_x=1.6, n_points=200, start_x=0.24, stop_t=500, functions=dict(stop_x=lambda x: x + cmd.get_var('a') + cmd.get_var('db'), funct_enable=False))
    prg.add(135204349, "BComp1 current ramp", start_t=0, stop_x=0.31, n_points=200, start_x=0.31, stop_t=500, functions=dict(stop_x=lambda x: x + cmd.get_var('a') + cmd.get_var('dbort'), funct_enable=False))
    prg.add(135204849, "BComp2 current ramp", start_t=0, stop_x=0.21, n_points=200, start_x=0.21, stop_t=500, functions=dict(stop_x=lambda x: x - cmd.get_var('a') + cmd.get_var('dbort'), funct_enable=False))
    prg.add(140205349, "AOM IR Horizontal freq", 80.00)
    prg.add(140205849, "Evaporation Ramp.sub")
    prg.add(240205849, "[VOID] End Evaporation")
    prg.add(240206849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(240207349, "IGBT BCompY field CLOSE", enable=False)
    prg.add(240207849, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(240208349, "MT_FastTransfer_to_Dipole10A", enable=False)
    prg.add(244208349, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(244210349, "DAC BCompZ", 0.2400)
    prg.add(244210849, "DAC BComp1", 0.3100)
    prg.add(244211349, "DAC BComp2", 0.2100)
    prg.add(244212349, "Swich Off Dipole")
    prg.add(244213849, "DAC BCompZ", 0.2400, functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(244218849, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(244218849, "Picture Na_2Gdet_offset", enable=False)
    prg.add(244218849, "Picture Na_2Gdet_shortrepumperoffset")
    prg.add(244218849, "Picture Na_1Gdet_offset", enable=False)
    prg.add(244218849, "Picture Na_offset", enable=False)
    prg.add(244218849, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(244218849, "Picture Na_3Gdet_offset", enable=False)
    prg.add(244218849, "Picture Na_4Gdet_offset", enable=False)
    prg.add(249218849, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(249223849, "Set MOT", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    return prg
def commands(cmd):
    import numpy as np
    dbort_arr, db_arr, pippo_arr = np.mgrid[-0.7:-0.59:0.1, 0:0.4:0.1, 0:2:1, ]
    iters = list(zip(dbort_arr.ravel(), db_arr.ravel(), pippo_arr.ravel()))
    j = 0
    while(cmd.running):
        dbort1, db1, pippo1 = iters[j]
        cmd.set_var('dbort', dbort1)
        cmd.set_var('db', db1)
        cmd.set_var('pippo', pippo1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndbort = %g\ndb = %g\npippo = %g\n'%(j+1, len(iters), dbort1, db1, pippo1))
        cmd.run(wait_end=True, add_time=500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
