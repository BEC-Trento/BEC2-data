prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-3040000, "AOM Repumper Amp", 1000)
    prg.add(-3030000, "AOM Repumper freq", 225.00)
    prg.add(-3025000, "Shutter RepumperMOT ON")
    prg.add(-3022500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-3020000, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-3013000, "Shutter Probe ON")
    prg.add(-4000, "IGBT BCompY field CLOSE")
    prg.add(-3500, "DAC BCompY", 0.5000)
    prg.add(-3000, "AOM Probe Detuning", 0.000)
    prg.add(-2200, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-2000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(-1700, "TTL Repumper MOT  ON")
    prg.add(-1300, "TTL Repumper MOT OFF", enable=False)
    prg.add(-1250, "AOM DS + RepumperMOT Amp ", 1, enable=False)
    prg.add(-300, "TTL Picture  ON")
    prg.add(100, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(500, "AOM Probe Amp ch2 (-)", 600)
    prg.add(1500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1900, "AOM Probe Amp ch1 (+)", 1)
    prg.add(2300, "TTL Picture OFF")
    prg.add(750300, "Shutter Probe OFF")
    prg.add(1009200, "TTL Picture  ON")
    prg.add(1009600, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(1010000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(1011000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1011400, "AOM Probe Amp ch1 (+)", 1)
    prg.add(1011800, "TTL Picture OFF")
    prg.add(1019800, "TTL Repumper MOT OFF")
    prg.add(2009300, "TTL Picture  ON")
    prg.add(2012100, "TTL Picture OFF")
    prg.add(3010100, "TTL Picture  ON")
    prg.add(3012900, "TTL Picture OFF")
    return prg
