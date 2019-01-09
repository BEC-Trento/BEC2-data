prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL uW 1 (100W) ON")
    prg.add(100, "TTL uW 1 (100W) OFF")
    prg.add(3100, "TTL uW 1 (100W) ON")
    prg.add(3300, "TTL uW 1 (100W) OFF")
    prg.add(6300, "TTL uW 1 (100W) ON")
    prg.add(6400, "TTL uW 1 (100W) OFF")
    return prg
