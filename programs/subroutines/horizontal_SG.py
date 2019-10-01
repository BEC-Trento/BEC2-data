prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-101000, "IGBT BcompX OPEN")
    prg.add(-100000, "DAC BCompX", 0.0000)
    prg.add(-50000, "IGBT BCompX CLOSE")
    prg.add(-49500, "DAC BCompX", 0.5000)
    prg.add(-30500, "DAC SRS ramp", start_t=0, stop_x=-9, n_points=100, start_x=0, stop_t=3, functions=dict(start_x=lambda x: 1e-3*cmd.get_var('SRS_voltage')))
    prg.add(-17500, "DAC BGradX", 10.0000)
    prg.add(-1000, "IGBT BGradX CLOSE")
    prg.add(-1000, "IGBT BGradX OPEN", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(-900, "IGBT BcompX OPEN", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(-800, "DAC BCompX", 0.0000, functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(-600, "DAC BGradX", 0.0000, functions=dict(time=lambda x: x + cmd.get_var('tof')))
    return prg
