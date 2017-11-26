import sarsa
import time
import sys
import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
import multiprocessing
from joblib import Parallel, delayed
import cPickle as pickle


start = datetime.datetime(1999,1,1)
end = datetime.date.today()

apple = web.DataReader("CSIQ", "yahoo", start, end).as_matrix()

#lastState = None
#lastAction = None

#ai = sarsa.Sarsa(actions=range(5), epsilon=0.01, alpha=0.1, gamma=0.90)
    
def calcState(diff, counter):
    if np.sign(diff) == np.sign(counter):
        counter += np.sign(counter)
        return counter
    else:
        counter = np.sign(diff)
        return np.sign(diff)
    

ending = []
epsilon0 = 0
alpha0 = 0.2
gamma0 = 0.99

#count = 0
#count2 = 0
#stock = 0
#money = 100000
def processInput(i):
    ending = []
    startingM = 10000
    for k in range(0,10):
        lastState = None
        lastAction = None
    
        ai = sarsa.Sarsa(actions=range(5), epsilon=epsilon0, alpha=alpha0, gamma=gamma0)
        
        count = 0
        count2 = 0
        stock = 0
        money = startingM
        value = startingM
        while count < len(apple):
            lastValue = value
            value = money + apple[count][5]*stock
            if count > 0 :
                adjclosediff = apple[count][5] - apple[count-1][5]
            else:
                adjclosediff = 0
            
            state = calcState(adjclosediff, count2)
            #reward = adjclosediff*stock
            
            reward = lastValue - value + adjclosediff*stock - np.sign(state)*money

            
            action = ai.chooseAction(state)
            
            if lastAction is not None:
                    ai.learn(lastState, lastAction, reward, state, action)
            
        
            if action == 1:
                if money >= apple[count][5]*50:
                    stock += 50
                    money += -apple[count][5]*50
                    
                else:
                    action = 0
                    
            if action == 2:
                if money >= apple[count][5]*100:
                    stock += 100
                    money += -apple[count][5]*100
                    
                else:
                    if money >= apple[count][5]*50:
                        stock += 50
                        money += -apple[count][5]*50
                        action = 1
                        
                    else:
                        action = 0
                        
            if action == 3:
                if stock > 50:
                    stock += -50
                    money += apple[count][5]*50
                    
                else:
                    action = 0
                    
            if action == 4:
                if stock > 100:
                    stock += -100
                    money += apple[count][5]*100
                    
                else:
                    if stock > 50:
                        stock += -50
                        money += apple[count][5]*50
                        action = 3
                    else:
                        action = 0
                        
            lastState = state
            lastAction = action
            
                    
            count += 1
            
            #print(money, stock)
            
                
        ending.append(money + apple[count-1][5]*stock)
    return ending
    
    
    
def main():
    num_cores = multiprocessing.cpu_count()
    
            
            
    ending = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in range(0,1000))
    
        
    
    z = []
    
    for k in ending:
        z.append(np.sum(k))
        
    z = np.sort(z)
    print "median:", np.median(z)
    print "mean:", np.mean(z)
    print "std:", np.std(z)
    print "max:", max(z)
    print "min:", min(z)
    
    percent = apple[-1][5]/apple[0][5]
    
    print percent
    print "other:", np.searchsorted(z,percent*100000)
    
    pickle.dump(z, open("data.p","wb"))

if __name__ == "__main__": main()