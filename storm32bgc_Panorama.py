import sl4a
import time
import array
import base64
import struct

droid = sl4a.Android()

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

def sgdata(outbyte):
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
  
  time.sleep(0.2)
  
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
 sgdata(outmp)

def CMD_SETPWMOUT(pwm):
 outmp = b'\x02\x13' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)
 
def ACT_YICAM_TRIGGER():
 CMD_SETPWMOUT(2000)
 time.sleep(0.5)
 CMD_SETPWMOUT(1000)

def ACT_YICAM_MODE():
 CMD_SETPWMOUT(2000)
 time.sleep(2)
 CMD_SETPWMOUT(1000)

def CMD_SETPITCH(pwm):
 outmp = b'\x02\x0A' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)
 
def CMD_SETROLL(pwm):
 outmp = b'\x02\x0B' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)

def CMD_SETYAW(pwm):
 outmp = b'\x02\x0C' + pwm2b(pwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)

def CMD_SETPITCHROLLYAW(ppwm,rpwm,ypwm):
 outmp = b'\x06\x12' + pwm2b(ppwm) + pwm2b(rpwm) + pwm2b(ypwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)
 
################## Main ##############################################

uuid='00001101-0000-1000-8000-00805F9B34FB' #couldn't get bluetooth to work without this uuid..
mac='20:15:05:11:11:94' #bluetooth module mac address

print("Try to connect BT ...")
try:
 btresult = droid.bluetoothConnect(uuid,mac)
 print("Connected")
 print(btresult)
 
 time.sleep(1)
 
 try:
 
  CMD_SETANGLE(0,0,0)
  
  # Active the remote control
  for i in range(0,3,1):
   ACT_YICAM_TRIGGER()
   time.sleep(2)
 
  delaybefore = 1
  delayafter = 1
 
  CMD_SETANGLE(-90,0,0)
  time.sleep(90/20)
  time.sleep(delaybefore)
  ACT_YICAM_TRIGGER()
  time.sleep(delayafter)
  
  CMD_SETANGLE(-90,0,-90)
  time.sleep(90/20)
  time.sleep(delaybefore)
  ACT_YICAM_TRIGGER()
  time.sleep(delayafter)
  
  pitch=-45
  numphoto = 3
  angletmp = 360.0 / numphoto
  dir = 1
  for i in range(0,numphoto,dir):
   CMD_SETANGLE(pitch,0,i*angletmp+angletmp/2-180)
   time.sleep(angletmp/20)
   time.sleep(delaybefore)
   ACT_YICAM_TRIGGER()
   time.sleep(delayafter)
  
  pitch=0
  numphoto = 6
  angletmp = 360.0 / numphoto
  dir = -1
  for i in range(numphoto,0,dir):
   CMD_SETANGLE(pitch,0,i*angletmp-angletmp/2-180)
   time.sleep((angletmp)/20)
   time.sleep(delaybefore)
   ACT_YICAM_TRIGGER()
   time.sleep(delayafter)  
  
  pitch=45
  numphoto = 3
  angletmp = 360.0 / numphoto
  dir = 1
  for i in range(0,numphoto,dir):
   CMD_SETANGLE(pitch,0,i*angletmp+angletmp/2-180)
   time.sleep(angletmp/20)
   time.sleep(delaybefore)
   ACT_YICAM_TRIGGER()
   time.sleep(delayafter)
   
  CMD_SETANGLE(0,0,0)
  
 except:
  print("Call sgdata fail!")
  
except:
 print("Connect fail!")

print("Try to stop BT and exit ...")
droid.bluetoothStop()
droid.exit()

