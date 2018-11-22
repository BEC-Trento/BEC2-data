prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompZfine OPEN")
    prg.add(50000, "Config field OFF")
    prg.add(100000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(115800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(165800, "Switch Off MOT")
    prg.add(5175800, "Set_BrightMOT", enable=False)
    prg.add(5175800, "Set_MOT")
    prg.add(50175800, "Switch Off MOT")
    prg.add(50178900, "DAC MT-MOT Current", 55.0000)
    prg.add(50179400, "DAC MT-MOT Voltage", 4.0000)
    prg.add(50182500, "GM_051018")
    prg.add(50232500, "wait")
    prg.add(50234500, "Config Field MT-MOT")
    prg.add(50236500, "DAC Horiz IR", 5.4000)
    prg.add(50237500, "AOM IR Horizontal freq", 80.00)
    prg.add(50238500, "AOM IR Horizontal Amp", 1000)
    prg.add(85238500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(89238500, "Horizontal Dipole Evaporation Ramp 10_2018")
    prg.add(121738500, "[VOID] End Evaporation")
    prg.add(124938500, "IGBT BCompZfine CLOSE")
    prg.add(127938500, "MT_to_Hor_Dipole_Cigar_Transfer_102018")
    prg.add(152838500, "Synchronize.sub")
    prg.add(153138500, "Swich Off Dipole", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(153140000, "uW ON", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(153190000, "uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(153190500, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(153191000, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(153191000, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018", enable=False)
    prg.add(153192600, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(153194709, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(153294709, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(153294709, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(153294709, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(153294709, "Picture Na_uW_Probe_hamamatsu", enable=False)
    prg.add(153294709, "Picture Na_2Gdet", enable=False)
    prg.add(153294709, "Picture Na_1Gdet", enable=False)
    prg.add(153294709, "Picture Na_0Gdet", enable=False)
    prg.add(153794709, "IGBT BCompZfine OPEN", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(158794709, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tpulse'), funct_enable=False))
    prg.add(158794709, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    #iters = np.concatenate([np.concatenate([np.arange(0.03,0.72,0.03),np.arange(4.03,4.72,0.03)]),np.arange(6.03,6.72,0.03)])
    iters = np.arange(250,300,2)
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
