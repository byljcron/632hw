#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
def readfile():

    f = open('prob_6_2.dat', 'r')
    result = list()
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('//'):
            continue
        nline=list()
        for a in line.split():
            nline.append(float(a))
        result.append(nline)
    table=np.array([np.asarray(result[:20]),np.asarray(result[20:40]),np.asarray(result[40:])])
    return table

def drawthehistogram(table):
    plt.bar(table[0].T[0]+0.25,table[0].T[2],0.5)
    plt.bar(table[1].T[0]+0.25,table[1].T[2],0.5,color='red')
    plt.bar(table[2].T[0]+0.25,table[2].T[2],0.5,color='yellow')
    plt.errorbar(table[1].T[0]+0.25,table[1].T[2] ,  yerr=table[1].T[2]-table[0].T[2]/2,color='pink')
    plt.errorbar(table[2].T[0]+0.25,table[2].T[2] ,  yerr=table[2].T[2]-table[0].T[2]/2,color='yellow')
    plt.show()

def cstest(table):
    X2=0
    sum1=0
    for i in range(0,20):
        sum1=sum1+(table[1][i][2])
    for i in range(0,20):
        X2=X2+(table[0][i][2]/49-(table[1][i][2])/sum1)**2/(table[1][i][2]/sum1)
    print("X2(theory1)",X2)

    X2=0
    for i in range(0,20):
        X2=X2+(table[0][i][2]/49-(table[2][i][2])/sum1)**2/(table[2][i][2]/sum1)
    print("X2(theory2)",X2)



def findk():
    global table
    k1=0
    k2=0
    sumk1=0
    sumk2=0

    for i in range(0,20):
        k1=k1+table[1][i][2]*(table[1][i][0]+0.25)
        k2=k2+table[2][i][2]*(table[2][i][0]+0.25)
        sumk1=sumk1+table[2][i][2]
        sumk2=sumk2+table[2][i][2]
    k1=k1/sumk1
    k2=k2/sumk2
    print(k1,k2)
    return [k1,k2]

def chisquareMC(df):
    x=np.random.random()*10
    fx=np.random.random()*1
    if chi2.pdf(x, df)>=fx:
        return x
    else :
        return chisquareMC(df)
def MC():
    df=findk()
    actualtheory=np.copy(table)
    for i in range(0,20):
        actualtheory[1][i][2]=0
        actualtheory[2][i][2]=0
    t1n=0
    t2n=0
    for i in range(0,10000):
        actualtheory[1][int(chisquareMC(df[0])*2)][2]+=1
        actualtheory[2][int(chisquareMC(df[1])*2)][2]+=1
    return actualtheory

def r100():
    random100=np.copy(table)
    for i in range(0,20):
        random100[1][i][2]=0
        random100[2][i][2]=0
    for i in range(0,100):
        r=np.random.randint(0,10000)
        sumr=0
        for j in range(0,20):
            sumr=sumr+actualtable[1][j][2]
            if sumr>=r:
                random100[1][j][2]+=1
                break
    return random100

def draw100histogram():
    for i in range(0,100):
        rtable=r100()
        plt.bar(rtable[1].T[0]+0.25,rtable[1].T[2],0.5,color=[(i*0.01,i*0.01,i*0.01)])
    plt.show()
#a,b
table=readfile()
drawthehistogram(table)
cstest(table)

#cd
actualtable=MC()
cstest(actualtable)
drawthehistogram(actualtable)

#e
draw100histogram()
