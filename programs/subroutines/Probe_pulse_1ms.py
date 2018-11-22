prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-500, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(0, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(9500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(10000, "AOM Probe Amp ch1 (+)", 1)
    return prg
