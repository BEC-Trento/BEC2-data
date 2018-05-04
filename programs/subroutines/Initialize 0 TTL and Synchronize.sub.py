prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL1")
    prg.add(100, "Initialize 0 TTL2")
    prg.add(5000, "Breakpoint Main Table OFF")
    prg.add(5100, "Breakpoint Source Table OFF")
    prg.add(5500, "Breakpoint Main Table ON")
    prg.add(5600, "Breakpoint Source Table ON")
    prg.add(6000, "Config field OFF")
    prg.add(8500, "Initialize_Dipole_Off")
    prg.add(11500, "All BComp ON")
    prg.add(15000, "DAC CC_AB", -6.0000)
    prg.add(25600, "Breakpoint Main Table OFF")
    prg.add(25700, "Breakpoint Source Table OFF")
    prg.add(25750, "BREAKPOINT")
    prg.add(26100, "NOP")
    prg.add(36100, "TTL Test Trigger ON")
    prg.add(36105, "TTL 1 ch2 ON")
    return prg
