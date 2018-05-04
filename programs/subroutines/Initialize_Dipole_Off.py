prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 120.00)
    prg.add(500, "AOM IR Vertical Amp", 1000)
    prg.add(1000, "DAC Vert IR", 4.0000)
    prg.add(1500, "AOM IR Horizontal freq", 120.00)
    prg.add(2000, "AOM IR Horizontal Amp", 1000)
    prg.add(2500, "DAC Horiz IR", 5.4000)
    return prg
