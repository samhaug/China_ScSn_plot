#!/bin/bash
boxregion=80/150/-10/50 
region=70/180/-30/60 
scale=m0.06i
file=count_map

#makecpt -Chot -D0/5000/10 -Z > cmap.cpt
makecpt -Chot -T0/5000/20 -Z > cmap.cpt
#xyz2grd count_map.dat -R$region -Gtmp.grd -I0.5/0.5
xyz2grd full_count.dat -R$region -Gtmp.grd -I0.5/0.5
grdimage tmp.grd -R$region -J$scale -Ba10 -K -Ccmap.cpt > $file.ps
pscoast -R$region -J$scale -W1,black -A1000 -K -O  >> $file.ps

ps2pdf $file.ps
convert -density 150 $file.pdf -quality 90 $file.png
evince $file.pdf
rm tmp.grd
rm cmap.cpt
rm $file.ps
