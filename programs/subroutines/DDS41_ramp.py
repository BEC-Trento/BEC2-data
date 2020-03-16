prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    
    _ramp_numpoint = 100
    import numpy
    ch0_freqs = numpy.linspace(100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3,
                       100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3,
                       _ramp_numpoint)
    
    ch1_freqs = numpy.linspace(100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3,
                       100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3,
                       _ramp_numpoint)                
    
    for i in range(_ramp_numpoint):
        
        prg.add(0 + i*cmd.get_var('RRR_duration')/float(_ramp_numpoint)*1e4,
            "DDS41_setfull",
            ch0_amp=cmd.get_var('uW_amp1'),
            ch0_freq=ch0_freqs[i],
            ch1_freq=ch1_freqs[i],
            ch0_phase=0.000,
            ch1_phase=4096,
            ch1_amp=cmd.get_var('uW_amp2'),
            )
       
    return prg
