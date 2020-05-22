prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-8000, "DAC 100W_amplitude", 10.0000, functions=dict(value=lambda x: cmd.get_var('uW_100WDAC')))
    prg.add(-2000, "DDS41_setfull", ch1_freq=0.000, ch0_amp=0, ch0_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_phase=lambda x: 0, ch1_phase=lambda x: 0, ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(-680, "DDS41_setfull", ch0_amp=1000, ch0_freq=1001636128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')), enable=False)
    prg.add(-100, "Oscilloscope Trigger ON", enable=False)
    prg.add(0, "TTL uW 1 (100W) ON")
    prg.add(0, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    return prg
