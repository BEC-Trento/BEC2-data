prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompZfine OPEN", enable=False)
    prg.add(50000, "Config field OFF", enable=False)
    prg.add(100000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(115800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(165800, "Switch Off MOT")
    prg.add(5175800, "Set_BrightMOT", enable=False)
    prg.add(5175800, "Set_MOT")
    prg.add(135175800, "Switch Off MOT")
    prg.add(135178900, "DAC MT-MOT Current", 55.0000)
    prg.add(135179400, "DAC MT-MOT Voltage", 4.0000)
    prg.add(135182500, "GM_051018")
    prg.add(135232500, "wait")
    prg.add(135233500, "Config Field MT-MOT")
    prg.add(135235500, "DAC Horiz IR", 5.4000)
    prg.add(135236500, "AOM IR Horizontal freq", 80.00)
    prg.add(135237500, "AOM IR Horizontal Amp", 1000)
    prg.add(235237500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(239237500, "Horizontal Dipole Evaporation Ramp 10_2018")
    prg.add(271737500, "[VOID] End Evaporation")
    prg.add(274737500, "IGBT BCompZfine CLOSE")
    prg.add(277737500, "MT_to_Hor_Dipole_Cigar_Transfer_102018")
    prg.add(302838500, "Synchronize.sub")
    prg.add(303138500, "uW ON")
    prg.add(303188500, "uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(303189000, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(303189500, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018", enable=False)
    prg.add(303189500, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(303191100, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(303191609, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(303391609, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(303391609, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(303391609, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(303391609, "Picture Na_uW_Probe_hamamatsu", enable=False)
    prg.add(303391609, "Picture Na_2Gdet", enable=False)
    prg.add(303391609, "Picture Na_1Gdet", enable=False)
    prg.add(303391609, "Picture Na_0Gdet", enable=False)
    prg.add(303891609, "IGBT BCompZfine OPEN")
    prg.add(308891609, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(308891609, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.03, 0.72, 0.03)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
