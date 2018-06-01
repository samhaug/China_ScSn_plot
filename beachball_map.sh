#!/bin/bash
boxregion=80/150/-10/50 
region=70/180/-30/60 
#scale=m0.08i
scale=m0.06i
file=beachball_map
beach_file=datfiles/beachballs.dat
#gmtset FONT_LABEL=8
#gmtset FONT_TITLE=8
#gmtset FONT_ANNOT_PRIMARY=8
#gmtset FONT_ANNOT_SECONDARY=8

#plot events
#psbasemap -R$region -J$scale -B10 -K -D$boxregion -F > $file.ps
#pscoast -R$region -J$scale -B10 -Slightblue -Gwhite -K  > $file.ps
#pscoast -R$region -J$scale -B10 -S#27A2B5 -G#B53A27 -K  > $file.ps
pscoast -R$region -J$scale -B10 -Swhite -A10000 -Glightgrey -K  > $file.ps
#pscoast -R$region -J$scale -B10 -Swhite -Glightgrey -K  > $file.ps

while read lat lon H mrr mtt mpp mrt mrp mtp e lon lat; do
psmeca -R$region -J$scale -Sm0.2i -K -O << END >> $file.ps
$lon $lat $H $mrr $mtt $mpp $mrt $mrp $mrp $e $lon $lat
END
done < $beach_file


ps2pdf $file.ps
rm $file.ps
convert -density 150 $file.pdf -quality 90 $file.png
evince $file.pdf
