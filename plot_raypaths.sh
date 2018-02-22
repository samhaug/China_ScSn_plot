#!/bin/bash
# Plot raypaths for ScS reverberations
file=reverb_raypaths
scale=P6
datadir=raypath_datfiles
gmt gmtset FONT_TITLE = 10p,Helvetica,black
gmt gmtset MAP_FRAME_PEN = thick,black
region=-30/60/3480/6371
region=50/130/3480/6371
#region3=30/150/3480/6371

#S plot
#gmt psxy CE_grid.dat -R$region3 -J$scale -B0 -Wthinnest,black -K -O -P >> $file.ps
gmt psxy $datadir/sScS0.dat -R$region -J$scale -Bxa20 -Bya500 \
                           -BwNsE -Wthin,black -Y20 -X0.1 -K -P > $file.ps
gmt psxy $datadir/sScS1.dat -R$region -J$scale \
                           -BwNsE -Wthin,#27A2B5 -K -O >> $file.ps
gmt psxy $datadir/sScS2.dat -R$region -J$scale \
                           -BwNsE -Wthin,#8127B5 -K -O >> $file.ps

gmt psxy $datadir/sScSScS0.dat -R$region -J$scale -Bxa20 -Bya500 \
                           -BwNsE -Wthin,black -X8 -K -O  >> $file.ps
gmt psxy $datadir/sScSScS1.dat -R$region -J$scale \
                           -BwNsE -Wthin,#27A2B5 -K -O >> $file.ps
gmt psxy $datadir/sScSScS2.dat -R$region -J$scale \
                           -BwNsE -Wthin,#8127B5 -K -O >> $file.ps
gmt psxy $datadir/sScSScS3.dat -R$region -J$scale \
                           -BwNsE -Wthin,#B53A27 -K -O >> $file.ps

#c -G#5BB527 
#c -G#B5AF27 

ps2pdf $file.ps
rm $file.ps
display $file.pdf
convert -density 150 $file.pdf -quality 90 $file.png

#ps2pdf $file.ps
#rm $file.ps
