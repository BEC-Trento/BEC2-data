prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "two_states_imaging_2", enable=False)
    prg.add(500, "two_states_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(500, "two_states_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +cmd.get_var('img_delay')), enable=False)
    prg.add(500, "two_states_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+2*cmd.get_var('img_delay')), enable=False)
    prg.add(500, "two_states_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+3*cmd.get_var('img_delay')), enable=False)
    prg.add(500, "two_states_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+4*cmd.get_var('img_delay')), enable=False)
    prg.add(500, "two_states_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+5*cmd.get_var('img_delay')), enable=False)
    prg.add(500, "beating", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +2*cmd.get_var('img_delay')), enable=False)
    prg.add(550, "TTL Picture Hamamatsu  ON", 'PTAI_probe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+3*cmd.get_var('img_delay')-0.3))
    prg.add(600, "Probe_pulse_Hamam", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+3*cmd.get_var('img_delay')))
    prg.add(700, "TTL Picture Hamamatsu  ON", 'PTAI_back', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+4*cmd.get_var('img_delay')))
    prg.add(5699, "TTL Picture Hamamatsu OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+4*cmd.get_var('img_delay')))
    return prg
