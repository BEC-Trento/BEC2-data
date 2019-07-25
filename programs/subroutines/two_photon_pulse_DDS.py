prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2000, "uW mixin amplitude", 1, functions=dict(amplitude=lambda x: cmd.get_var('uW_amp1')))
    prg.add(-1500, "uW2 mixin amplitude", 1, functions=dict(amplitude=lambda x: cmd.get_var('uW_amp2')))
    prg.add(-1000, "uW mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3))
    prg.add(-500, "uW2 mixin frequency", 0.00, functions=dict(frequency=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3))
    prg.add(0, "TTL uW 1 (100W) ON")
    prg.add(10, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(111100, "uW mixin amplitude", 1, functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(111600, "uW2 mixin amplitude", 1, functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    return prg
