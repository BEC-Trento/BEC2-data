prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1400, "TTL Picture Hamamatsu  ON", 'beating_0', functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(-200, "TTL uW 1 (100W) OFF")
    prg.add(250, "DDS41_setfull", ch1_freq=100808785.000, ch0_amp=100, ch0_freq=100443733.000, ch0_phase=8000.000, ch1_phase=0.000, ch1_amp=100, functions=dict(ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3, ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3, ch0_phase=lambda x: cmd.get_var('beat_phase')))
    prg.add(1100, "Oscilloscope Trigger ON", enable=False)
    prg.add(1300, "TTL uW 2 OFF")
    prg.add(1500, "TTL uW 1 (100W) ON")
    prg.add(1500, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(1550, "TTL uW 2 ON", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(1600, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(38600, "TTL Picture Hamamatsu  ON", 'beating_1', functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(40000, "DDS41_setfull", ch1_freq=100808785.000, ch0_amp=100, ch0_freq=100443733.000, ch0_phase=8000.000, ch1_phase=0.000, ch1_amp=150, functions=dict(ch0_phase=lambda x: cmd.get_var('beat_phase')+4096))
    prg.add(41300, "TTL uW 2 OFF")
    prg.add(41500, "TTL uW 1 (100W) ON")
    prg.add(41500, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(41550, "TTL uW 2 ON", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(41600, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    return prg
