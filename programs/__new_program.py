prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Shutter Probe Vert ON")
    prg.add(101000, "Shutter Probe Hor ON")
    prg.add(5101000, "Oscilloscope Trigger ON")
    prg.add(5101100, "Probe_pulse")
    prg.add(10106100, "Oscilloscope Trigger OFF")
    prg.add(10218600, "test_pictures")
    return prg
