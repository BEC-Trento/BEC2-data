prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-6000, "TTL ProbeVert OFF")
    prg.add(-5900, "TTL ProbeHor OFF")
    prg.add(-4700, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(-4200, "AOM Probe Amp ch2 (-)", 1000, functions=dict(amplitude=lambda x: cmd.get_var('amp'), funct_enable=False))
    prg.add(-3230, "TTL Picture Hamamatsu  ON")
    prg.add(0, "TTL ProbeVert ON")
    prg.add(50, "TTL ProbeVert OFF")
    prg.add(2000, "TTL Picture Hamamatsu OFF")
    prg.add(2500, "AOM Probe Amp ch1 (+)", 0)
    prg.add(3000, "AOM Probe Amp ch2 (-)", 0)
    return prg
