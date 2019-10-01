prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 110.00)
    prg.add(500, "AOM IR Horizontal freq", 130.00)
    prg.add(1000, "AOM IR Horiz_Ellipt freq", 145.00)
    prg.add(1100, "DAC Horiz IR", -1.0000)
    prg.add(1500, "AOM IR Horizontal Amp", 0)
    return prg
