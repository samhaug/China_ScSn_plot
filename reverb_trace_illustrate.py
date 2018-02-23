#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : reverb_trace_illustrate.py
Purpose : Make many illustrative figures of ScS reverb from synth trace
Creation Date : 23-02-2018
Last Modified : Fri 23 Feb 2018 05:59:21 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir
import obspy
from obspy.taup import TauPyModel
model = TauPyModel(model='prem')

#gmt psxy datfiles/ScS2.dat -R$region -J$scale -Sa0.10c \
#    -G#27A2B5 -t50 -K -O >> $file.ps
#gmt psxy datfiles/ScS3.dat -R$region -J$scale -Sa0.10c \
#    -G#8127B5  -t50 -K -O >> $file.ps
#gmt psxy datfiles/sScS.dat -R$region -J$scale -Sa0.10c \
#    -G#B53A27 -t50 -K -O >> $file.ps
#gmt psxy datfiles/sScS2.dat -R$region -J$scale -Sa0.10c \
#    -G#5BB527 -t50 -K -O >> $file.ps
#gmt psxy datfiles/sScS3.dat -R$region -J$scale -Sa0.10c \
#    -G#B5AF27 -t50 -K -O >> $file.ps

def main():
    syn_path='/home/samhaug/work1/China_ScSn_data/China_array/20160413/sts_T.h5'
    #syn_path='/home/samhaug/work1/China_ScSn_data/China_array/20161019/sts_T.h5'
    tr = return_trace(syn_path)
    #fig,ax = plot_little_s(tr,'sScS','sSv670SScS')
    #fig,ax = plot_little_s(tr,'sScSScS','sSv670SScSScS')
    fig,ax = plot_big_s(tr,'ScSScS','ScS^670ScS')
    #fig,ax = plot_big_s(tr,'ScSScS','ScS^400ScS')
    #fig,ax = plot_big_s(tr,'ScSScS','ScS^220ScS')
    #fig,ax = plot_big_s(tr,'ScSScS','ScS^400ScS')
    #fig,ax = plot_big_s(tr,'ScSScS','ScS^220ScS')
    #fig,ax = plot_big_s(tr,'ScSScS','sScS^670ScS')
    plt.show()

def plot_little_s(tr,parent,child):
    fig,ax = setup_figure()
    samp = tr.stats.sampling_rate
    p,c = return_ttime(tr,parent,child)
    diff = np.abs(p-c)
    r = tr.slice(tr.stats.starttime+p-50,tr.stats.starttime+p+500)
    t = np.linspace(-50,500,num=len(r.data))
    tp = np.linspace(-50,50,num=int(100*samp))
    ax.plot(t,r.data)
    ax.plot(tp,r.data[0:int(100*samp)])
    cd = r.data[int(diff*samp-30*samp):int(diff*samp+30*samp)]
    tc = np.linspace(-50+diff-30,-50+diff+30,num=len(cd))
    ax.plot(tc,cd)
    return fig,ax

def plot_big_s(tr,parent,child):
    fig,ax = setup_figure()
    samp = tr.stats.sampling_rate
    p,c = return_ttime(tr,parent,child)
    diff = np.abs(p-c)
    r = tr.slice(tr.stats.starttime+p-500,tr.stats.starttime+p+50)
    t = np.linspace(-500,50,num=len(r.data))
    pd = r.data[int(-100*samp)::]
    tp = np.linspace(-50,50,num=len(pd))
    ax.plot(t,r.data)
    ax.plot(tp,pd)

    cd = r.data[int(550*samp-diff*samp-30*samp):int(550*samp-diff*samp+30*samp)]
    tc = np.linspace(-diff-30+50,-diff+30+50,num=len(cd))
    ax.axvline(-diff)
    ax.axvline(0)

    ax.plot(tc,cd)
    return fig,ax

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

def return_trace(syn_path):
    st = obspy.read(syn_path)
    st.sort(['gcarc'])
    tr = st[-1]
    tr.filter('bandpass',freqmin=1./100,freqmax=1./10,zerophase=True)
    return tr

def setup_figure():
    fig,ax = plt.subplots()
    return fig,ax

main()









