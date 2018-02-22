#!/bin/bash
# Plot raypaths for ScS reverberations
file=reverb_raypaths
scale=P10
datadir=raypath_datfiles
gmt gmtset FONT_TITLE = 10p,Helvetica,black
gmt gmtset MAP_FRAME_PEN = thick,black
region=-30/60/3480/6371
region=30/150/3480/6371
#region3=30/150/3480/6371

#S plot
#gmt psxy CE_grid.dat -R$region3 -J$scale -B0 -Wthinnest,black -K -O -P >> $file.ps
gmt psxy $datadir/sScS.dat -R$region -J$scale -Bxa20 -Bya500 \
                           -BwNsE -Wblack -X4 > $file.ps
ps2pdf $file.ps
rm $file.ps

#gmt psscale -D11/2/2/0.2 -B$vmax:"10@+-6@+ s/km@+3@+": -Cv.cpt -K -O -P >> $file.ps

#P plot
#vmax=2.0
#dv=0.4
#gmt makecpt -C$colors -D -T-$vmax/$vmax/$dv -Z -I > v.cpt
#kern=P80_kernel_rotated.dat
#kern=P80_bandpass_rotated.dat
#awk {'print $1,6371.0-$2,$3}' $datadir/$kern > tmp.xy
#gmt blockmean tmp.xy -I1.0/10 -R$region2 > tmp_mean.xy
#gmt surface tmp_mean.xy -Gkernel.grd -I0.1/20 -R$region2 -T0.0
#gmt grdimage kernel.grd -Y-5 -R$region3 -J$scale -B0 -B+t"P" -Cv.cpt -P -K -O >> $file.ps
#gmt psxy CE_grid.dat -R$region3 -J$scale -B0 -Wthinnest,black -K -O -P >> $file.ps
#
#gmt psxy $datadir/Ppath_d80_rotated.dat -R$region3 -J$scale -W1 -K -O -P >> $file.ps
#gmt psxy $datadir/eq_S -R$region3 -J$scale -Sa0.35 -Gyellow -W0.5 -K -O -P >> $file.ps
#gmt psxy $datadir/rec_S -R$region3 -J$scale -St0.30 -Gred -W0.5 -N -K -O -P >> $file.ps
#
#gmt psscale -D11/2/2/0.2 -B$vmax:"10@+-6@+ s/km@+3@+": -Cv.cpt -K -O -P >> $file.ps

#SKS plot
#
#
#vmax=5.0
#dv=1.0
#gmt makecpt -C$colors -D -T-$vmax/$vmax/$dv -Z -I > v.cpt
#kern=SKS100_kernel_rotated.dat
#kern=SKS100_bandpass_rotated.dat
#awk {'print $1,6371.0-$2,$3}' $datadir/$kern > tmp.xy
#gmt blockmean tmp.xy -I1.0/10 -R$region2 > tmp_mean.xy
#gmt surface tmp_mean.xy -Gkernel.grd -I0.1/20 -R$region2 -T0.0
#gmt grdimage kernel.grd -Y-5 -R$region3 -J$scale -B0 -B+t"SKS" -Cv.cpt -P -K -O >> $file.ps
#gmt psxy CE_grid.dat -R$region3 -J$scale -B0 -Wthinnest,black -K -O -P >> $file.ps
#gmt psxy $datadir/SKS_leg1.dat -R$region3 -J$scale -W1 -K -O -P >> $file.ps
#gmt psxy $datadir/SKS_leg3.dat -R$region3 -J$scale -W1 -K -O -P >> $file.ps
#gmt psxy $datadir/eq_SKS -R$region3 -J$scale -Sa0.35 -Gyellow -W0.5 -K -O -P >> $file.ps
#gmt psxy $datadir/rec_SKS -R$region3 -J$scale -St0.30 -Gred -W0.5 -N -K -O -P >> $file.ps
#
#gmt psscale -D11/2/2/0.2 -B$vmax:"10@+-6@+ s/km@+3@+": -Cv.cpt -K -O -P >> $file.ps
#
#
#ps2pdf $file.ps
#rm $file.ps
