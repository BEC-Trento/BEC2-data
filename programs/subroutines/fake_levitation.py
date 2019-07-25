prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC MT-MOT Current", 40.0000)
    prg.add(500000, "Config field Levit")
    prg.add(650000, "Config field OFF")
    return prg
