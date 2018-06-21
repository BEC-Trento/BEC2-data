prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000000, "wait")
    prg.add(100011000, "Oscilloscope Trigger ON")
    prg.add(100011050, "TTL Test Trigger ON")
    prg.add(100211050, "Oscilloscope Trigger OFF")
    prg.add(100211150, "TTL Test Trigger OFF")
    return prg
