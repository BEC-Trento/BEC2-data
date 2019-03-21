prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(1000000, "Oscilloscope Trigger ON")
    prg.add(6000000, "Picture_Mirror_Na_resonant_hamamatsu")
    prg.add(10000000, "Shutter Probe Hor OFF")
    prg.add(11000000, "Oscilloscope Trigger OFF")
    return prg
