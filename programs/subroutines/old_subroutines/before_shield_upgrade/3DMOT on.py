prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL2")
    prg.add(1000, "All shutter open")
    prg.add(2000, "Shutter Probe OFF")
    prg.add(3000, "AOM 2DMOT Amp ch1 (+)", 1000)
    prg.add(5500, "AOM 2DMOT Amp ch2 (-)", 1000)
    prg.add(8000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(10500, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(11000, "AOM Repumper Amp", 1000)
    prg.add(12000, "AOM Repumper freq", 225.00)
    prg.add(12500, "AOM DS + RepumperMOT Freq", 406.00)
    prg.add(13000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(14000, "TTL Repumper MOT OFF")
    prg.add(15000, "TTL Dark Spot ON")
    prg.add(22300, "AOM Push Amp ch1 (+)", 1000)
    prg.add(24800, "AOM Push Amp ch2 (-)", 1000)
    prg.add(29800, "AOM Zeeman Slower Amp", 1000)
    prg.add(32300, "Shutter RepumperMOT OFF")
    prg.add(33300, "3D MOT Coils", 8.0000)
    return prg
