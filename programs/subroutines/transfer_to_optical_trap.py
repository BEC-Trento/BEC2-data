prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC BGradX", 0.0000)
    prg.add(500, "DAC BCompX", 0.0000)
    prg.add(1000, "DAC BGradY", 0.0000)
    prg.add(97899, "MT Current Ramp", start_t=0, stop_x=-0.5, n_points=200, start_x=18, stop_t=1000)
    prg.add(98000, "IGBT BCompZfine CLOSE")
    prg.add(99000, "BCompY current ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=1000, functions=dict(start_x=lambda x: cmd.get_var('BCompY_value'), stop_x=lambda x: cmd.get_var('BCompY_ODTcompensation')))
    prg.add(100000, "DAC SRS ramp", start_t=0, stop_x=-0.1, n_points=200, start_x=-9, stop_t=500, functions=dict(stop_x=lambda x: cmd.get_var('SRS_V')-cmd.get_var('arp_amplitude')))
    prg.add(100500, "IGBT BGradY CLOSE", enable=False)
    prg.add(101000, "DAC BGradY ramp", start_t=0, stop_x=0, n_points=100, start_x=0, stop_t=1000, functions=dict(stop_x=lambda x: cmd.get_var('BGradY_ODTcompensation')), enable=False)
    prg.add(10200100, "Config field OFF")
    prg.add(10201100, "IGBT BcompY OPEN")
    return prg
