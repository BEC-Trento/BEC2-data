prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-8000, "TTL Picture Hamamatsu OFF")
    prg.add(-4000, "TTL ProbeHor OFF")
    prg.add(-3990, "TTL ProbeVert OFF")
    prg.add(-2060, "AOM Probe Amp ch1 (+)", 1000, functions=dict(amplitude=lambda x: cmd.get_var('amp'), funct_enable=False))
    prg.add(-1560, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(0, "TTL ProbeVert ON")
    prg.add(50, "TTL ProbeVert OFF")
    prg.add(500, "TTL ProbeHor ON")
    prg.add(600, "TTL ProbeHor OFF")
    prg.add(700, "AOM Probe Amp ch1 (+)", 0)
    prg.add(1100, "AOM Probe Amp ch2 (-)", 0)
    return prg
