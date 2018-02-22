#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_reverb_paths.py
Purpose : Make data files to plot ScS reverb raypaths with plot_raypaths.sh
Creation Date : 22-02-2018
Last Modified : Thu 22 Feb 2018 12:53:21 PM EST
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

arr = model.get_ray_paths(source_depth_in_km=600,
                          distance_in_degree=60,
                          phase_list=['sScS',
                          phase_families['sScS'][0],
                          phase_families['sScS'][1]])

main_path = np.array([list((np.degrees(i[2]),6371-i[3]))
                      for i in arr[0].path])
rev_1 = np.array([list((np.degrees(i[2]),6371-i[3]))
                      for i in arr[1].path])
rev_2 = np.array([list((np.degrees(i[2]),6371-i[3]))
                      for i in arr[2].path])

main_path[:,0] += -1*main_path[:,0].max()+140
rev_1[:,0] += -1*rev_1[:,0].max()+140
rev_2[:,0] += -1*rev_2[:,0].max()+140

plt.plot(main_path[:,0],main_path[:,1])
plt.show()

np.savetxt('raypath_datfiles/sScS.dat',main_path)
np.savetxt('raypath_datfiles/sScS_1.dat',rev_1)
np.savetxt('raypath_datfiles/sScS_2.dat',rev_2)
