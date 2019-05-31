prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(0, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(1000, "AOM Probe Amp ch1 (+)", 1)
    return prg
