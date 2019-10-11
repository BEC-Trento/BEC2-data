prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000000, "DAC MT-MOT Current", 36.0000)
    prg.add(0, "Config field Levit")
    prg.add(0, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    return prg
