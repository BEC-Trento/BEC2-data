prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-4500, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-168000, "TTL Picture Hamamatsu  ON", 'ximag_probe')
    prg.add(-165000, "Probe_pulse_Hamam")
  
    for i in range(int(cmd.get_var('x'))):
#        prg.add(1400, "transfer_m1m2", functions=dict(time=lambda x: x + i*cmd.get_var('img_delay')))
        #prg.add(1400, "transfer_m1to0", functions=dict(time=lambda x: x + i*cmd.get_var('img_delay')))
        prg.add(-1500, "TTL Picture Hamamatsu  ON", functions=dict(time=lambda x: x + i*cmd.get_var('img_delay'), comment=lambda x: 'ximag_atoms_{}'.format(i) ))
        prg.add(1500, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + i*cmd.get_var('img_delay')))
    
#    prg.add(1500, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + (1 + int(cmd.get_var('x')))*cmd.get_var('img_delay')))
#    prg.add(700, "TTL Picture Hamamatsu  ON", 'background',functions=dict(time=lambda x: x + (cmd.get_var('x')+1)*cmd.get_var('img_delay')))
#    prg.add(5500, "TTL Picture Hamamatsu OFF", functions=dict(time=lambda x: x + + (cmd.get_var('x')+1)*cmd.get_var('img_delay')))
    return prg
