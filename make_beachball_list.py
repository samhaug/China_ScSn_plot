#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_beachball_list.py
Purpose : make file for gmt psmeca to read and plot beachballs on map
Creation Date : 19-02-2018
Last Modified : Thu 17 May 2018 04:30:33 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir
from glob import glob
import argparse

def main():
    parser = argparse.ArgumentParser(description='make beachball list 4 psmeca')
    parser.add_argument('-d','--dir_list',metavar='string',type=str,
                       help='comma delimited list of direcories')
    parser.add_argument('-f','--out_file',metavar='string',type=str,
                       help='output file name',default='beachballs.dat')
    args = parser.parse_args()
    #dir_list = args.dir_list.split(',')
    dir_list = glob(args.dir_list)

    outfile = file(args.out_file,'w')
    for d in dir_list:
        #string = read_cmt(d+'/axisem_input_'+d+'/CMTSOLUTION')
        string = read_cmt(d+'/input/CMTSOLUTION')
        outfile.write(string+'\n')

def read_cmt(path_to_cmt):
    f = open(path_to_cmt).readlines()
    lat = float(f[4].strip().split()[1])
    lon = float(f[5].strip().split()[1])
    h =   float(f[6].strip().split()[1])
    e = int(np.floor(np.log10(np.abs(float(f[7].strip().split()[1])))))
    mrr = float(f[7].strip().split()[1])/10**e
    mtt = float(f[8].strip().split()[1])/10**e
    mpp = float(f[9].strip().split()[1])/10**e
    mrt = float(f[10].strip().split()[1])/10**e
    mrp = float(f[11].strip().split()[1])/10**e
    mtp = float(f[12].strip().split()[1])/10**e
    string = '{} {} {} {} {} {} {} {} {} {} {} {}'.format(
            lon,lat,h,mrr,mtt,mpp,mrt,mrp,mtp,e,lon,lat)
    return string

main()
