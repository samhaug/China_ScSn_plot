#!/bin/bash
boxregion=80/150/-10/50 
region=70/160/-20/60 
scale=m0.04i
file=station_map
china_stations=datfiles/stations.dat
grid_stations=grid_stations.dat
#stations=datfiles/obspydmt_statcoords.dat
beach_file=datfiles/beachballs.dat
#gmtset FONT_LABEL=8

#plot events
#psbasemap -R$region -J$scale -B10 -K -D$boxregion -F > $file.ps
#pscoast -R$region -J$scale -B10 -S#27A2B5 -G#B53A27 -K  > $file.ps
pscoast -R$region -J$scale -Ba10 -Swhite -Glightgrey -A10000 -K  > $file.ps
gmt psxy $grid_stations -R$region -J$scale -Si0.10c -Gblack -K -O >> $file.ps
while read lat lon H mrr mtt mpp mrt mrp mtp e lon lat
do
psmeca -R$region -J$scale -Sm0.04i -K -O << EOF >> $file.ps
$lon $lat $H $mrr $mtt $mpp $mrt $mrp $mtp $e $lon $lat
EOF
done < $beach_file

pscoast -R$region -J$scale -Ba10 -Swhite -Glightgrey -A10000 -K -O -X4.5i >> $file.ps
gmt psxy $china_stations -R$region -J$scale -Si0.10c -Gblack -K -O >> $file.ps

while read lat lon H mrr mtt mpp mrt mrp mtp e lon lat
do
psmeca -R$region -J$scale -Sm0.04i -K -O << EOF >> $file.ps
$lon $lat $H $mrr $mtt $mpp $mrt $mrp $mtp $e $lon $lat
EOF
done < $beach_file
#gmt psxy jeannot_1.dat -R$region -J$scale -W2,red -K -O >> $file.ps
#gmt psxy jeannot_2.dat -R$region -J$scale -W2,blue -K -O >> $file.ps

ps2pdf $file.ps
convert -density 150 $file.pdf -quality 90 $file.png
rm $file.ps
evince $file.pdf &> /dev/null



