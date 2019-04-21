import numpy as np
from numpy import mat

def loadDataSet(filename):
    dataMat = []
    labelMat = []
    numFeat = len(open(filename).readline().split('\t')) - 1
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def standReges(XArr, yArr):
    XMat = mat(XArr)
    yMat = mat(yArr).T
    XTX = XMat.T * XMat
    if np.linalg.det(XTX) == 0.0:
        print("This matrix is singular,cannot do inverse")
        return
    Ws = XTX.I * XMat.T * yMat
    return Ws

D, L = loadDataSet('ex0.txt')
Ws = standReges(D, L)
print(Ws)

import matplotlib.pyplot as plt
DArr = np.array(D)
LArr = np.array(L)
plt.scatter(DArr[:, 1], LArr)
plt.show()

Dcopy = DArr.copy()
Dcopy.sort(0)
Dcopy[:5, :]
line_y = Dcopy*Ws

import matplotlib.pyplot as plt
DArr = np.array(D)
LArr = np.array(L)
plt.scatter(DArr[:, 1], LArr)
plt.plot(Dcopy[:, 1], line_y, c='r')
plt.show()
