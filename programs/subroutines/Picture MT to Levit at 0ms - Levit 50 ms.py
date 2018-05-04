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
    prg.add(1500, "DAC Magnetic Trap current", 9.5000)
    prg.add(2500, "IGBT BCompY field CLOSE")
    prg.add(5000, "BCompY current ramp", start_t=0, stop_x=10, n_points=50, start_x=0, stop_t=20)
    prg.add(486000, "AOM Probe Detuning", 0.000)
    prg.add(493000, "Config field OFF")
    prg.add(496500, "IGBT BCompY field OPEN")
    prg.add(497300, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(497500, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(497800, "TTL Repumper MOT  ON")
    prg.add(508200, "TTL Repumper MOT OFF")
    prg.add(508250, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(509200, "TTL Picture  ON")
    prg.add(509600, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(510000, "AOM Probe Amp ch2 (-)", 900)
    prg.add(511000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(511400, "AOM Probe Amp ch1 (+)", 1)
    prg.add(511800, "TTL Picture OFF")
    prg.add(1259800, "Shutter Probe OFF")
    prg.add(1518700, "TTL Picture  ON")
    prg.add(1519100, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(1519500, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(1520500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1520900, "AOM Probe Amp ch1 (+)", 1)
    prg.add(1521300, "TTL Picture OFF")
    prg.add(1529300, "TTL Repumper MOT OFF")
    prg.add(2518800, "TTL Picture  ON")
    prg.add(2521600, "TTL Picture OFF")
    prg.add(3519600, "TTL Picture  ON")
    prg.add(3522400, "TTL Picture OFF")
    prg.add(3523000, "IGBT BCompY field OPEN")
    return prg
