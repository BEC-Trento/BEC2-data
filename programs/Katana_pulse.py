prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-100000, "DAC 100W_amplitude", 0.0000, functions=dict(value=lambda x: cmd.get_var('uW_100WDAC')))
    prg.add(2000, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=1.000, ch1_phase=1.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_DeltaK')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_DeltaK')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(3000, "DDS41_trigger")
    prg.add(3100, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=80000000.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_phase=lambda x: cmd.get_var('uW_phi'), ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3+0.5*cmd.get_var('uW_delta3')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3-0.5*cmd.get_var('uW_delta3')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(5000, "TTL uW 1 (100W) ON")
    prg.add(5000, "DDS41_trigger", functions=dict(time=lambda x: x+cmd.get_var('kat_time')))
    prg.add(5010, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x+cmd.get_var('kat_time')), enable=False)
    return prg
