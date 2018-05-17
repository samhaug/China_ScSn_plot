#!/bin/bash
boxregion=80/150/-10/50 
region=70/180/-30/60 
#scale=m0.08i
scale=m0.06i
#file=reflection_map
file=station_map
#stations=full_stations.dat
stations=grid_stations.dat
beach_file=datfiles/axisem3d_beachballs.dat
#gmtset FONT_LABEL=8
#gmtset FONT_TITLE=8
#gmtset FONT_ANNOT_PRIMARY=8
#gmtset FONT_ANNOT_SECONDARY=8

#plot events
#psbasemap -R$region -J$scale -B10 -K -D$boxregion -F > $file.ps
#pscoast -R$region -J$scale -B10 -S#27A2B5 -G#B53A27 -K  > $file.ps
pscoast -R$region -J$scale -Ba10 -Swhite -Glightgrey -K  > $file.ps
gmt psxy $stations -R$region -J$scale -Si0.10c -Gblack -K -O >> $file.ps

while read lat lon H mrr mtt mpp mrt mrp mtp e lon lat; do
psmeca -R$region -J$scale -Sm0.2i -K -O << END >> $file.ps
$lon $lat $H $mrr $mtt $mpp $mrt $mrp $mrp $e $lon $lat
END
done < $beach_file

ps2pdf $file.ps
convert -density 150 $file.pdf -quality 90 $file.png
rm $file.ps
evince $file.pdf
