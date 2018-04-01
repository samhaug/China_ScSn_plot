#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : make_reflection_list.py
Purpose : make ascii files of reflection points for psxy
Creation Date : 19-02-2018
Last Modified : Sun 01 Apr 2018 03:14:05 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from subprocess import call
from os import listdir
import argparse
import h5py
from glob import glob

def main():
    parser = argparse.ArgumentParser(description='make list of reflection points')
    parser.add_argument('-d','--dir_list',metavar='string',type=str,
                       help='glob compatable list list of direcories')
    args = parser.parse_args()
    dir_list = glob(args.dir_list)
    ScS2 = file('ScS2.dat','w')
    ScS3 = file('ScS3.dat','w')
    sScS = file('sScS.dat','w')
    sScS2 = file('sScS2.dat','w')
    sScS3 = file('sScS3.dat','w')
    for d in dir_list:
        print d
        try:
            phase_names,coord = reflection_points(d+'/3dreflection_points.h5')
        except KeyError:
            continue
        for idx,ii in enumerate(phase_names):
            if ii == 'sScS':
                sScS.write(str(coord[idx][1])+' '+str(coord[idx][0])+'\n')
            if ii == 'sScSScS':
                sScS2.write(str(coord[idx][1])+' '+str(coord[idx][0])+'\n')
            if ii == 'sScSScSScS':
                sScS3.write(str(coord[idx][1])+' '+str(coord[idx][0])+'\n')
            if ii == 'ScSScS':
                ScS2.write(str(coord[idx][1])+' '+str(coord[idx][0])+'\n')
            if ii == 'ScSScSScS':
                ScS3.write(str(coord[idx][1])+' '+str(coord[idx][0])+'\n')
    ScS2.close()
    ScS3.close()
    sScS.close()
    sScS2.close()
    sScS3.close()

def reflection_points(fname):
    f = h5py.File(fname,'r',driver='core')
    phase_names = []
    coord = []
    for ikeys in f:
        for phase in f[ikeys]:
            if phase == 'ScSScS':
                hkey = f[ikeys][phase].keys()[118]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
            if phase == 'ScSScSScS':
                hkey = f[ikeys][phase].keys()[118]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
                hkey = f[ikeys][phase].keys()[289]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
            if phase == 'sScS':
                hkey = f[ikeys][phase].keys()[118]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
                hkey = f[ikeys][phase].keys()[289]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
            if phase == 'sScSScS':
                hkey = f[ikeys][phase].keys()[118]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
                hkey = f[ikeys][phase].keys()[289]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
                hkey = f[ikeys][phase].keys()[460]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
            if phase == 'sScSScSScS':
                hkey = f[ikeys][phase].keys()[118]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
                hkey = f[ikeys][phase].keys()[289]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
                hkey = f[ikeys][phase].keys()[460]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
                hkey = f[ikeys][phase].keys()[631]
                phase_names.append(phase)
                coord.append(f[ikeys][phase][hkey][:])
    return phase_names,coord
main()
