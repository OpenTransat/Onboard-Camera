import serial
import time
import subprocess

CMDMAX = 200
cmd = ""
cmdlen = 0

process = None

CAM_STATE_READY = 0
CAM_STATE_BUSY = 1

CAM_REPEAT_INTERVAL = 2

repeat_cmd = 0
state = CAM_STATE_READY


def readcmd():
    global cmd, cmdlen

    if ser.in_waiting:
        for ch in ser.read():
	    if ch == ';':
		execmd()
		cmd = ""
		cmdlen = 0
	    elif ch == '$':
		cmd = ""
		cmdlen = 0
	    else:
		cmd += ch
		cmdlen += 1

	    if cmdlen > CMDMAX - 2:
		cmd = ""
		cmdlen = 0

def execmd():
    global state, process

    print("COMMAND RECEIVED: "+cmd)

    i = 0
    while i < cmdlen and not cmd[i].isdigit() and cmd[i] != '-' and cmd[i] != '.':
	i += 1

    cmd1 = cmd[:i]
    cmd2_str = cmd[i:]
    cmd2 = int(cmd2_str)

    if cmd1 == "VID" and (cmd2 in [0, 10, 15, 30, 45, 60, 75, 120, 150, 180]):
	if state == CAM_STATE_READY:
	    print("Recording... "+str(cmd2))
	    process = subprocess.Popen(["sh", "picrec.sh", str(cmd2)])
	    state = CAM_STATE_BUSY

        ser.write("$BSY;")


print("python:starting raspi.py...")
ser = serial.Serial("/dev/ttyS0", 4800, timeout=5)

while True:
    if state == CAM_STATE_READY and time.time() > repeat_cmd + CAM_REPEAT_INTERVAL:
	ser.write("$RDY0;")
	repeat_cmd = time.time()

    if state == CAM_STATE_BUSY and process != None and process.poll() != None:
	exit()
	#halted by picrec.sh

    readcmd()
    time.sleep(0.002)
