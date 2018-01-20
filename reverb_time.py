#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : reverb_time.py
Purpose : Make plot of reverberation time differences
Creation Date : 20-12-2017
Last Modified : Sat 20 Jan 2018 01:48:08 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from obspy.taup import TauPyModel
from subprocess import call
mod = TauPyModel(model='prem50')

def main():
    fig,ax = fig_setup()
    top_depth_times(20,ax,'k',660)
    top_depth_times(200,ax,'k',660)
    top_depth_times(400,ax,'k',660)
    top_depth_times(640,ax,'k',660)
    bot_depth_times(20,ax,'b',660)
    bot_depth_times(200,ax,'b',660)
    bot_depth_times(400,ax,'b',660)
    bot_depth_times(640,ax,'b',660)

    top_depth_times(20,ax,'r',410)
    top_depth_times(200,ax,'r',410)
    top_depth_times(400,ax,'r',410)
    top_depth_times(640,ax,'r',410)
    bot_depth_times(20,ax,'orange',410)
    bot_depth_times(200,ax,'orange',410)
    bot_depth_times(400,ax,'orange',410)
    bot_depth_times(640,ax,'orange',410)

    top_depth_times(20,ax,'purple',200)
    top_depth_times(200,ax,'purple',200)
    top_depth_times(400,ax,'purple',200)
    top_depth_times(640,ax,'purple',200)
    bot_depth_times(20,ax,'green',200)
    bot_depth_times(200,ax,'green',200)
    bot_depth_times(400,ax,'green',200)
    bot_depth_times(640,ax,'green',200)

    top_depth_times(20,ax,'purple',300)
    top_depth_times(200,ax,'purple',300)
    top_depth_times(400,ax,'purple',300)
    top_depth_times(640,ax,'purple',300)
    bot_depth_times(20,ax,'green',300)
    bot_depth_times(200,ax,'green',300)
    bot_depth_times(400,ax,'green',300)
    bot_depth_times(640,ax,'green',300)

    top_depth_times(20,ax,'purple',500)
    top_depth_times(200,ax,'purple',500)
    top_depth_times(400,ax,'purple',500)
    top_depth_times(640,ax,'purple',500)
    bot_depth_times(20,ax,'green',500)
    bot_depth_times(200,ax,'green',500)
    bot_depth_times(400,ax,'green',500)
    bot_depth_times(640,ax,'green',500)

    plt.savefig('reverb_time.pdf')
    plt.show()
    call('evince reverb_time.pdf',shell=True)

def top_depth_times(depth,ax,color,conv):
    conv = str(conv)
    time_list = []
    for ii in range(0,80):
        arr = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=ii,
                                   phase_list=['sScS','sSv'+conv+'SScS'])
        time = arr[1].time-arr[0].time
        time_list.append(time)

    ax.plot(range(0,80),time_list,lw=0.8,color=color)

def bot_depth_times(depth,ax,color,conv):
    conv = str(conv)
    time_list = []
    for ii in range(0,80):
        arr = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=ii,
                                   phase_list=['ScSScS','ScS^'+conv+'ScS'])
        time = arr[1].time-arr[0].time
        time_list.append(time)

    ax.plot(range(0,80),time_list,lw=0.8,color=color)

def fig_setup():
    fig,ax = plt.subplots()
    ax.set_xlabel('Distance (deg)')
    ax.set_ylabel(r'$\Delta t$')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    return fig,ax


main()
