from numpy import random
from matplotlib import pyplot
def oneround (gamernumber):
    result=0
    tail=0
    head=0
    for nthgamer in range(0,gamernumber):
        result=random.random_integers(2)
        if result==1:
            tail=tail+1
        else:
            head=head+1

    if tail==1 or head ==1:
        return True
    else:
        return False

def onegame (gamernumber):
    nround=1;
    while oneround(gamernumber):
        nround=nround+1
    print(nround)
    return nround


games=2000
people=5
result=[0]*100
resultsum=0
for nthgame in range(1,games):
    resultsave=onegame(people)
    resultsum=resultsum+resultsave
    if resultsave>100:
        result[99]=result[99]+1
    else:
        result[resultsave]=result[resultsave]+1
print("average:")
print(resultsum/games)
pyplot.plot(result)
pyplot.show()
