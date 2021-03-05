prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC 100W_amplitude", 1.0000, functions=dict(value=lambda x: cmd.get_var('uW_100WDAC')))
    prg.add(1000, "DDS41_setfull", ch0_amp=0, ch0_freq=10.000, ch1_freq=20.000, ch0_phase=1.000, ch1_phase=1.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3+ 0.5*cmd.get_var('uW_delta3')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3 - 0.5*cmd.get_var('uW_delta3')*1e3))
    prg.add(10000, "DAC SRS ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=20.0, functions=dict(start_x=lambda x: cmd.get_var('SRS_V')-cmd.get_var('arp_amplitude'), stop_x=lambda x: cmd.get_var("SRS_V")-cmd.get_var("ARP_mid")))
    prg.add(410010, "TTL uW 2 ON")
    prg.add(429000, "Oscilloscope Trigger ON", enable=False)
    prg.add(429500, "DDS41_ch0amp_ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=100, functions=dict(stop_t=lambda x: cmd.get_var("ARP_time"), stop_x=lambda x: cmd.get_var("uW_amp1")))
    prg.add(430000, "DDS41_ch1amp_ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=100, functions=dict(stop_t=lambda x: cmd.get_var("ARP_time"), stop_x=lambda x: cmd.get_var("uW_amp2")))
    prg.add(430010, "TTL uW 1 (100W) ON")
    prg.add(430100, "DAC SRS ramp", start_t=0, stop_x=0.2, n_points=200, start_x=0, stop_t=100, functions=dict(stop_t=lambda x: cmd.get_var("ARP_time")+cmd.get_var("ARP_time2"), stop_x=lambda x: cmd.get_var("SRS_V"), start_x=lambda x: cmd.get_var('SRS_V')-cmd.get_var('ARP_mid'), start_t=lambda x: cmd.get_var("ARP_time")))
    prg.add(432100, "wait", functions=dict(time=lambda x: x+2*cmd.get_var("ARP_time")), enable=False)
    return prg
