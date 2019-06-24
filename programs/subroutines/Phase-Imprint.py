prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM PhaseImprint freq", 80.00)
    prg.add(500, "AOM PhaseImprint Amp", 1000)
    prg.add(1000, "phase imprint OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    prg.add(1060, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    prg.add(10700, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    return prg
