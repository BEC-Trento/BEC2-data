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
    prg.add(135081000, "Bright_Compressed_MOT", enable=False)
    prg.add(135089000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135089000, "switch off MOT fast")
    prg.add(135091849, "GM BrokenRamp_Short")
    prg.add(135141849, "Config Field MT")
    prg.add(135141849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135141849, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(135341849, "Evaporation Ramp.sub")
    prg.add(235341849, "[VOID] End Evaporation")
    prg.add(235342849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(235344349, "MT_FastTransfer_to_Dipole10A")
    prg.add(235344349, "MT_Piecewise_Transfer_to_Dipole10A", enable=False)
    prg.add(239344349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V", enable=False)
    prg.add(239344349, "Horizontal Dipole Evaporation Ramp variable")
    prg.add(261344349, "[VOID] End Evaporation")
    prg.add(261345000, "IGBT BCompY field CLOSE", enable=False)
    prg.add(261345500, "BCompY current ramp", start_t=0, stop_x=10, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(261395500, "MT Current Ramp", start_t=0, stop_x=0, n_points=15, start_x=3.5, stop_t=5, enable=False)
    prg.add(261497500, "Config field OFF")
    prg.add(261547500, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(261547500, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(261547500, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(261547500, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(261547500, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(261547500, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(261550500, "DAC BCompZ", 0.2400)
    prg.add(261551000, "Swich Off Dipole")
    prg.add(261771000, "Picture Na_Shortrepumper_offset")
    prg.add(261771000, "Picture Na_2Gdet_offset", enable=False)
    prg.add(261771000, "Picture Na_1Gdet_offset", enable=False)
    prg.add(261771000, "Picture Na_offset", enable=False)
    prg.add(261771000, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(261771000, "Picture Na_3Gdet_offset", enable=False)
    prg.add(261771000, "Picture Na_4Gdet_offset", enable=False)
    prg.add(266771000, "Initialize_Dipole_Off")
    prg.add(266776000, "Set MOT")
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
