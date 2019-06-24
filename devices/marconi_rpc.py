#!/usr/bin/env python
#

import argparse
import zerorpc


parser = argparse.ArgumentParser(description='Set Marconi')
parser.add_argument('-f', '--freq', type=float,help='uw freq MHz')
parser.add_argument('-a', '--amp', type=float, help='uw amp dBm')                   
args = parser.parse_args()

client = zerorpc.Client()
client.connect('tcp://192.168.1.153:4986')

client.set_params(args.freq*1e6, args.amp)
