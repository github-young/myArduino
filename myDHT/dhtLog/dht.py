#!coding:utf-8

import serial
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
#import serial.tools.list_ports

WDIR = "/path/to/the/working/dir/ended/with/a/slash/"
dataFileName = WDIR+"data.csv"

try:
    portN = "/dev/ttyUSB0"
    bps = 9600
    timeOut = 5
    ser = serial.Serial(portN, bps, timeout=timeOut)
    time = pd.Timestamp.now().strftime("%Y-%m-%d-%H-%M-%S")
    res = ser.readline()
    outputText = time+", "+res.decode("utf-8")
    with open(dataFileName, 'a') as f:
        f.writelines(outputText)
    f.close()
    print(outputText.rstrip())
    ser.close()
except Exception as e:
    print("Error: ", e)

# data
data = pd.DataFrame(pd.read_csv(dataFileName, header=None))
(rows, columns) = data.shape
#t = data[data.columns[0]]
t = pd.to_datetime(data[0], format="%Y-%m-%d-%H-%M-%S")
T = data[data.columns[1]]
H = data[data.columns[2]]

# Plot
fig, ax1 = pl.subplots(1, 1, figsize=[15,8])
Tplot = ax1.plot(t, T, 'r-', label="Temperature", alpha=0.7)

pl.xticks(rotation=30)
pl.minorticks_on()

ax2 = ax1.twinx()
Hplot = ax2.plot(t, H, 'b-', label="Humidity", alpha=0.7)

lns = Hplot+Tplot
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, fontsize=15)

ax1.grid()
ax1.set_title("Dulab Status: Temperature & Humidity", fontsize=20)
ax1.set_xlabel("Time", fontsize=15)
ax1.set_ylabel("Temperature / °C", fontsize=15)
ax2.set_ylabel("Humidity / %", fontsize=15)

pl.savefig(WDIR+"TH.svg", bbox_inches='tight', pad_inches=0.5)
pl.close()

