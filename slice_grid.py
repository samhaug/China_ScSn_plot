#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : slice_grid.py
Purpose : plot a slice of a CRP grid between two coordinates
Creation Date : 25-01-2018
Last Modified : Tue 30 Jan 2018 02:33:07 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import h5py
import argparse
from scipy.interpolate import RegularGridInterpolator


def main():
    parser = argparse.ArgumentParser(description='plot_reflection_points')
    parser.add_argument('-g','--grid',metavar='H5_FILE',type=str,
                        help='h5 grid CRP file')
    parser.add_argument('-c','--coords',metavar='float',type=float,nargs=4,
                        help='lat_1 lon1 lat_2 lon_2')
    args = parser.parse_args()
    lat_1 = args.coords[0]
    lon_1 = args.coords[1]
    lat_2 = args.coords[2]
    lon_2 = args.coords[3]
    g = h5py.File(args.grid,'r',driver='core')

    latspace = np.linspace(lat_1,lat_2,num=100)
    lonspace = np.linspace(lon_1,lon_2,num=100)
    #hspace = g['h'][:]
    hspace = np.linspace(200,700,num=500)
    hgrid_one,latgrid_one = np.meshgrid(hspace,latspace)
    hgrid_one,longrid_one = np.meshgrid(hspace,lonspace)
    hgrid = np.transpose([np.ravel(hgrid_one)])
    latgrid = np.transpose([np.ravel(latgrid_one)])
    longrid = np.transpose([np.ravel(longrid_one)])
    coords = np.hstack((longrid,latgrid,hgrid))
    print coords.shape

    grid_count = g['grid_count'][:]
    grid_count[grid_count == 0] = 1.
    grid = g['grid'][:]
    grid *= 1./grid_count
    lat = g['lat'][:]
    lon = g['lon'][:]
    h = g['h'][:]
    g.close()
    if lat_1 > max(lat) or lat_1 < min(lat):
        print 'lat_1 out of range'
    if lat_2 > max(lat) or lat_2 < min(lat):
        print 'lat_2 out of range'
    if lon_1 > max(lon) or lon_1 < min(lon):
        print 'lon_1 out of range'
    if lon_2 > max(lon) or lon_2 < min(lon):
        print 'lon_2 out of range'

    int3d = RegularGridInterpolator((lon,lat,h),grid)
    cross_section = int3d(coords)
    cross_section = np.reshape(cross_section,hgrid_one.shape).T
    plt.imshow(cross_section,aspect='auto',extent=[0,1,700,200])
    plt.show()


main()



