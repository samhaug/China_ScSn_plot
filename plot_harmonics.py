#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : plot_harmonics.py
Purpose : plot spherical harmonics
Creation Date : 17-02-2018
Last Modified : Tue 03 Apr 2018 12:33:05 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
import argparse
from pyshtools.shclasses import SHCoeffs, SHGrid, SHWindow


def main():
    parser = argparse.ArgumentParser(description='plot_reflection_points')
    parser.add_argument('-n','--n',metavar='integer',type=int,
                        help='n value',default=0)
    parser.add_argument('-l','--l',metavar='integer',type=int,
                        help='l value',default=0)
    parser.add_argument('-m','--m',metavar='integer',type=int,
                        help='m value',default=0)
    args = parser.parse_args()

    lmax = 200
    coeffs = np.zeros((2,lmax+1,lmax+1))
    coeffs[args.n,args.l,args.m] = 1.
    coeffs_l5m2 = SHCoeffs.from_array(coeffs)
    grid_l5m2 = coeffs_l5m2.expand('DH2')
    s = grid_l5m2.data.shape
    xx,yy=np.meshgrid(np.linspace(0,360,num=s[1]),np.linspace(-90,90,num=s[0]))
    xx = xx.ravel()
    yy = yy.ravel()
    dat = grid_l5m2.data.ravel()
    np.savetxt('spherical.dat',np.c_[xx,yy,dat],fmt='%8.3f')
    fig, ax = grid_l5m2.plot()
    plt.show()

main()

