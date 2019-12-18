prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5900, "TTL ProbeHor OFF")
    prg.add(-5800, "TTL ProbeVert OFF")
    prg.add(-4700, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(-4200, "AOM Probe Amp ch2 (-)", 120, functions=dict(amplitude=lambda x: cmd.get_var('probevert_amp'), funct_enable=False))
    prg.add(0, "TTL ProbeHor ON")
    prg.add(0, "TTL ProbeVert ON", enable=False)
    prg.add(20, "TTL ProbeHor OFF")
    prg.add(50, "TTL ProbeVert OFF", enable=False)
    prg.add(10000, "AOM Probe Amp ch1 (+)", 0)
    prg.add(10500, "AOM Probe Amp ch2 (-)", 0)
    return prg
