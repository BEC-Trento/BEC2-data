prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(110110000, "wait")
    prg.add(110212000, "+-1_mixture_preparation", enable=False)
    prg.add(110213650, "TTL uW 2 ON", enable=False)
    prg.add(110614650, "two_photon_pulse_DDS", enable=False)
    prg.add(110617620, "DAC BGradX", 1.0000, enable=False)
    prg.add(110617620, "IGBT BGradX CLOSE", enable=False)
    prg.add(110617620, "IGBT BGradX OPEN", enable=False)
    prg.add(110617620, "multi_images_Hamam", enable=False)
    prg.add(110669800, "soliton_imaging", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(110669820, "X_images_Hamam", enable=False)
    prg.add(110669820, "TTL uW 1 (100W) ON", enable=False)
    prg.add(110670820, "TTL uW 2 ON", enable=False)
    prg.add(110680720, "Oscilloscope Trigger ON")
    prg.add(110680820, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: 0.8*cmd.get_var('Cigar_compressed'), time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(110683820, "DAC Horiz IR", 0.0400, functions=dict(value=lambda x: cmd.get_var('Cigar_compressed'), time=lambda x: x - cmd.get_var('hold_time')))
    prg.add(110693820, "Switch Off Dipole")
    prg.add(110694970, "All uW OFF")
    prg.add(110695070, "TOF_Levitation")
    prg.add(110696170, "Oscilloscope Trigger OFF")
    prg.add(110698302, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(110699652, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(110729652, "TTL Picture Hamamatsu  ON", 'emptyprobe')
    prg.add(110732652, "Probe_pulse_Hamam")
    prg.add(110832652, "TTL Picture Hamamatsu  ON", 'background')
    prg.add(110837652, "TTL Picture Hamamatsu OFF")
    prg.add(118841862, "Cigar_beam_check")
    prg.add(118851862, "TTL uW 1 (100W) OFF")
    prg.add(158851862, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 1.500000, 16.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time = iters[j]
        cmd.set_var('hold_time', hold_time)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time = %g\n'%(j+1, len(iters), hold_time))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
