prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Shutter RepumperMOT ON")
    prg.add(-2290000, "AOM Repumper Amp", 1000)
    prg.add(-2280000, "AOM Repumper freq", 225.00)
    prg.add(-2272500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-2270000, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-2263000, "Shutter Probe ON")
    prg.add(-100000, "Relay BCompZ Normal")
    prg.add(0, "Config field gradient to levit", enable=False)
    prg.add(0, "Config Field Unif to Levit")
    prg.add(500, "Oscilloscope Trigger ON")
    prg.add(1500, "DAC Magnetic Trap current", 9.5000)
    prg.add(2000, "IGBT BCompY field CLOSE")
    prg.add(2500, "BCompY current ramp", start_t=0, stop_x=10, n_points=10, start_x=0, stop_t=10)
    prg.add(10000, "IGBT Bcompz field OPEN")
    prg.add(20000, "IGBT BCompz field CLOSE")
    prg.add(20099, "IGBT BComp1 field CLOSE")
    prg.add(20200, "IGBT BComp2 field CLOSE")
    prg.add(21000, "Compensate_external_Mag_Field", enable=False)
    prg.add(21000, "DAC BComp1", 0.2600)
    prg.add(21500, "DAC BComp2", 0.2500)
    prg.add(22000, "DAC BCompZ", 0.2800)
    prg.add(22500, "DAC BCompY", 10.0000)
    prg.add(200000, "Config field OFF")
    prg.add(202000, "AOM DS + RepumperMOT Freq", 408.00, enable=False)
    prg.add(207000, "AOM Probe Detuning", 0.000)
    prg.add(207800, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(208300, "TTL Repumper MOT  ON")
    prg.add(208700, "TTL Repumper MOT OFF", enable=False)
    prg.add(208750, "AOM DS + RepumperMOT Amp ", 1, enable=False)
    prg.add(209700, "TTL Picture  ON")
    prg.add(210000, "Oscilloscope Trigger OFF")
    prg.add(210100, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(210500, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(211500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(211900, "AOM Probe Amp ch1 (+)", 1)
    prg.add(212300, "TTL Picture OFF")
    prg.add(960300, "Shutter Probe OFF")
    prg.add(1219200, "TTL Picture  ON")
    prg.add(1219600, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(1220000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(1221000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1221400, "AOM Probe Amp ch1 (+)", 1)
    prg.add(1221800, "TTL Picture OFF")
    prg.add(1229800, "TTL Repumper MOT OFF")
    prg.add(2219300, "TTL Picture  ON")
    prg.add(2222100, "TTL Picture OFF")
    prg.add(3220100, "TTL Picture  ON")
    prg.add(3222900, "TTL Picture OFF")
    prg.add(3230000, "DAC BCompY", 0.0000)
    return prg
