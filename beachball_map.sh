#!/bin/bash
region=80/150/-10/50 
scale=m0.1i
file=beachball_map
gmtset FONT_LABEL=8
gmtset FONT_TITLE=8
gmtset FONT_ANNOT_PRIMARY=8
gmtset FONT_ANNOT_SECONDARY=8

#plot events
psbasemap -Y5i -R$region -J$scale -B10 -K -P > $file.ps
pscoast -R$region -J$scale -Wthin,black -N1/thick,black -N2/thin,black \
	-Slightblue -Di -K -O -P >> $file.ps

while read lat lon H mrr mtt mpp mrt mrp mtp e lon lat; do
psmeca -R$region -J$scale -Sm0.4 -K -O << END >> $file.ps
lon lat dep stk dip rake mag
$lon $lat $H $mrr $mtt $mpp $mrt $mrp $mrp $e $lon $lat
END

done < beachballs.dat

ps2pdf $file.ps
rm $file.ps
