prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "AOM IR Horizontal freq", 120.00)
    prg.add(500, "AOM IR Vertical freq", 120.00, enable=False)
    prg.add(4500, "AOM IR Horizontal freq", 80.00)
    prg.add(5000, "AOM IR Vertical freq", 80.00)
    return prg
