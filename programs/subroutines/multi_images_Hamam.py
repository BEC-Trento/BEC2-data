prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Probe_pulse_Hamam")
    prg.add(35000, "two_states_imaging")
    prg.add(105000, "two_states_imaging")
    prg.add(140000, "two_states_imaging")
    prg.add(175000, "two_states_imaging")
    prg.add(210000, "TTL Picture Hamamatsu  ON")
    prg.add(212000, "TTL Picture Hamamatsu OFF")
    return prg
