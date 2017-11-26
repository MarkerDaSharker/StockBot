import cPickle as pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.ticker as ticker
import datetime

start = datetime.datetime(1999,1,1)
end = datetime.datetime(2017,4,1)

apple = web.DataReader("FB", "yahoo", start, end).as_matrix()
print apple[0][5]
print apple[1][5]

fb = pickle.load(open("FB Sample.p","rb"))

zz = []
total = [100000.0000]
price= [apple[0][5]]
stocks = [0]
for k in range(0,len(fb[0])):
    total2 = 0
    for s in range(0,len(fb)):
        total2 += fb[s][k][0]
    total.append(total2)
    
for k in range(0,len(fb[0])):
    total2 = 0
    for s in range(0,len(fb)):
        total2 += fb[s][k][1]
    stocks.append(total2)
    
for k in range(0,len(fb[0])):
    price.append(fb[0][k][2])

fig, ax1 = plt.subplots()

r = np.arange(0,len(total))


ax1.set_ylabel('Value of Portfolio')
ax1.set_xlabel('Days')
ln1 = ax1.plot(r, np.asarray(total), linestyle='-', color='black', linewidth=2.0)



ax2 = ax1.twinx()

ax1.xaxis.set_ticks(np.arange(0,len(r),150))

ax2.set_ylabel('FB Price')
ln2 = ax2.plot(r, np.asarray(price), linestyle='-', color='red', linewidth=2.0)

ax1.legend(loc=9)
ax2.legend(loc=9)


plt.legend((ln1[0],ln2[0]), ['AI',"FB Price"], loc=4)
plt.show()