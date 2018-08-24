#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : grid_to_thickness.py
Purpose : get thickness/topo of transition zone from grid file
Creation Date : 21-08-2018
Last Modified : Fri 24 Aug 2018 10:34:56 AM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir
import h5py
import argparse

def main():
    parser = argparse.ArgumentParser(description='make GMT file for plot')
    parser.add_argument('-f','--file', metavar='H5_FILE',type=str,
                        help='h5 grid file')
    parser.add_argument('-d','--dis', metavar='discont',type=int,
                        help='discontinuity depth')
    parser.add_argument('-n','--name', type=str,
                       help='filename',default='discont_topo.dat')
    args = parser.parse_args()

    f = h5py.File(args.file,'r')
    gc = f['grid_count'][:]+1
    gcmask = np.mean(gc,axis=2)
    gcmask[gcmask < 500] = 0.
    gcmask[gcmask >= 500] = 1.
    grid = f['grid'][:]*(1./gc)
    h = f['h'][:]
    idx = np.where(h==args.dis)[0][0]
    m = np.argmax(grid[:,:,idx-50:idx+50],axis=2)
    m = args.dis-((args.dis-50)+(m))
    m = m*gcmask
    lat = f['lat'][:]
    lon = f['lon'][:]
    yy,xx = np.meshgrid(lat,lon)
    yy = np.reshape(yy,yy.size)
    xx = np.reshape(xx,xx.size)
    m = np.reshape(m,m.size)
    #plt.imshow(gcmask,aspect='auto')
    #plt.show()
    gcmask = np.reshape(gcmask,gcmask.size)
    np.savetxt(args.name,np.c_[xx,yy,m])
    np.savetxt('mask_'+args.name,np.c_[xx,yy,gcmask])

main()



