prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "All shutter close")
    prg.add(4000000, "DAC Vert IR", 3.0000)
    prg.add(4001000, "AOM IR Vertical freq", 80.00)
    prg.add(4002000, "TTL Picture  ON")
    prg.add(4003000, "AOM IR Vertical freq", 120.00)
    prg.add(4004000, "TTL Picture OFF")
    return prg
