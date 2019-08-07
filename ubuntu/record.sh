
#clear space if necessary

freespace=`df -k . | tail -1 | cut -f 6 -d' '`
if [ $freespace -lt 1000000 ]
    then
	randomf=`ls -v *.raw 2>/dev/null | sort -R | tail -1`
	echo "no free space, deleting $randomf"
	rm $randomf
fi


#capture params

frames=$(($1 * 30))
lastnum=`sh lastnum.sh raw`
lastnum=$(($lastnum+1))
newfile="$lastnum.raw"

#capture

echo "capturing to $newfile"
sudo v4l2-ctl --set-fmt-video=width=1920,height=1080,pixelformat=1
sudo v4l2-ctl --set-parm=30
./capture -c $frames -o > $newfile
