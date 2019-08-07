# Onboard Camera

Tested with Logitech C920 USB webcam connected to Raspberry Pi 3 running Ubuntu 16.04

The [Python program](https://github.com/OpenTransat/Onboard-Camera/blob/master/ubuntu/raspi.py) running on Ubuntu is listening for serial commands from the main controller running Arduino code: [camera.h](https://github.com/OpenTransat/OpenTransat-Navigator/blob/master/software/main/camera.h), [camera.ino](https://github.com/OpenTransat/OpenTransat-Navigator/blob/master/software/main/camera.ino).


### System Configuration:

Copy [files](https://github.com/OpenTransat/Onboard-Camera/tree/master/ubuntu) to `/home/ubuntu` (the user home folder)

Run startup script on boot:
```
chmod +x /home/ubuntu/startup_script
crontab -e
```
Add line: `@reboot /home/ubuntu/startup_script`

Disable console:

```
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
nano /boot/firmware/cmdline.txt
```

Remove:

net.ifnames=0 dwc_otg.lpm_enable=0 ~~console=ttyAMA0,115200 console=tty1~~ root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait

Remove time-consuming tasks:

```
systemd-analyze
systemd-analyze blame
sudo apt-get purge cloud-init
```
