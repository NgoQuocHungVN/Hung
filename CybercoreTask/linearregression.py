from __future__ import division, print_function, unicode_literals
import csv
import numpy as np
import matplotlib.pyplot as plt

X = []
y = []
with open('train.csv') as csvDataFile:
    file = csv.reader(csvDataFile)
    file.next();
    for row in file:
        if len(row) <=1:
            continue
        X.append(row[0])
        y.append(row[1])
X = np.array([X], dtype=float).T
y = np.array([y], dtype=float).T

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)

w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 100, 2)
y0 = w_0 + w_1*x0

plt.plot(X.T, y.T, 'ro')

plt.plot(x0, y0)
plt.plot(X,w_1*X+w_0)
plt.axis([0, 100, 0, 100])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

