prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT")
    prg.add(135078900, "DAC MT-MOT Current", 55.0000)
    prg.add(135079400, "DAC MT-MOT Voltage", 4.0000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133500, "Config Field MT-MOT")
    prg.add(135135500, "DAC Horiz IR", 5.4000)
    prg.add(135136500, "AOM IR Horizontal freq", 80.00)
    prg.add(135137500, "AOM IR Horizontal Amp", 1000)
    prg.add(235137500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(239137500, "Horizontal Dipole Evaporation Ramp 10_2018")
    prg.add(271637500, "[VOID] End Evaporation")
    prg.add(271737500, "Relay BCompZ Invert")
    prg.add(271937500, "IGBT BCompz CLOSE")
    prg.add(271947500, "DAC BCompZ", 0.1000)
    prg.add(272447500, "MT_to_Hor_Dipole_Cigar_Transfer_102018")
    prg.add(292508000, "Synchronize.sub")
    prg.add(292808000, "uW ON")
    prg.add(292808000, "uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(292808500, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(292809000, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018", enable=False)
    prg.add(292809000, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(292810600, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(292811109, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(293011109, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(293011109, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(293011109, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(293011109, "Picture Na_uW_Probe_hamamatsu", enable=False)
    prg.add(293011109, "Picture Na_2Gdet", enable=False)
    prg.add(293011109, "Picture Na_1Gdet", enable=False)
    prg.add(293011109, "Picture Na_0Gdet", enable=False)
    prg.add(298011109, "Set_MOT")
    prg.add(298011109, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.1, 10, 1)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
