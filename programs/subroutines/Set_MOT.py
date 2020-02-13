prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2500000, "TTL MirrorBottom MOT")
    prg.add(-2001000, "TTL Relay Upper Coil CLOSE")
    prg.add(-2000000, "TTL Relay Lower Coil CLOSE")
    prg.add(500, "AOM Zeeman Slower Amp", 1000)
    prg.add(1000, "TTL Repumper MOT OFF", enable=False)
    prg.add(1500, "DAC MT-MOT Voltage", 8.0000)
    prg.add(2000, "DAC MT-MOT Current", 30.0000, functions=dict(value=lambda x: cmd.get_var('mot_I'), funct_enable=False))
    prg.add(10000, "AOM Zeeman Slower freq", 170.00)
    prg.add(13000, "AOM Probe Amp ch1 (+)", 0)
    prg.add(14000, "AOM Probe Detuning", 100.000)
    prg.add(16000, "AOM Probe Amp ch2 (-)", 0)
    prg.add(22000, "AOM 2DMOT Amp ch1 (+)", 1000)
    prg.add(25000, "AOM 2DMOT Amp ch2 (-)", 1000)
    prg.add(28000, "AOM 2DMOT Detuning", -13.000)
    prg.add(31000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(34000, "AOM 3DMOT Amp ch2 (-)", 650, functions=dict(amplitude=lambda x: cmd.get_var('mot_amplitude')))
    prg.add(37000, "AOM 3DMOT Detuning", -18.000, functions=dict(frequency=lambda x: cmd.get_var('mot_detuning')))
    prg.add(40000, "AOM Push Amp ch1 (+)", 175)
    prg.add(40500, "AOM Push Amp ch2 (-)", 150, functions=dict(amplitude=lambda x: cmd.get_var('push_amplitude')))
    prg.add(41000, "AOM Push Detuning", 12.000)
    prg.add(41500, "AOM GM Amp ch1 (+)", 0)
    prg.add(42000, "AOM GM Amp ch2 (-)", 0)
    prg.add(42500, "AOM GM Detuning", 40.000)
    prg.add(49000, "AOM Repumper Amp", 1000)
    prg.add(52000, "AOM DS + RepumperMOT Amp ", 500, enable=False)
    prg.add(52000, "AOM DS + RepumperMOT Amp ", 600, functions=dict(amplitude=lambda x: cmd.get_var('ds_amplitude')))
    prg.add(55000, "AOM Repumper freq", 225.00)
    prg.add(58000, "AOM DS + RepumperMOT Freq", 406.00)
    prg.add(60000, "All uW OFF")
    prg.add(61000, "TTL Dark Spot ON")
    prg.add(61500, "TTL Repumper MOT OFF")
    prg.add(61500, "TTL Repumper MOT  ON", enable=False)
    prg.add(61800, "DAC SRS", -9.0000)
    prg.add(62000, "phase imprint OFF")
    prg.add(64000, "shutter MOT open")
    prg.add(67000, "Config Field MT-MOT")
    prg.add(67800, "IGBT BCompZfine OPEN")
    prg.add(68000, "TTL GM Repumper OFF")
    prg.add(69000, "Set_BComp")
    return prg
