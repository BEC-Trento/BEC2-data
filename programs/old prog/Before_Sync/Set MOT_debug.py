prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-3000000, "Shutter Gray Molasses OFF")
    prg.add(0, "AOM Zeeman Slower Amp", 1000)
    prg.add(500, "TTL Repumper MOT OFF", enable=False)
    prg.add(500, "TTL Repumper MOT  ON")
    prg.add(9000, "AOM Zeeman Slower freq", 170.00)
    prg.add(12000, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(15000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(21000, "AOM 2DMOT Amp ch1 (+)", 1000)
    prg.add(24000, "AOM 2DMOT Amp ch2 (-)", 1000)
    prg.add(27000, "AOM 2DMOT Detuning", -15.000)
    prg.add(30000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(33000, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(36000, "AOM 3DMOT Detuning", -13.000)
    prg.add(39000, "AOM Push Amp ch1 (+)", 400)
    prg.add(42000, "AOM Push Amp ch2 (-)", 400)
    prg.add(45000, "AOM Push Detuning", 12.000)
    prg.add(48000, "AOM Repumper Amp", 1000)
    prg.add(51000, "AOM DS + RepumperMOT Amp ", 450, enable=False)
    prg.add(51000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(54000, "AOM Repumper freq", 225.00)
    prg.add(57000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(60000, "TTL Dark Spot ON", enable=False)
    prg.add(60000, "TTL Dark spot OFF")
    prg.add(63000, "shutter MOT open", enable=False)
    prg.add(63000, "shutter Bright MOT open")
    prg.add(66000, "IGBT MOT field ON")
    prg.add(72000, "AOM GM Detuning", 40.000)
    prg.add(73000, "TTL GM Repumper ON")
    return prg
