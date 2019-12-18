prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL uW 1 (100W) OFF")
    prg.add(10, "TTL uW 2 OFF")
    prg.add(20, "TTL uW 3 OFF")
    prg.add(30, "TTL uW 4 OFF")
    prg.add(40, "TTL uW coupling OFF")
    return prg
