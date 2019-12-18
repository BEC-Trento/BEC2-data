prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(0, "Probe_pulse_cleaning")
    prg.add(50000, "TTL Picture Hamamatsu  ON", 'phaseimp_probe')
    prg.add(53000, "Probe_pulse_Hamam")
    prg.add(133000, "TTL Picture Hamamatsu  ON", 'phaseimp_position')
    prg.add(136000, "Probe_pulse_Hamam")
    return prg
