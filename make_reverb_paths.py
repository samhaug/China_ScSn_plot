#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_reverb_paths.py
Purpose : Make data files to plot ScS reverb raypaths with plot_raypaths.sh
Creation Date : 22-02-2018
Last Modified : Thu 22 Feb 2018 04:14:49 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
import obspy
from matplotlib import pyplot as plt
from obspy.taup import TauPyModel
model = TauPyModel(model='prem')

phase_families = {'sScS':['sSv670SScS','sScSSv670S'],
                 'sScSScS':['sSv670SScSScS','sScSSv670SScS','sScSScSSv670S'],
                 'sScSScSScS':['sSv670SScSScSScS','sScSSv670SScSScS',
                               'sScSScSSv670SScS','sScSScSScSSv670S'],
                 'ScSScS':['ScS^670ScS'],
                 'ScSScSScS':['ScS^670ScSScS','ScScS^670ScS']}

def find_paths(parent_phase):
    phase_list = [parent_phase]
    for ii in phase_families[parent_phase]:
        phase_list.append(ii)

    arrivals = model.get_ray_paths(source_depth_in_km=600,
                                   distance_in_degree=60,
                                   phase_list=phase_list)
    for idx,arr in enumerate(arrivals):
        print arr.purist_name
        path = np.array([list((np.degrees(i[2]),6371-i[3]))
                              for i in arr.path])
        path[:,0] += 60
        plt.plot(path[:,0],path[:,1])
        np.savetxt('raypath_datfiles/'+parent_phase+str(idx)+'.dat',path)
        plt.show()

for keys in phase_families:
    find_paths(keys)



