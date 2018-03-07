#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : reverb_trace_illustrate.py
Purpose : Make many illustrative figures of ScS reverb from synth trace
Creation Date : 23-02-2018
Last Modified : Tue 06 Mar 2018 08:00:34 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir
import obspy
from obspy.taup import TauPyModel
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
model = TauPyModel(model='prem')


def main():
    fig,ax = setup_figure()
    syn_path='/home/samhaug/work1/China_ScSn_data/China_array/20120814/sts_T.h5'
    dat_path='/home/samhaug/work1/China_ScSn_data/China_array/20120814/st_T_clean.h5'
    tr = return_trace(syn_path,dat_path,50)

    t = np.linspace(tr.stats.o,tr.stats.npts/tr.stats.sampling_rate+tr.stats.o,num=tr.stats.npts)
    ax.plot(t,tr.data,color='r',lw=0.8)
    plt.savefig('reverb_trace_illustrate.png',dpi=300)

def return_ttime(tr,parent,child):
    parent_arr =  model.get_travel_times(source_depth_in_km=tr.stats.evdp,
                           distance_in_degree=tr.stats.gcarc,
                           phase_list=[parent])
    child_arr = model.get_travel_times(source_depth_in_km=tr.stats.evdp,
                           distance_in_degree=tr.stats.gcarc,
                           phase_list=[child])
    parent_t = parent_arr[0].time
    child_t = child_arr[0].time
    print parent_t,child_t
    return parent_t,child_t

def return_trace(syn_path,dat_path,idx):
    sts = obspy.read(syn_path)
    #std = obspy.read(dat_path)
    #s = []
    #d = []
    #for tr in sts:
    #    tr.stats.name = tr.stats.network+tr.stats.station+tr.stats.location
    #    s.append(tr.stats.name)
    #for tr in std:
    #    tr.stats.name = tr.stats.network+tr.stats.station+tr.stats.location
    #    d.append(tr.stats.name)
    #c = set(s).intersection(set(d))
    #for tr in sts:
    #    if tr.stats.name not in c:
    #        sts.remove(tr)
    #for tr in std:
    #    if tr.stats.name not in c:
    #        std.remove(tr)
    #sts.sort(['name'])
    #std.sort(['name'])

    trs = sts[idx]
    #trd = std[idx]
    #trd.filter('bandpass',freqmin=1./100,freqmax=1./10,zerophase=True)
    trs.filter('bandpass',freqmin=1./100,freqmax=1./10,zerophase=True)
    trs.normalize()
    #trd.normalize()
    trs.data *= 50
    #trd.data *= 80
    return trs

def setup_figure():
    fig,ax = plt.subplots(figsize=(12,5))
    #plt.tight_layout()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_ticklabels([])
    ax.yaxis.set_ticks([])
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_ylim(-5,5)
    ax.set_xlim(800,3400)
    ax.xaxis.set_ticks(np.arange(800,3600,200))
    ax.spines['bottom'].set_bounds(800,3400)
    minorLocator = MultipleLocator(50)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.set_xlabel('Time (s)',size=16)
    return fig,ax

main()




