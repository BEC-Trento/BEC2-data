prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 80.00)
    prg.add(500, "AOM IR Vertical Amp", 200)
    prg.add(1000, "DAC Vert IR", 7.0000)
    prg.add(1500, "AOM IR Horizontal freq", 80.00)
    prg.add(2000, "AOM IR Horizontal Amp", 200)
    prg.add(2500, "DAC Horiz IR", 8.0000)
    return prg
