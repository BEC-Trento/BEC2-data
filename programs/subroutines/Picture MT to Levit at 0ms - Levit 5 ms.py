prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2805000, "Shutter RepumperMOT ON")
    prg.add(-2290000, "AOM Repumper Amp", 1000)
    prg.add(-2280000, "AOM Repumper freq", 225.00)
    prg.add(-2272500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-2270000, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-2263000, "Shutter Probe ON")
    prg.add(0, "Config field gradient to levit")
    prg.add(1500, "DAC Magnetic Trap current", 9.2000)
    prg.add(50000, "Config field OFF")
    prg.add(57000, "AOM Probe Detuning", 0.000)
    prg.add(57800, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(58000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(58300, "TTL Repumper MOT  ON")
    prg.add(58700, "TTL Repumper MOT OFF")
    prg.add(58750, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(59700, "TTL Picture  ON")
    prg.add(60100, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(60500, "AOM Probe Amp ch2 (-)", 600)
    prg.add(61500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(61900, "AOM Probe Amp ch1 (+)", 1)
    prg.add(62300, "TTL Picture OFF")
    prg.add(810300, "Shutter Probe OFF")
    prg.add(1069200, "TTL Picture  ON")
    prg.add(1069600, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(1070000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(1071000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1071400, "AOM Probe Amp ch1 (+)", 1)
    prg.add(1071800, "TTL Picture OFF")
    prg.add(1079800, "TTL Repumper MOT OFF")
    prg.add(2069300, "TTL Picture  ON")
    prg.add(2072100, "TTL Picture OFF")
    prg.add(3070100, "TTL Picture  ON")
    prg.add(3072900, "TTL Picture OFF")
    return prg
