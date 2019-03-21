prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "Oscilloscope Trigger ON")
    prg.add(2000000, "Oscilloscope Trigger OFF")
    prg.add(10000000, "Oscilloscope Trigger OFF")
    return prg
