#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : reflection_points.py
Purpose : Plot ScS reflection points
Creation Date : 19-01-2018
Last Modified : Sat 20 Jan 2018 05:10:29 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import h5py
import argparse

def main():
    parser = argparse.ArgumentParser(description='plot_reflection_points')
    parser.add_argument('-f','--ref_points',metavar='H5_FILE',type=str,
                        help='h5 reflection_points')
    parser.add_argument('-s','--stride',metavar='integer',default=1,type=int,
                        help='plot every nth station')
    parser.add_argument('-d','--depth',metavar='float',default=670,type=int,
                        help='conversion depth')
    args = parser.parse_args()

    f = h5py.File(args.ref_points,'r')

    for keys in f.keys()[::args.stride]:
        

main()
