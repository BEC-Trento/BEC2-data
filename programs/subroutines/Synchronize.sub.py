prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(5000, "Breakpoint Main Table OFF")
    prg.add(5100, "Breakpoint Source Table OFF")
    prg.add(5500, "Breakpoint Main Table ON")
    prg.add(5600, "Breakpoint Source Table ON")
    prg.add(25600, "Breakpoint Main Table OFF")
    prg.add(25700, "Breakpoint Source Table OFF")
    prg.add(25750, "BREAKPOINT")
    prg.add(26100, "NOP")
    prg.add(505600, "Breakpoint Main Table OFF", enable=False)
    prg.add(505700, "Breakpoint Source Table OFF", enable=False)
    return prg
