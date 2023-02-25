import serial
import socket
import struct
import sys
import time
import ntplib




ser = serial.Serial('COM4', baudrate=115200)

# def RequestTimefromNtp(addr='th.pool.ntp.org'):
#     REF_TIME_1970 = 2208988800  # Reference time
#     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     data = b'\x1b' + 47 * b'\0'
#     client.sendto(data, (addr, 123))
#     data, address = client.recvfrom(1024)
#     if data:
#         t = struct.unpack('!12I', data)[10]
#         t -= REF_TIME_1970
#     return time.ctime(t), t

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
