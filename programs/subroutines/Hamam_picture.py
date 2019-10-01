prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3020000, "Shutter Probe Vert ON")
    prg.add(-2600, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-2300, "TTL Picture Hamamatsu  ON")
    prg.add(0, "Probe_pulse")
    prg.add(1200, "TTL Picture Hamamatsu OFF")
    return prg
