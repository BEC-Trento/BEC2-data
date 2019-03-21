prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 120.00)
    prg.add(1000, "AOM IR Horizontal freq", 120.00)
    prg.add(2000, "AOM IR Horiz_Ellipt freq", 145.00)
    return prg
