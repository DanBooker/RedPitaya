import numpy as np
import redpitaya_scpi as scpi
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------

'''Create figure please'''
plt.ion()
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_ylabel('Voltage(V)')
ax.set_xlabel('Time(ms)')

#-----------------------------------------------------------------------------

rp_s = scpi.scpi('152.78.193.126') #connect to red pitaya ip

timescale = 1 #timescale of x-axis in ms

sample_rate_dict = {'125':'125MHz', '15.6': '15_6MHz', '1.9': '1_9MHz'} #possible sample rates

rp_s.tx_txt('ACQ:DEC 64') #decimation
rp_s.tx_txt('ACQ:SRAT '+ sample_rate_dict['125']) #sample rate
rp_s.tx_txt('ACQ:TRIG:LEV 0') #trigger level in mV
rp_s.tx_txt('ACQ:TRIG:DLY 8192') #trigger delay in sample steps
rp_s.tx_txt('ACQ:AVG OFF')

#-----------------------------------------------------------------------------

'''Function to read data from Red Pitaya and return as array'''
def getdata(ch=1, tch=2):
    rp_s.tx_txt('ACQ:START')
    rp_s.tx_txt('ACQ:TRIG CH%d_PE' % tch)
    while 1:        
        rp_s.tx_txt('ACQ:TRIG:STAT?')
        if rp_s.rx_txt() == 'TD':
            break
    rp_s.tx_txt('ACQ:SOUR%d:DATA:LAT:N? 16384' % ch)
    buff_string = rp_s.rx_txt()
    buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
    buff = map(float, buff_string)
    return buff

#-----------------------------------------------------------------------------

buff = getdata() #get data from red pitaya
#time = np.linspace(0, timescale, len(buff))
l, = ax.plot(buff) #plot data
plt.show()

while 1:
    try:
        buff = getdata() #get new set of data
        l.set_ydata(buff) #updata graph
        ax.set_ylim([0.97*np.min(buff), np.max(buff)])
        #ax.set_ylim([0.28, 0.32])
        plt.draw()
        plt.pause(0.00001)
    except KeyboardInterrupt:
        rp_s.tx_txt('ACQ:RST')   #reset acqusition
        break