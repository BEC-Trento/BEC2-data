prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "AOM Zeeman Slower Amp", 1000)
    prg.add(50500, "Config field OFF")
    prg.add(63000, "AOM Zeeman Slower freq", 170.00)
    prg.add(73000, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(83000, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(93000, "AOM Probe Detuning", 0.000)
    prg.add(103000, "AOM 2DMOT Amp ch1 (+)", 1000)
    prg.add(113000, "AOM 2DMOT Amp ch2 (-)", 1000)
    prg.add(123000, "AOM 2DMOT Detuning", -15.000)
    prg.add(133000, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(143000, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(153000, "AOM 3DMOT Detuning", -13.000)
    prg.add(163000, "AOM Push Amp ch1 (+)", 1000)
    prg.add(173000, "AOM Push Amp ch2 (-)", 1000)
    prg.add(183000, "AOM Push Detuning", 0.000)
    prg.add(193000, "AOM Repumper Amp", 1000)
    prg.add(203000, "AOM Repumper freq", 225.00)
    prg.add(213000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(223000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(233000, "TTL Dark Spot ON")
    prg.add(243000, "TTL Repumper MOT  ON")
    prg.add(244000, "TTL ProbeHor ON")
    prg.add(245000, "TTL ProbeVert ON")
    prg.add(253000, "All shutter open")
    prg.add(263000, "Config Field MT-MOT")
    prg.add(273000, "AOM GM Amp ch1 (+)", 1000)
    prg.add(283000, "AOM GM Amp ch2 (-)", 1000)
    prg.add(283500, "AOM GM Detuning", 40.000)
    prg.add(293000, "Initialize_Dipole_Off")
    prg.add(300000, "AOM PhaseImprint Amp", 1000)
    prg.add(301000, "AOM PhaseImprint freq", 80.00)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 5.000000, 5.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        x = iters[j]
        cmd.set_var('x', x)
        print('\n')
        print('Run #%d/%d, with variables:\nx = %g\n'%(j+1, len(iters), x))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
