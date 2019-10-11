prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5000, "transfer_m1to0", enable=False)
    prg.add(-200, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(250, "DDS41_setfull", ch0_amp=100, ch0_freq=100443853.000, ch1_freq=100808289.000, ch0_phase=8000.000, ch1_phase=0.000, ch1_amp=102, functions=dict(ch0_phase=lambda x: cmd.get_var('beat_phase')), enable=False)
    prg.add(1100, "Oscilloscope Trigger ON")
    prg.add(1500, "TTL uW 1 (100W) ON", enable=False)
    prg.add(2200, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False), enable=False)
    prg.add(2570, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse'), funct_enable=False), enable=False)
    return prg
