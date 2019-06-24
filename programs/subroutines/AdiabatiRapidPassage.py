prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL RF-arp ON")
    prg.add(0, "DAC SRS ramp", start_t=0, stop_x=0.5, n_points=200, start_x=-0.5, stop_t=200)
    prg.add(2001000, "TTL RF-arp OFF")
    return prg
