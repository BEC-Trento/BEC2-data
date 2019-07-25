prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')))
    prg.add(10, "TTL uW 2 ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse')), enable=False)
    prg.add(20, "TTL uW 1 (100W) OFF")
    prg.add(30, "TTL uW 2 OFF", enable=False)
    prg.add(5000000, "All uW OFF")
    return prg
