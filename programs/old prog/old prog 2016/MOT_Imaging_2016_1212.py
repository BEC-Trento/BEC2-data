prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL2")
    prg.add(5000, "Set MOT")
    prg.add(130005000, "3D MOT Coils", 0.0000)
    prg.add(131005000, "MOT Lights off")
    prg.add(131105000, "Picture Na")
    prg.add(231105000, "Set MOT")
    return prg
