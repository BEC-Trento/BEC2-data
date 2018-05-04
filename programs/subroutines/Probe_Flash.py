prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-3000000, "Shutter Probe ON")
    prg.add(-2999000, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-2998000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-1000, "AOM Probe Detuning", 0.000)
    prg.add(-500, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(0, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(40000, "AOM Probe Amp ch2 (-)", 1)
    prg.add(40500, "AOM Probe Amp ch1 (+)", 1)
    return prg
