import cPickle as pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime

csiq = pickle.load(open("CSIQ Lifetime.p", 'rb'))
csiqR = pickle.load(open("CSIQ Random Lifetime.p", 'rb'))
tsla = pickle.load(open("TSLA Lifetime.p", 'rb'))
tslaR = pickle.load(open("TSLA Random Lifetime.p", 'rb'))
fb = pickle.load(open("FB Lifetime.p", 'rb'))
fbR = pickle.load(open("FB Random Lifetime.p", 'rb'))

print np.median(csiq), np.median(csiqR)
print np.median(tsla), np.median(tslaR)


start = datetime.datetime(1999,1,1)
end = datetime.datetime(2017,4,1)

FB = web.DataReader("FB", "yahoo", start, end).as_matrix()
CSIQ = web.DataReader("CSIQ", "yahoo", start, end).as_matrix()
TSLA = web.DataReader("TSLA", "yahoo", start, end).as_matrix()



a = [np.median(csiq),np.median(fb),np.median(tsla)]
b = [np.max(csiq),np.max(fb),np.max(tsla)]
c = [np.median(csiqR),np.median(fbR),np.median(tslaR)]
d =[CSIQ[-1][5]/CSIQ[0][5]*100000,FB[-1][5]/FB[0][5]*100000,TSLA[-1][5]/TSLA[0][5]*100000]

x = ["CSIQ","FB","TSLA"]

ini = np.arange(30,33)

ax = plt.subplot(111)

w = .25

bar1 = ax.bar(ini +w/2, a, w-.05, color='r')
bar2 = ax.bar(ini+ w+w/2-.05 , b, w-.05, color='g')
bar3 = ax.bar(ini+ w*2+w/2-.05*2 , c, w-.05, color='y')
bar4 = ax.bar(ini+ w*3-.05*.5, d, w-.05, color='b')

ax.set_xticks(ini+w*2+.025)
ax.set_xticklabels( ('CSIQ', 'FB', 'TSLA') )

ax.legend( (bar1[0], bar2[0], bar3[0], bar4[0]), ('AI Med', 'AI Max', 'Random', 'Market'), loc = "upper left" )

plt.title("AI vs Other Methods")
plt.show()