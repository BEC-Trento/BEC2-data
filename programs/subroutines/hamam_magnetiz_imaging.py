prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-12000, "Probe_pulse_cleaning", functions=dict(time=lambda x: x + cmd.get_var('magn_tof')))
    prg.add(-5000, "AOM Probe Detuning", -1.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-230, "TTL uW 1 (100W) OFF")
    prg.add(-20, "TTL uW 2 OFF")
    prg.add(20, "magnTOF_imaging", functions=dict(time=lambda x: x + cmd.get_var('magn_tof')))
    prg.add(50, "Oscilloscope Trigger ON")
    prg.add(30000, "Switch Off Dipole", enable=False)
    prg.add(150000, "TTL Picture Hamamatsu  ON", 'PTAI_probe', functions=dict(time=lambda x: x + cmd.get_var('magn_tof')))
    prg.add(151000, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('magn_tof')))
    prg.add(200000, "TTL Picture Hamamatsu  ON", 'PTAI_back', functions=dict(time=lambda x: x + cmd.get_var('magn_tof')))
    prg.add(202000, "TTL Picture Hamamatsu OFF", functions=dict(time=lambda x: x + cmd.get_var('magn_tof')))
    prg.add(210000, "AOM Probe Detuning", 100.000, functions=dict(time=lambda x: x + cmd.get_var('magn_tof')))
    return prg
