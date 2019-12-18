prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1500, "AOM Probe Detuning", 0.000)
    prg.add(-1000, "TTL Picture Hamamatsu  ON", 'fieldlock_red', functions=dict(time=lambda x: x + cmd.get_var('uW_lockpulse')))
    prg.add(0, "DDS41_setfull", ch0_amp=50, ch0_freq=100081128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_lockfreq')*1e3 + cmd.get_var('uW_lockdelta')*1e3, ch0_amp=lambda x: cmd.get_var('uW_lockamp')))
    prg.add(2000, "TTL uW 1 (100W) ON")
    prg.add(2000, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_lockpulse')))
    prg.add(2100, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('uW_lockpulse')))
    prg.add(191000, "Probe_pulse_cleaning")
    prg.add(196000, "DDS41_setfull", ch0_amp=50, ch0_freq=100081128.000, ch1_freq=80000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_lockfreq')*1e3 - cmd.get_var('uW_lockdelta')*1e3, ch0_amp=lambda x: cmd.get_var('uW_lockamp')))
    prg.add(199000, "TTL Picture Hamamatsu  ON", 'fieldlock_blue', functions=dict(time=lambda x: x + cmd.get_var('uW_lockpulse')))
    prg.add(201000, "Oscilloscope Trigger ON", enable=False)
    prg.add(201500, "Oscilloscope Trigger OFF", enable=False)
    prg.add(202000, "TTL uW 1 (100W) ON")
    prg.add(202000, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_lockpulse')))
    prg.add(202100, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('uW_lockpulse')))
    prg.add(291000, "Probe_pulse_cleaning")
    prg.add(299000, "TTL Picture Hamamatsu  ON", 'fieldlock_probe')
    prg.add(303200, "Probe_pulse_Hamam")
    prg.add(353200, "TTL Picture Hamamatsu  ON", 'fieldlock_back')
    prg.add(358200, "TTL Picture Hamamatsu OFF")
    prg.add(370000, "AOM Probe Detuning", 100.000)
    return prg
