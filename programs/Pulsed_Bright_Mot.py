prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Set Bright MOT")
    prg.add(20000000, "TTL Repumper MOT OFF")
    return prg
