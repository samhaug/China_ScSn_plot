#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_reverb_paths.py
Purpose : Make data files to plot ScS reverberation raypaths
Creation Date : 22-02-2018
Last Modified : Thu 22 Feb 2018 11:43:07 AM EST
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
                          distance_in_degree=45,
                          phase_list=['sScS',
                                     phase_families['sScS'][0],
                                     phase_families['sScS'][1]])

main_path = np.array([list((np.degrees(i[2]),i[3])) for i in arr[0].path])
rev_1 = np.array([list((np.degrees(i[2]),i[3])) for i in arr[1].path])
rev_2 = np.array([list((np.degrees(i[2]),i[3])) for i in arr[2].path])

np.savetxt('raypath_datfiles/sScS.dat',main_path)
np.savetxt('raypath_datfiles/sScS_1.dat',rev_1)
np.savetxt('raypath_datfiles/sScS_2.dat',rev_2)
