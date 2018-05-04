prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "All shutter close")
    prg.add(1000, "AOM 2DMOT Amp ch1 (+)", 1)
    prg.add(3500, "AOM 2DMOT Amp ch2 (-)", 1)
    prg.add(6000, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(8500, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(11000, "AOM Push Amp ch1 (+)", 1)
    prg.add(13500, "AOM Push Amp ch2 (-)", 1)
    prg.add(16000, "AOM Zeeman Slower Amp", 1)
    prg.add(18500, "TTL Repumper MOT OFF")
    prg.add(21000, "TTL Dark spot OFF")
    prg.add(21000, "3D MOT Coils", 0.0000)
    return prg
