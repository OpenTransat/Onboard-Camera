
#capture params

lastnum=`sh lastnum.sh jpg`
lastnum=$(($lastnum+1))
newfile="$lastnum.jpg"

#capture

echo "capturing to $newfile"
sudo v4l2-ctl --set-fmt-video=width=1920,height=1080,pixelformat=2
sudo v4l2-ctl --set-parm=30
./capture -c 1 -o > $newfile
