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
				android:text="Status/Mode:" android:layout_weight="1" android:gravity="center" />
			<TextView android:id="@+id/statusinfo" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:textColor="#0bda51"
				android:text="-----" android:layout_weight="1" android:gravity="center" />
			<TextView android:id="@+id/lb3" android:layout_width="fill_parent"
				android:layout_height="fill_parent" android:textColor="#0bda51"
				android:text="Voltage/Detail:" android:layout_weight="1" android:gravity="center" />
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
			android:text="Program" android:layout_weight="1" android:gravity="center" />
		<LinearLayout android:layout_width="fill_parent"
			android:layout_weight="1" android:layout_height="fill_parent"
			android:orientation="horizontal">
			<Button android:id="@+id/pgpano" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="Panorama" />
			<Button android:id="@+id/pgtl" android:layout_width="fill_parent"
				android:layout_weight="1" android:layout_height="fill_parent"
				android:text="Time-lapse" />
		</LinearLayout>
		<TextView android:id="@+id/lb7" android:layout_width="fill_parent"
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
 #print("Try to send bytes ...")
 try:
  #droid.bluetoothWrite("\xfa\x00\x01\x00\x00")
  #droid.bluetoothWrite("".join(map(chr, [0xfa, 0x00, 0x0b, 0, 0])))
  #print("outbyte = ",outbyte)
  #droid.bluetoothWrite(outbyte)
  outstr = base64.b64encode(outbyte).decode("utf-8")
  #print("outstr = ",outstr)
  droid.bluetoothWriteBinary(outstr)
  #print("Sent!")
  
  if(waittime==0):
   waittime=0.1
  time.sleep(waittime)
  
  #Receive byte
  #print("Try to receive bytes ...")
  try:
   #instr = droid.bluetoothRead(4096).result
   instr = droid.bluetoothReadBinary(4096).result
   #print("Received! Get base64 " , len( instr ) , " byte(s)")
   #print("instr = ",instr)
   
   #print("Try to decode the receive bytes ...")
   try:
    inbyte = base64.b64decode(bytes(instr,encoding = "utf8"))
    #inbyte = base64.b64decode(instr)
    #print("Received! Get " , len( inbyte ) , " byte(s)")
    #print("inbyte = ",inbyte)
    #for b in inbyte :
    # print(b)
   except:
    print("Decode fail!")
    droid.fullSetProperty("volinfo","text","Decode fail!")
   
  except:
   print("Receive fail!")
   droid.fullSetProperty("volinfo","text","Receive fail!")
 
 except:
  print("Send fail!")
  droid.fullSetProperty("volinfo","text","Send fail!")

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
 time.sleep(0.25)
 CMD_SETPWMOUT(1000)

def ACT_YICAM_MODE():
 CMD_SETPWMOUT(2000)
 time.sleep(2)
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

def calc_waittime(np,ny):
 global cp
 global cy
 dp = 1.0 * abs(cp-np) / 25
 dy = 1.0 * abs(cy-ny) / 25
 cp = np
 cy = ny
 if(dp>dy):
  return dp
 else:
  return dy

def takephoto(np,ny):
 droid.fullSetProperty("volinfo","text","SETANGLE("+str(np)+",0,"+str(ny)+")")
 CMD_SETANGLE(np,0,ny)
 temp = calc_waittime(np,ny)
 #print("calc_waittime(np,ny) = ",temp)
 droid.fullSetProperty("volinfo","text","calc_waittime "+str(temp))
 time.sleep(temp)
 #print("delaybefore = ",delaybefore)
 droid.fullSetProperty("volinfo","text","delaybefore "+str(delaybefore))
 time.sleep(delaybefore)
 droid.fullSetProperty("volinfo","text","YICAM_TRIGGER")
 ACT_YICAM_TRIGGER()
 #print("delayafter = ",delayafter)
 droid.fullSetProperty("volinfo","text","delayafter "+str(delayafter))
 time.sleep(delayafter)

