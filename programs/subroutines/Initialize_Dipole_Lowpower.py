prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "AOM IR Vertical freq", 80.00)
    prg.add(500, "AOM IR Vertical Amp", 70)
    prg.add(1000, "DAC Vert IR", 2.0000)
    prg.add(1500, "AOM IR Horizontal freq", 80.00)
    prg.add(2000, "AOM IR Horizontal Amp", 70)
    prg.add(2500, "DAC Horiz IR", 2.0000)
    prg.add(3000, "AOM IR Horiz_Ellipt freq", 110.00)
    prg.add(3500, "AOM IR Horiz_Ellipt Amp", 70)
    prg.add(4000, "DAC IR Horiz_Ellipt", 2.0000)
    return prg
def commands(cmd):
    import numpy as np
    det_arr, amp_arr, mot_I_arr = np.mgrid[-22:-17:1, 200:500:50, 25:35:1, ]
    iters = list(zip(det_arr.ravel(), amp_arr.ravel(), mot_I_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        det1, amp1, mot_I1 = iters[j]
        cmd.set_var('det', det1)
        cmd.set_var('amp', amp1)
        cmd.set_var('mot_I', mot_I1)
        print('\n')
        print('Run #%d/%d, with variables:\ndet = %g\namp = %g\nmot_I = %g\n'%(j+1, len(iters), det1, amp1, mot_I1))
        cmd.run(wait_end=True, add_time=5000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
