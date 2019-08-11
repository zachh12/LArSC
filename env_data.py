import pandas as pd
import numpy as np
import serial
import time
import warnings
warnings.filterwarnings('ignore',category=pd.io.pytables.PerformanceWarning)

#Define Dataframe
cols = ["Time", "Temperature (K)", "Pressure (arb)", "Flow (L)"]
df = pd.DataFrame(columns=cols)

#Connect to Arduino
try:
    port = '/dev/tty.usbmodem14101'
    ard = serial.Serial(port,9600,timeout=5)
except:
    print("Failed to connect to arduino, check ports")
    exit()

#Connect to Alicat Flow
#try:
#    port = '/dev/tty.usbserial-FTU876JR'
#    flow = serial.Serial(port,9600,timeout=5)
#except:
#    print("Failed to connect to Alicat Flow Gauge, check ports")

#Take Data
idx, group = 0, 0
while idx > -1:
    #Tell arduino to take reading, only one delay
    if (ard.inWaiting() >= 2):
        print(ard.inWaiting())
        temp = (float)(ard.readline()[:-2])
        pressure = (float)(ard.readline()[:-2])
        print(ard.inWaiting())
        #temp, pressure = 0, 0

        #Read from Alicat flow gauge
        flow = open('flow.txt', 'r')
        line = flow.readlines()[-1]
        row = []
        num = ""
        for l in line:
            if l == '\t':
                row.append(num)
                num = ""
            else:
                num += l
        flow.close()

        df.loc[idx] = [row[0], temp, pressure, row[11]]

        idx += 1
        group += 1
        if group >= 6:
            #print("Savedd!")
            df.to_hdf("LAr_Env.h5", key='data')
            group = 0
            #print(df)
            #exit()

