#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : slice_grid.py
Purpose : plot a slice of a CRP grid between two coordinates
Creation Date : 25-01-2018
<<<<<<< HEAD
Last Modified : Thu 17 May 2018 05:45:01 PM EDT
=======
Last Modified : Thu 17 May 2018 04:03:56 PM EDT
>>>>>>> cd5d229ead33328ef8d5b9fb9b4a90762978ab52
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import sys
import h5py
import argparse
from scipy.interpolate import RegularGridInterpolator
import matplotlib.gridspec as gridspec


def main():
    parser = argparse.ArgumentParser(description='plot_reflection_points')
    parser.add_argument('-g','--grid',metavar='H5_FILE',type=str,
                        help='h5 grid CRP file')
    parser.add_argument('-c','--coords',metavar='float',type=float,nargs=4,
                        help='lat_1 lon1 lat_2 lon_2')
    parser.add_argument('-s','--ScS2',action='store_true',
                        help='only plot ScS2')
    args = parser.parse_args()
    lat_1 = args.coords[0]
    lon_1 = args.coords[1]
    lat_2 = args.coords[2]
    lon_2 = args.coords[3]
    g = h5py.File(args.grid,'r',driver='core')

    latspace = np.linspace(lat_1,lat_2,num=200)
    lonspace = np.linspace(lon_1,lon_2,num=200)
    #hspace = g['h'][:]
    hspace = np.arange(50,805,5)
    hgrid_one,latgrid_one = np.meshgrid(hspace,latspace)
    hgrid_one,longrid_one = np.meshgrid(hspace,lonspace)

    hgrid = np.transpose([np.ravel(hgrid_one)])
    latgrid = np.transpose([np.ravel(latgrid_one)])
    longrid = np.transpose([np.ravel(longrid_one)])
    coords = np.hstack((longrid,latgrid,hgrid))

    if args.ScS2:
        grid_count = g['grid_count_ScS2'][:]
        grid_count[grid_count == 0] = 1.
        grid = g['grid_ScS2'][:]
    else:
        grid_count = g['grid_count'][:]
        grid_count[grid_count == 0] = 1.
        grid = g['grid'][:]
    #grid *= 1./grid_count
    lat = g['lat'][:]
    lon = g['lon'][:]
    h = g['h'][:]
    #print lon.shape
    #print lat.shape
    #print h.shape
    #print grid.shape
    g.close()

    if lat_1 > max(lat) or lat_1 < min(lat):
        print 'lat_1 out of range'
        print min(lat),max(lat),
        sys.exit()
    if lat_2 > max(lat) or lat_2 < min(lat):
        print 'lat_2 out of range'
        print min(lat),max(lat)
        sys.exit()
    if lon_1 > max(lon) or lon_1 < min(lon):
        print 'lon_1 out of range'
        print min(lon),max(lon)
        sys.exit()
    if lon_2 > max(lon) or lon_2 < min(lon):
        print 'lon_2 out of range'
        print min(lon),max(lon)
        sys.exit()

    fig,ax0,ax1 = setup_figure()
    int3d = RegularGridInterpolator((lon,lat,h),grid)
    count_int3d = RegularGridInterpolator((lon,lat,h),grid_count)
    cross_section = int3d(coords)
    count_cross_section = count_int3d(coords)
    cross_section = np.reshape(cross_section,hgrid_one.shape).T
    count_cross_section = np.reshape(count_cross_section,hgrid_one.shape).T
    count = np.sum(count_cross_section,axis=0)/count_cross_section.shape[0]
    x = np.linspace(0,200,num=len(count))
    ax1.fill_between(x,count,0,color='k')

    for ii in range(cross_section.shape[1]):
        cross_section[:,ii] *= 1./np.max(np.abs(cross_section[:,ii]))
    ax0.imshow(cross_section,aspect='auto',extent=[0,200,800,50],alpha=1.7,
               cmap='coolwarm',interpolation='lanczos')
    ax0.axhline(400,c='green',lw=1.5,ls='--')
    ax0.axhline(670,c='green',lw=1.5,ls='--')
    plot_wiggles(cross_section,hspace,ax0)

    plt.savefig('slice_grid.png')
    plt.show()

def setup_figure():
    #fig,ax = plt.subplots(2,1,figsize=(15,5))
    fig = plt.figure(figsize=(12,8))
    gs = gridspec.GridSpec(100,100)
    ax0 = plt.subplot(gs[0:80,:])
    ax1 = plt.subplot(gs[80::,:])
    ax1.set_xlim(0,200)
    ax0.set_ylim(800,300)
    ax0.set_xlim(0,200)

    ax0.get_xaxis().set_ticks([])
    ax1.get_xaxis().set_ticks([])
    ax0.tick_params(axis='both', which='major', labelsize=8)
    ax1.tick_params(axis='both', which='major', labelsize=8)
    ax0.set_ylabel('Depth (km)',size=12)
    ax1.set_ylabel('Counts',size=12)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.grid()
    plt.tight_layout()
    return fig,ax0,ax1

def plot_wiggles(cross_section,h,ax,color='k',alpha=0.4,zorder=0):
    for idx,ii in enumerate(range(cross_section.shape[1])[::2]):
        wiggle = cross_section[:,ii]/np.max(np.abs(cross_section[:,ii]))
        ax.fill_betweenx(h,2*wiggle+2*idx,2*idx,
                        where=wiggle+2*idx >= 2*idx,
                        facecolor=color,lw=0.5,alpha=alpha)
        ax.plot(2*wiggle+2*idx,h,lw=0.5,alpha=1.0,color='k')

main()



