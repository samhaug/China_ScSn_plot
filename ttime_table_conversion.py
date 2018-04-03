#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : ttime_table.py
Purpose : make traveltime plots
Creation Date : 20-12-2017
Last Modified : Tue 03 Apr 2018 12:10:35 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from obspy.taup import TauPyModel
from subprocess import call
from matplotlib.ticker import MultipleLocator
from collections import OrderedDict
import argparse

def main():
    parser = argparse.ArgumentParser(description='make xyz gridcount file')
    parser.add_argument('-d','--evdp',type=int,
                       help='event depth')
    parser.add_argument('-g','--gcarc',type=int,
                       help='distance in degree')
    args = parser.parse_args()
    fig,ax = fig_setup()
    evdp = args.evdp
    gcarc = args.gcarc
    ax.set_title('evdp: {} km, gcarc: {} deg'.format(evdp,gcarc))
    main_phases = ['ScS','sScS','ScSScS','sScSScS','ScSScSScS','sScSScSScS']
    main_phase_name = ['ScS','sScS','ScS_{2}','sScS_{2}','ScS_{3}','sScS_{3}']
    for idx,phase in enumerate(main_phases):
        plot_zeroth_order(phase,evdp,gcarc,ax,main_phase_name[idx])
    conv_list = np.arange(100,805,5)
    c_dict = ttime_curves(conv_list,evdp,gcarc)
    for keys in c_dict:
        d = np.array(c_dict[keys])
        p = ax.plot(d[:,0],d[:,1],lw=0.8)
        c = p[0].get_color()
        deg = np.degrees(np.arctan2(d[-1,1]-d[-10,1],d[-1,0]-d[-10,0]))
        ax.text(500,d[int(len(d)/2.),1]+20,keys,size=8,color=c,rotation=deg)
    plt.tight_layout()
    plt.savefig('ttime_table_conversion.pdf')
    plt.show()
    call('evince ttime_table_conversion.pdf',shell=True)

def plot_zeroth_order(phase,depth,distance,ax,name):
    mod = TauPyModel(model='prem')
    arr = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=distance,
                                   phase_list=[phase])
    ax.axhline(arr[0].time,color='k',lw=0.8,alpha=0.5)
    ax.text(700,arr[0].time+20,r'$'+name+'$',size=8)

def ttime_curves(conv_list,depth,distance):
    c_dict = OrderedDict([('ScSSvXS',[]),('sSvXSScS',[]),
              ('ScS^XScS',[]),('sScS^XScS',[]),
              ('ScSSvXSScS',[]),
              ('ScSScSSvXS',[]),('sSvXSScSScS',[]),
              ('ScS^XScSScS',[]),('sScS^XScSScS',[]),
              ('ScSSvXSScSScS',[])])
    for dconv in conv_list:
        conv = str(dconv)
        c_list = ['ScSSv'+conv+'S','sSv'+conv+'SScS',
                  'ScS^'+conv+'ScS','sScS^'+conv+'ScS',
                  'ScSSv'+conv+'SScS',
                  'ScSScSSv'+conv+'S','sSv'+conv+'SScSScS',
                  'ScS^'+conv+'ScSScS','sScS^'+conv+'ScSScS',
                  'ScSSv'+conv+'SScSScS']
        mod = TauPyModel(model='prem'+conv)
        for idx,phase in enumerate(c_list):
            arr = mod.get_travel_times(source_depth_in_km=depth,
                                       distance_in_degree=distance,
                                       phase_list=[phase])
            c_dict[c_dict.keys()[idx]].append((dconv,arr[0].time))

    return c_dict

def fig_setup():
    fig,ax = plt.subplots(figsize=(5,9))
    ax.set_xlabel('conversion_depth')
    ax.set_ylabel(r'$Arrival time (s)$')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    yminorLocator = MultipleLocator(100)
    ax.yaxis.set_minor_locator(yminorLocator)
    xminorLocator = MultipleLocator(10)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.set_xlim(100,850)

    return fig,ax


main()
