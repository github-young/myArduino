#!coding:utf-8

import serial
#import serial.tools.list_ports

try:
    portN = "/dev/ttyUSB0"
    bps = 9600
    timeOut = 5
    ser = serial.Serial(portN, bps, timeout=timeOut)
    #print(ser)
    #print(ser.port)
    #print(ser.baudrate)
    res = ser.readline()
    #print(ser.in_waiting())
    print(res.decode("utf-8"))
    print(type(res))

    ser.close()
except Exception as e:
    print("Error: ", e)
