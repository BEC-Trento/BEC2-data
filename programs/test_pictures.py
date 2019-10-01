prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(5999000, "Oscilloscope Trigger ON", enable=False)
    prg.add(6000000, "three-pictures_VarProbeDet_190625", enable=False)
    prg.add(6000000, "two_states_imaging")
    prg.add(10000000, "Shutter Probe Hor OFF")
    prg.add(11000000, "Oscilloscope Trigger OFF", enable=False)
    return prg
