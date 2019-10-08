prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-3000, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-2000, "imaging_repump")
    prg.add(-2000, "transfer_m1to0", enable=False)
    prg.add(-2000, "transfer_0to0", enable=False)
    prg.add(-2000, "transfer_p1to0", enable=False)
    prg.add(-2000, "transfer_m1m2", enable=False)
    prg.add(-300, "TTL Picture  ON")
    prg.add(-100, "Oscilloscope Trigger ON", enable=False)
    prg.add(0, "Probe_pulse")
    prg.add(2300, "TTL Picture OFF")
    prg.add(15000, "Oscilloscope Trigger OFF")
    prg.add(1008100, "TTL Picture  ON")
    prg.add(1009600, "Probe_pulse")
    prg.add(1011800, "TTL Picture OFF")
    prg.add(2009199, "TTL Picture  ON")
    prg.add(2012100, "TTL Picture OFF")
    return prg
