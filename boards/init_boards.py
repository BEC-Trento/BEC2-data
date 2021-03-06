"""
EXAMPLES for an arbitrary .py file in folder data/boards
see board module for details


import libraries.board as lib_board

def board_list_init(board_lst):

    #DDS BOARD
    board_lst.add("BOARD NAME",             #BOARD NAME is arbitrary but must be unique in the list (eg DDS32)
                  lib_board.DdsBoard,       #board type
                  address=33,               #hardware address
                  parameters=dict(amp_to_lut={1: lambda x: x, 2: lambda x: x,
                                  freq_to_lut={1: lambda x: x, 2: lambda x: x),
                  comment="arbitrary board description")
                  #Parameters for DDS boards are composed of a dictionary with two elements:
                  #the encoders for DDS amplitude converted into LUT number (amp_to_lut),
                  #and encoders for for DDS frequency converted into LUT number (freq_to_lut).
                  #Each group of encoders is a dictionary, with the numbers of the DDS channels as keys,
                  #and lambda functions mapping the relative values to LUT numbers.
                  #Be careful with divisions in python.

    #TTL BOARD
    board_lst.add("BOARD NAME",
                  lib_board.DigitalBoard,
                  address=33,
                  comment="arbitrary board description")

    #ANALOG BOARD
    board_lst.add("BOARD NAME",
                  lib_board.AnalogBoard,
                  address=33,
                  parameters=dict(ang_to_dig={1: lambda x: x}),
                  comment="arbitrary board description")
                  #Parameters for Analog boards are similar to the DDS boards
                  #with a key ang_to_dig mapping the input values to the DAC range.
"""

import libraries.board as lib_board
def board_list_init(board_lst):
    
#    board_lst.add("DDS36", lib_board.DdsBoard,
#                  address=36,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
#                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 +500}))
#    board_lst.add("DDS32", lib_board.DdsBoard,
#                  address=32,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
#                                  freq_to_lut={1: lambda x: 51 + (float(x)-1600-112.5)*1.0/1.6}))

###################  DDS  ######################
    board_lst.add("DDS40", lib_board.DdsBoard,
                  address=40,
                  parameters=dict(amp_to_lut={},
                                  freq_to_lut={}))

    board_lst.add("DDS39", lib_board.DdsBoard,
                  address=39,
                  parameters=dict(
                    amp_to_lut={1: lambda x: int(max(min(x/10.0, 100),0)+400),
                                2: lambda x: (int(x)+4000)*1.0/10 +500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)/0.25,
                                 2: lambda x: (float(x)-59.75)/0.25 +500}))
                  
    board_lst.add("DDS38", lib_board.DdsBoard,
                  address=38,
                  parameters=dict(amp_to_lut={},
                                  freq_to_lut={}))

    board_lst.add("DDS37", lib_board.DdsBoard,
                  address=37,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 +500}))

    board_lst.add("DDS35", lib_board.DdsBoard,
                  address=35,
                  parameters=dict(amp_to_lut={1: lambda x: 799 + int(x/10), 2: lambda x: 900 + int(x/10)},
                                  freq_to_lut={1: lambda x: 401 + int(x/(2*0.125))}))

    board_lst.add("DDS34", lib_board.DdsBoard,
                  address=34,
                  parameters=dict(amp_to_lut={1: lambda x: 799 + int(x/10), 2: lambda x: 900 + int(x/10)},
                                  freq_to_lut={1: lambda x: 401 + int(x/(2*0.125))}))

    board_lst.add("DDS33", lib_board.DdsBoard,
                  address=33,
                  parameters=dict(amp_to_lut={1: lambda x: 799 + int(x/10), 2: lambda x: 900 + int(x/10)},
                                  freq_to_lut={1: lambda x: 401 + int(x/(2*0.125))}))

    board_lst.add("DDS32", lib_board.DdsBoard,
                  address=32,
                  parameters=dict(amp_to_lut={1: lambda x: 799 + int(x/10), 2: lambda x: 900 + int(x/10)},
                                  freq_to_lut={1: lambda x: 401 + int(x/(2*0.125))}))

    board_lst.add("DDS30", lib_board.DdsBoard,
                  address=30,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
                                  freq_to_lut={1: lambda x: (float(x)/2-59.75)*1.0/0.25, 2: lambda x: (float(x)/2 -59.75)*1.0/0.25 +500}))

    board_lst.add("DDS36", lib_board.DdsBoard,
                  address=36,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
                                  freq_to_lut={1: lambda x: (float(x)/4-59.75)*1.0/0.25, 2: lambda x: (float(x)/2-59.75)*1.0/0.25 +500}))

    board_lst.add("DDS31", lib_board.DdsBoard,
                  address=31,
                  parameters=dict(amp_to_lut={1: lambda x: 799 + int(x/10), 2: lambda x: 900 + int(x/10)},
                                  freq_to_lut={1: lambda x: 401 + int(x/(4*0.125))}))
   
    board_lst.add("dds41", lib_board.DdsBoard,
                  address=41,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
                                  freq_to_lut={1: lambda x: (float(x)/2-59.75)*1.0/0.25, 2: lambda x: (float(x)/2 -59.75)*1.0/0.25 +500}))


    board_lst.add("DDS64", lib_board.DdsBoard,
                  address=30,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
                                  freq_to_lut={1: lambda x: (float(x)/2-59.75)*1.0/0.25, 2: lambda x: (float(x)/2 -59.75)*1.0/0.25 +500}))



