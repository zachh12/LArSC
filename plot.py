import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

for i in range(0, 1000):
    df = pd.read_hdf("LAr_Env.h5", key='data')
    #plt.plot(df['Temperature (K)'])
    #plt.show()
    #exit()

    time = np.array(df['Time'], dtype=float)
    time = time/60

    plt.figure(1)
    plt.subplot(3,2,2)
    plt.title("Pressure")
    press = np.array(df['Pressure (arb)'], dtype=float)
    plt.plot(time, press, color='green')
    plt.xlabel("Time (min)")
    plt.ylabel("Pressure (arb)")

    plt.subplot(3,2,1)
    plt.title("Cooldown")
    plt.plot(time, df['Temperature (K)'], color='red')
    plt.axhline(88, color='blue')
    plt.xlabel("Time (min)")
    plt.ylabel("Temperature (K)")

    plt.subplot(3,1,2)
    plt.title("Volume")
    plt.xlabel("Time (min)")
    plt.ylabel("Liquid Volume (mL)")
    flow = np.array(df['Flow (L)'], dtype=float)
    plt.plot(time, (1000*(flow/784)), color='blue')

    plt.subplots_adjust(hspace=1)
    print((1000*(flow/784))[-1], press[-1])
    plt.pause(60)
plt.show()