prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-10000, "TTL Picture Hamamatsu  ON", 'PTAI_p1')
    prg.add(-400, "Oscilloscope Trigger ON", enable=False)
    prg.add(-100, "transfer_m1to0", enable=False)
    prg.add(-100, "transfer_p1to0", enable=False)
    prg.add(-100, "transfer_0to0", enable=False)
    prg.add(0, "hamam_twofastpictures")
    prg.add(5000, "TTL Picture Hamamatsu  ON", 'PTAI_m1')
    prg.add(6050, "transfer_m1to0")
    prg.add(6050, "transfer_p1to0", enable=False)
    prg.add(9000, "Oscilloscope Trigger OFF", enable=False)
    return prg
