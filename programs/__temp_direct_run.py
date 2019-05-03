prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135050150, "Oscilloscope Trigger ON")
    prg.add(135060000, "Switch Off MOT", enable=False)
    prg.add(135060000, "Switch Off MOT_fast")
    prg.add(135061250, "GM_051018")
    prg.add(135111250, "Oscilloscope Trigger OFF")
    prg.add(135111480, "Picture_Na_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(140111480, "Set_MOT")
    prg.add(140111480, "Set_BrightMOT", enable=False)
    return prg
