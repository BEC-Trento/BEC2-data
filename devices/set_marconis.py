#!/usr/bin/env python
#

import argparse
import zerorpc


parser = argparse.ArgumentParser(description='Set Marconi')
parser.add_argument('-f1', '--freq1', type=float,help='uw freq1 MHz')
parser.add_argument('-a1', '--amp1', type=float, help='uw amp1 dBm')    
parser.add_argument('-f2', '--freq2', type=float,help='uw freq2 MHz')
parser.add_argument('-a2', '--amp2', type=float, help='uw amp2 dBm')                 
args = parser.parse_args()

client1 = zerorpc.Client()
client1.connect('tcp://192.168.1.153:4987')

client2 = zerorpc.Client()
client2.connect('tcp://192.168.1.153:4986')

m1 = client1.set_params(args.freq1*1e6, args.amp1, async=True)
m2 = client2.set_params(args.freq2*1e6, args.amp2, async=True)

for m in [m1, m2]:
    print(m.get())
