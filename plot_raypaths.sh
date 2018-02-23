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
#############################################################################
gmt psxy $datadir/sScS0.dat -R$region -J$scale -Bxa180  \
                           -BwNsE -Wthin,black -Y20 -X0.1 -K -P > $file.ps
gmt psxy $datadir/sScS1.dat -R$region -J$scale \
                           -BwNsE -Wthin,#27A2B5 -K -O >> $file.ps
gmt psxy $datadir/sScS2.dat -R$region -J$scale \
                           -BwNsE -Wthin,#8127B5 -K -O >> $file.ps

gmt psxy $datadir/670.dat -R$region -J$scale \
                           -BwNsE -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/410.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/220.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps

gmt psxy $datadir/earthquake.dat -R$region -J$scale -O -K -Sa.3 \
                            -Wthick,yellow >> $file.ps

#############################################################################
gmt psxy $datadir/sScSScS0.dat -R$region -J$scale -Bxa180 \
                           -BwNsE -Wthin,black -X6.5 -K -O  >> $file.ps
gmt psxy $datadir/sScSScS1.dat -R$region -J$scale \
                           -BwNsE -Wthin,#27A2B5 -K -O >> $file.ps
gmt psxy $datadir/sScSScS2.dat -R$region -J$scale \
                           -BwNsE -Wthin,#8127B5 -K -O >> $file.ps
gmt psxy $datadir/sScSScS3.dat -R$region -J$scale \
                           -BwNsE -Wthin,#B53A27 -K -O >> $file.ps

gmt psxy $datadir/670.dat -R$region -J$scale \
                           -BwNsE -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/410.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/220.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps

gmt psxy $datadir/earthquake.dat -R$region -J$scale -O -K -Sa.3 \
                            -Wthick,yellow >> $file.ps
#############################################################################
gmt psxy $datadir/sScSScSScS0.dat -R$region -J$scale -Bxa180 \
                           -BwNsE -Wthin,black -X6.5 -K -O  >> $file.ps
gmt psxy $datadir/sScSScSScS1.dat -R$region -J$scale \
                           -BwNsE -Wthin,#27A2B5 -K -O >> $file.ps
gmt psxy $datadir/sScSScSScS2.dat -R$region -J$scale \
                           -BwNsE -Wthin,#8127B5 -K -O >> $file.ps
gmt psxy $datadir/sScSScSScS3.dat -R$region -J$scale \
                           -BwNsE -Wthin,#B53A27 -K -O >> $file.ps
gmt psxy $datadir/sScSScSScS4.dat -R$region -J$scale \
                           -BwNsE -Wthin,#5BB527 -K -O >> $file.ps

gmt psxy $datadir/670.dat -R$region -J$scale \
                           -BwNsE -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/410.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/220.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps

gmt psxy $datadir/earthquake.dat -R$region -J$scale -O -K -Sa.3 \
                            -Wthick,yellow >> $file.ps
#############################################################################
gmt psxy $datadir/ScSScS0.dat -R$region -J$scale -Bxa180 \
                           -BwNsE -Wthin,black -Y-3 -X-9.7 -K -O >> $file.ps
gmt psxy $datadir/ScSScS1.dat -R$region -J$scale \
                           -BwNsE -Wthin,#27A2B5 -K -O >> $file.ps

gmt psxy $datadir/670.dat -R$region -J$scale \
                           -BwNsE -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/410.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/220.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps

gmt psxy $datadir/earthquake.dat -R$region -J$scale -O -K -Sa.3 \
                            -Wthick,yellow >> $file.ps
#############################################################################

gmt psxy $datadir/ScSScSScS2.dat -R$region -J$scale -Bxa180 \
                           -BwNsE -Wthin,black -X6.5 -K -O >> $file.ps
gmt psxy $datadir/ScSScSScS1.dat -R$region -J$scale \
                           -BwNsE -Wthin,#27A2B5 -K -O >> $file.ps
gmt psxy $datadir/ScSScSScS0.dat -R$region -J$scale \
                           -BwNsE -Wthin,#8127B5 -K -O >> $file.ps

gmt psxy $datadir/670.dat -R$region -J$scale \
                           -BwNsE -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/410.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps
gmt psxy $datadir/220.dat -R$region -J$scale \
                           -Wthinnest,black -K -O >> $file.ps

gmt psxy $datadir/earthquake.dat -R$region -J$scale -O -K -Sa.3 \
                            -Wthick,yellow >> $file.ps
#############################################################################

ps2pdf $file.ps
rm $file.ps
display $file.pdf
convert -density 150 $file.pdf -quality 90 $file.png

#ps2pdf $file.ps
#rm $file.ps
