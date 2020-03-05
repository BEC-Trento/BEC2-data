prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "phase imprint ON")
    prg.add(0, "phase imprint OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    return prg
