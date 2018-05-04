prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "MOT Lights off", enable=False)
    prg.add(0, "switch off MOT ")
    prg.add(10000, "DAC Horiz IR", 0.0000, enable=False)
    prg.add(20000, "DAC Vert IR", 0.0000, enable=False)
    prg.add(5050000, "Set Bright MOT", enable=False)
    prg.add(5050000, "Set MOT")
    prg.add(5055000, "DAC Horiz IR", 6.0000, enable=False)
    prg.add(5060000, "DAC Vert IR", 6.0000, enable=False)
    prg.add(85050000, "switch off MOT ", enable=False)
    prg.add(85050000, "switch off MOT _ Depumper ")
    prg.add(85052350, "GM pulse 05ms")
    prg.add(85063000, "GM Ramp 12 Gamma")
    prg.add(85063000, "GM Ramp DipoleLoad", enable=False)
    prg.add(85326000, "Picture Na")
    prg.add(85525000, "Picture Na Pushprobe", enable=False)
    prg.add(85685000, "Picture Na Vert", enable=False)
    prg.add(95666000, "DAC Horiz IR", 0.0000, enable=False)
    prg.add(95668000, "DAC Vert IR", 0.0000, enable=False)
    prg.add(106597098, "Set Bright MOT", enable=False)
    prg.add(106604058, "Set MOT")
    return prg
