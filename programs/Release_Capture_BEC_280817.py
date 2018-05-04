prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 8.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.0000)
    prg.add(5181000, "DAC Horiz IR", 3.0000)
    prg.add(5181500, "AOM IR Horizontal freq", 80.00)
    prg.add(135081000, "Bright_Compressed_MOT")
    prg.add(135089000, "switch off MOT _ Depumper ")
    prg.add(135091350, "GM BrokenRamp_Short")
    prg.add(135141350, "Config Field MT")
    prg.add(135341350, "MT_Compression", enable=False)
    prg.add(135341350, "MT_Compression_20A", enable=False)
    prg.add(140541350, "Evaporation Ramp.sub")
    prg.add(315541350, "[VOID] End Evaporation")
    prg.add(315541850, "MT_Transfer_to_Dipole", enable=False)
    prg.add(315541850, "MT20A_Transfer_to_Dipole", enable=False)
    prg.add(315546850, "MT_Transfer_to_Dipole10A", enable=False)
    prg.add(315546850, "MT_FastTransfer_to_Dipole10A", enable=False)
    prg.add(315546850, "MT_FastTransfer_to_Dipole8A")
    prg.add(316561850, "Horizontal Dipole Evaporation Ramp trials", enable=False)
    prg.add(316561850, "Horizontal Dipole Evaporation Ramp Dimple3V")
    prg.add(416562850, "Dipole_Turnoff_and_Recapture")
    prg.add(416564850, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    prg.add(416569850, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    prg.add(416769850, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x+ cmd.get_var('dt')))
    prg.add(416769850, "Picture Na_2Gdet_offset", enable=False)
    prg.add(416769850, "Picture Na_1Gdet_offset", enable=False)
    prg.add(416769850, "Picture Na_offset", enable=False)
    prg.add(416769850, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(416769850, "Picture Na_3Gdet_offset", enable=False)
    prg.add(416769850, "Picture Na_4Gdet_offset", enable=False)
    prg.add(420874449, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    prg.add(420879449, "Set MOT", functions=dict(time=lambda x: x + cmd.get_var('dt')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(10, 150, 10)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
