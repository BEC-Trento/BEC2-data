prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1200, "uW2 mixin amplitude", 93, functions=dict(amplitude=lambda x: cmd.get_var('uW_amp2'), funct_enable=False))
    prg.add(-800, "uW mixin amplitude", 100, functions=dict(amplitude=lambda x: cmd.get_var('uW_amp1'), funct_enable=False))
    prg.add(-400, "uW2 mixin frequency", 100808735.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 +cmd.get_var('uW_Delta2')*1e3, funct_enable=False))
    prg.add(0, "uW mixin frequency", 100444389.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, funct_enable=False))
    prg.add(500, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(500, "TTL uW 1 (100W) ON")
    prg.add(175400, "uW2 mixin amplitude", 1)
    prg.add(175900, "uW mixin amplitude", 1)
    return prg
