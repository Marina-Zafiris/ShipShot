import io
import ais
import serial
from time import sleep

ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=5.0)
#this is silly, used to send fake NMEA data, shouldn't be necessary in Akwe
sleep(2)
ser.write(b'\x1b')
sleep(2)
ser.write(b'T')
sleep(2)
ser.write(b'\r')
#end silly
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

while 1:
    try:
        line = sio.readline()
        print("line = ",line)
        try:
            s = line.split(',')[5]
            print("s = ",s)
        except:
            print ('whoops')
            continue
        msg = ais.decode(s,0)
        print(repr(msg))
    except serial.SerialException as e:
        print('Device error: {}'.format(e))
        break
