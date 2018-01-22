#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : reflection_points.py
Purpose : Plot ScS reflection points
Creation Date : 19-01-2018
Last Modified : Mon 22 Jan 2018 11:09:42 AM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import h5py
from mpl_toolkits.basemap import Basemap
import argparse

def main():
    parser = argparse.ArgumentParser(description='plot_reflection_points')
    parser.add_argument('-f','--ref_points',metavar='H5_FILE',type=str,
                        help='h5 reflection_points')
    parser.add_argument('-s','--stride',metavar='integer',default=1,type=int,
                        help='plot every nth station')
    parser.add_argument('-d','--depth',metavar='float',default=670,type=int,
                        help='conversion depth')
    parser.add_argument('-p','--phase',metavar='string',default='all',type=str,
                        help='Phase name')
    args = parser.parse_args()

    f = h5py.File(args.ref_points,'r')

    fig = plt.figure(figsize=(10,10))
    m = Basemap(llcrnrlon=80,llcrnrlat=-20,urcrnrlon=180,
            urcrnrlat=60,projection='mill')
    m.drawcoastlines(linewidth=1.2)

    coords = f[f.keys()[0]]['coords'][:]
    x,y = m(coords[5],coords[4])
    m.scatter(x,y,marker='*',color='r',s=100)
    for ikeys in f.keys()[::args.stride]:
        coords = f[ikeys]['coords'][:]
        x,y = m(coords[3],coords[2])
        m.scatter(x,y,marker='1',alpha=0.3,color='k')

        for jkeys in f[ikeys]:
            if args.phase == 'all':
                if not jkeys.startswith('c'):
                    try:
                        bounce = f[ikeys][jkeys][str(args.depth)][:]
                    except KeyError:
                        continue
                    for ii in bounce:
                        x,y = m(ii[1],ii[0])
                        if jkeys == 'ScSScS':
                            m.scatter(x,y,marker='+',alpha=0.3,
                                      color='r',rasterized=True)
                        if jkeys == 'ScScSScS':
                            m.scatter(x,y,marker='+',alpha=0.3,
                                     color='g',rasterized=True)
                        if jkeys == 'sScS':
                            m.scatter(x,y,marker='+',alpha=0.3,
                                     color='b',rasterized=True)
                        if jkeys == 'sScSScS':
                            m.scatter(x,y,marker='+',alpha=0.3,
                                     color='orange',rasterized=True)
                        if jkeys == 'sScSScSScS':
                            m.scatter(x,y,marker='+',alpha=0.3,
                                     color='purple',rasterized=True)
            else:
                try:
                    bounce = f[ikeys][args.phase][str(args.depth)][:]
                except KeyError:
                    continue
                for ii in bounce:
                    x,y = m(ii[1],ii[0])
                    if args.phase == 'ScSScS':
                        m.scatter(x,y,marker='+',alpha=0.3,
                                  color='r',rasterized=True)
                    if args.phase == 'ScScSScS':
                        m.scatter(x,y,marker='+',alpha=0.3,
                                 color='g',rasterized=True)
                    if args.phase == 'sScS':
                        m.scatter(x,y,marker='+',alpha=0.3,
                                 color='b',rasterized=True)
                    if args.phase == 'sScSScS':
                        m.scatter(x,y,marker='+',alpha=0.3,
                                 color='orange',rasterized=True)
                    if args.phase == 'sScSScSScS':
                        m.scatter(x,y,marker='+',alpha=0.3,
                                 color='purple',rasterized=True)

    plt.show()


main()
