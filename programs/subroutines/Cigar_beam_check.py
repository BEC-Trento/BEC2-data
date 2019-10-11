prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC Horiz IR", 5.0000)
    prg.add(1000, "Oscilloscope Trigger ON", enable=False)
    prg.add(5000, "AOM IR Horizontal Amp", 1000)
    prg.add(5500, "AOM IR Horizontal freq", 80.00)
    prg.add(100000, "TTL Picture  ON")
    prg.add(105000, "TTL Picture OFF")
    prg.add(210000, "Oscilloscope Trigger OFF")
    prg.add(260000, "Initialize_Dipole_Off")
    return prg
