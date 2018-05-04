prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "MOT_Imaging_2016_1212", enable=False)
    prg.add(20000, "Startup", enable=False)
    return prg
