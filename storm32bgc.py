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
 time.sleep(50)
 CMD_SETPWMOUT(1000)

def ACT_YICAM_MODE():
 CMD_SETPWMOUT(2000)
 time.sleep(200)
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

def CMD_SETSTANDBY(bstr):
 outmp = b'\x01\x0E' + bstr
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)

def ACT_STANDBY(innum):
 outmp = b'\x00'
 if(innum == 1):
  outmp = b'\x01'
 CMD_SETSTANDBY(outmp)

def CMD_SETPANMODE(bstr):
 outmp = b'\x01\x0D' + bstr
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)

def CMD_SETPITCHROLLYAW(ppwm,rpwm,ypwm):
 outmp = b'\x06\x12' + pwm2b(ppwm) + pwm2b(rpwm) + pwm2b(ypwm)
 outmp = b'\xfa' + outmp + crc(outmp)
 sgdata(outmp)

def CMD_GETDATA():
 outmp = b'\x01\x05\x00'
 outmp = b'\xfa' + outmp + crc(outmp)
 data = sgdata(outmp)
 return data[5:len(data)-2]

def ACT_GETVOL(data):
 #data = CMD_GETDATA()
 #print(data)
 #print(data[8:10])
 vol = 1.0 * struct.unpack("I",data[8:10]+b'\x00\x00')[0] / 1000.0
 #print(vol)
 return vol

 def ACT_STRSTATUS(status):
 outstr = "" + statue
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

def ACT_GETSTATUS(data):
 #data = CMD_GETDATA()
 return struct.unpack("I",data[0:2]+b'\x00\x00')[0]
 
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
  print("Vol = " , ACT_GETVOL())

 except:
  print("Logic action fail!")
  
except:
 print("Connect fail!")

print("Try to stop BT and exit ...")
droid.bluetoothStop()
droid.exit()

