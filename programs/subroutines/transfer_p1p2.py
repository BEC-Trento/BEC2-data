prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-10680, "DAC 100W_amplitude", 10.0000, functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_p1p2')))
    prg.add(-5000, "DDS41_setfull", ch0_amp=0, ch0_freq=80000000.000, ch1_freq=104364107.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1000, functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_p1p2')))
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse_p1p2')))
    prg.add(0, "TTL uW 1 (100W) OFF")
    return prg
