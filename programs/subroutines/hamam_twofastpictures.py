prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-8000, "TTL Picture Hamamatsu OFF")
    prg.add(-4000, "TTL ProbeHor OFF")
    prg.add(-3990, "TTL ProbeVert OFF")
    prg.add(-3500, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(-3000, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(0, "TTL ProbeVert ON")
    prg.add(50, "TTL ProbeVert OFF")
    prg.add(6150, "TTL ProbeVert ON")
    prg.add(6200, "TTL ProbeVert OFF")
    prg.add(7000, "TTL Picture Hamamatsu OFF")
    prg.add(8300, "AOM Probe Amp ch1 (+)", 0)
    prg.add(8800, "AOM Probe Amp ch2 (-)", 0)
    return prg
