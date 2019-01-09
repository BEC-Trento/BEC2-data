prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135062100, "Oscilloscope Trigger ON")
    prg.add(135063200, "GM_051018")
    prg.add(135110700, "Oscilloscope Trigger OFF")
    prg.add(135310700, "wait")
    prg.add(135311900, "Picture Na_VariableDet_hamamatsu")
    prg.add(140311900, "Set_MOT")
    prg.add(140311900, "Set_BrightMOT", enable=False)
    return prg
