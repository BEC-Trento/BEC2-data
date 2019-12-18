prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5000, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(0, "magnetization_imaging")
    prg.add(20000, "TTL Picture Hamamatsu  ON", 'beating_0')
    prg.add(29900, "interferometer")
    prg.add(30000, "hamam_twofastpictures")
    prg.add(35000, "TTL Picture Hamamatsu  ON", 'PTAI_m1_2')
    prg.add(36100, "transfer_m1to0")
    prg.add(150000, "TTL Picture Hamamatsu  ON", 'PTAI_probe')
    prg.add(151000, "Probe_pulse_Hamam")
    prg.add(200000, "TTL Picture Hamamatsu  ON", 'PTAI_back')
    prg.add(202000, "TTL Picture Hamamatsu OFF")
    prg.add(210000, "AOM Probe Detuning", 100.000)
    return prg
