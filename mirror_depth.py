#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : mirror_depth.py
Purpose : Demonstrate the mirroring depth of ScS reverberations
Creation Date : 15-02-2018
Last Modified : Thu 15 Feb 2018 11:01:16 AM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import obspy
from obspy.taup import TauPyModel
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def main():
    fig,ax = setup_figure()
    gcarc = 40
    h = np.arange(50,1850,50)

    top_list,bot_list = depth_time(h,670,gcarc)
    idx = np.argmin(np.abs(np.array(top_list)-np.array(bot_list)))
    ax.axvline(h[idx],lw=0.5,color='k')
    ax.plot(h,top_list,color='#C92323',zorder=0)
    ax.plot(h,bot_list,color='#C92323',ls='--',zorder=0)
    ax.text(1440,1728,'h=670 km',size=8,rotation=30,color='#C92323')
    ax.text(h[idx]-60,1190,str(h[idx])+' km',size=8,rotation=90)

    top_list,bot_list = depth_time(h,60,gcarc)
    idx = np.argmin(np.abs(np.array(top_list)-np.array(bot_list)))
    ax.axvline(h[idx],lw=0.5,color='k')
    ax.plot(h,top_list,color='#23C9C9',zorder=1)
    ax.plot(h,bot_list,color='#23C9C9',ls='--',zorder=1)
    ax.text(1440,1600,'h=60 km',size=8,rotation=30,color='#23C9C9')
    ax.text(h[idx]-60,1200,str(h[idx])+' km',size=8,rotation=90)

    ax.text(211,1392,'Top side',size=8,rotation=40)
    ax.text(211,1657,'Bottom side',size=8,rotation=-40)
    plt.tight_layout()
    plt.savefig('mirror_depth.pdf')
    plt.show()

def depth_time(h,evdp,gcarc):
    bot_list = []
    top_list = []
    for ii in h:
        model = TauPyModel(model='prem'+str(ii))
        top_phase = 'sSvXSScS'.replace('X',str(ii))
        bot_phase = 'ScS^XScS'.replace('X',str(ii))
        top_arr = model.get_travel_times(source_depth_in_km=evdp,
                               distance_in_degree=gcarc,
                               phase_list=[top_phase])
        bot_arr = model.get_travel_times(source_depth_in_km=evdp,
                               distance_in_degree=gcarc,
                               phase_list=[bot_phase])
        top_list.append(top_arr[0].time)
        bot_list.append(bot_arr[0].time)
    return top_list,bot_list

def setup_figure():
    fig,ax = plt.subplots(figsize=(5,5))
    yminorLocator = MultipleLocator(10)
    xminorLocator = MultipleLocator(50)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.set_title('Mirroring depths',size=14)
    ax.set_xlabel('Reflection depth (km)',size=12)
    ax.set_ylabel('Arrival time (s)',size=12)
    ax.tick_params(axis='both',which='major',labelsize=8)
    #ax.tick_params(direction='out', length=6, width=2, colors='r')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return fig,ax



main()
