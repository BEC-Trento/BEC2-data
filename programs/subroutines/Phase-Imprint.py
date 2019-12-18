prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "phase imprint ON")
    prg.add(100, "TTL Picture Hamamatsu  ON", 'image0', enable=False)
    prg.add(500, "phase imprint OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    prg.add(1100, "TTL Picture Hamamatsu OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')), enable=False)
    return prg
