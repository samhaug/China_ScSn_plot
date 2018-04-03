#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : ttime_table.py
Purpose : make traveltime plots
Creation Date : 20-12-2017
Last Modified : Tue 03 Apr 2018 10:20:59 AM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from obspy.taup import TauPyModel
from subprocess import call
from matplotlib.ticker import MultipleLocator
import argparse

def main():
    parser = argparse.ArgumentParser(description='make xyz gridcount file')
    parser.add_argument('-d','--evdp',type=int,
                       help='event depth')
    parser.add_argument('-c','--cvdp',type=int,
                       help='depth of conversion')
    args = parser.parse_args()
    fig,ax = fig_setup()
    #peg_depth_times(200,35,ax)
    evdp = args.evdp
    cvdp = args.cvdp
    ttime_curves(evdp,cvdp,ax)
    ax.set_title('evdp: {} km, conv depth: {} km'.format(evdp,cvdp))
    plt.savefig('ttime_table.pdf')
    #plt.show()
    call('evince ttime_table.pdf',shell=True)

def ttime_curves(depth,conv,ax):
    conv = str(conv)
    time_dict = {}
    peg_dict = {'ScS':[],'ScSSv'+conv+'S':[]}
    top_dict = {'sScS':[],'sSv'+conv+'SScS':[]}
    bot_dict = {'ScSScS':[],'ScS^'+conv+'ScS':[]}
    other_dict = {'sScS^'+conv+'ScS':[],'ScSSv'+conv+'SScS':[]}
    mod = TauPyModel(model='prem'+conv)

    for ii in np.linspace(0,50):
        arr_peg = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=ii,
                                   phase_list=['ScS','ScSSv'+conv+'S'])
        peg_dict['ScS'].append(arr_peg[0].time)
        peg_dict['ScSSv'+conv+'S'].append(arr_peg[1].time)

        arr_top = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=ii,
                                   phase_list=['sScS','sSv'+conv+'SScS'])
        top_dict['sScS'].append(arr_top[0].time)
        top_dict['sSv'+conv+'SScS'].append(arr_top[1].time)

        arr_bot = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=ii,
                                   phase_list=['ScS^'+conv+'ScS','ScSScS'])
        bot_dict['ScSScS'].append(arr_bot[1].time)
        bot_dict['ScS^'+conv+'ScS'].append(arr_bot[0].time)

        arr_other = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=ii,
                                   phase_list=['sScS^'+conv+'ScS',
                                               'ScSSv'+conv+'SScS'])
        other_dict['sScS^'+conv+'ScS'].append(arr_other[1].time)
        other_dict['ScSSv'+conv+'SScS'].append(arr_other[0].time)

    for keys in peg_dict:
        ax.plot(np.linspace(0,50),np.array(peg_dict[keys]),lw=1.0,
                label=keys,ls='-')
    for keys in top_dict:
        ax.plot(np.linspace(0,50),np.array(top_dict[keys]),lw=1.0,label=keys,
                ls='-',color='k',alpha=0.5)
    for keys in bot_dict:
        ax.plot(np.linspace(0,50),np.array(bot_dict[keys]),lw=1.0,label=keys,
                ls='-',color='k',alpha=0.5)
    for keys in other_dict:
        ax.plot(np.linspace(0,50),np.array(other_dict[keys]),lw=1.0,label=keys,
                ls='-',color='k',alpha=0.5)
    ax.legend()

def peg_depth_times(depth,dist,ax):
    time_dict = {}
    peg_dict = {'ScS':[],'ScSSv#S':[]}
    top_dict = {'sScS':[],'sSv#SScS':[]}
    bot_dict = {'ScSScS':[],'ScS^#ScS':[]}

    for ii in np.arange(50,850,50):
        conv = str(int(ii))
        mod = TauPyModel(model='prem'+conv)
        arr_peg = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=dist,
                                   phase_list=['ScS','ScSSv'+conv+'S'])
        peg_dict['ScS'].append(arr_peg[0].time)
        peg_dict['ScSSv#S'].append(arr_peg[1].time)

        arr_top = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=dist,
                                   phase_list=['sScS','sSv'+conv+'SScS'])
        top_dict['sScS'].append(arr_peg[0].time)
        top_dict['sSv#SScS'].append(arr_peg[1].time)

        arr_bot = mod.get_travel_times(source_depth_in_km=depth,
                                   distance_in_degree=dist,
                                   phase_list=['ScS^'+conv+'ScS','ScSScS'])
        bot_dict['ScSScS'].append(arr_peg[1].time)
        bot_dict['ScS^#ScS'].append(arr_peg[0].time)

    print peg_dict['ScSSv#S']
    for keys in peg_dict:
        plt.plot(np.arange(50,850,50),np.array(peg_dict[keys]),lw=0.7)
    for keys in top_dict:
        plt.plot(np.arange(50,850,50),np.array(top_dict[keys]),lw=0.7)
    for keys in bot_dict:
        plt.plot(np.arange(50,850,50),np.array(bot_dict[keys]),lw=0.7)

def fig_setup():
    fig,ax = plt.subplots()
    ax.set_xlabel('Distance (deg)')
    ax.set_ylabel(r'$\Delta t$')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    yminorLocator = MultipleLocator(25)
    ax.yaxis.set_minor_locator(yminorLocator)
    xminorLocator = MultipleLocator(5)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.set_xlim(0,50)

    return fig,ax


main()
