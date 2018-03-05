#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : pretty_prem.py
Purpose : Make nice plot of PREM for slideshow
Creation Date : 04-03-2018
Last Modified : Sun 04 Mar 2018 05:52:26 PM EST
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir

def main():
    prem = np.genfromtxt('PREM_1s.csv',delimiter=',')
    fig,ax = setup_figure()
    r = prem[:,1]
    d = prem[:,2]
    p = prem[:,3]
    s = prem[:,5]
    ax.plot(p,r,color='#4B29AB',label=r'$v_{P}$',lw=2)
    ax.plot(s,r,color='#AB4B29',label=r'$v_{S}$',lw=2)
    ax.plot(d,r,color='#29AB4B',label=r'$\rho$',lw=2)
    #ax.axhline(670,color='r',alpha=0.5,ls='--')
    #ax.axhline(400,color='r',alpha=0.5,ls='--')
    ax.legend(loc='lower left',fontsize=14)
    plt.savefig('pretty_prem.png')
    plt.show()

def setup_figure():
    fig,ax = plt.subplots(figsize=(7,9))
    ax.set_ylim(6371,-10)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel(r'(km/s),(kg/$m^3$)',size=14)
    ax.set_ylabel('Depth (km)',size=14)
    return fig,ax


main()
