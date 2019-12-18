prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-4500, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-400, "Oscilloscope Trigger ON", enable=False)
    prg.add(-5, "transfer_p1p2_2")
    prg.add(0, "Probe_pulse_Hamam")
    prg.add(30200, "Oscilloscope Trigger OFF")
    prg.add(34995, "transfer_m1m2_2")
    prg.add(35000, "Probe_pulse_Hamam")
    prg.add(44000, "wait")
    prg.add(100000, "Probe_pulse_Hamam", enable=False)
    prg.add(150000, "TTL Picture Hamamatsu  ON", enable=False)
    prg.add(152000, "TTL Picture Hamamatsu OFF", enable=False)
    return prg
