#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : mean_wiggle.py
Purpose : plot vertical wiggles
Creation Date : 17-02-2018
Last Modified : Sat 17 Feb 2018 01:42:55 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import h5py
import argparse

def main():
    parser = argparse.ArgumentParser(description='plot_reflection_points')
    parser.add_argument('-d','--data',metavar='H5_FILE',type=str,
                        help='data gridfile',default='data_grid.h5')
    parser.add_argument('-s','--synth',metavar='H5_FILE',type=str,
                        help='synth gridfile',default='synth_grid.h5')
    args = parser.parse_args()
    fig,ax = setup_figure()
    data = h5py.File(args.data,'r',driver='core')
    synth = h5py.File(args.synth,'r',driver='core')
    get_wiggles(synth,ax,axes=0,color='r')
    get_wiggles(data,ax,axes=0,color='k',alpha=0.7)
    ax.set_ylim(data['h'][:].max(),data['h'][:].min())
    plt.show()
    data.close()
    synth.close()

def get_wiggles(f,ax,axes=1,color='k',alpha=0.5,zorder=0):
    grid = f['grid'][:]
    gc = f['grid_count'][:]+1
    grid *= 1./gc
    h = f['h'][:]
    for idx,ii in enumerate(np.mean(grid,axis=1)):
        wiggle = ii/np.max(np.abs(ii))
        wiggle = wiggle
        ax.fill_betweenx(h,wiggle+idx,idx,
                        facecolor=color,lw=0.5,alpha=alpha)


def setup_figure():
    fig,ax = plt.subplots(figsize=(8,5))
    return fig,ax


main()
