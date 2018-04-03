#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_count_map.py
Purpose : plot spherical harmonics
Creation Date : 17-02-2018
Last Modified : Tue 03 Apr 2018 01:38:11 PM EDT
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
    print gc.shape
    plt.imshow(gc,aspect='auto')
    plt.show()
    #gc = np.flipud(np.transpose(gc))
    lon = f['lon'][:]
    lat = f['lat'][:]
    print lon.shape,lat.shape
    xx,yy = np.meshgrid(lat,lon)
    print 'lon'
    print xx.shape
    plt.imshow(xx)
    plt.show()
    print 'lat'
    print yy.shape
    plt.imshow(yy)
    plt.show()
    gc = np.ravel(gc)
    xx = np.ravel(xx)
    yy = np.ravel(yy)
    plt.scatter(xx,yy,c=gc,lw=0)
    plt.show()
    np.savetxt('count_map.dat',np.c_[xx,yy,gc],fmt='%8.3f')

main()


