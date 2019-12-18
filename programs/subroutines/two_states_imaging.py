prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-4500, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-3000, "TTL Picture Hamamatsu  ON", 'PTAI_p1')
    prg.add(-400, "Oscilloscope Trigger ON")
    prg.add(-100, "transfer_m1to0", enable=False)
    prg.add(-100, "transfer_p1to0")
    prg.add(0, "Probe_pulse_Hamam")
    prg.add(30200, "Oscilloscope Trigger OFF")
    prg.add(32000, "TTL Picture Hamamatsu  ON", 'PTAI_m1')
    prg.add(34990, "transfer_p1to0", enable=False)
    prg.add(34990, "transfer_m1to0")
    prg.add(35000, "Probe_pulse_Hamam")
    prg.add(44000, "wait")
    prg.add(34990000, "transfer_p1to0")
    return prg
