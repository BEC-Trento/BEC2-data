prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 120.00)
    prg.add(400, "AOM IR Vertical Amp", 1000)
    prg.add(800, "DAC Vert IR", 4.0000)
    prg.add(1200, "AOM IR Horizontal freq", 120.00)
    prg.add(1600, "AOM IR Horizontal Amp", 1000)
    prg.add(2000, "DAC Horiz IR", 5.4000)
    prg.add(2400, "AOM IR Horiz_Ellipt freq", 145.00)
    prg.add(2800, "AOM IR Horiz_Ellipt Amp", 1000)
    return prg
