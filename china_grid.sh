#!/usr/bin/bash                                                                 

gmt pscoast -R80/150/-10/50 -Jm0.1i -B10g0.5 -G#FFB06B -S#6BBAFF -p150/20 > china.ps 
ps2pdf china.ps                                                   
display china.pdf                                                              


                     
