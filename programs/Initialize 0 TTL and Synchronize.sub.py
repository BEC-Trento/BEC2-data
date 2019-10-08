prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompZfine OPEN")
    prg.add(500, "Config field OFF")
    prg.add(5000, "Initialize 0 TTL1", enable=False)
    prg.add(5100, "Initialize 0 TTL2", enable=False)
    prg.add(5500, "Initialize 0 TTL3", enable=False)
    prg.add(10000, "Breakpoint Main Table OFF")
    prg.add(10100, "Breakpoint Source Table OFF")
    prg.add(10500, "Breakpoint Main Table ON")
    prg.add(10600, "Breakpoint Source Table ON")
    prg.add(11200, "Config field OFF")
    prg.add(13700, "Initialize_Dipole_Off")
    prg.add(18000, "TTL Relay Upper Coil CLOSE")
    prg.add(18500, "TTL Relay Lower Coil CLOSE")
    prg.add(30800, "Breakpoint Main Table OFF")
    prg.add(30900, "Breakpoint Source Table OFF")
    prg.add(30950, "BREAKPOINT")
    prg.add(31300, "NOP")
    prg.add(35000, "Set MarconiS", amplitude1=4.000000, amplitude2=3.000000, frequency2=1769.000000, frequency1=1769.000000, functions=dict(frequency1=lambda x: 1771.0 + cmd.get_var('uW_freq1')*1e-3 + cmd.get_var('uW_Delta')*1e-3, frequency2=lambda x: 1771.0 + cmd.get_var('uW_freq2')*1e-3 + cmd.get_var('uW_Delta')*1e-3, amplitude2=lambda x: cmd.get_var('uW_dB2'), amplitude1=lambda x: cmd.get_var('uW_dB1')), enable=False)
    return prg
