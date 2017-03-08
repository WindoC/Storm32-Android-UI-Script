layout="""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout android:id="@+id/MainWidget"
	android:layout_width="fill_parent" android:layout_height="fill_parent"
	xmlns:android="http://schemas.android.com/apk/res/android">
	<LinearLayout android:layout_width="fill_parent"
		android:layout_height="fill_parent" android:orientation="vertical">
		<TextView android:id="@+id/lb1" android:layout_width="fill_parent"
			android:layout_height="fill_parent" android:textColor="#0bda51"
			android:text="Status" android:layout_weight="1" android:gravity="center" />
		<LinearLayout android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:orientation="horizontal">
			<TextView android:id="@+id/lb2" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:textColor="#0bda51"
				android:text="Status:" android:layout_weight="1" android:gravity="center" />
			<TextView android:id="@+id/statusinfo" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:textColor="#0bda51"
				android:text="-----" android:layout_weight="1" android:gravity="center" />
			<TextView android:id="@+id/lb3" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:textColor="#0bda51"
				android:text="Voltage:" android:layout_weight="1" android:gravity="center" />
			<TextView android:id="@+id/volinfo" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:textColor="#0bda51"
				android:text="-----" android:layout_weight="1" android:gravity="center" />
		</LinearLayout>
		<Button android:id="@+id/getstatus" android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:text="Reflash Status" />

		<TextView android:id="@+id/lb4" android:layout_width="fill_parent"
			android:layout_height="fill_parent" android:textColor="#0bda51"
			android:text="MODE" android:layout_weight="1" android:gravity="center" />
		<LinearLayout android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:orientation="horizontal">
			<Button android:id="@+id/M1" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="H H H" />
			<Button android:id="@+id/M2" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="H H P" />
			<Button android:id="@+id/M3" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:layout_weight="1"
				android:text="P H P" />
		</LinearLayout>
		<TextView android:id="@+id/lb5" android:layout_width="fill_parent"
			android:layout_height="fill_parent" android:textColor="#0bda51"
			android:text="Pointing" android:layout_weight="1" android:gravity="center" />

		<Button android:id="@+id/U2" android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:text="U2" />
		<Button android:id="@+id/U1" android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:text="U1" />
		<LinearLayout android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:orientation="horizontal">
			<Button android:id="@+id/L2" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="L2" />
			<Button android:id="@+id/L1" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="L1" />
			<Button android:id="@+id/MI" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:layout_weight="1"
				android:text="Recenter" />
			<Button android:id="@+id/R1" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="R1" />
			<Button android:id="@+id/R2" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="R2" />
		</LinearLayout>
		<Button android:id="@+id/D1" android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:text="D1" />
		<Button android:id="@+id/D2" android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:text="D2" />
		<TextView android:id="@+id/lb6" android:layout_width="fill_parent"
			android:layout_height="fill_parent" android:textColor="#0bda51"
			android:text="Control" android:layout_weight="1" android:gravity="center" />
		<LinearLayout android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:orientation="horizontal">
			<Button android:id="@+id/S0" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="Resume" />
			<Button android:id="@+id/S1" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="Standby" />
			<Button android:id="@+id/disconnectexit" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:text="Disconnect + Exit"
				android:layout_weight="1" />
		</LinearLayout>
	</LinearLayout>
</RelativeLayout>
"""

import sl4a
import os
import datetime
import time
import array
import base64
import struct

################## Function ##########################################

def pwm2b(pwmv):
 return struct.pack('I',pwmv)[:2]

def f2b(fn):
 return struct.pack("f",fn)

def crc_accumulate(b,crcTmp):
 tmp = 0
 tmp = ( b ^ ( crcTmp & 0xff ) ) & 0xff
 tmp = ( tmp ^ ( tmp<<4 ) ) & 0xff
 crcTmp = ( (crcTmp>>8) ^ (tmp<<8) ^ (tmp<<3) ^ (tmp>>4) ) & 0xffff
 return crcTmp

