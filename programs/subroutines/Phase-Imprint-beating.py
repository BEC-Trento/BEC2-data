prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM PhaseImprint Amp", 1000)
    prg.add(500, "AOM PhaseImprint freq", 80.00)
    prg.add(500, "phase imprint OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    prg.add(2000, "beating", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    prg.add(5000000, "All uW OFF")
    return prg
