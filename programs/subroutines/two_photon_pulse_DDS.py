prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3000, "DDS41_setfull", ch1_freq=0.000, ch0_amp=0, ch0_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3, ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(-100, "Oscilloscope Trigger ON")
    prg.add(0, "TTL uW 1 (100W) ON")
    prg.add(0, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(111100, "uW mixin amplitude", 1, functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(111600, "uW2 mixin amplitude", 1, functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    return prg