def crc(bstr):
 crcTmp = 0xffff
 for b in bstr :
  crcTmp = crc_accumulate(b,crcTmp)
 #return crcTmp
 #return struct.pack('>I', 0xffff & crcTmp)[:2]
 return struct.pack('I', 0xffff & crcTmp)[:2]

def sgdata(outbyte,waittime):
 #Send byte
 print("Try to send bytes ...")
 try:
  #droid.bluetoothWrite("\xfa\x00\x01\x00\x00")
  #droid.bluetoothWrite("".join(map(chr, [0xfa, 0x00, 0x0b, 0, 0])))
  print("outbyte = ",outbyte)
  #droid.bluetoothWrite(outbyte)
  outstr = base64.b64encode(outbyte).decode("utf-8")
  print("outstr = ",outstr)
  droid.bluetoothWriteBinary(outstr)
  print("Sent!")
  
  if(waittime==0):
   waittime=0.1
  time.sleep(waittime)
  
  #Receive byte
  print("Try to receive bytes ...")
  try:
   #instr = droid.bluetoothRead(4096).result
   instr = droid.bluetoothReadBinary(4096).result
   print("Received! Get base64 " , len( instr ) , " byte(s)")
   print("instr = ",instr)
   
   print("Try to decode the receive bytes ...")
   try:
    inbyte = base64.b64decode(bytes(instr,encoding = "utf8"))
    #inbyte = base64.b64decode(instr)
    print("Received! Get " , len( inbyte ) , " byte(s)")
    print("inbyte = ",inbyte)
    for b in inbyte :
     print(b)
   except:
    print("Decode fail!")
   
  except:
   print("Receive fail!")
 
 except:
  print("Send fail!")

 return inbyte

def CMD_SETANGLE(pitch,roll,yaw):
 outmp = b'\x0e\x11' + f2b(pitch) + f2b(roll) + f2b(yaw) + b'\x00\x00'
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)

def CMD_SETPWMOUT(pwm):
 outmp = b'\x02\x13' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)
 
def ACT_YICAM_TRIGGER():
 CMD_SETPWMOUT(2000)
 time.sleep(50)
 CMD_SETPWMOUT(1000)

def ACT_YICAM_MODE():
 CMD_SETPWMOUT(2000)
 time.sleep(200)
 CMD_SETPWMOUT(1000)

def CMD_SETPITCH(pwm):
 outmp = b'\x02\x0A' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)
 
def CMD_SETROLL(pwm):
 outmp = b'\x02\x0B' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)

def CMD_SETYAW(pwm):
 outmp = b'\x02\x0C' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)

def CMD_SETSTANDBY(bstr):
 outmp = b'\x01\x0E' + bstr
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)

def ACT_STANDBY(innum):
 outmp = b'\x00'
 if(innum == 1):
  outmp = b'\x01'
 CMD_SETSTANDBY(outmp)

def CMD_SETPANMODE(bstr):
 outmp = b'\x01\x0D' + bstr
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)

def CMD_SETPITCHROLLYAW(ppwm,rpwm,ypwm):
 outmp = b'\x06\x12' + pwm2b(ppwm) + pwm2b(rpwm) + pwm2b(ypwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp,0.1)

def CMD_GETDATA():
 outmp = b'\x01\x05\x00'
 outmp = b'\xfa' + outmp + crc(outmp)
 data = sgdata(outmp,1)
 return data[5:len(data)-2]

def ACT_GETVOL(data):
 #data = CMD_GETDATA()
 print(data)
 print(data[8:10])
 vol = 1.0 * struct.unpack("I",data[8:10]+b'\x00\x00')[0] / 1000.0
 print(vol)
 return vol

def ACT_GETSTATUS(data):
 #data = CMD_GETDATA()
 print(data)
 print(data[0:2])
 thestatus = struct.unpack("I",data[0:2]+b'\x00\x00')[0]
 print(thestatus)
 return thestatus

