prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "MOT Lights off")
    prg.add(50049999, "Set MOT")
    prg.add(50049999, "Set Bright MOT", enable=False)
    prg.add(130049999, "switch off MOT ")
    prg.add(130051999, "GM pulse 05ms", enable=False)
    prg.add(130061999, "Picture Na")
    prg.add(130201999, "Picture Na Vert", enable=False)
    prg.add(151130599, "Set Bright MOT", enable=False)
    prg.add(151137559, "Set MOT")
    return prg
