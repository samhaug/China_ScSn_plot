#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_beachball_list.py
Purpose : make file for gmt psmeca to read and plot beachballs on map
Creation Date : 19-02-2018
Last Modified : Tue 20 Feb 2018 12:01:55 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from subprocess import call
import obspy
from os import listdir
import argparse

def main():
    parser = argparse.ArgumentParser(description='make beachball list 4 psmeca')
    parser.add_argument('-d','--dir_list',metavar='string',type=str,
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
