prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-8500, "DAC 100W_amplitude", 0.0000, functions=dict(value=lambda x: cmd.get_var('uW_100WDAC')))
    prg.add(-3000, "DDS41_setfull", ch0_amp=100, ch0_freq=100443733.000, ch1_freq=100808785.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=150, functions=dict(ch1_phase=lambda x: cmd.get_var('beat_phase'), ch0_freq=lambda x: 100e6 +cmd.get_var('beat_freq0')*1e3, time=lambda x: x - cmd.get_var('beating_pulse'), ch1_freq=lambda x: 100e6 + cmd.get_var('beat_freq1')*1e3, ch0_phase=lambda x: 1, ch0_amp=lambda x: cmd.get_var('beat_amp0'), ch1_amp=lambda x: cmd.get_var('beat_amp1')), enable=False)
    prg.add(-3000, "DDS41_setnotrigger", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch1_phase=lambda x: cmd.get_var('beat_phase'), ch0_freq=lambda x: 100e6 +cmd.get_var('beat_freq0')*1e3, time=lambda x: x - cmd.get_var('beating_pulse'), ch1_freq=lambda x: 100e6 + cmd.get_var('beat_freq1')*1e3, ch0_phase=lambda x: 1, ch0_amp=lambda x: cmd.get_var('beat_amp0'), ch1_amp=lambda x: cmd.get_var('beat_amp1')))
    prg.add(-500, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x - cmd.get_var('beating_pulse')))
    prg.add(-200, "DDS41_trigger", functions=dict(time=lambda x: x - cmd.get_var('beating_pulse')))
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('beating_pulse')))
    prg.add(0, "TTL uW 1 (100W) OFF")
    return prg
