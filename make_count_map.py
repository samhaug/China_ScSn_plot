#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_count_map.py
Purpose : plot spherical harmonics
Creation Date : 17-02-2018
Last Modified : Tue 03 Apr 2018 01:04:42 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
import h5py
import argparse
from matplotlib import pyplot as plt

def main():
    parser = argparse.ArgumentParser(description='make_count_map')
    parser.add_argument('-f','--file',metavar='file',type=str,
                        help='grid file')
    args = parser.parse_args()
    f = h5py.File(args.file,'r')
    gc = f['grid_count'][:]
    gc += -1*gc.min()
    gc += 0.001
    gc = np.log10(np.mean(gc,axis=2))
    #gc = np.fliplr(np.transpose(gc))
    lat = f['lat'][:]
    lon = f['lon'][:]
    print len(lon),len(lat)
    print gc.shape
    x = np.linspace(lon.min(),lon.max(),num=gc.shape[0])
    y = np.linspace(lat.min(),lat.max(),num=gc.shape[1])
    xx,yy = np.meshgrid(x,y)
    gc = np.ravel(gc)
    xx = np.transpose(np.ravel(xx))
    yy = np.transpose(np.ravel(yy))
    np.savetxt('count_map.dat',np.c_[xx,yy,gc],fmt='%8.3f')

main()

