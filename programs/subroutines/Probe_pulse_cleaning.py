prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5028, "TTL ProbeVert OFF")
    prg.add(-5023, "TTL ProbeHor OFF")
    prg.add(-4700, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(-4000, "AOM Probe Amp ch2 (-)", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probevert_amp')))
    prg.add(0, "TTL ProbeVert ON")
    prg.add(50, "TTL ProbeVert OFF")
    prg.add(2500, "AOM Probe Amp ch1 (+)", 0)
    prg.add(3000, "AOM Probe Amp ch2 (-)", 0)
    return prg
