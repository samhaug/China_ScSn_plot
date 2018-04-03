#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_count_map.py
Purpose : plot spherical harmonics
Creation Date : 17-02-2018
Last Modified : Tue 03 Apr 2018 12:38:32 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
import h5py
import argparse


def main():
    parser = argparse.ArgumentParser(description='make_count_map')
    parser.add_argument('-f','--file',metavar='file',type=str,
                        help='grid file')
    args = parser.parse_args()
    f = h5py.File(args.file,'r')
    gc = f['grid_count'][:]
    gc += -1*gc.min()
    gc = np.flipud(np.transpose(np.log10(np.mean(gc,axis=2))))
    lat = f['lat'][:]
    lon = f['lon'][:]
    xx,yy = np.meshgrid(lon,lat)
    gc = np.ravel(gc)
    xx = np.ravel(xx)
    yy = np.ravel(yy)
    np.savetxt('count_map.dat',np.c_[xx,yy,gc],fmt='%8.3f')

main()

