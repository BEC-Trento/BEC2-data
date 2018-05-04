prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(3500000, "Set MOT")
    prg.add(10000500, "TTL Dark spot OFF")
    return prg
