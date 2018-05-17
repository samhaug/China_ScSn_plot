#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : reverb_trace_illustrate.py
Purpose : Make many illustrative figures of ScS reverb from synth trace
Creation Date : 23-02-2018
Last Modified : Sun 29 Apr 2018 02:45:37 PM EDT
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
    trs,trd = return_trace(syn_path,dat_path,581)

    td = np.linspace(-1*trd.stats.o,trd.stats.npts/trd.stats.sampling_rate+-1*trd.stats.o,
                     num=trd.stats.npts)
    ts = np.linspace(0,trs.stats.npts/trs.stats.sampling_rate,num=trs.stats.npts)
    print trs.stats.gcarc
    print trd.stats.gcarc
    ax.plot(ts,2.5*trs.data/np.abs(trs.data).max(),color='r',lw=0.8)
    ax.plot(td,1+1.5*trd.data/np.abs(trd.data).max(),color='k',lw=0.8)
    ax.text(1000,3,str(int(trs.stats.gcarc)))
    ax.text(1000,3.5,str(int(trs.stats.evdp)))
    plt.savefig('reverb_trace_illustrate.pdf')
    plt.show()

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
    std = obspy.read(dat_path)
    sts.sort(['gcarc'])
    std.sort(['gcarc'])
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
    trd = std[idx]
    trd.filter('bandpass',freqmin=1./100,freqmax=1./10,zerophase=True)
    trs.filter('bandpass',freqmin=1./100,freqmax=1./10,zerophase=True)
    trs.normalize()
    trd.normalize()
    return trs,trd

def setup_figure():
    fig,ax = plt.subplots(figsize=(7.5,3))
    plt.tight_layout()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_ticklabels([])
    ax.yaxis.set_ticks([])
    ax.tick_params(axis='both', which='major', labelsize=8)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_ylim(-2,4)
    ax.set_xlim(800,3400)
    ax.xaxis.set_ticks(np.arange(800,3600,200))
    ax.spines['bottom'].set_bounds(800,3400)
    minorLocator = MultipleLocator(50)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.set_xlabel('Time (s)',size=12)
    return fig,ax

main()




