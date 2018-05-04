prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(1000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "TTL Test Trigger ON")
    prg.add(50005, "TTL 1 ch2 ON")
    return prg
