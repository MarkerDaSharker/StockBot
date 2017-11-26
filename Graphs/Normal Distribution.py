import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.ticker as ticker
import datetime

start = datetime.datetime(1999,1,1)
end = datetime.datetime(2017,4,1)

fig, ax1 = plt.subplots()

FB = web.DataReader("CSIQ", "yahoo", start, end).as_matrix()
fb = pickle.load(open("CSIQ Lifetime.p", 'rb'))

mu, std = norm.fit(fb)

plt.hist(fb, bins=50, normed=True, alpha=.6, color='blue')

a1 = plt.axvline(x=np.median(fb), color = 'r')

a2 = plt.axvline(x=FB[-1][5]/FB[0][5]*100000, color = 'orange')

ax1.set_xlabel('Final Portfolio Values')

ax1.yaxis.set_ticks(np.arange(0))

plt.title("Distribution of CSIQ Stock AI")

ax1.legend((a1,a2), ('Median','Market'), loc = "upper left" )

plt.show()