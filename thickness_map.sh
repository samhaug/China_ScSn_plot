#!/bin/bash
region=90/150/-10/50 
boxregion=70/180/-30/60 
scale=m0.06i
file=thickness_map

echo "makecpt"
#makecpt -Cviridis -T640/700/5 > cmap.cpt
makecpt -Cpolar -T265/275/1 -I> cmap.cpt
#makecpt -Cgray -T0/5000/5 > gcmap.cpt
makecpt -Cgray -T0/2/1 > mcmap.cpt
echo "xyz2grd"
xyz2grd $1 -R$region -Gtmp.grd -I0.81/0.81
#xyz2grd $2 -R$region -Ggtmp.grd -I0.51/0.51
xyz2grd $2 -R$region -Gmtmp.grd -I0.51/0.51
echo "grdimage"
grdimage tmp.grd -R$region -J$scale -Ba10 -K -Ccmap.cpt -Y6c > $file.ps
grdimage mtmp.grd -R$region -J$scale -Ba10 -K -O -Cmcmap.cpt -t80 >> $file.ps
echo "psscale"
psscale -Ccmap.cpt -Dx0c/-2c+w9.2c/0.5c+h -Bxaf+l"Thickness (km)" -K -O >> $file.ps
echo "pscoast"
pscoast -R$region -J$scale -W1,black -A1000 -K -O >> $file.ps

#grdimage gtmp.grd -R$region -J$scale -Ba10 -K -O -Cgcmap.cpt -X12c -t5 >> $file.ps
#pscoast -R$region -J$scale -W1,black -A1000 -K -O >> $file.ps
#psscale -Cgcmap.cpt -Dx0c/-2c+w9.2c/0.5c+h -Bxaf+l"Pick count" -K -O >> $file.ps

ps2pdf $file.ps &> /dev/null
convert -density 150 $file.pdf -quality 90 $file.png &> /dev/null
rm {g,}tmp.grd &> /dev/null
rm {g,}cmap.cpt &> /dev/null
rm $file.ps
evince $file.pdf &> /dev/null

