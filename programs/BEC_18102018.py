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
    prg.add(135079400, "DAC MT-MOT Voltage", 7.5000)
    prg.add(135082500, "GM_051018")
    prg.add(135132500, "wait")
    prg.add(135133500, "Config Field MT-MOT")
    prg.add(135135500, "DAC Horiz IR", 3.8000)
    prg.add(135136500, "AOM IR Horizontal freq", 80.00)
    prg.add(135137500, "AOM IR Horizontal Amp", 1000)
    prg.add(195137500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(199137500, "Horizontal Dipole Evaporation Ramp 10_2018", enable=False)
    prg.add(199137500, "Horizontal Dipole Evaporation Ramp_3.5V_11_2018")
    prg.add(231637500, "[VOID] End Evaporation")
    prg.add(251637500, "Config field OFF")
    prg.add(251639100, "Swich Off Dipole")
    prg.add(251640330, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(251640330, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(251640330, "Picture Na_resonant_hamamatsu")
    prg.add(251640330, "Picture Na_2Gdet", enable=False)
    prg.add(251640330, "Picture Na_1Gdet", enable=False)
    prg.add(251640330, "Picture Na_0Gdet", enable=False)
    prg.add(256640330, "Set_MOT")
    prg.add(256640330, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 15, 2)
    j = 0
    while(cmd.running):
        TOF1 = iters[j]
        cmd.set_var('TOF', TOF1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nTOF = %g\n'%(j+1, len(iters), TOF1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
