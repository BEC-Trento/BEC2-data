prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2805000, "Shutter RepumperMOT ON")
    prg.add(-2290000, "AOM Repumper Amp", 1000)
    prg.add(-2280000, "AOM Repumper freq", 225.00)
    prg.add(-2272500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-2270000, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-2263000, "Shutter Probe ON")
    prg.add(-1000, "DAC BCompZ", 2.0000, enable=False)
    prg.add(0, "Config field OFF")
    prg.add(2000, "DAC 3DMOT Coils Current", 9.0000)
    prg.add(2500, "Config Field Levitation")
    prg.add(300000, "Config field OFF")
    prg.add(307000, "AOM Probe Detuning", 0.000)
    prg.add(307800, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(308000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(308300, "TTL Repumper MOT  ON")
    prg.add(308700, "TTL Repumper MOT OFF", enable=False)
    prg.add(308750, "AOM DS + RepumperMOT Amp ", 1, enable=False)
    prg.add(309700, "TTL Picture  ON")
    prg.add(310100, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(310500, "AOM Probe Amp ch2 (-)", 600)
    prg.add(311500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(311900, "AOM Probe Amp ch1 (+)", 1)
    prg.add(312300, "TTL Picture OFF")
    prg.add(1060300, "Shutter Probe OFF")
    prg.add(1319200, "TTL Picture  ON")
    prg.add(1319600, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(1320000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(1321000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1321400, "AOM Probe Amp ch1 (+)", 1)
    prg.add(1321800, "TTL Picture OFF")
    prg.add(1329800, "TTL Repumper MOT OFF")
    prg.add(2319300, "TTL Picture  ON")
    prg.add(2322100, "TTL Picture OFF")
    prg.add(3320100, "TTL Picture  ON")
    prg.add(3322900, "TTL Picture OFF")
    return prg