prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL2")
    prg.add(1000, "3DMOT on")
    prg.add(201000, "3DMOT off")
    prg.add(301000, "Picture Na")
    return prg
