#!/bin/bash
boxregion=80/150/-10/50 
region=70/180/-30/60 
#scale=m0.08i
scale=m0.05i
file=reflection_map
#gmtset FONT_LABEL=8
#gmtset FONT_TITLE=8
#gmtset FONT_ANNOT_PRIMARY=8
#gmtset FONT_ANNOT_SECONDARY=8

#plot events
#psbasemap -R$region -J$scale -B10 -K -D$boxregion -F > $file.ps
#pscoast -R$region -J$scale -B10 -S#27A2B5 -G#B53A27 -K  > $file.ps
pscoast -R$region -J$scale -Ba10 -Swhite -Glightgrey -K  > $file.ps

gmt psxy stations.dat -R$region -J$scale -Si0.10c -Gblack -K -O >> $file.ps

gmt psxy ScS2.dat -R$region -J$scale -Sa0.10c -G#27A2B5 -K -O >> $file.ps
#gmt psxy ScS3.dat -R$region -J$scale -Sa0.10c -G#8127B5 -t50 -K -O >> $file.ps
#gmt psxy sScS.dat -R$region -J$scale -Sa0.10c -G#B53A27 -t50 -K -O >> $file.ps
#gmt psxy sScS2.dat -R$region -J$scale -Sa0.10c -G#5BB527 -t50 -K -O >> $file.ps
#gmt psxy sScS3.dat -R$region -J$scale -Sa0.10c -G#B5AF27 -t50 -K -O >> $file.ps

while read lat lon H mrr mtt mpp mrt mrp mtp e lon lat; do
psmeca -R$region -J$scale -Sm0.2i -K -O << END >> $file.ps
$lon $lat $H $mrr $mtt $mpp $mrt $mrp $mrp $e $lon $lat
END
done < one_beachball.dat

ps2pdf $file.ps
rm $file.ps
