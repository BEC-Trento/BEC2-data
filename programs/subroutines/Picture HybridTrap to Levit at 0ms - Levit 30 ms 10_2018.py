prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2805000, "Shutter RepumperMOT ON")
    prg.add(-2290000, "AOM Repumper Amp", 1000)
    prg.add(-2280000, "AOM Repumper freq", 225.00)
    prg.add(-2272500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-2270000, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-2264000, "Shutter Probe Hor ON")
    prg.add(-2263000, "Shutter Probe Vert ON")
    prg.add(0, "Config field gradient to levit", enable=False)
    prg.add(0, "Config field MT-MOT to Levit")
    prg.add(1500, "DAC MT-MOT Current", 42.0000)
    prg.add(100000, "DAC BCompY", 0.1000)
    prg.add(102000, "IGBT BCompY CLOSE")
    prg.add(300000, "Config field OFF")
    prg.add(307000, "AOM Probe Detuning", 0.000)
    prg.add(307700, "TTL Picture Hamamatsu  ON")
    prg.add(308000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(308300, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(308600, "TTL Repumper MOT  ON")
    prg.add(309000, "TTL Repumper MOT OFF")
    prg.add(309050, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(310000, "TTL Picture  ON")
    prg.add(310200, "Oscilloscope Trigger ON", enable=False)
    prg.add(310300, "Probe_pulse")
    prg.add(311500, "Oscilloscope Trigger ON", enable=False)
    prg.add(312600, "TTL Picture OFF")
    prg.add(313300, "Oscilloscope Trigger OFF", enable=False)
    prg.add(315500, "TTL Picture Hamamatsu OFF")
    prg.add(321530, "Oscilloscope Trigger OFF")
    prg.add(1318400, "TTL Picture  ON")
    prg.add(1318500, "TTL Picture Hamamatsu  ON")
    prg.add(1319900, "Probe_pulse")
    prg.add(1322100, "TTL Picture OFF")
    prg.add(1329100, "TTL Picture Hamamatsu OFF")
    prg.add(1330100, "TTL Repumper MOT OFF")
    prg.add(2319500, "TTL Picture  ON")
    prg.add(2319600, "TTL Picture Hamamatsu  ON")
    prg.add(2322400, "TTL Picture OFF")
    prg.add(2330400, "TTL Picture Hamamatsu OFF")
    prg.add(3320300, "TTL Picture  ON")
    prg.add(3321300, "TTL Picture Hamamatsu  ON")
    prg.add(3324100, "TTL Picture OFF")
    prg.add(3332090, "TTL Picture Hamamatsu OFF")
    prg.add(3341191, "IGBT BcompY OPEN")
    prg.add(3342191, "DAC BCompY", 0.0000)
    return prg
