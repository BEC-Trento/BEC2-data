prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135110000, "Picture Na_4Gdet", enable=False)
    prg.add(135110000, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(135110000, "Picture Na_3Gdet_hamamatsu")
    prg.add(135110000, "Picture Na_2Gdet", enable=False)
    prg.add(135110000, "Picture Na_1Gdet", enable=False)
    prg.add(135110000, "Picture Na_0Gdet", enable=False)
    prg.add(140110000, "Set_MOT")
    prg.add(140110000, "Set_BrightMOT", enable=False)
    return prg
