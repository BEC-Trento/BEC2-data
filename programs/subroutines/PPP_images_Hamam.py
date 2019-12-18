prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-4500, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-165000, "Probe_pulse_Hamam")
  
    for i in range(16):
        prg.add(200, "transfer_m1m2", functions=dict(time=lambda x: x + i*cmd.get_var('img_delay')))
        prg.add(500, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + i*cmd.get_var('img_delay')))
    
    prg.add(700, "TTL Picture Hamamatsu  ON", functions=dict(time=lambda x: x + (i+1)*cmd.get_var('img_delay')))
    prg.add(5500, "TTL Picture Hamamatsu OFF", functions=dict(time=lambda x: x + + (i+1)*cmd.get_var('img_delay')))
    return prg
