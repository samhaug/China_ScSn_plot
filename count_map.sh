#!/bin/bash
region=80/150/-10/50 
boxregion=70/180/-30/60 
scale=m0.07i
file=count_map

echo "makecpt"
#makecpt -Cviridis -T640/700/5 > cmap.cpt
makecpt -Chot -T0/4000/5 > cmap.cpt
echo "xyz2grd"
xyz2grd $1 -R$region -Gtmp.grd -I0.51/0.51
echo "grdimage"
grdimage tmp.grd -R$region -J$scale -Ba10 -K -Ccmap.cpt -Y6c > $file.ps
echo "psscale"
psscale -Ccmap.cpt -Dx0c/-2c+w12.5c/0.5c+h -Bxaf+l"Pierce count" -K -O >> $file.ps
echo "pscoast"
pscoast -R$region -J$scale -W1,black -A1000 -K -O >> $file.ps

ps2pdf $file.ps &> /dev/null
convert -density 150 $file.pdf -quality 90 $file.png &> /dev/null
rm tmp.grd
rm cmap.cpt
rm $file.ps
evince $file.pdf &> /dev/null

