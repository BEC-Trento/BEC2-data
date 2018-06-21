prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Horizontal freq", 120.00)
    prg.add(500, "AOM IR Vertical freq", 120.00)
    prg.add(2000, "AOM IR Horizontal freq", 80.00)
    prg.add(2500, "AOM IR Vertical freq", 80.00)
    return prg
