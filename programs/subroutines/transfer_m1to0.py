prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "uW mixin amplitude", 1000)
    prg.add(500, "uW2 mixin amplitude", 1)
    prg.add(1000, "uW mixin frequency", 100444324.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3, funct_enable=False))
    prg.add(1500, "uW2 mixin frequency", 100000000.00)
    prg.add(2000, "TTL uW 1 (100W) ON")
    prg.add(3017, "TTL uW 1 (100W) OFF")
    return prg
