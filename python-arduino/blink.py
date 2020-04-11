import serial
import time
ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)

for i in range(10):
    ser.writelines(b'H')   # send a byte
    time.sleep(0.5)        # wait 0.5 seconds
    ser.writelines(b'L')   # send a byte
    time.sleep(0.5)

ser.close()
