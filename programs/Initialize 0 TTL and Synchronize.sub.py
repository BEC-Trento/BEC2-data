prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompZfine OPEN")
    prg.add(500, "Config field OFF")
    prg.add(5000, "Initialize 0 TTL1")
    prg.add(5100, "Initialize 0 TTL2")
    prg.add(5500, "Initialize 0 TTL3")
    prg.add(10000, "Breakpoint Main Table OFF")
    prg.add(10100, "Breakpoint Source Table OFF")
    prg.add(10500, "Breakpoint Main Table ON")
    prg.add(10600, "Breakpoint Source Table ON")
    prg.add(11200, "Config field OFF")
    prg.add(13700, "Initialize_Dipole_Off")
    prg.add(16700, "All BComp ON", enable=False)
    prg.add(30800, "Breakpoint Main Table OFF")
    prg.add(30900, "Breakpoint Source Table OFF")
    prg.add(30950, "BREAKPOINT")
    prg.add(31300, "NOP")
    prg.add(41300, "TTL Test Trigger ON", enable=False)
    return prg
