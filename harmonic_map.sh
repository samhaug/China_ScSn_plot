#!/bin/bash
boxregion=80/150/-10/50 
region=70/180/-30/60 
#scale=m0.08i
scale=m0.06i
#file=reflection_map
file=reflection_map
stations=datfiles/stations.dat
beachballs=datfiles/beachballs.dat

makecpt -Cpolar -D-15/15/0.01 -Z > cmap.cpt
xyz2grd spherical.dat -R$region -Gtmp.grd -I0.5/0.5
grdimage tmp.grd -R$region -J$scale -Ba10 -K -Ccmap.cpt > $file.ps
pscoast -R$region -J$scale -W1,black -A1000 -K -O  >> $file.ps

ps2pdf $file.ps
convert -density 150 $file.pdf -quality 90 $file.png
display $file.png
rm tmp.grd
rm cmap.cpt
rm $file.ps
