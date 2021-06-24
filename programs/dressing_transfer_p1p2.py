prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2100, "TTL uW 2 OFF", functions=dict(time=lambda x: x-cmd.get_var('uW_pulse_p1p2')))
    prg.add(-2000, "DDSdressing_LUT", 3, functions=dict(time=lambda x: x-cmd.get_var('uW_pulse_p1p2')))
    prg.add(-1500, "DDSdressing_LUT", 500, functions=dict(time=lambda x: x-cmd.get_var('uW_pulse_p1p2')))
    prg.add(0, "TTL uW 2 ON", functions=dict(time=lambda x: x-cmd.get_var('uW_pulse_p1p2')))
    prg.add(0, "TTL uW 2 OFF")
    prg.add(100, "DDSdressing_LUT", 1)
    prg.add(200, "TTL uW 2 ON", enable=False)
    return prg
