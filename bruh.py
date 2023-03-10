import serial
import socket
import struct
import sys
import time
import ntplib

ser = serial.Serial('COM4', baudrate=115200)


asd = ntplib.NTPClient()
while True:
    try:
        response = asd.request('time.nist.gov')
        bruh = str(time.ctime(response.tx_time))
        bruh = bruh[11:20]
        bruh = bruh + "\n"
        bruh = bruh.encode()
        ser.write(bruh)
        time.sleep(1)
    except Exception:
        errorr = "NTP ERROR"
        errorr = errorr + "\n"
        errorr = errorr.encode()
        ser.write(errorr)
