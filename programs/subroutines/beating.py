prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3000, "TTL uW 1 (100W) OFF")
    prg.add(-1400, "TTL Picture Hamamatsu  ON", 'beating_0', functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(1100, "Oscilloscope Trigger ON", enable=False)
    prg.add(1300, "TTL uW 2 OFF", functions=dict(time=lambda x: x - cmd.get_var('beating_pulse')))
    prg.add(1310, "interferometer")
    prg.add(1400, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(1550, "TTL uW 2 ON", functions=dict(time=lambda x: x - cmd.get_var('beating_pulse')))
    prg.add(38600, "TTL Picture Hamamatsu  ON", 'beating_1', functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(40000, "TTL uW 2 OFF")
    prg.add(41400, "interferometer_2")
    prg.add(41550, "TTL uW 2 ON", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    prg.add(41600, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('beating_pulse')))
    return prg
