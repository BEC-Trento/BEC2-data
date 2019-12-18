prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(500, "Config field OFF")
    prg.add(5000, "Initialize 0 TTL1", enable=False)
    prg.add(5100, "Initialize 0 TTL2", enable=False)
    prg.add(5500, "Initialize 0 TTL3", enable=False)
    prg.add(11200, "Config field OFF")
    prg.add(13700, "Initialize_Dipole_Off")
    prg.add(20000, "Synchronize.sub")
    return prg
