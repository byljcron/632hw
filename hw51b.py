#! python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def read_data():
  class1=np.array([[0,1,5], [1, 2,6], [2, 3,4],[3,3,7],[4,5,6],[5,5,5]], dtype=np.float)

  class2=np.array([[1,0,4], [2,1,3], [3,1,5],[3,2,4],[5,3,4],[6,5,6]], dtype=np.float)

  return class1, class2


def main():

  class1, class2=read_data()

  mean1=np.mean(class1, axis=0)
  mean2=np.mean(class2, axis=0)

  #calculate variance within class
  Sw=np.dot((class1-mean1).T, (class1-mean1))+np.dot((class2-mean2).T, (class2-mean2))

  #calculate weights which maximize linear separation
  w=np.dot(np.linalg.inv(Sw), (mean2-mean1))

  print( "vector of max weights", w)
  print(np.dot(class1, w),np.mean(np.dot(class1, w)),np.cov(np.dot(class1, w)))
  print(np.dot(class2, w),np.mean(np.dot(class2, w)),np.cov(np.dot(class2, w)))

  #projection of classes on 1D space
  plt.plot(np.dot(class1, w), [0]*class1.shape[0], "bo", label="Iris-setosa")
  plt.plot(np.dot(class2, w), [0]*class2.shape[0], "go", label="Iris-versicolor and Iris-virginica")
  plt.legend()

  plt.show()

main()
