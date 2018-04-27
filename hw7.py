import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import  svm
from sklearn.svm import SVC
r=5.0
n=1000
def rclass2():
    rr=np.random.normal(0,1,n)
    phi=2.0*np.random.random(n)*math.pi
    actualr=r+rr
    return [actualr*np.cos(phi),actualr*np.sin(phi)]

def rclass1():
    return [np.random.normal(0,1,n),np.random.normal(0,1,n)]

def selectsample():
    global sample
    global cls
    for i in range(0,100):
        n=np.random.randint(0,2000)
        if n<1000:
            sample.append([class1[0][n],class1[1][n]])
            cls.append(0)
        else  :
            sample.append([class2[0][n-1000],class2[1][n-1000]])
            cls.append(1)

def a():
    plt.plot(class1[0],class1[1],'ro',color='r')
    plt.plot(class2[0],class2[1],'ro',color='b')
    plt.show()

def b():
    plt.hist(class1[0]+class2[0])
    plt.show()

    classs=np.concatenate((class1,class2), axis=1)


    xmin = classs[0].min()
    xmax = classs[0].max()
    ymin = classs[1].min()
    ymax = classs[1].max()

    X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([X.ravel(), Y.ravel()])
    values = np.vstack(classs)
    kernel = stats.gaussian_kde(values)
    Z = np.reshape(kernel(positions).T, X.shape)
    fig, ax = plt.subplots()

    ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r, extent=[xmin, xmax, ymin, ymax])
    plt.show()
def c():
    classs=np.concatenate((class1,class2), axis=1)
    xmin = classs[0].min()
    xmax = classs[0].max()
    ymin = classs[1].min()
    ymax = classs[1].max()

    global sample
    global cls
    global clf
    selectsample()
    clf=SVC()
    clf.fit(sample,cls)
    plt.clf()
    plt.scatter(classs[0], classs[1], c=[0]*1000+[1]*1000, zorder=10, cmap=plt.cm.Paired,
                edgecolor='k', s=20)
    XX, YY = np.mgrid[xmin:xmax:200j, ymin:ymax:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                linestyles=['--', '-', '--'], levels=[-.5, 0, .5])

    plt.show()

def d():
    global clf
    class1predit=(clf.predict(np.array(class1).T))
    class2predit=(clf.predict(np.array(class2).T))
    p1=0.0
    p2=0.0
    for i in class1predit:
        if i == 1:p1=p1+1

    for i in class2predit:
        if i == 0:p2=p2+1
    print((p1+p2)/2000)




class1=rclass1()
class2=rclass2()
sample=[]
cls=[]


a()
b()
c()
d()
