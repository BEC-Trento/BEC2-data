prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "BEC_2019-06-25")
    prg.add(195251000, "wait")
    prg.add(195252250, "Hybrid_to_Xigar_transfer")
    prg.add(205352250, "wait")
    prg.add(205353250, "Oscilloscope Trigger ON")
    prg.add(205354250, "DAC BGradX", 0.0000)
    prg.add(205454250, "IGBT BGradX CLOSE")
    prg.add(205455250, "DAC BGradX", 5.0000)
    prg.add(205955250, "IGBT BGradX OPEN")
    prg.add(205956250, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(205957250, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(205957290, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(205957290, "multi_images_Hamam", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(211457290, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(211957290, "fake_levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(226957290, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof') +cmd.get_var('hold_time')))
    prg.add(226958290, "AOM IR Horizontal Amp", 1000)
    prg.add(226958290, "Set_BrightMOT", enable=False)
    return prg
