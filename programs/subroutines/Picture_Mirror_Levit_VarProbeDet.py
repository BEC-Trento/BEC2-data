prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4354000, "AOM Repumper Amp", 1000, enable=False)
    prg.add(-4350000, "AOM Repumper freq", 225.00, enable=False)
    prg.add(-3511500, "AOM Probe Amp ch2 (-)", 0)
    prg.add(-3501500, "AOM Probe Amp ch1 (+)", 0)
    prg.add(-3250000, "TTL MirrorBottom Probe", enable=False)
    prg.add(-3013000, "Shutter Probe Hor ON", enable=False)
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-3010000, "Shutter RepumperMOT ON", enable=False)
    prg.add(-102100, "DAC BCompY", 0.1000, enable=False)
    prg.add(-99100, "IGBT BCompY CLOSE", enable=False)
    prg.add(-11500, "Config field OFF")
    prg.add(-5000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-3000, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-2300, "TTL Picture Hamamatsu  ON")
    prg.add(-2000, "AOM DS + RepumperMOT Freq", 408.00, enable=False)
    prg.add(-500, "TTL Repumper MOT  ON")
    prg.add(-300, "TTL Picture  ON")
    prg.add(-100, "TTL Repumper MOT OFF")
    prg.add(-100, "Oscilloscope Trigger ON", enable=False)
    prg.add(0, "Probe_pulse")
    prg.add(0, "Probe_pulse_1ms", enable=False)
    prg.add(1200, "Oscilloscope Trigger ON", enable=False)
    prg.add(2300, "TTL Picture OFF")
    prg.add(3000, "Oscilloscope Trigger OFF", enable=False)
    prg.add(3500, "AOM DS + RepumperMOT Amp ", 0)
    prg.add(5200, "TTL Picture Hamamatsu OFF")
    prg.add(11230, "Oscilloscope Trigger OFF", enable=False)
    prg.add(1007900, "TTL Repumper MOT  ON")
    prg.add(1008100, "TTL Picture  ON")
    prg.add(1008199, "TTL Picture Hamamatsu  ON")
    prg.add(1008300, "TTL Repumper MOT OFF")
    prg.add(1009600, "AOM Probe Amp ch1 (+)", 1000, enable=False)
    prg.add(1009600, "Probe_pulse")
    prg.add(1009600, "Probe_pulse_1ms", enable=False)
    prg.add(1011800, "TTL Picture OFF")
    prg.add(1018800, "TTL Picture Hamamatsu OFF")
    prg.add(1019800, "TTL Repumper MOT OFF")
    prg.add(1690000, "Probe_pulse", enable=False)
    prg.add(2009000, "TTL Repumper MOT  ON")
    prg.add(2009199, "TTL Picture  ON")
    prg.add(2009300, "TTL Picture Hamamatsu  ON")
    prg.add(2009400, "TTL Repumper MOT OFF")
    prg.add(2012100, "TTL Picture OFF")
    prg.add(2020100, "TTL Picture Hamamatsu OFF")
    prg.add(3010000, "TTL Picture  ON", enable=False)
    prg.add(3010100, "TTL Picture Hamamatsu  ON", enable=False)
    prg.add(3012900, "TTL Picture OFF", enable=False)
    prg.add(3020899, "TTL Picture Hamamatsu OFF", enable=False)
    prg.add(3030000, "IGBT BcompY OPEN")
    prg.add(3031000, "DAC BCompY", 0.0000)
    prg.add(4000000, "TTL Picture Hamamatsu  ON", enable=False)
    prg.add(4010000, "TTL Picture Hamamatsu OFF", enable=False)
    return prg
