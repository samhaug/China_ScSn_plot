#!/bin/bash
file=CE_kernels
scale=P10
datadir=/geo/work10/romaguir/projects/plume_resolution/data/kernels
colors=/geo/home/romaguir/utils/colors/BlueWhiteGreen.cpt
vmax=3.0
dv=1.0
gmt gmtset FONT_TITLE   			= 10p,Helvetica,black
gmt gmtset MAP_FRAME_PEN			= thick,black
gmt makecpt -C$colors -D -T-$vmax/$vmax/$dv -Z -I > v.cpt
region=0/360/11.3/2867.0
region2=0/360/3500/6371
region3=-100/20/3500/6371
region4=-110/10/3500/6371
region3=30/150/3500/6371

#S plot
kern=S80_kernel_rotated.dat
kern=S80_bandpass_rotated.dat
awk {'print $1,6371.0-$2,$3}' $datadir/$kern > tmp.xy
gmt blockmean tmp.xy -I1.0/10 -R$region2 > tmp_mean.xy
gmt surface tmp_mean.xy -Gkernel.grd -I0.1/20 -R$region2 -T0.0
gmt grdimage kernel.grd -Y18 -R$region3 -J$scale -B0 -B+t"S" -Cv.cpt -P -K > $file.ps
gmt psxy CE_grid.dat -R$region3 -J$scale -B0 -Wthinnest,black -K -O -P >> $file.ps
gmt psxy $datadir/Spath_d80_rotated.dat -R$region3 -J$scale -W1 -K -O -P >> $file.ps
gmt psxy $datadir/eq_S -R$region3 -J$scale -Sa0.35 -Gyellow -W0.5 -K -O -P >> $file.ps
gmt psxy $datadir/rec_S -R$region3 -J$scale -St0.30 -Gred -W0.5 -N -K -O -P >> $file.ps

gmt psscale -D11/2/2/0.2 -B$vmax:"10@+-6@+ s/km@+3@+": -Cv.cpt -K -O -P >> $file.ps

#P plot
vmax=2.0
dv=0.4
gmt makecpt -C$colors -D -T-$vmax/$vmax/$dv -Z -I > v.cpt
kern=P80_kernel_rotated.dat
kern=P80_bandpass_rotated.dat
awk {'print $1,6371.0-$2,$3}' $datadir/$kern > tmp.xy
gmt blockmean tmp.xy -I1.0/10 -R$region2 > tmp_mean.xy
gmt surface tmp_mean.xy -Gkernel.grd -I0.1/20 -R$region2 -T0.0
gmt grdimage kernel.grd -Y-5 -R$region3 -J$scale -B0 -B+t"P" -Cv.cpt -P -K -O >> $file.ps
gmt psxy CE_grid.dat -R$region3 -J$scale -B0 -Wthinnest,black -K -O -P >> $file.ps

gmt psxy $datadir/Ppath_d80_rotated.dat -R$region3 -J$scale -W1 -K -O -P >> $file.ps
gmt psxy $datadir/eq_S -R$region3 -J$scale -Sa0.35 -Gyellow -W0.5 -K -O -P >> $file.ps
gmt psxy $datadir/rec_S -R$region3 -J$scale -St0.30 -Gred -W0.5 -N -K -O -P >> $file.ps

gmt psscale -D11/2/2/0.2 -B$vmax:"10@+-6@+ s/km@+3@+": -Cv.cpt -K -O -P >> $file.ps

#SKS plot
vmax=5.0
dv=1.0
gmt makecpt -C$colors -D -T-$vmax/$vmax/$dv -Z -I > v.cpt
kern=SKS100_kernel_rotated.dat
kern=SKS100_bandpass_rotated.dat
awk {'print $1,6371.0-$2,$3}' $datadir/$kern > tmp.xy
gmt blockmean tmp.xy -I1.0/10 -R$region2 > tmp_mean.xy
gmt surface tmp_mean.xy -Gkernel.grd -I0.1/20 -R$region2 -T0.0
gmt grdimage kernel.grd -Y-5 -R$region3 -J$scale -B0 -B+t"SKS" -Cv.cpt -P -K -O >> $file.ps
gmt psxy CE_grid.dat -R$region3 -J$scale -B0 -Wthinnest,black -K -O -P >> $file.ps
gmt psxy $datadir/SKS_leg1.dat -R$region3 -J$scale -W1 -K -O -P >> $file.ps
gmt psxy $datadir/SKS_leg3.dat -R$region3 -J$scale -W1 -K -O -P >> $file.ps
gmt psxy $datadir/eq_SKS -R$region3 -J$scale -Sa0.35 -Gyellow -W0.5 -K -O -P >> $file.ps
gmt psxy $datadir/rec_SKS -R$region3 -J$scale -St0.30 -Gred -W0.5 -N -K -O -P >> $file.ps

gmt psscale -D11/2/2/0.2 -B$vmax:"10@+-6@+ s/km@+3@+": -Cv.cpt -K -O -P >> $file.ps


ps2pdf $file.ps
rm $file.ps
