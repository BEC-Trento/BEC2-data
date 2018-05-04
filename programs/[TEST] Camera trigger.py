prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(10000, "Shutter Probe ON")
    prg.add(50000, "TTL Picture  ON")
    prg.add(52500, "TTL Picture OFF")
    prg.add(60000, "wait")
    return prg
