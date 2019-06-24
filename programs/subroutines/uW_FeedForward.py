prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-11000, "TTL uW 2 ON")
    prg.add(-3000, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det'), funct_enable=False))
    prg.add(-2300, "TTL Picture Hamamatsu  ON")
    prg.add(-1000, "TTL uW 2 OFF")
    prg.add(0, "Probe_pulse")
    prg.add(5200, "TTL Picture Hamamatsu OFF")
    prg.add(995000, "TTL Picture Hamamatsu  ON")
    prg.add(1000000, "Probe_pulse")
    prg.add(1005000, "TTL Picture Hamamatsu OFF")
    prg.add(1989000, "TTL uW 2 ON")
    prg.add(1995000, "TTL Picture Hamamatsu  ON")
    prg.add(1999000, "TTL uW 2 OFF")
    prg.add(2000000, "Probe_pulse")
    prg.add(2005000, "TTL Picture Hamamatsu OFF")
    prg.add(2995000, "TTL Picture Hamamatsu  ON")
    prg.add(3000000, "Probe_pulse")
    prg.add(3005000, "TTL Picture Hamamatsu OFF")
    return prg