def act_pano():
 try:
  droid.fullSetProperty("statusinfo","text","Panorama")
  droid.fullSetProperty("volinfo","text","Init...")
  
  global delaybefore
  global delayafter
  delaybefore = 1
  delayafter = 2
  try:
   delaybefore = float(droid.dialogGetInput('Storm32BGC Panorama', 'Delay (sec) before take photo?',str(delaybefore)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.")
   droid.fullSetProperty("volinfo","text","error")
  try:
   delayafter = float(droid.dialogGetInput('Storm32BGC Panorama', 'Delay (sec) after take photo?',str(delayafter)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","error")
  
  #change to HHH
  #CMD_SETPANMODE(b'\x02')
   
  global cp
  global cy
  cp = 0
  cy = 0
  
  droid.fullSetProperty("volinfo","text","SetAngle(0,0,0)")
  CMD_SETANGLE(0,0,0)
  
  wakeremote = 0
  try:
   wakeremote = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'Did you need to wake up the remote control(1=need)?',str(wakeremote)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","wakeremote error")
  if(wakeremote==1):
   # Active the remote control
   droid.fullSetProperty("volinfo","text","Wakeup BT remote")
   ACT_YICAM_TRIGGER()
   droid.fullSetProperty("volinfo","text","sleep 1")
   time.sleep(1)
  
  droid.fullSetProperty("volinfo","text","Start")
  countemp = 0
  takephoto(-90,0)
  countemp+=1
  droid.fullSetProperty("statusinfo","text","Pano "+str(countemp)+"/20")
  
  takephoto(-90,-90)
  countemp+=1
  droid.fullSetProperty("statusinfo","text","Pano "+str(countemp)+"/20")
  
  pitch=-45
  numphoto = 4
  angletmp = 360.0 / numphoto
  dir = 1
  for i in range(0,numphoto,dir):
   takephoto(pitch,i*angletmp+angletmp/2-180)
   countemp+=1
   droid.fullSetProperty("statusinfo","text","Pano "+str(countemp)+"/20")
  
  pitch=0
  numphoto = 6
  angletmp = 360.0 / numphoto
  dir = -1
  for i in range(numphoto,0,dir):
   takephoto(pitch,i*angletmp-angletmp/2-180)
   countemp+=1
   droid.fullSetProperty("statusinfo","text","Pano "+str(countemp)+"/20")
  
  pitch=45
  numphoto = 4
  angletmp = 360.0 / numphoto
  dir = 1
  for i in range(0,numphoto,dir):
   takephoto(pitch,i*angletmp+angletmp/2-180)
   countemp+=1
   droid.fullSetProperty("statusinfo","text","Pano "+str(countemp)+"/20")
   
  CMD_SETANGLE(0,0,0)
  #time.sleep(calc_waittime(0,0))
  
  #change to HHP
  #time.sleep(2)
  #CMD_SETPANMODE(b'\x01')
  droid.fullSetProperty("statusinfo","text","Finish")
  droid.fullSetProperty("volinfo","text","-")
 except:
  print("act_pano fail!")
  droid.fullSetProperty("volinfo","text","act_pano fail!")

def act_tl():
 try:
  droid.fullSetProperty("statusinfo","text","Time-lapse")
  droid.fullSetProperty("volinfo","text","Init...")
  #delaybefore = 1
  #try:
  # delaybefore = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'Delay (sec) before take photo?',str(delaybefore)).result)
  # #droid.dialogDismiss()
  #except:
  # #print("It is not a number. Use default values here.")
  # droid.fullSetProperty("volinfo","text","delaybefore error")
  #delayafter = 1
  #try:
  # delayafter = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'Delay (sec) after take photo?',str(delayafter)).result)
  # #droid.dialogDismiss()
  #except:
  # #print("It is not a number. Use default values here.") 
  # droid.fullSetProperty("volinfo","text","delayafter error")
  startpi = 0
  try:
   startpi = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'Start Patch angle(degree)?',str(startpi)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","startpi error")
  startya = 45
  try:
   startya = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'Start Yaw angle(degree)?',str(startya)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","startya error")
  endpi = 0
  try:
   endpi = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'End Patch angle(degree)?',str(endpi)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","endpi error")
  endya = -45
  try:
   endya = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'End Yaw angle(degree)?',str(endya)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","endya error")
  usetime = 180
  try:
   usetime = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'Use how many time(Sec)?',str(usetime)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","usetime error")
  wakeremote = 0
  try:
   wakeremote = float(droid.dialogGetInput('Storm32BGC Time-lapse', 'Did you need to wake up the remote control(1=need)?',str(wakeremote)).result)
   #droid.dialogDismiss()
  except:
   #print("It is not a number. Use default values here.") 
   droid.fullSetProperty("volinfo","text","wakeremote error")
  if(wakeremote==1):
   # Active the remote control
   droid.fullSetProperty("volinfo","text","Wakeup BT remote")
   ACT_YICAM_TRIGGER()
   droid.fullSetProperty("volinfo","text","sleep 1")
   time.sleep(1)
  
  currpi = startpi
  currya = startya 
  CMD_SETANGLE(currpi,0,currya)
  #droid.fullSetProperty("volinfo","text","1")
  time.sleep(10)
  eachdelay = 0.5
  #droid.fullSetProperty("volinfo","text","1.1")
  loopcycle = int(1.0 * usetime / eachdelay)
  #droid.fullSetProperty("volinfo","text","1.2")
  steppi = (endpi - startpi) / loopcycle
  #droid.fullSetProperty("volinfo","text","1.3")
  stepya = (endya - startya) / loopcycle
  #droid.fullSetProperty("volinfo","text","2")
  
  droid.fullSetProperty("volinfo","text","Start")
  ACT_YICAM_TRIGGER()
  #droid.fullSetProperty("volinfo","text","3")
  
  for i in range(loopcycle,0,-1):
   #droid.fullSetProperty("volinfo","text","4")
   currpi += steppi
   currya += stepya 
   CMD_SETANGLE(currpi,0,currya)
   droid.fullSetProperty("volinfo","text","Remain step(s) "+str(i))
   time.sleep(eachdelay)
  
  droid.fullSetProperty("volinfo","text","End")
  ACT_YICAM_TRIGGER()
  
  time.sleep(1)
  CMD_SETANGLE(0,0,0)
  
  droid.fullSetProperty("statusinfo","text","Finish")
  droid.fullSetProperty("volinfo","text","-")
 except:
  print("act_tl fail!")
  droid.fullSetProperty("volinfo","text","act_tl fail!")
  
def eventloop():
 udpwmstep = -50
 lrpwmstep = 10
 pitchpwm = 1500
 lastpitchpwm = 0
 yawpwm = 1500
 lastyawpwm = 0
 while True:
  try:
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
               CMD_SETANGLE(0,0,0)
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
           elif event["data"]["id"]=="pgpano":
               act_pano()
           elif event["data"]["id"]=="pgtl":
               act_tl()
           if pitchpwm!=lastpitchpwm or yawpwm!=lastyawpwm :
               CMD_SETPITCHROLLYAW(pitchpwm,1500,yawpwm)
               lastpitchpwm = pitchpwm
               lastyawpwm = yawpwm
  except:
   print("Spmething fail in eventloop!")
   droid.fullSetProperty("volinfo","text","eventloop fail!")

################## Main ##############################################

droid = sl4a.Android()

uuid='00001101-0000-1000-8000-00805F9B34FB' #couldn't get bluetooth to work without this uuid..
mac='98:D3:31:40:19:88' #bluetooth module mac address

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
