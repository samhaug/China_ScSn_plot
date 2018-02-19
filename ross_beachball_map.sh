#!/bin/bash
region=242/257/40/49
region=246/253/42/47
#region=-107/-114/41/48
scale=m0.4i
file=Yellowstone_region
colordir=/geo/home/romaguir/utils/colors/
colors=$colordir/colombia
etopo=/geo/home/romaguir/utils/ETOPO1.grd
relief=/geo/home/romaguir/utils/etopo_graddiv2.grd
makecpt -C$colors -D -Z -T-8000/10000/100 > cmap.cpt
makecpt -C$colors -D -Z -T-7250/10000/100 > cmap.cpt
makecpt -C$colors -D -Z -T-6800/10000/100 > cmap.cpt
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
grdimage $etopo -R$region -J$scale -I$relief -Ccmap.cpt -K -O -P >> $file.ps
pscoast -R$region -J$scale -A10 -Wthin,black -N1/thick,black -N2/thin,black \
	-Slightblue -Di -K -O -P >> $file.ps
psxy domain_box -R$region -J$scale -W6,black,- -K -O -P >> $file.ps

while read date lat lon H Mw Stk Dip Rake Ref Model Auth ; do

psmeca -R -J -Sa0.4 -H1 -K -O -P << END >> $file.ps
lon lat dep stk dip rake mag
$lon $lat $H $Stk $Dip $Rake $Mw
END

done < YS_moment_tensors.dat

#plot networks
psbasemap -X3.5i -R$region -J$scale -Ba2/a2/WSne -K -O -P >> $file.ps
grdimage $etopo -R$region -J$scale -I$relief -Ccmap.cpt -K -O -P >> $file.ps
pscoast -R$region -J$scale -A10 -Wthin,black -N1/thick,black -N2/thin,black \
	-Slightblue -Di -K -O -P >> $file.ps
psxy domain_box -R$region -J$scale -W6,black,- -K -O -P >> $file.ps

#psxy Yellowstone_allstations.dat -R -J -St0.175 -W2 -Gmagenta -K -O -P >> $file.ps
#psxy Yellowstone_TA.dat -R -J -St0.175 -W2 -Gcyan -K -O -P >> $file.ps
tail -n +5 networks2012/IM.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/IW.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/2G.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/RE.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/TA.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/US.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/XC.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/YH.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/XS.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/XT.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/XV.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/Z2.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps
tail -n +5 networks2012/WY.dat | psxy -R -J -Si0.2 -W2 -Gmagenta -K -O -P >> $file.ps

pslegend -R/0/1/0/1 -JX3.5i -Dx0.0/-4.0/7.0/3.0/BL -F -C0.05i/0.05i -L1.2 -K -O -P \
<< EOF >> $file.ps
S 0.2 t 0.2 cyan 0.25p 0.3i IW
S 0.2 t 0.2 purple 0.25p 0.3i TA
S 0.2 t 0.2 magenta 0.25p 0.3i US
S 0.2 t 0.2 green 0.25p 0.3i XC
S 0.2 c 0.15 cyan 0.25p 0.3i XS
S 0.2 c 0.15 purple 0.25p 0.3i XT
S 0.2 c 0.15 magenta 0.25p 0.3i XV
S 0.2 c 0.15 green 0.25p 0.3i Z2
EOF

ps2pdf $file.ps
rm $file.ps
