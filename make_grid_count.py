#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_grid_count.py
Purpose : make xyz file for grid count values
Creation Date : 19-02-2018
Last Modified : Tue 20 Feb 2018 03:39:13 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from subprocess import call
import obspy
from os import listdir
import argparse

def main():
    parser = argparse.ArgumentParser(description='make xyz gridcount file')
    parser.add_argument('-f','--file',metavar='H5 FILE',type=str,
                       help='comma delimited list of direcories')
    args = parser.parse_args()
    dir_list = args.dir_list.split(',')
    outfile = file('stations.dat','w')
    for d in dir_list:
        st = obspy.read(d+'/sts_T.h5')
        for tr in st:
            string = '{} {}'.format(tr.stats.stlo,tr.stats.stla)
            outfile.write(string+'\n')
    outfile.close()

main()
