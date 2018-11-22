prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM 2DMOT Amp ch1 (+)", 1)
    prg.add(2500, "AOM 2DMOT Amp ch2 (-)", 1)
    prg.add(5000, "AOM 3DMOT Amp ch1 (+)", 1)
    prg.add(7500, "AOM 3DMOT Amp ch2 (-)", 1)
    prg.add(10000, "AOM Push Amp ch1 (+)", 1)
    prg.add(12500, "AOM Push Amp ch2 (-)", 1)
    prg.add(15000, "AOM Zeeman Slower Amp", 1, enable=False)
    prg.add(17500, "TTL Repumper MOT OFF")
    prg.add(20000, "TTL Dark spot OFF")
    return prg