def ACT_STRSTATUS(status):
 print(status)
 outstr = ""
 if(status == 0):
  outstr = "S_MOTORS"
 elif(status == 1):
  outstr = "S_SETTLE"
 elif(status == 2):
  outstr = "S_CALIBRATE"
 elif(status == 3):
  outstr = "S_LEVEL"
 elif(status == 4):
  outstr = "S_MOTORDIRDETECT"
 elif(status == 5):
  outstr = "S_RELEVEL"
 elif(status == 6):
  outstr = "NORMAL"
 elif(status == 7):
  outstr = "STANDBY"
 return outstr

def eventloop():
  udpwmstep = -50
  lrpwmstep = 10
  pitchpwm = 1500
  lastpitchpwm = 0
  yawpwm = 1500
  lastyawpwm = 0
  while True:
    event=droid.eventWait(50).result
    
    if event != None:
        print(event)
        if event["name"]=="key":
            droid.vibrate(30)
            if event["data"]["key"] == '4':
                return
        elif event["name"]=="screen":
            if event["data"]=="destroy":
                return
        elif event["name"]=="click":
            if event["data"]["id"]=="disconnectexit":
                return
            elif event["data"]["id"]=="U2":
                print("U2")
                pitchpwm += udpwmstep*2
            elif event["data"]["id"]=="U1":
                pitchpwm += udpwmstep
            elif event["data"]["id"]=="D1":
                pitchpwm -= udpwmstep
            elif event["data"]["id"]=="D2":
                pitchpwm -= udpwmstep*2
            elif event["data"]["id"]=="L2":
                yawpwm += lrpwmstep*2
            elif event["data"]["id"]=="L1":
                yawpwm += lrpwmstep
            elif event["data"]["id"]=="R1":
                yawpwm -= lrpwmstep
            elif event["data"]["id"]=="R2":
                yawpwm -= lrpwmstep*2
            elif event["data"]["id"]=="MI":
                pitchpwm = 1500
                yawpwm = 1500
            elif event["data"]["id"]=="S0":
                ACT_STANDBY(0)
            elif event["data"]["id"]=="S1":
                ACT_STANDBY(1)
            elif event["data"]["id"]=="M1":
                CMD_SETPANMODE(b'\x02')
            elif event["data"]["id"]=="M2":
                CMD_SETPANMODE(b'\x01')
            elif event["data"]["id"]=="M3":
                CMD_SETPANMODE(b'\x05')
            elif event["data"]["id"]=="getstatus":
                data = CMD_GETDATA()
                droid.fullSetProperty("statusinfo","text",ACT_STRSTATUS(ACT_GETSTATUS(data)))
                thevol = str(ACT_GETVOL(data))
                print(thevol)
                if(len(thevol) > 5):
                    thevol = thevol[:5]
                print(thevol)
                droid.fullSetProperty("volinfo","text",thevol)
            if pitchpwm!=lastpitchpwm or yawpwm!=lastyawpwm :
                CMD_SETPITCHROLLYAW(pitchpwm,1500,yawpwm)
                lastpitchpwm = pitchpwm
                lastyawpwm = yawpwm

################## Main ##############################################

droid = sl4a.Android()

uuid='00001101-0000-1000-8000-00805F9B34FB' #couldn't get bluetooth to work without this uuid..
mac='20:15:05:11:11:94' #bluetooth module mac address

print("Try to connect BT ...")
try:
 btresult = droid.bluetoothConnect(uuid,mac)
 print("Connected")
 print(btresult)
 
 time.sleep(1)
 
 try:
  print(droid.fullShow(layout))
  eventloop()  
 except:
  print("GUI Fail!")
  
except:
 print("Connect fail!")

droid.fullDismiss()
print("Try to stop BT and exit ...")
droid.bluetoothStop()
droid.exit()