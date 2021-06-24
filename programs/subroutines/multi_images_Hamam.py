prg_comment = ""
prg_version = "0.7"

def program(prg, cmd):

    #This part must remain, it is just for preparation
    prg.add(-50100, "TTL Picture Hamamatsu  ON", 'PTAI_preprobe')
#    prg.add(-12000, "Probe_pulse_cleaning")
    prg.add(-50000, "TTL Picture Hamamatsu OFF")
    prg.add(-5000, "AOM Probe Detuning", -1.000, functions = dict(frequency=lambda x: cmd.get_var("probe_det")))
    prg.add(-230, "TTL uW 1 (100W) OFF")
    prg.add(-20, "TTL uW 2 OFF")
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    
    n_images = cmd.get_var('n_images')
    time_delay = cmd.get_var('time_delay_hamam')*1e4
    prg.add(-400, "Oscilloscope Trigger ON", enable=True)
    
    for i in range(n_images):
#        prg.add(-10000 + i*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_m1_%i'%i)
#        prg.add(-100 + i*time_delay, "transfer_m1m2")
#            
#        prg.add(i*time_delay, "hamam_twofast2furious")
#        prg.add(1000 + i*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_p1_%i'%i)
#        prg.add(10400+ i*time_delay, "transfer_p1p2")
#        prg.add(10500 + i*time_delay, "hamam_twofast2furious")
        prg.add(-10000+ i*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_m1_%i'%i)
        prg.add(-8000 + i*time_delay, "TTL Picture Hamamatsu OFF")
        prg.add(-4000 + i*time_delay, "TTL ProbeVert OFF")
        prg.add(-3990 + i*time_delay, "TTL ProbeHor OFF")
        prg.add(-2060 + i*time_delay, "AOM Probe Amp ch1 (+)", 200)
        prg.add(-1560 + i*time_delay, "AOM Probe Amp ch2 (-)", 200)
        prg.add(-100 + i*time_delay, "transfer_m1m2")

        prg.add(i*time_delay, "TTL ProbeVert ON")
        prg.add(50 + i*time_delay, "TTL ProbeVert OFF")
#        prg.add(500 + i*time_delay, "TTL ProbeHor ON")
#        prg.add(600 + i*time_delay, "TTL ProbeHor OFF")
        prg.add(700 + i*time_delay, "AOM Probe Amp ch1 (+)", 0)
        prg.add(1100 + i*time_delay, "AOM Probe Amp ch2 (-)", 0)

#        prg.add(8006 + i*time_delay, "AOM Probe Amp ch2 (-)", 1000)
#        prg.add(8492 + i*time_delay, "AOM Probe Amp ch1 (+)", 1000)
#        prg.add(8500 + i*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_p1_%i'%i)
#        prg.add(10300 + i*time_delay, "TTL Picture Hamamatsu OFF")
#        prg.add(10400 + i*time_delay, "transfer_p1p2")
#        
#        prg.add(10500 + i*time_delay, "TTL ProbeVert ON")
#        prg.add(10550 + i*time_delay, "TTL ProbeVert OFF")
#        prg.add(11000 + i*time_delay, "TTL ProbeHor ON")
#        prg.add(11100 + i*time_delay, "TTL ProbeHor OFF")
#        prg.add(11200 + i*time_delay, "AOM Probe Amp ch1 (+)", 0)
#        prg.add(12300 + i*time_delay, "AOM Probe Amp ch2 (-)", 0)

    
    prg.add(50 + n_images*time_delay, "Oscilloscope Trigger OFF", enable=True)
    prg.add(150000 + n_images*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_probe')
    prg.add(151000 + n_images*time_delay, "Probe_pulse_Hamam")
    prg.add(210000 + n_images*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_back')
    prg.add(212000 + n_images*time_delay, "TTL Picture Hamamatsu OFF")
    prg.add(213000 + n_images*time_delay, "AOM Probe Detuning", 100.000)
    
    return prg


#This part should be useless, it is hamam_magnetiz_image but it took some time to open it
#in this form so it is worth to keep it

#        prg.add(-10000 + i*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_m1_%i'%i)
#        prg.add(-8000 + i*time_delay, "TTL Picture Hamamatsu OFF")
#        prg.add(-4000 + i*time_delay, "TTL ProbeVert OFF")
#        prg.add(-3990 + i*time_delay, "TTL ProbeHor OFF")
#        prg.add(-2060 + i*time_delay, "AOM Probe Amp ch1 (+)", 1000)
#        prg.add(-1560 + i*time_delay, "AOM Probe Amp ch2 (-)", 1000)

#        prg.add(-100 + i*time_delay, "transfer_m1m2")



#        prg.add(0 + i*time_delay, "TTL ProbeVert ON")
#        prg.add(50 + i*time_delay, "TTL ProbeVert OFF")
#        prg.add(700 + i*time_delay, "AOM Probe Amp ch1 (+)", 0)
#        prg.add(1100 + i*time_delay, "AOM Probe Amp ch2 (-)", 0)

#        prg.add(8006 + i*time_delay, "AOM Probe Amp ch2 (-)", 1000)
#        prg.add(8492 + i*time_delay, "AOM Probe Amp ch1 (+)", 1000)
#        prg.add(8500 + i*time_delay, "TTL Picture Hamamatsu  ON", 'PTAI_p1_%i'%i)
#        prg.add(10300 + i*time_delay, "TTL Picture Hamamatsu OFF")
#        prg.add(10400 + i*time_delay, "transfer_p1p2")
#        
#        prg.add(10500 + i*time_delay, "TTL ProbeVert ON")
#        prg.add(10550 + i*time_delay, "TTL ProbeVert OFF")
#        prg.add(11500 + i*time_delay, "AOM Probe Amp ch1 (+)", 0)
#        prg.add(12000 + i*time_delay, "AOM Probe Amp ch2 (-)", 0)
