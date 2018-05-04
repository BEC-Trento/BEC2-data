prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "DAC BComp1", 0.2600, functions=dict(value=lambda x: cmd.get_var('B1'), funct_enable=False))
    prg.add(500, "DAC BComp2", 0.2500, functions=dict(value=lambda x: cmd.get_var('B2'), funct_enable=False))
    prg.add(1000, "DAC BCompZ", 0.2800, functions=dict(value=lambda x: cmd.get_var('BZ'), funct_enable=False))
    prg.add(1500, "DAC BCompY", 0.0000)
    prg.add(2000, "IGBT BCompY field OPEN")
    return prg
