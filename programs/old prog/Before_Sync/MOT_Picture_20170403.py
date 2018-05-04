prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "MOT Lights off")
    prg.add(10000000, "Set MOT")
    prg.add(10000000, "Set MOT_debug", enable=False)
    prg.add(10160000, "Set Bright MOT", enable=False)
    prg.add(90000000, "switch off MOT ")
    prg.add(90010000, "Picture Na")
    prg.add(90010000, "Picture Na Debug", enable=False)
    prg.add(100010000, "Set MOT")
    prg.add(100010000, "Set MOT_debug", enable=False)
    prg.add(100010000, "Set Bright MOT", enable=False)
    return prg
