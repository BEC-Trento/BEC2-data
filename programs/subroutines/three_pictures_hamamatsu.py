prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3100, "AOM Probe Detuning", -2.000)
    prg.add(-1000, "TTL Picture Hamamatsu  ON", 'atoms')
    prg.add(-250, "imaging_repump")
    prg.add(0, "Probe_pulse_Hamam")
    prg.add(149000, "TTL Picture Hamamatsu  ON", 'probe')
    prg.add(149750, "imaging_repump")
    prg.add(150000, "Probe_pulse_Hamam")
    prg.add(299000, "TTL Picture Hamamatsu  ON", 'back')
    prg.add(302100, "TTL Picture Hamamatsu OFF")
    return prg
