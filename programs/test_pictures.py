prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "Shutter Probe Vert ON")
    prg.add(5989900, "Oscilloscope Trigger ON")
    prg.add(5990000, "TTL Picture Hamamatsu  ON", 'image0', enable=False)
    prg.add(6000000, "hamam_twofastpictures", enable=False)
    prg.add(6000000, "magnetization_imaging", enable=False)
    prg.add(6000000, "soliton_imaging")
    prg.add(6005000, "TTL Picture Hamamatsu  ON", 'image1', enable=False)
    prg.add(90005000, "Oscilloscope Trigger OFF")
    return prg
