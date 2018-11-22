prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-95120, "DAC BCompZ", 0.2000)
    prg.add(-500, "Oscilloscope Trigger ON")
    prg.add(0, "RF Landau-Zener ON")
    prg.add(200, "RF Landau-Zener OFF")
    prg.add(1220, "Oscilloscope Trigger OFF")
    return prg
