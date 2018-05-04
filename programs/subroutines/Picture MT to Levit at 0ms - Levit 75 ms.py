prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2505000, "Shutter RepumperMOT ON")
    prg.add(-2290000, "AOM Repumper Amp", 1000)
    prg.add(-2280000, "AOM Repumper freq", 225.00)
    prg.add(-2272500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-2270000, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-2263000, "Shutter Probe ON")
    prg.add(0, "Config field gradient to levit")
    prg.add(1500, "DAC Magnetic Trap current", 9.5000)
    prg.add(750000, "Config field OFF")
    prg.add(757000, "AOM Probe Detuning", 0.000)
    prg.add(757800, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(758000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(758300, "TTL Repumper MOT  ON")
    prg.add(758700, "TTL Repumper MOT OFF", enable=False)
    prg.add(758750, "AOM DS + RepumperMOT Amp ", 1, enable=False)
    prg.add(759700, "TTL Picture  ON")
    prg.add(760100, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(760500, "AOM Probe Amp ch2 (-)", 600)
    prg.add(761500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(761900, "AOM Probe Amp ch1 (+)", 1)
    prg.add(762300, "TTL Picture OFF")
    prg.add(1510300, "Shutter Probe OFF")
    prg.add(1769200, "TTL Picture  ON")
    prg.add(1769600, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(1770000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(1771000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1771400, "AOM Probe Amp ch1 (+)", 1)
    prg.add(1771800, "TTL Picture OFF")
    prg.add(1779800, "TTL Repumper MOT OFF")
    prg.add(2769300, "TTL Picture  ON")
    prg.add(2772100, "TTL Picture OFF")
    prg.add(3770100, "TTL Picture  ON")
    prg.add(3772900, "TTL Picture OFF")
    return prg
