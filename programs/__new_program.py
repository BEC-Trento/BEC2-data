prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(5000000, "RF Landau-Zener Amp", 1000.000)
    prg.add(5001000, "RF Landau-Zener Freq", 10.000)
    prg.add(5050000, "Oscilloscope Trigger ON")
    prg.add(5050040, "RF Landau-Zener ON")
    prg.add(5050150, "RF Landau-Zener OFF")
    prg.add(5050200, "Oscilloscope Trigger OFF")
    return prg