############   TTL    #################

    board_lst.add("ttl1",
                  lib_board.DigitalBoard,
                  address=1,
                  comment="arbitrary board description")

    board_lst.add("ttl2",
                  lib_board.DigitalBoard,
                  address=2,
                  comment="arbitrary board description")

    board_lst.add("ttl3",
                  lib_board.DigitalBoard,
                  address=3,
                  comment="arbitrary board description")


############   DAC    #################

    board_lst.add("ANG11", lib_board.AnalogBoard,
                  address=11,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))

    board_lst.add("ANG12", lib_board.AnalogBoard,
                  address=12,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))

    board_lst.add("ANG13", lib_board.AnalogBoard,
                  address=13,
                  parameters=dict(ang_to_dig={1: lambda x: 0.5*float(x)*32767*1.0/10}))

    board_lst.add("ANG14", lib_board.AnalogBoard,
                  address=14,
                  parameters=dict(ang_to_dig={1: lambda x: 0.5*float(x)*32767*1.0/10}))

    board_lst.add("ANG15", lib_board.AnalogBoard,
                  address=15,
                  parameters=dict(ang_to_dig={1: lambda x: 0.5*float(x)*32767*1.0/10}))

    board_lst.add("ANG16", lib_board.AnalogBoard,
                  address=16,
                  parameters=dict(ang_to_dig={1: lambda x: 0.5*float(x)*32767*1.0/10}))

    board_lst.add("ANG17", lib_board.AnalogBoard,
                  address=17,
                  parameters=dict(ang_to_dig={1: lambda x: 0.05*float(x)*32767*1.0/10}))

    board_lst.add("ANG18", lib_board.AnalogBoard,
                  address=18,
                  parameters=dict(ang_to_dig={1: lambda x: (5.0/15.3)*float(x)*32767*1.0/10}))

    board_lst.add("ANG19", lib_board.AnalogBoard,
                  address=19,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))

    board_lst.add("ANG20", lib_board.AnalogBoard,
                  address=20,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
    
    board_lst.add("ANG21", lib_board.AnalogBoard,
                  address=21,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))

    board_lst.add("ANG22", lib_board.AnalogBoard,
                  address=22,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))

    board_lst.add("ANG60", lib_board.AnalogBoard,
                  address=60,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
    board_lst.add("ANG61", lib_board.AnalogBoard,
                  address=61,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
