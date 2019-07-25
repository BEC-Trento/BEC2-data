prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC PiezoHorizEllipt", 0.0000)
    prg.add(1000, "DAC SRS", -6.0000)
    prg.add(1000000, "DAC PiezoHorizEllipt", 0.5000)
    prg.add(1001000, "DAC SRS", 6.0000)
    return prg
