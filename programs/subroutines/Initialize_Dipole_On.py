prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 80.00)
    prg.add(500, "AOM IR Vertical Amp", 1000)
    prg.add(1000, "DAC Vert IR", 6.0000)
    prg.add(1500, "AOM IR Horizontal freq", 80.00)
    prg.add(2000, "AOM IR Horizontal Amp", 1000)
    prg.add(2500, "DAC Horiz IR", 6.0000)
    prg.add(3000, "DAC IR Horiz_Ellipt", 9.0000)
    prg.add(3500, "AOM IR Horiz_Ellipt Amp", 1000)
    prg.add(4000, "AOM IR Horiz_Ellipt freq", 110.00)
    return prg
