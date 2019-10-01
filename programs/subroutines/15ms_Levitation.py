prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000000, "DAC MT-MOT Current", 40.0000)
    prg.add(0, "Config field Levit")
    prg.add(150000, "Config field OFF")
    return prg
