#!/bin/bash
region=80/150/-10/50 
scale=m0.4i
file=beachball_map
gmtset LABEL_FONT_SIZE=8
gmtset HEADER_FONT_SIZE=8
gmtset ANNOT_FONT_SIZE_SECONDARY=8
gmtset ANNOT_FONT_SIZE_PRIMARY=8

minlon=246.0-360.0
maxlon=253.0-360.0
minlat=42.0
maxlat=47.0

#plot events
psbasemap -Y5i -R$region -J$scale -Ba2/a2/WSne -K -P > $file.ps
pscoast -R$region -J$scale -A10 -Wthin,black -N1/thick,black -N2/thin,black \
	-Slightblue -Di -K -O -P >> $file.ps

while read lat lon H mrr mtt mpp mrt mrp mtp e lon lat; do
psmeca -R -J -Sm0.4 -K -O << END >> $file.ps
lon lat dep stk dip rake mag
$lon $lat $H $mrr $mtt $mpp $mrt $mrp $mrp $e $lon $lat
END

done < beachballs.dat

ps2pdf $file.ps
rm $file.ps
