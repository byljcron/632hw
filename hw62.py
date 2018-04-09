#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
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
    for i in range(0,20):
        X2=X2+(table[0][i][2]-table[1][i][2])**2/table[1][i][2]
    print("X2(theory1",X2)

    X2=0
    for i in range(0,20):
        X2=X2+(table[0][i][2]-table[2][i][2])**2/table[2][i][2]
    print("X2(theory2",X2)

table=readfile()
drawthehistogram(table)
cstest(table)


