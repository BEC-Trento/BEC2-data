prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC BComp1")
    prg.add(500, "DAC BComp2")
    prg.add(1000, "DAC BCompZ", 0.3050, functions=dict(value=lambda x: cmd.get_var('BZ'), funct_enable=False))
    prg.add(1500, "DAC BCompY", 0.0000)
    return prg
