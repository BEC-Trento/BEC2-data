prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM PhaseImprint freq", 80.00)
    prg.add(100, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(200, "TTL uW 2 OFF", enable=False)
    prg.add(500, "AOM PhaseImprint Amp", 1000)
    prg.add(1000, "phase imprint OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')))
    prg.add(1050, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x + cmd.get_var('PI_time')), enable=False)
    prg.add(1055, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')), enable=False)
    prg.add(1060, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time')), enable=False)
    prg.add(1065, "TTL uW 2 ON", functions=dict(time=lambda x: x + cmd.get_var('PI_time')), enable=False)
    prg.add(1070, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time') + cmd.get_var('uW_pulse')), enable=False)
    prg.add(1075, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('PI_time') + cmd.get_var('uW_pulse')), enable=False)
    prg.add(5000000, "All uW OFF")
    return prg
